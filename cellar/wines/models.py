import os

from django.db import models

from PIL import Image


def _get_upload_path(instance, filename):
    return os.path.join('wine/img/', str(instance.name), filename)


class Wine(models.Model):
    name = models.CharField(max_length=200, blank=True)
    grapes = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    year = models.DateTimeField()
    notes = models.TextField(blank=True, help_text='Add description or additional info about the wine')
    picture = models.ImageField(upload_to=_get_upload_path)

    def __unicode__(self):
        return self.name

    def save(self, size=(250, 300)):
        """
        Save Wine after ensuring that wine's picture is not blank. Resize as needed.
        """

        if not self.id and not self.picture:
            return

        super(Wine, self).save()

        image = Image.open(self.picture)

        image.thumbnail(size, Image.ANTIALIAS)
        image.save(self.picture.path)
