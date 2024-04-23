from django.shortcuts import render, redirect
import pyrebase
from firebase_admin import auth

Config = {
   #apikey aqui.
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()


def Logar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return redirect('home')
        except:
            return render(request, 'Login.html', {'error': 'Credenciais inválidas!'})
    else:
        return render(request, 'Login.html')
    
def Cadastrar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            return redirect('login')
        except:
            return render(request, 'Cadastrar.html', {'error': 'Credenciais inválidas!'})
    else:
        return render(request, 'Cadastrar.html')


def Home(request):
    return render(request, 'Home.html')
       