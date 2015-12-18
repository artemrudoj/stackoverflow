
import datetime
import json
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from .models import Question, Answer
from django.views.generic.list import ListView
from django.utils import timezone
from question.forms import QuestionAddForm, AnswerAddForm
from .models import Rates,Tag, Rates
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
class QuestionsListView(ListView):

    queryset = Question.objects.all()
    template_name = "questions.html"
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data(**kwargs)
        q = self.request.GET.get("sort")
        if q != None:
            context['input'] = "sort=" + q + "&"
        else:
            context['input'] = ""
        return context

    def get_queryset(self):
        queryset = Question.objects.all()
        if self.request.GET.get("sort"):
            selection = self.request.GET.get("sort")
            queryset = Question.objects.filter(tags__nameType=selection)
        else:
            queryset = Question.objects.order_by("-data")[:20]
        return queryset


class QuestionView(DetailView):
    template_name = 'question.html'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data()
        return context


@login_required
def QuestionAdd(request):
    if request.method == 'POST':
        form = QuestionAddForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            title = form.cleaned_data['title']
            question = Question()
            question.title = title
            question.text = description
            rate = Rates()
            rate.count = 0
            rate.save()
            rate.users.add(request.user)

            question.rate = rate
            question.data = datetime.datetime.now()
            question.author = request.user
            question.save()
            send_mail("qdqd","asdsdd","artem.rudoj@frtk.ru",["artem.rudoi@phystech.edu"], "551995eytxf")
            for tagName in form.cleaned_data['tags'].split( ):
                question.addTag(tagName)
            return HttpResponseRedirect(reverse('question', args=(question.id,)))
        else:
            print form.errors
            return render(request, "question_add.html", {"form" : form } )
    else:
        form = QuestionAddForm()
        context = {'form': form}
        return render_to_response('question_add.html', context, context_instance=RequestContext(request))

def AnswerAdd(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
        form = AnswerAddForm(request.POST)
        if form.is_valid():
            id = int(request.POST.get("title", ""))
            description = form.cleaned_data['description']
            answer = Answer()
            answer.question = Question.objects.get(id=id)
            answer.text = description
            rate = Rates()
            rate.count = 0
            rate.save()
            answer.rate = rate
            answer.data = datetime.datetime.now()
            answer.author = request.user
            answer.save()
            return HttpResponseRedirect(reverse('question', args=(id,)))
        else:
            return render(request, "question_add.html", {"form" : form } )
    else:
        form = AnswerAddForm()
        context = {'form': form}
        return render_to_response('question_add.html', context, context_instance=RequestContext(request))



def like(request):
    if request.method == 'POST':
        user = request.user
        if not user.is_authenticated():
            resp = HttpResponse(json.dumps({'message': "error"}), content_type='application/json')
            resp.status_code = 400
            return resp
        id = request.POST.get('id', None)
        type = request.POST.get('type', None)
        if type != None and id != None:
            total_likes = 0
            if type == "question":
                question = Question.objects.get(id=id)

                question.rate.count = question.rate.count + 1
                total_likes = question.rate.count
                question.rate.users.add(user)
                question.rate.save()
                question.save()
            else:
                answer = Answer.objects.get(id=id)
                answer.rate.count = answer.rate.count + 1
                total_likes = answer.rate.count
                answer.rate.users.add(user)
                answer.rate.save()
                answer.save()

            ctx = {'likes_count': total_likes, 'message': "saf"}
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')

def popularTags(request):
    tags = Tag.objects.annotate(counts=Count('question')).order_by('-counts')[:5]
    return render(request, "popular_tags.html", {"tags" : tags } )

def popularUsers(request):
    users = User.objects.annotate(counts=Count('rate')).order_by('-counts')[:5]
    return render(request, "popular_users.html", {"users" : users } )