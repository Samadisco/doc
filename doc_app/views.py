from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "doc_app/index.html")  

def case_history(request):
    return render(request, "doc_app/case_history.html") 

def dashboard(request):
    return render(request, "doc_app/dashboard.html") 

def main(request):
    return render(request, "doc_app/main.html") 

def va(request):
    return render(request, "doc_app/va.html") 

def vitals(request):
    return render(request, "doc_app/vitals.html")  
