from django.shortcuts import render

# Create your views here.
def example1(request):
    return render(request,'example1.html',{})
