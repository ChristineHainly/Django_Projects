import datetime

from django.db import models
from django.utils import timezone     

class Question(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
    question_text = models.CharField('Question', max_length=200)
    pub_date = models.DateTimeField('Date Published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Choice Text', max_length=200)
    votes = models.IntegerField('Vote Quantity', default=0)
    def __str__(self):
    	return self.choice_text
