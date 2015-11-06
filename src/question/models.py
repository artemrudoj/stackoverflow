from django.db import models


class Tag(models.Model):
    nameType = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.nameType)

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(default="")
    data = models.DateTimeField('date published')
    rate  = models.IntegerField(default=0)
    user = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers")
    text = models.TextField(default="")
    data = models.DateTimeField('date published')
    rate  = models.IntegerField(default=0)
    user = models.IntegerField(default=0)
    trueFlag = models.BooleanField(default=False)


