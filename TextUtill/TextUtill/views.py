from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import  CustomUser
from django.contrib import messages
import random


def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,'Username Taken please choose another name')
                return redirect('signup_page')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request,'Email Taken')
                return redirect('signup_page')
            # Use the create_user method to create a new user
            else:
                global new_user
                new_user = CustomUser.objects.create_user(username=username, email=email, password=password)

            subject = 'Welcome to TextUtill.com'
            message = f'''Hi {username}, your account has been created successfully on TextUtill.com.
            We will help you convert strings format into another format.'''
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('log')
        else:
            return HttpResponse("Your password and confirm password are not the same!!!")
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        # Use the authenticate function to check the credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Use the login function to log the user in
            login(request, user)

            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            new_user.otp = otp
            new_user.save()
            subject = 'Email Verification'
            message = f'Hi {username}, email verification is required. Please login with this OTP: {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('otp_login')
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'login.html')

def otp_login(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user_otp = CustomUser.objects.get(otp=otp)
        if user_otp.otp == otp:
            user_otp.otp = None
            user_otp.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid OTP")
    return render(request, 'otp_login.html')

        


@login_required(login_url='log')
def homepage(request):
    return render(request,'home.html')

def logoutpage(request):
    # logout(request)
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
    
