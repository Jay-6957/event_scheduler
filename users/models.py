from django.db import models
from django.contrib.auth.models import User
# from tasks.models import my_task

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    roll = models.CharField(max_length=9,default='0')
    batch = models.CharField(max_length=13,default='0')
    programme = models.CharField(max_length=13,default='0')
    department = models.CharField(max_length=50,default='0')

    def _str_(self):
        return f'{self.user.first_name} profile'

    def get_rsvp_tasks(self):
        # return the tasks which are related to this user (using the m2m relation my_task.rsvp_users)
        return self.rsvp_tasks.all()
