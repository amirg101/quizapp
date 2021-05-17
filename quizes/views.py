from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Quiz
from django.utils import timezone
from questions.models import Question,Answer
from django.views.generic import ListView
from results.models import Result
from django.contrib.auth.models import User
from questions.forms import QuestionForm,AnswerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
class QuizListView(ListView):
    model=Quiz
    template_name='quizes/main.html'


@login_required
def quiz_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    questions={}
    for q in quiz.get_questions():
        answers=[]
        for a in q.get_answers():
            answers.append(a.text)
        questions[str(q)]=answers
    return render(request,'quizes/quiz.html',{'obj':quiz,'questions':questions})


def save_quiz_view(request,pk):
    print(request.POST)
    if request.is_ajax():
        questions =[]
        data=request.POST
        data_=dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            question=Question.objects.get(text=k)
            questions.append(question)
        
        user =request.user

        quiz=Quiz.objects.get(pk=pk)
        score=0
        multiplier=100 / quiz.no_of_questions
        results=[]
        correct_answer = None

        for q in questions:
            a_selected=request.POST.get(q.text)
            if a_selected !="":
                question_answers=Answer.objects.filter(question=q)
                for a in question_answers:   
                    if a_selected==a.text:
                        if a.correct:
                            score+=1
                            correct_answer=a.text
                    else:
                        if a.correct:
                            correct_answer=a.text
                results.append({str(q):{'correct_answer': correct_answer,'answered':a_selected}})
            else:
                results.append({str(q):'not answered'})
        score_=score*multiplier
        print(score_)
        Result.objects.create(quiz=quiz,user=user,score=score_)
        if score_>=quiz.required_score_to_pass:
            return JsonResponse({'passed':True,'score':score_ ,'results':results})
        else:
            return JsonResponse({'passed':False,'score':score_ ,'results':results})
        
    return JsonResponse({
        'score':score,
        'results':results,
        'text':'works',
    })

from .forms import QuizForm,createUserForm
  
# Create your views here
@login_required
def home_view(request):
    context ={}
    form=QuizForm()
    
    
    if request.method == "POST":

        form = QuizForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print(form)
            form.save()

            return redirect('/add-questions')
        # add_questions(request,pk=QuizForm.pk)

    else:   
    
        context['form']= form
     


        
    return render(request, "quizes/home.html", context)

def add_questions(request):
    return render(request,"quizes/addq.html")



def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
            
        else:
            messages.info(request,"username or password is incorrect")
            return redirect('quizes:login')

    context={}
    return render(request,'quizes/Login.html',context)


def registerView(request):
    form=createUserForm()

    if request.method=="POST":
        form=createUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"account was created for " + user)
            return redirect('quizes:login')
    context={
        "form":form
    }
    return render(request,'quizes/register.html',context)

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("quizes:main-view")