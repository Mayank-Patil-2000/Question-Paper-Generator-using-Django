from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from loginapp.models import questionBank
import random


def index(request):
    return render(request, 'index.html')

def generatePaper(request):
    print('GenertePaperRequest')
    return render(request, 'generatePaper.html')

def about(request):
    mytext = request.POST.get('ques1', 'default')    #get the text from text box
    noOfQues = request.POST.get('noOfQues', 'NULL')
    print("mytext: "+mytext)
    print("noOFQes: "+noOfQues)

    k=''
    l=[]
    for i in mytext:
        k=k+i
        if i=='\n':
            k = k.strip()
            l.append(k)
            k=''

    finalListOfQues = []
    
    print(l)
    i = 0
    while i < int(noOfQues):
        rand = random.choice(l)
        if rand not in finalListOfQues:
            finalListOfQues.append(rand)
            i=i+1

    print(finalListOfQues)

    lastString = ''
    z = 1
    for i in finalListOfQues:
        i = "Q" + str(z) + ". " + i
        lastString = lastString + i + "\n"
        z = z+1

    params = {"q1" : lastString}
    return render(request, 'questions.html', params)


def addQuestion(request):
    return render(request, 'addQuestion.html')

def getQuestion(request):
    questionBan = questionBank()
    questionBan.question = request.POST.get('question', 'default')
    questionBan.chapter = request.POST.get('chapter', 0)
    questionBan.difficulty = request.POST.get('difficulty', 0)
    questionBan.marks = request.POST.get('marks', 0)
    questionBan.unit = request.POST.get('unit',0)
    questionBan.sem = request.POST.get('sem', 0)
    questionBan.year = request.POST.get('year', 0)
    questionBan.subname = request.POST.get('subname', 'default')
    
    questionBan.save()
    print(questionBan.subname)
    return render(request, 'getQuestion.html')

def displayQuestionBank(request):
    questionBank = questionBank.objects.all()
    year = request.POST.get('year')
    subname = request.POST.get('subname')
    l=[]
    for i in questionBank:
        if i.year == year and i.subname == subname:
            l.append(i.question)
    random.shuffle(l)
    params = {"ques":l}
    return render(request, 'showQuestions')

# def generatePaper(request):
