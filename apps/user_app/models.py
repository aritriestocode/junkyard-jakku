from __future__ import unicode_literals
from ..login_app.models import User

from django.db import models

# Create your models here.
class FriendManager(models.Manager):
    def createFriend(self, postData):
        results = {'status' : True, 'errors' : [], 'friend' : None}
        if len(postData['first_name']) < 2:
            results['status'] = False
            results['errors'].append('This is fucking hard')
        if len(postData['last_name']) < 2:
            results['status'] = False
            results['errors'].append('This is fucking hard')
        if results['status'] == True:
            print '******', postData['user_id'], '******'
            

class Friend(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)

    objects = FriendManager()
