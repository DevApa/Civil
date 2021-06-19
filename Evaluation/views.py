from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'Evaluation/index.html')

def contacts(request):

    return render(request,'Evaluation/contacts.html')
