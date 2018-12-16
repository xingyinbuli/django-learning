from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Question

def index(request):
    latest_question_list=Question.objects.all()
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request,question_id):
    return HttpResponse("你在看question_id%s."%question_id)

def results(request,question_id):
    return HttpResponse("你在看results question_id%s."%question_id)

def vote(request,question_id):
    return HttpResponse("你在看vote question_id%s."%question_id)



