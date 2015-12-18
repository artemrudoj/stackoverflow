from django import forms

__author__ = 'artem'



class QuestionAddForm(forms.Form):
    title = forms.CharField(label=(u'User name'))
    description = forms.CharField(label=(u'description'),widget=forms.Textarea)
    tags = forms.CharField(label=(u'tags'))


class AnswerAddForm(forms.Form):
    description = forms.CharField(label=(u'description'),widget=forms.Textarea)