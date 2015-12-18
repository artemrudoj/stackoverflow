from django.db import models
from django.conf import settings

class Tag(models.Model):
    nameType = models.CharField(max_length=15)
    def __unicode__(self):
        return str(self.nameType)
class Rates(models.Model):
    count = models.IntegerField(default=0)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return str(self.count)



class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(default="")
    data = models.DateTimeField('date published')
    rate  = models.ForeignKey(Rates, related_name="rate")
    user = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return self.title
    def addTag(self, tagName):
        try:
            tag = Tag.objects.get(nameType=tagName)
        except Tag.DoesNotExist:
            tag = Tag()
            tag.nameType = tagName
            tag.save()
        self.tags.add(tag)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers")
    text = models.TextField(default="")
    data = models.DateTimeField('date published')
    rate  = models.ForeignKey(Rates, related_name="likes")
    user = models.IntegerField(default=0)
    trueFlag = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)




