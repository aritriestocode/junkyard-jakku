from __future__ import unicode_literals
import re

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []
        if not postData['first_name'] or len(postData['first_name']) < 3:
            results['status'] = False
            results['errors'].append('First name must be longer than 2 characters')

        if not postData['last_name'] or len(postData['last_name']) < 3:
            results['status'] = False
            results['errors'].append('First name must be longer than 2 characters')

        if not postData['email'] or not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = False
            results['errors'].append('Email is not valid')

        if not postData['password'] or len(postData['password']) < 5 or postData['password'] != postData['confirm_password']:
            results['status'] = False
            results['errors'].append('Password does not match')

        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])

        if len(user) != 0:
            results['status'] = False
            results['errors'].append('Something went wrong. Try again?')
        print results['errors']
        return results
        print "models register"

	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(f_name = postData['f_name'], l_name = postData['l_name'], email = postData['email'], password = p_hash)
		return user

    def loginVal(self, postData):
        results = {'status': True, 'errors' : [], 'user': None}
        if len(postData['email']) < 3:
            results['status'] = False
            results['errors'].append('Something went wrong. Try again?')

        else:
            user = User.objects.filter(email = postData['email'])

            if len(user) <= 0:
                results['status'] = False
                results['errors'].append('Something went wrong. Try again?')

            elif len(postData['password']) < 5 or postData['password'] != user[0].password:
                results['status'] = False
                results['errors'].append('Something went wrong. Try again?')

            else:
                results['user'] = user[0]
        print results['user']
        print "models login"
        return results


class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    objects = UserManager()
