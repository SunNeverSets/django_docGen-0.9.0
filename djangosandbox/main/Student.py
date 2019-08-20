class Stud():
    """
    Stud propties
    """
    
    def __init__(self):
        self.col_const = 47
        self.id = 1
        self.name = 5
        self.birth = 6
        self.gender = 12
        self.nationality = 13
        self.en_stud_name = 14
        self.stud_end_year = 16
        self.finish_study = 18
        self.faculty = 19
        self.edu_level = 20
        self.form_of_study = 22
        self.stud_spec = 26
        self.edu_prog = 28
        self.stud_prev_document = 42
        self.ver_heading = ['blank','Diploma_id', 'Supp_id', 'Ukr_Name', 
            'Ukr_Surname', 'End_Name', 'End_Surname', 'BirthDate', 'Proj_Ukr', 
            'Proj_Eng', 'Diploma_Uk', 'Diploma_En', 'Nostr_uk', 'Nostr_eng', 
            '----']
        self.filename_full_time = "Supp_Info_Full_Time.xlsx"
        self.filename_part_time = "Supp_Info_Part_Time.xlsx"
    
        self.endyearlist = [2019, 2020, 2021, 2020]
        self.is_foreign = 'Ні'    
        self.is_ukrainian = 'Так'    

        self.female = 'Жіноча'
        self.male = 'Чоловіча'

        self.bh = 'Бакалавр'
        self.ma = 'Магістр'

        self.fac_arch = 'Архітектурний'
        self.fac_const = 'Будівельний'
        self.fac_auto = 'Автоматизації та інформаційних технологій'
        self.fac_geo = 'Геоінформаційних систем і управління територіями'
        self.fac_budTech = 'Будівельно-технологічний'
        self.fac_ingSyst = 'Інженерних систем та екології'
        self.fac_urban = 'Урбаністики та просторового планування'

        self.rectorType_transDic = {
            'dn': {
                'en': 'First vice-rector',
                'uk': 'Перший проректор',
                'ru': '',
                'fr': '',
            },
            'kh': {
                'en': 'Vice-rector',
                'uk': 'Проректор',
                'ru': '',
                'fr': '',
            }
        }
        self.rectorName_transDic = {
            'dn': {
                'en': 'D.Chernyshev',
                'uk': 'Чернишов Д.О.',
                'ru': '',
                'fr': '',
            },
            'kh': {
                'en': 'D.Chernyshev',
                'uk': 'Хоменко А.А.',
                'ru': '',
                'fr': '',
            }
        }
        self.specialty_transDic = {
            '191 Архітектура та містобудування':{
                'en': "191 \"Architecture and Urban Development\"",    
                'uk': "191 \"Архітектура та містобудування\"",
                'ru': 'Russian',
                'fr': 'French',
            },
            '192 Будівництво та цивільна інженерія':{
                'en': '192 \"Construction and Civil Engineering\"',    
                'uk': '192 \"Будівництво та цивільна інженерія\"',
                'ru': 'Russian',
                'fr': 'French',
            },
            '023 Образотворче мистецтво, декоративне мистецтво, реставрація':{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            '141 Електроенергетика, електротехніка та електромеханіка':{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            '073 Менеджмент':{
                'en': '073 \"Management\"',    
                'uk': '073 \"Менеджмент\"',
                'ru': 'Russian',
                'fr': 'French',
            },
            '193 Геодезія та землеустрій':{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            "122 Комп'ютерні науки":{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            '051 Економіка':{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            "151 Автоматизація та комп’ютерно-інтегровані технології":{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            '133 Галузеве машинобудування':{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            "122 Комп’ютерні науки та інформаційні технології":{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
            '022 Дизайн':{
                'en': 'English',    
                'uk': 'Ukrainian',
                'ru': 'Russian',
                'fr': 'French',
            },
        }

        self.faculty_transDic = {
            'Архітектурний':{
                'en': 'architecture',
                'uk': 'архітектурного факультету',
                'ru': 'архитектурного факультета',
                'fr': '---'
            },
            'Будівельний':{
                'en': 'construction',
                'uk': 'будівельного факультету',
                'ru': 'строительного факультета',
                'fr': '---'
            },
            'Автоматизації та інформаційних технологій':{
                'en': 'automation and integrated technologies',
                'uk': 'факультету автоматизації та інформаційних технологій',
                'ru': 'факультета автоматизации и информационных технологий',
                'fr': '---'
            },
            'Геоінформаційних систем і управління територіями':{
                'en': 'geoinformation systems and territorial management',
                'uk': 'факультету геоінформаційних систем і управління територіями',
                'ru': 'факультета геоинформационных систем и управления территориями',
                'fr': '---'
            },
            'Будівельно-технологічний':{
                'en': 'construction and technological',
                'uk': 'будівельно-технологічного факультету',
                'ru': 'строительно-технологического факультета',
                'fr': '---'
            },
            'Інженерних систем та екології':{
                'en': 'systems engineering and ecology',
                'uk': 'факультету інженерних систем та екології',
                'ru': 'факультета инженерных систем и экологии',
                'fr': '---'
            },
            'Урбаністики та просторового планування':{
                'en': 'urban and spatial planning',
                'uk': 'факультету урбаністики та просторового планування',
                'ru': 'факультета урбанистики и территориального планирования',
                'fr': '---'
            }
        }

        self.studForm_transDic = {
            'Денна': {
                'en': 'full-time',
                'uk': 'денної',
                'ru': 'дневной',
                'fr': '',
            },
            'Заочна': {
                'en': 'part-time',
                'uk': 'заочної',
                'ru': 'заочной',
                'fr': '',
            },
            'Вечірня': {
                'en': '---',
                'uk': '---',
                'ru': '---',
                'fr': '---',
            },
        }

        self.countries_transDic = {
            'mr':{
                'en': 'Morocco',
                'uk': 'Королівств Марокко',
                'ru': 'Королевство Марокко',
                'fr': '',
            },
            'tr':{
                'en': 'Turkey',
                'uk': 'Турецька Республіка',
                'ru': 'Турецкая Республика',
                'fr': '',
            },
        }
        self.eduLevel_transDic = {
            self.bh: {
                'en': 'Bachelor',
                'uk': '\"Магіст\"',
                'ru': '\"Магистр\"',
                'fr': '',
            },
            self.ma: {
                'en': 'Master',
                'uk': '\"Магіст\"',
                'ru': '\"Бакалавр\"',
                'fr': '',
            }
        }
        
        self.courseFullBh_transDic = {
            '2020':{
                'en': 'fourth',
                'uk': 'четвертого',
                'ru': '',
                'fr': '',
            },
            '2021':{
                'en': 'third',
                'uk': 'третього',
                'ru': '',
                'fr': '',
            },
            '2022':{
                'en': 'second',
                'uk': 'другого',
                'ru': '',
                'fr': '',
            },
            '2023':{
                'en': 'first',
                'uk': 'першого',
                'ru': '',
                'fr': '',
            }
        }
        self.coursePartBh_transDic = {
            '2020':{
                'en': 'fifth',
                'uk': "п'ятого",
                'ru': '',
                'fr': '',
            },
            '2021':{
                'en': 'fourth',
                'uk': 'четвертого',
                'ru': '',
                'fr': '',
            },
            '2022':{
                'en': 'third',
                'uk': 'третього',
                'ru': '',
                'fr': '',
            },
            '2023':{
                'en': 'second',
                'uk': 'другого',
                'ru': '',
                'fr': '',
            },
            '2024':{
                'en': 'first',
                'uk': 'першого',
                'ru': '',
                'fr': '',
            }
        }
        self.courseMa_transDic = {
            '2020':{
                'en': 'second',
                'uk': "другого",
                'ru': '',
                'fr': '',
            },
            '2021':{
                'en': 'first',
                'uk': 'першого',
                'ru': '',
                'fr': '',
            },
        }

        self.formOfSt_full = 'Денна'
        self.formOfSt_part = 'Заочна'
        self.formOfSt_evening = 'Вечірня'

    def get_gradYear(self, form, level, year, language):
        """Returns a valid current year 
        args: form, level, year, language
        """
        if level == self.bh:
            if form == self.formOfSt_part:
                return self.coursePartBh_transDic[year][language]
            elif form == self.formOfSt_full:
                return self.courseFullBh_transDic[year][language]
        else:
            return self.courseMa_transDic[year][language]

    def get_heading(self, locList):
        """
        Gets the heading with all the parameters
        """
        outList = []
        for i in range(len(locList[0])):
            outList.append(locList[0][i])
        return outList 