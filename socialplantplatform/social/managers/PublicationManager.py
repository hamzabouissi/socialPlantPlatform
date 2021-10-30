from django.db import models
from django.db.models import QuerySet

from socialplantplatform.plants.models import User


class PublicationManager(models.QuerySet):

    def get_user_follows_stories(self, user: User) -> QuerySet:
        users_list = user.am_follow.values_list("follow_to", flat=True)
        publications = self.filter(user__in=users_list, story=True)
        return publications

    def get_user_follows_publications(self, user: User) -> QuerySet:
        users_list = user.am_follow.values_list("follow_to", flat=True)
        publications = self.filter(user__in=users_list, story=False)
        return publications

