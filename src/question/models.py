from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.DateTimeField('date published')
    rate  = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers")
    text = models.TextField(default="")
