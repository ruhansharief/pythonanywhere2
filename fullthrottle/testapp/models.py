from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.CharField(primary_key=True,max_length=64)
    real_name = models.CharField(max_length=64)
    tz = models.CharField(max_length=64)

    def __str__(self):
        return self.real_name

class ActivityPeroidModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="activity_periods")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    