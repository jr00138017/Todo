from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login



def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})

    else:
        # Create a new User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),'error': 'That user name has already been taken. Please choose a new username'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error':'Password did not match'})
            # Tell the user the passwords didn't match

def currenttodos(request):
    pass