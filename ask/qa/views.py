from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from qa.forms import AskForm, AnswerForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as ll

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
		q.author = reques.user
		q = form.save()
		q.author = reques.user
		q.save()
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
		q.author = reques.user
		q.save()
		return HttpResponseRedirect('/question/' + str(q.id))
	else:
		form = AskForm()
	return render(request, "qa/ask.html" , {'form': form})

def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		s = form["username"].value()
		p = form["password"].value()
		u = User.objects.create_user(s,"ss",p)
		u.save()
		q = authenticate(username=u.username, password=p)
		print(q)
		ll(request, q)
		r = HttpResponseRedirect('/')
		r.set_cookie("user", q.username, max_age=1000)
		return r
	else:
		form = UserForm()
	return render(request, "qa/signup.html" , {'form': form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		s = form["username"].value()
		p = form["password"].value()
		print(s)
		try:
			request.user = User.objects.get(username=s, password=p)
		except ObjectDoesNotExist:
			raise Http404(request)
		
		return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, "qa/login.html" , {'form': form})
	




