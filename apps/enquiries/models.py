from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampUUIDModel

# Create your models here.
class Enquiry(TimeStampUUIDModel):
    name = models.CharField(_("Your Name"), max_length=150)
    phone_number = PhoneNumberField(_("Phone Number"), max_length=30,default="+8801793745514")
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=150)
    message = models.TextField(_("Message"))

    def __str__(self) :
        return self.email

    class Meta:
        verbose_name_plural = "Enquiries"
