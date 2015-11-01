from django.views.generic import DetailView
from .models import Question
from django.views.generic.list import ListView
from django.utils import timezone



class QuestionsListView(ListView):

    queryset = Question.objects.all()
    template_name = "questions.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class QuestionView(DetailView):
    template_name = ''
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data()
        return context

