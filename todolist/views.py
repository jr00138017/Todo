from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.models import User

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})

    else:
        # Create a new User
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
            User.save()
        else:
            print("hello")
            # Tell the user the passwords didn't match

