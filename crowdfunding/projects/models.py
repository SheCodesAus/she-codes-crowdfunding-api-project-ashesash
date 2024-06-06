from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

User = get_user_model()

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    Project_type = (
        ('goods', 'GOODS'),
        ('adoption', 'ADOPTION'),
        ('shelter', 'SHELTER'),
        ('animal healthcare', 'ANIMAL HEALTHCARE'),
        ('events', 'EVENTS')
    )
    cause = models.CharField(choices=Project_type, max_length=20, default="ADOPTION")
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_projects'
    )
    image=models.URLField()
    is_open=models.BooleanField()
    is_active=models.BooleanField(default=True)
    date_created=models.DateTimeField(default=datetime.now())
    date_end=models.DateTimeField(default=(datetime.now() + timedelta(days=60)))
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

@property
def total_likes(self):
    return self.liked_by.aggregate(count=models.Count('id'))['count']

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

