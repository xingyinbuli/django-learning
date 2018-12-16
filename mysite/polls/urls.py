from django.urls import path

from polls import views
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<question_id>/',views.detail,name='detail'),
    path('results/<question_id>/',views.results,name='results'),
    path('vote/<question_id>/',views.vote,name='vote')

]
