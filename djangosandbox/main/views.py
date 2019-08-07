import csv, io

from docxtpl import DocxTemplate

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from .forms import DocForm

from .models import Page
from .Student import Stud

st = Stud()



def is_valid_queryPar(param):
    return param != '' and param is not None

# def generate_docx(request):
#     qs = Page.objects.all

def homepage(request):
    qs = Page.objects.all()
    page_id_query = request.GET.get('unique_id')
    print(page_id_query)
    if is_valid_queryPar(page_id_query):
        print("Done")
    page_name_query = request.GET.get('text-unique')
    page_gradYear_query = request.GET.get('select-box')
    if is_valid_queryPar(page_name_query):
        qs = qs.filter(page_name__icontains = page_name_query )
    if is_valid_queryPar(page_gradYear_query):
        qs = qs.filter(page_gradYear = page_gradYear_query)
    context = {
        'students': qs
    }

    print(page_name_query, page_gradYear_query)
    return render(request, 'main/home.html', context)


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
            if row[st.nationality] == st.is_foreign:
                _, created = Page.objects.update_or_create(
                    page_id = row[st.id],
                    page_name = row[st.name],
                    page_birth = row[st.birth],
                    page_nationality = row[st.nationality],
                    page_nameEn = row[st.en_stud_name],
                    page_gradYear = row[st.stud_end_year],
                    page_formOfStudy = row[st.form_of_study],
                    page_specialty = row[st.stud_spec],
                    page_prevDoc = row[st.stud_prev_document],
                    # page_country is not available
                    slug = row[st.id],
                )
        # if uploaded_file.file.name.endswith('.csv'):
            # outData = csv.reader(uploaded_file, delimiter=';', quotechar='"')
            # print(outData[1])
        print(uploaded_file)
        print(uploaded_file.size)
    return render(request, "main/upload.html")

def doc_gen(request, slug):
    unique_post = get_object_or_404(Page, slug=slug)
    form = DocForm(request.POST or None,
                    instance=unique_post)
    if form.is_valid():
        form.save()
        htp = request.build_absolute_uri().split('/')[0]
        domain = request.build_absolute_uri().split('/')[2]
        url = htp + '//' + domain
        messages.info(request, url)
        return redirect(url + '/static/Template.docx')
    
    context = {
        'form': form
    }
    
    return render(request, 'main/detail.html', context)

# Create your views here.
