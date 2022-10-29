from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "doc_app/index.html")  

def case_history(request):
    return render(request, "doc_app/case_history.html") 

def dashboard(request):
    if request.method =="POST":
        print(request.POST)
          
        #     print(i['temperature'])
            # print(request.POST)
        # age = request.POST['age']
        # print(age)
        # print('Heyyyy')
    
    return render(request, "doc_app/dashboard.html") 

def main(request):
    return render(request, "doc_app/main.html") 

def va(request):
    return render(request, "doc_app/va.html") 

def vitals(request):
    return render(request, "doc_app/vitals.html")  

def post_handler(request):
    if request.method =="POST":
        print('post method is working')
    
    return render(request, "doc_app/index.html")     
