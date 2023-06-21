from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':5,'b':20,'c':50}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'Ankitha'}
    return render(request,'loop.html',d)