from django.contrib import admin

# Register your models here.
from socialplantplatform.social.models import Publication, Like, Comment

admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Like)
