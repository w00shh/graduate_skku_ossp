import pandas as pd
import sys
import csv

"""
xlsx 형식으로 되어있는 엑셀 파일을 읽어 csv 확장자로 변환하고,
내용을 읽어 전공과목과 교양과목으로 분류해 저장합니다.
형식은 다음과 같습니다.
major_clsses = List[Dict[]]
"""

file_path = sys.argv[1]
df = pd.read_excel(file_path)
output_path=file_path.split('.xlsx')[0]+'.csv'
df.to_csv(output_path)

data = pd.read_csv(output_path)

odd_rows = df.iloc[1::2,:] # 홀수 번째 row만을 추출합니다.

odd_rows = odd_rows.values.tolist()

major_classes = list() # 전공 과목
GE_classes = list() # 교양 과목 영어로: general elective subject


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
        
        
print(major_classes)
print(GE_classes)