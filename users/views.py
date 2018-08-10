from .models import Profile
from .forms import RegisterUser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def registerUser(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form['username'].value(),
                             email=form['email'].value(),
                             password=form['password'].value())
            user.save(commit=False)
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('users:login')
    else:
        form = RegisterUser()
        print (form.errors)
    return render(request, '../templates/registration/cadastro.html', {'form': form})
