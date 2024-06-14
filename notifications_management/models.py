
from django.db import models
from datetime import datetime
class Notification(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.now)
      
def __str__(self):
     return self.message