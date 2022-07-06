from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import *
from myapp.models import Book

# Create your views here.

def Home(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.POST['author']
        description = request.POST['description']

        all_book = Book(book_name=book_name, author=author,
                        description=description)
        all_book.save()
    all_book = Book.objects.all()
    return render(request, 'home.html', {'all_book': all_book})


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).first():
            messages.info(request, "Username already found")
            return redirect('register')

        if User.objects.filter(email=email).first():
            messages.info(request, "Email id already found")
            return redirect('register')
        else:
            usr = User.objects.create(username=username, email=email)
            usr.set_password(password)
            usr.save()
            return redirect('register')

    return render(request, 'register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usr = User.objects.filter(username=username).first()
        if not usr:
            messages.info(request, "Username not found")
            return redirect('login')

        else:
            usr = authenticate(request, username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('home')
            else:
                messages.info(request, "Invalid Password")
                return redirect('login')

    return render(request, 'login.html')


def delete_view(request, id):
    dlt = Book.objects.get(pk=id)
    dlt.delete()
    return redirect('home')


def update(request, id):
    if request.method == 'POST':
        updt = Book.objects.get(pk=id)
        frm = BookForm(request.POST, instance=updt)
        if frm.is_valid():
            frm.save()
    else:
        updt = Book.objects.get(pk=id)
        frm = BookForm(instance=updt)

    return render(request, 'update.html', {'frm': frm})


def logout_data(request):
    logout(request)
    return redirect('home')
