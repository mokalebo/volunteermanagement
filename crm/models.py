from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Volunteer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='volunteer')
    vol_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.vol_name)


class Availability(models.Model):
    vol_name = models.CharField(max_length=50)
    service_category = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    setup_time = models.DateTimeField(
        default=timezone.now)
    cleanup_time = models.DateTimeField(
        default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.vol_name)

class Organization(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20, default='Omaha')
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    phone = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.organization_id)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name

# class Opportunity(models.Model):
    # vol_name = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='opportunity')
    # company_name = models.CharField(max_length=100)
    # company_description = models.CharField(max_length=300)
    # website = models.CharField(max_length=100, default="")
    # filled = models.BooleanField(default=False)
    # created_date = models.DateTimeField(
        # default=timezone.now)
    # updated_date = models.DateTimeField(auto_now_add=True)

    # def created(self):
        # self.created_date = timezone.now()
        # self.save()

    # def updated(self):
        # self.updated_date = timezone.now()
        # self.save()

    # def __str__(self):
        # return str(self.vol_name)

class Opportunity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    time = models.TimeField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "Volunteer Opportunity on %s %s with %s" % (self.date, self.time, self.organization)


class Assignment(models.Model):
	#organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
	opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
	volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	# opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
	created_date = models.DateTimeField(
        default=timezone.now)
	# status = models.IntegerField(default=0)
	
	class Meta:
		unique_together = (('volunteer', 'opportunity'),)

	def __str__(self):
		#org = Organization.objects.get(id=self.organization_id)
		vol = Volunteer.objects.get(id=self.volunteer_id)
		tim = Opportunity.objects.get(id=self.opportunity_id)
		return '%s at %s' % (vol, tim)


# class Organization(models.Model):
    # name = models.CharField(max_length=100)
    # street = models.CharField(max_length=30)
    # city = models.CharField(max_length=20, default='Omaha')
    # state = models.CharField(max_length=2)
    # zip = models.CharField(max_length=5)
    # phone = models.IntegerField(blank=False, null=False)
    # created_date = models.DateTimeField(
        # default=timezone.now)

    # def __str__(self):
        # return str(self.organization_id)

    # class Meta:
        # verbose_name = "Organization"
        # verbose_name_plural = "Organizations"

    # def __str__(self):
        # return self.name


# class Opportunity(models.Model):
    # organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # date = models.DateField(db_index=True)
    # time = models.TimeField()

    # def __str__(self):
        # return "Volunteer Opportunity on %s %s with %s" % (self.date, self.time, self.organization)