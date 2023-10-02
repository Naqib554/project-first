from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
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
    return render(request, 'analyze.html', params)
    
