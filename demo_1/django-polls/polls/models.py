import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now
        # return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_data'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chioce_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.chioce_test

