from django.db import models
from django.urls import reverse
from enum import Enum

class Status(Enum):
    NEW = 'NEW'
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'

# Create your models here.
class IssueModel(models.Model):
    all_status_choice = [(status.name, status.value) for status in Status]
    host = models.CharField(max_length=100)
    odo_link = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(choices=all_status_choice, max_length=20, default='NEW')

    def __str__(self):
        return f'Host: {self.host} with status {self.status}'

    def get_absolute_url(self):
        return reverse('issues')
        # return reverse('issue_detail', args=[str(self.id)])
