from django.db import models
from django.db.models.deletion import CASCADE

# Each game entity will have these attributes.

class Title(models.Model):
    """Game titles."""
    text = models.CharField(max_length=64)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation Model above."""
        return self.text

class Entry(models.Model):
    """Little descriptions of game-entities and about availability."""
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """String representation of Model above."""
        return f"{self.text[:32]}..."
