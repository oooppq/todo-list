from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == "GET": return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user != None:
            print('check')
            auth.login(request, user)
            return redirect('home')
        else: return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def register(request):
    if request.method ==  'GET': return render(request, 'register.html')
    if request.method == 'POST':
        username =  request.POST['username']
        password =  request.POST['password']
        password2 = request.POST['password2']
        ln = request.POST['lastName']
        fn = request.POST['firstName']
        if password != password2:
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=username, password=password, last_name=ln, first_name=fn)
            auth.login(request, user)
            return redirect('home')
        
        