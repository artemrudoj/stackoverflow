from django.views.generic import DetailView, TemplateView
from .models import Question
from django.views.generic.list import ListView
from django.utils import timezone



class QuestionsListView(ListView):

    queryset = Question.objects.all()
    template_name = "questions.html"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class QuestionView(DetailView):
    template_name = 'question.html'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data()
        return context

class QuestionAdd(TemplateView):
    template_name = "question_add.html"
