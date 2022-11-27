import pandas as pd
import sys
import csv

from software_check import *
from side_check import *

"""
xlsx 형식으로 되어있는 엑셀 파일을 읽어 csv 확장자로 변환하고,
내용을 읽어 전공과목과 교양과목으로 분류해 저장합니다.
형식은 다음과 같습니다.
major_clsses = List[Dict[]]

Usage:
sys.argv[1] = input file path (xlsx)
sys.argv[2] = your student id

$ python read_courses.py sample_data/전공별성적_20221125023802.xlsx 2019312493
"""

def check_remaining_credits (classes, curriculum):
    length = len(curriculum)
    lectures_credits_taken = [0 for j in range(length)]
    
    for lecture in classes:
        for i in range(length):
            # print(list(curriculum[i].values())[0])
            if lecture['name'] in list(curriculum[i].values())[0]:
                lectures_credits_taken[i] += lecture['credit']
                break
    
    return lectures_credits_taken

"""
after which_division_remains(), student_ID_list will be [0, -2, 0, -2, 0, 0, 0, -3, 0, -9] for example.
That means you need to take two more credits on leadership.
"""
def which_division_remains (student_ID_list, GE_list):
    for i in range(len(GE_list)):
        student_ID_list[i] -= GE_list[i]
        # GE_list[i] -= student_ID_list[i]
        
                

def main(file_path_arg, student_ID_arg):
    file_path = file_path_arg
    student_ID = student_ID_arg
    
    # file_path = sys.argv[1]
    # student_ID = sys.argv[2]

    admission_year = int(student_ID[:4]) # 입학 년도


    df = pd.read_excel(file_path)
    output_path=file_path.split('.xlsx')[0]+'.csv'
    df.to_csv(output_path)

    data = pd.read_csv(output_path)
    
    odd_rows = data.iloc[1::2,:].values.tolist() # 홀수번째 row만을 추출합니다

    major_classes = list() # 전공 과목
    GE_classes = list() # 교양 과목: general elective subject
    
    total_classes_names = []
    
    for row in odd_rows:
        lecture = {'name':row[4],'classification':row[5], 'credit':int(row[6]), 'grade':row[8]}
        total_classes_names.append(row[4])
        
        if row[6] == 'P':
            lecture['grade'] = 4.5
        if row[6] == 'F':
            lecture['grade'] = 0.0
        if lecture['classification'] == '전공':
            major_classes.append(lecture)
        if lecture['classification'] == '교양':
            GE_classes.append(lecture)
            
    total_credits_major = 0.0
    total_credits_GE = 0.0

    # print(odd_rows[2])
    # exit(0)
    # for row in odd_rows:
    #     lecture = {'name':row[3],'classification':row[4], 'credit':row[5], 'grade':row[7]}
        
    #     if row[6] == 'P':
    #         lecture['grade'] = 4.5
    #     if row[6] == 'F':
    #         lecture['grade'] = 0.0
    #     if lecture['classification'] == '전공':
    #         major_classes.append(lecture)
    #     if lecture['classification'] == '교양':
    #         GE_classes.append(lecture)
    
            
    total_credits_major = 0
    total_credits_GE = 0

    GPA_major = 0.0
    GPA_GE = 0.0
    GPA_total = 0.0

    for course in major_classes:
        total_credits_major += course['credit']
        GPA_major += course['credit'] * course['grade']

    for course in GE_classes:
        total_credits_GE += course['credit']
        GPA_GE += course['credit'] * course['grade']

    GPA_total = (GPA_major + GPA_GE) / (total_credits_major + total_credits_GE)
    GPA_major /= total_credits_major
    GPA_GE /= total_credits_GE

    
    experiment_credit = 0.0 # 실험실습.
    major_core_credit = 0.0 # 전공코어 (or 전공핵심).
    major_credit = 0.0 # 전공일반 (or 전공심화).

    if admission_year < 2021:
        experiment_credit = 14
        major_core_credit = 27
        major_credit = 24 
        for lecture in major_classes:
            if lecture['name'] in oldSoft[0]:
                major_core_credit -= lecture['credit']
            if lecture['name'] in oldSoft[1]:
                major_credit -= lecture['credit']
            if lecture['name'] in oldSoft[2]:
                experiment_credit -= lecture['credit']
                
    if admission_year >= 2021:
        experiment_credit = 6
        major_core_credit = 36
        major_credit = 21
        for lecture in major_classes:
            if lecture['name'] in newSoft[0]:
                major_core_credit -= lecture['credit']
            if lecture['name'] in newSoft[1]:
                major_credit -= lecture['credit']
            if lecture['name'] in newSoft[2]:
                experiment_credit -= lecture['credit']
                
    curriculum = None
    student_ID_list = []
    
    if admission_year <= 2016:
        curriculum = sixteenVersion
    if admission_year > 2016 and admission_year <= 2019:
        curriculum = seventeenVersion
    if admission_year == 2020:
        curriculum = secondVersion
    if admission_year > 2020:
        curriculum = thirdVersion
        
    student_ID_list = check_remaining_credits(GE_classes, curriculum)

    
    GE_16_list = [2,2,4,2,4,4,2,3,3,3,21]
    GE_17_19_list = [2,2,4,2,4,2,3,3,3,24]
    GE_20_list = [2,3,4,3,8,6,3,3,3,18]
    GE_21_22_list = [22,3,4,3,11,6,6,18]
    
    which_division_remains(student_ID_list, GE_17_19_list)
    """
    after which_division_remains(), student_ID_list will be [0, -2, 0, -2, 0, 0, 0, -3, 0, -9] for example.
    That means you need to take two more credits on leadership.
    """
    
    
    

    result_path = "./sample_data/" +  student_ID + "_result.txt"
    f = open(result_path, "w")
    f.write("student ID: %d\n\n" % int(student_ID))
    f.write("GPA_total: %f\n" % GPA_total)
    f.write("GPA_major: %f\n" % GPA_major)
    f.write("GPA_GE: %f\n" % GPA_GE)
    f.write("\n")
    f.write("credits_total: %d\n" % (total_credits_major + total_credits_GE))
    f.write("credits_major: %d\n" % total_credits_major)
    f.write("credits_GE: %d\n" % total_credits_GE)
    f.write("\n")
    f.write("remaining_major_core_credit: %d\n" % major_core_credit)
    f.write("remaining_major_credit: %d\n" % major_credit)
    f.write("remaining_experiment_credit: %d\n" % experiment_credit)
    f.write("\nGE left:\n")
    for i in range(len(student_ID_list)):
        # f.write("%d " % student_ID_list[i])
        if student_ID_list[i] < 0:
            curriculum_name = list(curriculum[i].keys())[0]
            f.write("%s: " %  curriculum_name)
            curriculum_courses = curriculum[i][curriculum_name]
            for item in curriculum_courses:
                if item not in total_classes_names:
                    f.write("%s " % item)
            f.write("\n")
    
    f.close()
    
    


if __name__=='__main__':
    main()
