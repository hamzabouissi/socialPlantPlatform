import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from socialplantplatform.Base.BaseModels import BaseModel

User = get_user_model()


def publication_video_path_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'publication_video_{0}/{1}'.format(instance.id, uuid.uuid4())

class Publication(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publications", blank=False, null=False)
    title = models.CharField(null=True, blank=True, max_length=50)
    video = models.FileField(upload_to=publication_video_path_upload, null=True,blank=True)
    story = models.BooleanField(default=False)


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", blank=False, null=False)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField(null=False, blank=False, max_length=350)
    reply_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def parent(self) -> bool:
        return self.reply_to is None


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", blank=False, null=False)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, blank=False, null=False)