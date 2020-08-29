from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('<h1>Hello</h1> <a href="http://127.0.0.1:8000/about" >Facebook</a>')
    return render (request,'index.html')
def about(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('about','off')
    newlineremoval=request.POST.get('newlineremoval','off')
    capsUp=request.POST.get('capsUp','off')
    spaceremoval=request.POST.get('spaceremoval','off')
    count = 0
    if removepunc=="on":
        analyse=""
        punctualtion='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctualtion:
                analyse=analyse+char
                count=count+1
        params={'analysed_text':analyse,'purpose':'abc','count': count}
        djtext=analyse
        # return render(request,'analyse.html',params)
    if(newlineremoval=="on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                 analyzed = analyzed + char
        params = {'analysed_text': analyzed, 'purpose': 'Removed new line'}
        djtext=analyzed
        # return render(request, 'analyse.html', params)
    if (spaceremoval == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'analysed_text': analyzed, 'purpose': 'Removed new line'}
        djtext=analyzed
        # return render(request, 'analyse.html', params)
    if(capsUp=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'analysed_text': analyzed, 'purpose': 'Changed to upper case'}
        djtext=analyzed
        # return render(request, 'analyse.html', params)
    if ( removepunc!="on" and newlineremoval!="on" and spaceremoval!="on" and capsUp!="on"):
        return HttpResponse("Please Select any Operations!!")
    return render(request, 'analyse.html', params)

# def home(request):
#     return HttpResponse("Hello Anni")
# def classs(request):
#     return HttpResponse("Hello Anni")


