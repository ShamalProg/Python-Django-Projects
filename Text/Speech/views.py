from django.shortcuts import render

# Create your views here.
import pyttsx3
from django.shortcuts import render
def converter(request):
    text=pyttsx3.init()
    name=request.POST.get('name')
    text.say(name)
    return render(request,'next.html',text.runAndWait())
