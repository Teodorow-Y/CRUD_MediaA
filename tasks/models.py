from django.db import models

# Create your models here.
class mediaDB(models.Model):
    # This is and schema to create check list on plant
    task = models.CharField(max_length = 200)
    description_task = models.TextField(blank = True)
    supervisor = models.TextField(max_length = 200)
    date = models.DateField(auto_now_add=True)
    condition = models.BooleanField(default = False)
    active = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.task

