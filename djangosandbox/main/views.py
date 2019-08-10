import csv
import io
import os
import glob
import time

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
    if is_valid_queryPar(page_name_query):
        qs = qs.filter(page_name__icontains=page_name_query)
    if is_valid_queryPar(page_gradYear_query):
        qs = qs.filter(page_gradYear=page_gradYear_query)
    if is_valid_queryPar(page_faculty_query):
        qs = qs.filter(page_faculty=page_faculty_query)
    if is_valid_queryPar(page_eduLevel_query):
        if page_eduLevel_query == 'bh':
            qs = qs.filter(page_eduLevel= st.bh)
        elif page_eduLevel_query == 'ma':
            qs = qs.filter(page_eduLevel= st.ma)
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
        doc_type_list = [
                'en_template.docx', 
                'uk_template.docx', 
                'fr_template.docx', 
                'ru_template.docx'
                ]
        # Delete all prev unneeded files
        file_list = glob.glob(settings.BASE_DIR + '\\main\\static\\*.docx')
        for file in file_list:
            # print(os.path.basename(file)[:2])
            if os.path.basename(file) not in doc_type_list:
                os.remove(file)
                

        # Get basic domain name
        dn = get_basic_DN(request)
        # document creation

        
        
        currentPage_docPath = create_doc(form)
        

        messages.info(request, "Ducument created")
        #  redirect(dn + f"/static/{form.cleaned_data['page_nameEn']}.docx")

        # os.remove(current_docPath)

    context = {
        'form': form
    }

    return render(request, 'main/detail.html', context)


'''
        HANDY FUNCTIONS
'''


def is_valid_queryPar(param):
    return param != '' and param is not None

def get_basic_DN(request):
    htp = request.build_absolute_uri().split('/')[0]
    domain = request.build_absolute_uri().split('/')[2]
    url = htp + '//' + domain
    return url


def create_doc(form):
    if form.cleaned_data['doc_type'] == 'en':
        return create_docEnglish(form)
    elif form.cleaned_data['doc_type'] == 'uk':
        return create_docUkrainian(form)
    # if document is English


def create_docEnglish(form):
    doc_path = settings.BASE_DIR + '\\main\\static\\en_template.docx'
    doc = DocxTemplate(doc_path)

    if form.cleaned_data['rector'] == 'dn':
        rc_type = 'First vice-rectot'
        rc_name = 'D.Chernyshev'
    elif form.cleaned_data['rector'] == 'kh':
        rc_type = 'Vice-rector'
        rc_name = 'O.Khomenko'

    if form.cleaned_data['page_eduLevel'] == st.bh:
        eduLevel = 'Bachelor'
        if form.cleaned_data['page_gradYear'] == '2020':
            course = 'fourth'
        elif form.cleaned_data['page_gradYear'] == '2021':
            course = 'third'
        elif form.cleaned_data['page_gradYear'] == '2022':
            course = 'second'
        elif form.cleaned_data['page_gradYear'] == '2023':
            course = 'first'
    elif form.cleaned_data['page_eduLevel'] == st.ma:
        eduLevel = 'Master'
        if form.cleaned_data['page_gradYear'] == '2020':
            course = 'first' 
        elif form.cleaned_data['page_gradYear'] == '2021':
            course = 'second' 

    if form.cleaned_data['page_gender'] == st.female:
        gender_1 = 'Her'
    elif form.cleaned_data['page_gender'] == st.male:
        gender_1 = 'His'
    
    if form.cleaned_data['page_faculty'] == st.fac_arch:
        faculty = 'architecture'
    elif form.cleaned_data['page_faculty'] == st.fac_const:
        faculty = 'construction'
    elif form.cleaned_data['page_faculty'] == st.fac_auto:
        faculty = 'automation and information technologies'
    elif form.cleaned_data['page_faculty'] == st.fac_geo:
        faculty = 'geoinforamtion systems and territorial management'
    elif form.cleaned_data['page_faculty'] == st.fac_budTech:
        faculty = 'tecnologico-construction'
    elif form.cleaned_data['page_faculty'] == st.fac_ingSyst:
        faculty = 'Engineering systems and ecology'
    elif form.cleaned_data['page_faculty'] == st.fac_urban:
        faculty = 'Urbanistins and environmental planning'

    if form.cleaned_data['page_formOfStudy'] == st.formOfSt_full:
        formOfStudy = 'full-time'
    elif form.cleaned_data['page_formOfStudy'] == st.formOfSt_part:
        formOfStudy = 'part-time'
        # add bh and master course correction 
    elif form.cleaned_data['page_formOfStudy'] == st.formOfSt_evening:
        formOfStudy = 'Вечірня????-_- к такому меня жизнь не готовила'
    
    time_string = form.cleaned_data['page_studFinish']
    grad_time = time.strptime(time_string, "%d.%m.%Y")
    if grad_time.tm_mon == 6:
        finish_time = f"June, {grad_time.tm_year}"
    elif grad_time.tm_mon == 2:
        finish_time = f"Feb, {grad_time.tm_year}"
    elif grad_time.tm_mon == 12:
        finish_time = f"Dec, {grad_time.tm_year}"

    if form.cleaned_data['page_specialty'][:3] == '191':
        specialty = "191 \"Architecture and Urban Development\""
    elif form.cleaned_data['page_specialty'][:3] == '192':
        specialty = '192 \"Construction and Civil Engineering\"'
    elif form.cleaned_data['page_specialty'][:3] == '073':
        specialty = '073 \"Management\"'

    # if form.cleaned_data['page_gradYear'] == 

    
    nameEn_parced = form.cleaned_data['page_nameEn'].split(' ')
    nameEn = ''
    for word in nameEn_parced:
        if word != '-':
            nameEn += word + ' '


    if form.cleaned_data['country'] == 'mr':
        country = 'Morocco'
    elif form.cleaned_data['country'] == 'tr':
        country = 'Turkey'

    doc_context = {
        'country': country,
        'name': nameEn,
        'grade': course,
        'study_form': formOfStudy,
        'faculty': faculty,
        'gender': gender_1,
        'specialty': specialty,
        'education_degree': eduLevel,     
        'grad_year': finish_time,
        'rector_type': rc_type,
        'rector_name': rc_name,
    }

    doc.render(doc_context)
    doc.save(settings.BASE_DIR + f"\main\static\{form.cleaned_data['page_nameEn']}.docx")

    return (settings.BASE_DIR + f"\main\static\{form.cleaned_data['page_nameEn']}.docx")

