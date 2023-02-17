from django.db import models

class TypeOfFile(models.Model):
  name = models.CharField(max_length=20)
  created_at = models.DateField(auto_now_add=True)

  class Meta:
    db_table = 'type_of_file'

  def __str__(self):
    return self.name