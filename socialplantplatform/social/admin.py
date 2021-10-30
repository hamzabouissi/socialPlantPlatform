from django.contrib import admin

# Register your models here.
from socialplantplatform.social.models import Publication, Like, Comment, UserFollow

admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserFollow)
