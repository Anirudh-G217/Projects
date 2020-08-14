'''
A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.
For more info, refer to https://docs.djangoproject.com/en/3.0/topics/db/models/

'''

from django.db import models

class Query(models.Model):
    '''
    Class for storing the fields as class attributes.
    intent and response are database field of the model. 
    They are specified as class attributes, and map to a database column.
    '''
    intent = models.CharField(max_length=2000)
    response = models.CharField(max_length=5530)
    
    def __str__(self):
        return 'Intent: ' + self.intent

class Unanswered_Query(models.Model):
    '''
    Class for storing the fields as class attributes.
    unanswered_query are database field of the model. 
    They are specified as class attributes, and map to a database column.
    '''
    unanswered_query = models.CharField(max_length=2000)
    
    def __str__(self):
        return 'Query: ' + self.unanswered_query
