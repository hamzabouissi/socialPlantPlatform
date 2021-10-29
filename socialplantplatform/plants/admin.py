from django.contrib import admin

# Register your models here.
from socialplantplatform.plants.models import Plant, UserPlant

admin.site.register(Plant)
admin.site.register(UserPlant)
