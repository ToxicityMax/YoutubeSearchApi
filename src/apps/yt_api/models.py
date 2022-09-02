from django.db import models


class VideoDetails(models.Model):
    yt_id = models.CharField(max_length=255, primary_key=True)  # Unique youtube video id
    keyword = models.CharField(max_length=255, blank=True, null=True)  # Keyword related to video
    thumbnail = models.URLField()
    title = models.CharField(max_length=511, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    channel_id = models.CharField(max_length=255, blank=True, null=True)
    channel_title = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField()  # Published date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Indexes for database tables"""
        indexes = [
            models.Index(fields=['title', 'description']),
            models.Index(fields=['channel_id']),
            models.Index(fields=['keyword'])]

    def __str__(self):
        return f"{self.yt_id}->{self.title}"

    def get_image_url(self):
        return self.image.url
