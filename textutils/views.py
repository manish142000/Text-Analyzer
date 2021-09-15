from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render

par = {
    "name": "manish",
    "place": "Mumbai",  
}

def home(request):
    return render(request, 'home.html', par)    

def about(request):
    return HttpResponse("This is the about page")

def convert_str(is_puncremoved, is_uppercase, is_newlineremover, is_extraspaceremoved, text)-> str:
    
    punc = '''!()-[]{;:'"\,}<>./?@#$%^&*_~'''
    
    temp = text
    analyzed_text = ""

    if is_newlineremover == "on":
        for ch in temp:
            if ch != '\n' and ch != '\r':
                analyzed_text = analyzed_text + ch

    if analyzed_text != "":
        temp = analyzed_text

    analyzed_text = "" 

    if is_puncremoved == 'on':
        for ch in temp:
            if ch not in punc:
                analyzed_text = analyzed_text + ch

    if analyzed_text != "":
        temp = analyzed_text
    analyzed_text = ""

    if is_uppercase == "on":
        analyzed_text = temp.upper()

    if analyzed_text != "":
        temp = analyzed_text
    
    analyzed_text = ""

    if is_extraspaceremoved == "on":
        for index, ch in enumerate(temp):
            if temp[index] == ' ' and temp[index+1] == ' ':
                pass
            else:
                analyzed_text =  analyzed_text + ch
    if analyzed_text != "":
        return analyzed_text
    else:
        return temp

def analyze(request):
    text = request.POST.get('text', 'default')
    is_puncremoved = request.POST.get('removepunc', 'off')
    is_uppercase = request.POST.get('UPPERCASE', 'off')
    is_newlineremover = request.POST.get('removenewliner', 'off')
    is_extraspaceremoved = request.POST.get('removeextraspace', 'off')
    if is_uppercase == "on" or is_puncremoved == "on" or is_newlineremover == "on" or is_extraspaceremoved == "on":
        analyzed_text = convert_str(is_puncremoved, is_uppercase, is_newlineremover, is_extraspaceremoved, text)
        print(analyzed_text)
        params = {"analyzed_text": analyzed_text}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')
