import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

from socialplantplatform.users.managers.UserManager import UserManager


def user_image_path_upload(instance, filename):
    return f"user_images/{instance.id}/{uuid.uuid4()}"


class User(AbstractUser):
    """Default user for socialPlantPlatform."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    image = ImageField(upload_to=user_image_path_upload, null=True, blank=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    objects = UserManager()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
