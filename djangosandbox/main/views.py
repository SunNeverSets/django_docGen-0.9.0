import csv, io

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

from .models import Page

from .Student import Stud

st = Stud()

def homepage(request):
    return render(request, 'main/home.html', {'students': Page.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else: 
            for msg in form.error_messages:
                messages.error(request, f"f{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request, "main/register.html", {"form": form})\


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logger out")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else: 
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "main/login.html", {'form': form})

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        unpacked_file = uploaded_file.read().decode('ANSI')
        io_string = io.StringIO(unpacked_file)

        uploaded_data = csv.reader(io_string, delimiter=';')

        i = 0        
        for row in uploaded_data:
            print(len(row))
            _, created = Page.objects.update_or_create(
                page_id = row[st.id],
                page_name = row[st.name],
                page_birth = row[st.birth],

            )
            i += 1
            if  i == 7: 
                break
        # if uploaded_file.file.name.endswith('.csv'):
            # outData = csv.reader(uploaded_file, delimiter=';', quotechar='"')
            # print(outData[1])
        print(uploaded_file)
        print(uploaded_file.size)
    return render(request, "main/upload.html")

# Create your views here.
