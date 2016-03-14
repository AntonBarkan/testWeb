from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
	return HttpResponse('OK')


def all_q(request, *args, **kwargs):
	questions = Question.objects.all().order_by("-id")
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

def answer(request):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		q = form.save()
		return HttpResponseRedirect('/question/' + str(q.question_id))
	#return render(request, "qa/ask.html", {
	#	"form":form
	#})

def question(request, id):

	try:
		question = Question.objects.get(id=id)
	except ObjectDoesNotExist:
		raise Http404(request)
	form = AnswerForm()
	return render(request, "qa/question.html", {
		'title':question.title	,
		'text':question.text,
		"ans" : question.answer_set.all(),
		"form":form
	})
	

def ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		q = form.save()
		return HttpResponseRedirect('/question/' + str(q.id))
	else:
		form = AskForm()
	return render(request, "qa/ask.html" , {'form': form})




