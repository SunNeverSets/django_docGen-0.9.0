class Stud():
    """
    Stud propeties
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

        self.specialty_transDic = {
            '191':{
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

        self.formOfSt_full = 'Денна'
        self.formOfSt_part = 'Заочна'
        self.formOfSt_evening = 'Вечірня'
    def get_heading(self, locList):
        """
        Gets the heading with all the parameters
        """
        outList = []
        for i in range(len(locList[0])):
            outList.append(locList[0][i])
        return outList 