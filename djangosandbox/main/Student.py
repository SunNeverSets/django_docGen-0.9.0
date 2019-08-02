class Stud():
    """
    Stud propeties
    """
    def __init__(self):
        self.col_const = 47
        self.id = 1
        self.name = 5
        self.birth = 6
        self.nationality = 13
        self.en_stud_name = 14
        self.stud_end_year = 16
        self.form_of_study = 22
        self.stud_spec = 26
        self.stud_prev_document = 42
        self.ver_heading = ['blank','Diploma_id', 'Supp_id', 'Ukr_Name', 
            'Ukr_Surname', 'End_Name', 'End_Surname', 'BirthDate', 'Proj_Ukr', 
            'Proj_Eng', 'Diploma_Uk', 'Diploma_En', 'Nostr_uk', 'Nostr_eng', 
            '----']
        self.filename_full_time = "Supp_Info_Full_Time.xlsx"
        self.filename_part_time = "Supp_Info_Part_Time.xlsx"

        self.endyearlist = [2019, 2020, 2021, 2020]
        
    def get_heading(self, locList):
        """
        Gets the heading with all the parameters
        """
        outList = []
        for i in range(len(locList[0])):
            outList.append(locList[0][i])
        return outList 