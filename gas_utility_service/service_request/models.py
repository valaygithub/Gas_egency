import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    customer = models.CharField(max_length=100)
    Mobile_number = models.BigIntegerField(default=9999999999)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submited_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f'Service Request {self.id} by {self.customer} - submitted on {self.submited_at}'

class Tracking(models.Model):
         STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
          ]
         service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
         status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
         submitted_at = models.DateTimeField(auto_now_add=True)
         resolved_at = models.DateTimeField(blank=True, null=True)

def __str__(self):
      return f'Tracking ID: {self.pk} - Status: {self.status}'
