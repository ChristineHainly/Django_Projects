from django.contrib import admin
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('polls/', views.PollsView.as_view(), name='polls'),
    path('polls/detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('polls/results/<int:pk>', views.ResultsView.as_view(), name='results'),
    path('polls/vote/<int:question_id>', views.vote, name='vote'),
]