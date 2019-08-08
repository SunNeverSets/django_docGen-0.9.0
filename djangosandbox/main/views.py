import csv
import io
import os

from docxtpl import DocxTemplate

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
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


@login_required(login_url='main:login')
def homepage(request):
    qs = Page.objects.all()
    page_id_query = request.GET.get('unique_id')
    facultiesList = qs.values_list('page_faculty', flat=True).distinct()

    page_name_query = request.GET.get('text-unique')
    page_gradYear_query = request.GET.get('select-box1')
    page_faculty_query = request.GET.get('select-box2')
    page_eduLevel_query = request.GET.get('select-box3')
    print(page_faculty_query + ' here ')
    if is_valid_queryPar(page_name_query):
        qs = qs.filter(page_name__icontains=page_name_query)
    if is_valid_queryPar(page_gradYear_query):
        qs = qs.filter(page_gradYear=page_gradYear_query)
    if is_valid_queryPar(page_faculty_query):
        qs = qs.filter(page_faculty=page_faculty_query)
    if is_valid_queryPar(page_eduLevel_query):
        qs = qs.filter(page_eduLevel=page_eduLevel_query)
    context = {
        'students': qs,
        'faculties': facultiesList
    }

    return render(request, 'main/home.html', context)


# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"New Account Created: {username}")
#             login(request, user)
#             messages.info(request, f"You are now logged in as {username}")
#             return redirect("main:homepage")
#         else:
#             for msg in form.error_messages:
#                 messages.error(request, f"f{msg}: {form.error_messages[msg]}")

#     form = NewUserForm
#     return render(request, "main/register.html", {"form": form})\


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


@login_required(login_url='main:login')
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
                    page_id=row[st.id],
                    page_name=row[st.name],
                    page_birth=row[st.birth],
                    page_gender=row[st.gender],
                    page_nationality=row[st.nationality],
                    page_nameEn=row[st.en_stud_name],
                    page_gradYear=row[st.stud_end_year],
                    page_studFinish=row[st.finish_study],
                    page_faculty=row[st.faculty],
                    page_eduLevel=row[st.edu_level],
                    page_formOfStudy=row[st.form_of_study],
                    page_specialty=row[st.stud_spec],
                    page_eduProg=row[st.edu_prog],
                    page_prevDoc=row[st.stud_prev_document],
                    slug=row[st.id],
                )
        # if uploaded_file.file.name.endswith('.csv'):
            # outData = csv.reader(uploaded_file, delimiter=';', quotechar='"')
            # print(outData[1])
        print(uploaded_file)
        print(uploaded_file.size)
    return render(request, "main/upload.html")


@login_required(login_url='main:login')
def doc_gen(request, slug):
    unique_post = get_object_or_404(Page, slug=slug)
    form = DocForm(request.POST or None,
                   instance=unique_post)
    if form.is_valid():
        form.save()
        # Get basic domain name
        dn = get_basic_DN(request)
        # document creation

        if form.cleaned_data['doc_type'] == 'en':
            doc_path = settings.BASE_DIR + '\main\static\en_template.docx'
        elif form.cleaned_data['doc_type'] == 'uk':
            doc_path = settings.BASE_DIR + '\main\static\en_template.docx'

        doc = DocxTemplate(doc_path)

        current_docPath = create_doc(form, doc)
        doc.save(current_docPath)

        messages.info(request, "Success")
        print(form.cleaned_data['doc_type'])
        return redirect(dn + f"/static/{form.cleaned_data['page_nameEn']}.docx")

        os.remove(current_docPath)

    context = {
        'form': form
    }

    return render(request, 'main/detail.html', context)


def get_basic_DN(request):
    htp = request.build_absolute_uri().split('/')[0]
    domain = request.build_absolute_uri().split('/')[2]
    url = htp + '//' + domain
    return url


def create_doc(form, doc):

    if form.cleaned_data['rector'] == 'dn':
        rc_type = 'First vice-rectot'
        rc_name = 'D.Chernyshev'
    doc_context = {
        'country': form.cleaned_data['country'],
        'name': form.cleaned_data['page_nameEn'],
        'grade': form.cleaned_data['page_gradYear'],
        'study_form': form.cleaned_data['page_formOfStudy'],
        'faculty': form.cleaned_data['page_faculty'],
        'gender': form.cleaned_data['page_gender'],
        'specialty': form.cleaned_data['page_specialty'],
        'education_degree': form.cleaned_data['page_eduLevel'],
        'grad_year': form.cleaned_data['page_studFinish'],
        'rector_type': rc_type,
        'rector_name': rc_name,
    }
    doc.render(doc_context)
    return (settings.BASE_DIR + f"\main\static\{form.cleaned_data['page_nameEn']}.docx")


# Create your views here.
