from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'test_app/index.html',{"name":"my name is"})
