import pandas as pd
import sys
import csv

from software_check import *

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

file_path = sys.argv[1]
student_ID = sys.argv[2]

admission_year = int(student_ID[:4]) # 입학 년도


df = pd.read_excel(file_path)
output_path=file_path.split('.xlsx')[0]+'.csv'
df.to_csv(output_path)

data = pd.read_csv(output_path)

odd_rows = df.iloc[1::2,:].values.tolist() # 홀수번째 row만을 추출합니다


major_classes = list() # 전공 과목
GE_classes = list() # 교양 과목: general elective subject


for row in odd_rows:
    lecture = {'name':row[3],'classification':row[4], 'credit':row[5], 'grade':row[7]}
    
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

    
# print(GPA_major)
# print(GPA_GE)
# print(GPA_total)

experiment_credit = 0.0 # 실험실습.
major_core_credit = 0.0 # 전공코어 (or 전공핵심).
major_credit = 0.0 # 전공일반 (or 전공심화).

# if admission_year < 2021:
#     print(oldSoft)

result_path = "./sample_data/" +  student_ID + "_result.txt"
f = open(result_path, "w")
f.write("GPA_total: %f\n" % GPA_total)
f.write("GPA_major: %f\n" % GPA_major)
f.write("GPA_GE: %f\n" % GPA_GE)
f.write("\n")
f.write("credits_total: %f\n" % (total_credits_major + total_credits_GE))
f.write("credits_major: %f\n" % total_credits_major)
f.write("credits_GE: %f\n" % total_credits_GE)

f.close()