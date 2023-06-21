from django.test import TestCase

# Create your tests here.
def conditions(request):
    d={'a':5,'b':20,'c':50}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'Ankitha'}
    return render(request,'loop.html',d)