def create_docUkrainian(form):
    doc_path = settings.BASE_DIR + '\\main\\static\\uk_template.docx'
    doc = DocxTemplate(doc_path)

    if form.cleaned_data['rector'] == 'dn':
        rc_type = 'Перший  проректор'
        rc_name = 'Чернишов Д.О.'
    elif form.cleaned_data['rector'] == 'kh':
        rc_type = 'Проректор'
        rc_name = 'Хоменко А.А.'

    if form.cleaned_data['page_eduLevel'] == st.bh:
        eduLevel = '\"Бакалавр\"'
        if form.cleaned_data['page_gradYear'] == '2020':
            course = 'четвертого'
        elif form.cleaned_data['page_gradYear'] == '2021':
            course = 'третього'
        elif form.cleaned_data['page_gradYear'] == '2022':
            course = 'другого'
        elif form.cleaned_data['page_gradYear'] == '2023':
            course = 'першого'
    elif form.cleaned_data['page_eduLevel'] == st.ma:
        eduLevel = '\"Магіст\"'
        if form.cleaned_data['page_gradYear'] == '2020':
            course = 'першого' 
        elif form.cleaned_data['page_gradYear'] == '2021':
            course = 'другого' 

    if form.cleaned_data['page_gender'] == st.female:
        gender_1 = 'грамадянинці'
        gender_2 = 'вона'
    elif form.cleaned_data['page_gender'] == st.male:
        gender_1 = 'громадянину'
        gender_2 = 'він'
    
    if form.cleaned_data['page_faculty'] == st.fac_arch:
        faculty = 'архітектурного'
    elif form.cleaned_data['page_faculty'] == st.fac_const:
        faculty = 'будівельного'
    elif form.cleaned_data['page_faculty'] == st.fac_auto:
        faculty = 'автоматизації та інформаційних технологій'
    elif form.cleaned_data['page_faculty'] == st.fac_geo:
        faculty = 'Геоінформаційних систем і управління територіями'
    elif form.cleaned_data['page_faculty'] == st.fac_budTech:
        faculty = 'Будівельно-технологічний'
    elif form.cleaned_data['page_faculty'] == st.fac_ingSyst:
        faculty = 'Інженерних систем та екології'
    elif form.cleaned_data['page_faculty'] == st.fac_urban:
        faculty = 'Урбаністики та просторового планування'

    if form.cleaned_data['page_formOfStudy'] == st.formOfSt_full:
        formOfStudy = 'денної'
    elif form.cleaned_data['page_formOfStudy'] == st.formOfSt_part:
        formOfStudy = 'заочної'
        # add bh and master course correction 
    elif form.cleaned_data['page_formOfStudy'] == st.formOfSt_evening:
        formOfStudy = 'Вечірня????-_- к такому меня жизнь не готовила'
    
    time_string = form.cleaned_data['page_studFinish']
    grad_time = time.strptime(time_string, "%d.%m.%Y")
    if grad_time.tm_mon == 6:
        finish_time = f"червні, {grad_time.tm_year}"
    elif grad_time.tm_mon == 2:
        finish_time = f"лютому, {grad_time.tm_year}"
    elif grad_time.tm_mon == 12:
        finish_time = f"грудень, {grad_time.tm_year}"

    if form.cleaned_data['page_specialty'][:3] == '191':
        specialty = "191 \"Архітектура та містобудування\""
    elif form.cleaned_data['page_specialty'][:3] == '192':
        specialty = '192 \"Будівництво та цивільна інженерія\"'
    elif form.cleaned_data['page_specialty'][:3] == '073':
        specialty = '073 \"Менеджмент\"'

    # if form.cleaned_data['page_gradYear'] == 

    
    nameEn_parced = form.cleaned_data['page_name'].split(' ')
    nameEn = ''
    for word in nameEn_parced:
        if word != '-':
            nameEn += word + ' '


    if form.cleaned_data['country'] == 'mr':
        country = 'Королівства Марокко'
    elif form.cleaned_data['country'] == 'tr':
        country = 'Турецької Республіки'

    doc_context = {
        'country': country,
        'name': nameEn,
        'grade': course,
        'study_form': formOfStudy,
        'faculty': faculty,
        'gender_1': gender_1,
        'gender_2': gender_2,
        'specialty': specialty,
        'education_degree': eduLevel,     
        'grad_year': finish_time,
        'rector_type': rc_type,
        'rector_name': rc_name,
    }

    doc.render(doc_context)
    doc.save(settings.BASE_DIR + f"\main\static\{form.cleaned_data['page_name']}.docx")

    return (settings.BASE_DIR + f"\main\static\{form.cleaned_data['page_name']}.docx")

    # Create your views here.

