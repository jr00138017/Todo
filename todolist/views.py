from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .form import TodoForm
from .models import Todo


def home(request):
    return render(request, 'todo/home.html')


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
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'That user name has already been taken. Please choose a new username'})
        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Password did not match'})
            # Tell the user the passwords didn't match


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'todo/login.html', {'form': AuthenticationForm(), 'error': 'User is not exists'})
        else:
            login(request, user)
            return redirect('currenttodos')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodoform = form.save(commit=False)
            newtodoform.user = request.user
            newtodoform.save()
            return redirect('currenttodos')
        except:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error': 'Bad data, Try again.'})


def currenttodos(request):
    # 只顯示當前使用者的todo
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)

    return render(request, 'todo/currenttodos.html', {'todos': todos})


def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    form = TodoForm(todo_pk)

    return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
