from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import check_password


class UserManager(BaseUserManager):

    def profile_aggregate(self, user_id: int):
        user = self.get(id=user_id)
        publications = user.publications.count()
        am_follow = user.am_follow.count()
        follow_me = user.followed_me.count()
        return {
            "publications": publications,
            "am_follow": am_follow,
            "follow_me": follow_me
        }

    def authenticate_user(self, username, password):
        user = self.filter(username=username).first()
        if user is None:
            return False
        valid = check_password(password,user.password)
        return valid
