"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from question.views import QuestionsListView, QuestionView, QuestionAdd, like, AnswerAdd, popularTags, popularUsers
from users.views import LoginRequest,  MyUserRegistration, LogoutRequest, UsersListView, UserView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions/$', QuestionsListView.as_view(), name='question-list'),
    url(r'^questions/(?P<pk>\d+)/$', QuestionView.as_view(), name='question'),
    url(r'^login/', LoginRequest, name='login'),
    url(r'^registration/', MyUserRegistration, name='registration'),
    url(r'^logout/', LogoutRequest, name='logout'),
    url(r'^question_add/', QuestionAdd, name='question_add'),
    url(r'^comment_add/$', AnswerAdd, name='comment_add'),
    url(r'^users/$', UsersListView.as_view(), name='users-list'),
    url(r'^users/(?P<pk>\d+)/$', UserView.as_view(), name='user'),
    url(r'^like/$', like, name='like'),
    url(r'^populartags/$', popularTags, name='populartags'),
    url(r'^popularusers/$', popularUsers, name='popularusers'),
]
