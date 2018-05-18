from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.shortcuts import redirect
from . import views

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/website/profile/')
    else:
        form = AuthenticationForm()
    return render(request,'website/login.html',{'form':form})

def listagem(request):
    render(request, 'ListaCursos.html')
