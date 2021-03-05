from django.db import models

# Create your models here.

class Info(models.Model):
    disease = models.CharField(max_length=600)
    causes = models.TextField()
    things_to_avoid = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.disease