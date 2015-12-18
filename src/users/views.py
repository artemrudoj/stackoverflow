import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .forms import RegistrationForm, LoginForm


def MyUserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/questions/')
    if request.method == 'POST':
        data = request.POST.copy()
        data['date_joined'] = datetime.date.today()
        data['last_login'] = datetime.datetime.now()
        form = RegistrationForm(data)
        print  "asd"
        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/questions/')
        else:
            return render_to_response('registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form':form}
        return  render_to_response('registration.html',context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/questions/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            myUser = authenticate(username=username, password=password)
            if myUser is not None:
                login(request, myUser)
                next = request.GET.get("next", "/questions/")
                return HttpResponseRedirect(next)
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/questions/')

class UsersListView(ListView):
    User = get_user_model()
    queryset = User.objects.all()
    template_name = "users.html"
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class UserView(DetailView):
    template_name = 'user.html'
    User = get_user_model()
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data()
        return context