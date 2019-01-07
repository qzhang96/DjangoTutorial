import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
#Table Name: Question
class Question (models.Model):
  #colName               #datatype  #default
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
#it's important to add __str__() methods to your models, not only for own convenience when dealing with the interactive prompt, but also because objects' representations are used throughout Djanfo's automatically-generated admin
  def __str__(self):
      return self.question_text

#return boolean
  def was_published_recently(self):
    now =timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <=now


class Choice (models.Model):
  #colName            #datatype
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  #colName            #foreignkey
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
      return self.choice_text



