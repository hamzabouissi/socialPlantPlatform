import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from socialplantplatform.Base.BaseModels import BaseModel

User = get_user_model()


# Create your models here.

def plant_image_path_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'plant_image_{0}/{1}'.format(instance.id, uuid.uuid4())


class Plant(BaseModel):
    name = models.CharField(_("Name of Plant"), blank=False, null=False, max_length=50, unique=True)
    description = models.TextField(_("Description of Plant"), blank=True, max_length=255)
    image = models.ImageField(_("Name of Plant"), upload_to=plant_image_path_upload, blank=False, null=False)
    grow_days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UserPlant(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name="plants")
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, blank=False, null=False)
    price = models.FloatField(_("Price of Plant"), blank=False, null=False, default=0)
