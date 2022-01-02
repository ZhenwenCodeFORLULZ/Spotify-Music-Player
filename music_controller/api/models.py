from django.db import models
import string
import random 

# Create your models here.
# write python code and operates database commands

#code should be random and unique
def generate_unique_code():
    length = 6 
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length)) 
        # generates a random code with the length of 6, thats upper case
        if Room.objects.filter(code = code).count() == 0:
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length = 8,default = generate_unique_code,unique = True)
    host = models.CharField(max_length = 50, unique = True)    
    guest_can_pause = models.BooleanField(null = False, default = False)
    votes_to_skip = models.IntegerField(null = False, default = 1)
    created_at = models.DateTimeField(auto_now_add = True)

    # you can also add methods in this class
    # we want fat models thin views, or put most of your logic onto the models

