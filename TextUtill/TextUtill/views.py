from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# these two lines is imported for the wellcome email sending
from django.core.mail import send_mail
from django.conf import settings





@login_required(login_url='login')
def homepage(request):
    return render(request,"home.html")

def signup_page(request):
    # this line mean that form data is comming
    if request.method=='POST':
        # we store the form data in variables
        Uname=request.POST.get('username')
        Email=request.POST.get('email')
        Password=request.POST.get('password1')
        Cpassword=request.POST.get('password2')
        if Password!=Cpassword:
            return HttpResponse("your password and confirm passwrod are not same!!!")
        else:
            # object: refers a manager perform operation on database User table.
            my_user=User.objects.create_user(Uname,Email,Password)
            subject='Welcome to the Caseconvert.come'
            message=f'Hi {Uname}  we will help you to converter strings formate into anotther formate'
            from_email=settings.EMAIL_HOST_USER
            recipient_list=[Email]
            send_mail(subject,message,from_email,recipient_list, fail_silently=False)
            my_user.save()
            
            return redirect('log')
    
        # check data, IS really comming the form Data?
        # print(Uname,Email,Password,Cpassword)
    return render(request,'signup.html')


def login_page(request):
    if request.method=='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('pass')
        user=authenticate(request,username=username1,password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect!!!")
    return render(request,'login.html')
def logoutpage(request):
    logout(request)
    return redirect('log')


def contact(request):
    return render(request,'contact.html')
def about_view(request):
    return render(request,'about.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    wordscounter=request.POST.get('wordscounter','off')
    lowercase=request.POST.get('lowercase','off')
    sentencecase=request.POST.get('sentencecase','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n':
                analyzed+= char
        params = {'purpose': 'Remove NewLines', 'lineremover': analyzed}
        return render(request, 'analyze.html', params) 

        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if charcounter == 'on':
        analyzed = 0
        for char in djtext:
           if char != ' ':
            analyzed += 1
        params = {'purpose': 'Total characters of user is', 'analyzed_text': analyzed}
        # djtext=analyzed
        return render(request, 'analyze.html', params)  

    if(wordscounter=='on'):
        analyzed=0
        words=djtext.split()
        analyzed=len(words)
        params = {'purpose': 'Total characters of user is', 'analyzed_text': analyzed}
        # djtext=analyzed
        return render(request, 'analyze.html', params)     
    

    if(lowercase=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.lower()
        params = {'purpose': 'Change to lower case', 'analyzed_text': analyzed}
        djtext=analyzed

        # return render(request, 'analyze.html', params) 
        
    
    if(sentencecase=='on'):
        analyzed=djtext
        capital=analyzed.capitalize()
        params = {'purpose': 'Change to sentence case', 'analyzed_text': capital}
        # return render(request, 'analyze.html', params)
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and wordscounter!='on'
       and charcounter!='on' and lowercase!='on' and sentencecase!='on' ):
        return render(request,'message.html')  
    
    return render(request, 'analyze.html', params)
    
