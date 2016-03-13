from django.shortcuts import render
from django.http import HttpResponse, Http404
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

def test(request, *args, **kwargs):
	return HttpResponse('OK')


def all_q(request, *args, **kwargs):
	questions = Question.objects.all().order_by("-addet_at")
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, request.GET.get('limit', 10))
	page = paginator.page(page)	
	return render(request, "qa/all.html", 
	{	
		'questions': page.object_list,
		'paginator': paginator,
		'page': page
	})

def popular(request, *args, **kwargs):
	questions = Question.objects.all().order_by("-rating")
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, request.GET.get('limit', 10))
	page = paginator.page(page)	
	return render(request, "qa/all.html", 
	{	
		'questions': page.object_list,
		'paginator': paginator,
		'page': page
	})

def question(request, id):
	try:
		question = Question.objects.get(id=id)
	except ObjectDoesNotExist:
		raise Http404(request)
	strin = ""
	for i in question.answer_set.all():
		strin += str(i.text)
	return HttpResponse(question.title + " " + question.text + " " + strin)





