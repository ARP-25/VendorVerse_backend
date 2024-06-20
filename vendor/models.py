from django.db import models
from django.utils.text import slugify
from userauths.models import User, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='vendor/', null=True, blank=True, default="default/default-user.jpg")
    name = models.CharField(max_length=100, help_text='Vendor name', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=100, help_text='Mobile Number', null=True, blank=True)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=500, unique=False, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else ""

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if self.slug in [None, '']:
            self.slug = slugify(self.name)
        super(Vendor, self).save(*args, **kwargs)

# Signal to create Vendor instance when User is created
@receiver(post_save, sender=User)
def create_user_vendor(sender, instance, created, **kwargs):
    if created:
        vendor = Vendor.objects.create(user=instance)
        vendor.name = instance.email  # Set the vendor name to the user's email
        vendor.save()

@receiver(post_save, sender=User)
def save_user_vendor(sender, instance, **kwargs):
    try:
        instance.vendor.name = instance.email  # Update the vendor name to the user's email on save
        instance.vendor.save()
    except Vendor.DoesNotExist:
        Vendor.objects.create(user=instance, name=instance.email)  # Create Vendor if it does not exist
