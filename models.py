from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


# -User-User--User--User--User--User--User--User--User--User--User--User--User--User--User--User--User--User-
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null= False)
    last_name = models.CharField(max_length=50, blank=False, null= False)
    email = models.EmailField(max_length=50, blank=False, null= False)
    identity = models.CharField(max_length=9, blank=False, null= False)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(default= timezone.now, blank=True)
    sex = models.CharField(max_length=2, choices=(('1','MALE'), ('2', 'FEMALE')), blank=True)
    profile_img = models.ImageField(upload_to=('avatars/'),blank=True)
    first_time = models.BooleanField(null=False, default=True)    
    class ROLE(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        READER = "READER", "Reader"
        LIBRARIAN = "LIBRARIAN", "Librarian"

    role = models.CharField(max_length=20, choices=ROLE.choices, default = ROLE.READER)

    def init_identity(self):
        if self.role == "ADMIN":
            name = 'AD'
        if self.role == "LIBRARIAN":
            name = 'LB'
        if self.role == "READER":
            name = 'RD'
        self.identity = name + str(Profile.objects.filter(role=self.role).count())

    def __str__(self):
        return str(self.identity)

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        user_profile.init_identity()
        user_profile.save()

class ReaderRequest(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null= False)
    last_name = models.CharField(max_length=50, blank=False, null= False)
    email = models.EmailField(max_length=50, blank=False, null= False)
    status = models.CharField(
        max_length=2, choices=(("1", "Wait"), ("2", "Accept"), ("3", "Decline")), default=1
    )
    def __str__(self):
        return str('Request_' + self.email)

# -ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN
class Category(models.Model):
    name = models.CharField(blank=False, null=False, max_length=250)
    description = models.TextField(blank=True, null=True, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)
    image = models.ImageField(null=False, blank=False, upload_to="images/")

    def __str__(self):
        return str(f"{self.name}")


class SourceType(models.Model):
    code = models.CharField(blank=False, null=False, max_length=50)
    name = models.CharField(null= False, blank=False, max_length=250)
    description = models.TextField(blank=True, null=True, max_length=400)
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class Language(models.Model):
    code = models.CharField(max_length=50, blank=False, null=False)
    fullname = models.CharField(max_length=250,blank=False, null=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.fullname}")