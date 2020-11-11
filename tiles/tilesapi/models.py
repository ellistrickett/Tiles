from django.db import models

# Create your models here.

STATUS_CHOICES = [
  ('live', 'Live'),
  ('pending', 'Pending'),
  ('archived', 'Archived')
]

class Tile(models.Model):
  title = models.CharField(max_length=50)
  launch_date = models.CharField(max_length=50)
  status = models.CharField(choices=STATUS_CHOICES, max_length=12, db_index=True)

  def __str__(self):
    return self.title

class Task(models.Model):
  title = models.CharField(max_length=50)
  order_field = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  type = models.CharField(max_length=200)
  tile = models.ForeignKey(Tile, on_delete=models.CASCADE)

  def __str__(self):
    return self.title