from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.


# -User-User--User--User--User--User--User--User--User--User--User--User--User--User--User--User--User--User-
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
    profile_img = models.ImageField(upload_to=('avatars/'),default=('avatars/default.jpg'))
    first_time = models.BooleanField(null=False, default=True)
    bio = models.CharField(null=True, max_length=50, default="Edit profile for more.")
    date_joined = models.DateField(null=True, default=timezone.now)    
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


# -ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null = True)
    def __str__(self):
        return str(f"{self.name}")


class SourceType(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class Language(models.Model):
    code = models.CharField(max_length=50)
    fullname = models.CharField(max_length=250)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.fullname}")


class Book(models.Model):
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()
    author = models.CharField(max_length=250)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True, null=True)
    sourcetype = models.ForeignKey(SourceType, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    image = models.ImageField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        words = self.title.split()
        abbreviations = [word[0].upper() for word in words if word]
        return ''.join(abbreviations)

class LoanTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_loan = models.DateField(default=timezone.now, null= False)
    date_expired = models.DateField(default=(timezone.now() + timedelta(7)), null= False)
    returned = models.CharField(
        max_length=2, choices=(("0", "No"), ("1", "Yes")), default=0
    )
    class Meta:
            unique_together = ('user', 'book')
    def __str__(self):
        return str(f'{self.user.profile.identity}_{self.book}')
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.profile.first_name} {self.user.profile.last_name} on {self.book.title} at {self.created_at}"
    
