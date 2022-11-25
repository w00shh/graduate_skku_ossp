#2017~2020학번은 전공핵심, 전공일반, 실험실습 순으로 27/24/14 학점 필요, 2차원 배열로 전공핵심, 전공일반, 실험실습을 나눈상태
oldSoft = [['데이터베이스개론', '소프트웨어공학개론', '시스템프로그램', '알고리즘개론', '운영체제', '자료구조개론', '컴퓨터구조개론', '컴퓨터네트웍개론', '프로그래밍언어'],
             ['기계학습원론', '문제해결', '인공지능개론', 'AI캡스톤디자인', 'HCI개론', 'ICT사업운영론', 'ICT스타트업', '디지털논리회로', '멀티코어컴퓨팅',
             '멀티코어컴퓨팅', '모델링과시뮬레이션', '빅데이터분석방법론', '산학협력프로젝트1', '산학협력프로젝트2', '산학협력프로젝트3', '소프트웨어세미나', '소프트웨어연구학점1',
             '소프트웨어연구학점2', '소프트웨어연구학점3', '소프트웨어연구학점4', '소프트웨어연구학점5', '소프트웨어창업현장실습1', '소프트웨어창업현장실습2',
             '소프트웨어특강1', '소프트웨어특강2', '소프트웨어현장실습1', '소프트웨어현장실습2', '소프트웨어현장실습3', '소프트웨어현장실습4',
             '심층신경망개론', '오토마타', '인터넷서비스와정보보호', '임베디드소프트웨어개론', '정보보호개론', '캡스톤설계프로젝트', '컴퓨터개론', '컴퓨터그래픽스개론',
             '컴퓨터비전개론', '프로그래밍입문', '확률과랜덤프로세스'], ['JAVA프로그래밍실습', '네트워크프로젝트', '데이터베이스프로젝트', '모바일앱프로그래밍실습',
             '시스템프로그래밍실습', '오픈소스소프트웨어실습', '웹프로그래밍실습', '인공지능프로젝트', '임베디드시스템프로젝트']]
#2021, 2022학번은 전공코어, 전공심화, 실험실습 순으로 36/21/6 학점 필요, 2차원 배열로 전공코어, 전공심화, 실험실습을 나눈상태
#문제해결, 인공지능개론, 기계학습원론만 전공코어이지만 전공일반으로 취급하므로 배열을 다르게 만든상태
newSoft = [['데이터베이스개론', '소프트웨어공학개론', '시스템프로그램', '알고리즘개론', '운영체제', '자료구조개론', '컴퓨터구조개론', '컴퓨터네트웍개론', '프로그래밍언어',
             '기계학습원론', '문제해결', '인공지능개론'], ['AI캡스톤디자인', 'HCI개론', 'ICT사업운영론', 'ICT스타트업', '디지털논리회로', '멀티코어컴퓨팅',
             '멀티코어컴퓨팅', '모델링과시뮬레이션', '빅데이터분석방법론', '산학협력프로젝트1', '산학협력프로젝트2', '산학협력프로젝트3', '소프트웨어세미나', '소프트웨어연구학점1',
             '소프트웨어연구학점2', '소프트웨어연구학점3', '소프트웨어연구학점4', '소프트웨어연구학점5', '소프트웨어창업현장실습1', '소프트웨어창업현장실습2',
             '소프트웨어특강1', '소프트웨어특강2', '소프트웨어현장실습1', '소프트웨어현장실습2', '소프트웨어현장실습3', '소프트웨어현장실습4',
             '심층신경망개론', '오토마타', '인터넷서비스와정보보호', '임베디드소프트웨어개론', '정보보호개론', '캡스톤설계프로젝트', '컴퓨터개론', '컴퓨터그래픽스개론',
             '컴퓨터비전개론', '프로그래밍입문', '확률과랜덤프로세스'], ['JAVA프로그래밍실습', '네트워크프로젝트', '데이터베이스프로젝트', '모바일앱프로그래밍실습',
             '시스템프로그래밍실습', '오픈소스소프트웨어실습', '웹프로그래밍실습', '인공지능프로젝트', '임베디드시스템프로젝트']]
#영어버전
oldEnSoft =[['Introduction to Database', 'Introduction to Software Engineering', 'System Program', 'Algorithms', 'Operating Systems', 'Data Structures',
             'Introduction to Computer Architectures', 'Computer Networks', 'Programming Languages'], ['Fundamentals of machine learning', 'Problem Solving Techniques', 'Introduction to Artificial Intelligence',
             'AI Capstone Design', 'Introduction to Human Computer Interaction', 'ICT Business Management', 'ICT Startup', 'Digital Logic Circuits', 'Multicore Computing', 'Multicore Computing',
             'Modeling Simulation', 'Introduction to Big Data Analytics', 'Industry-Academy Cooperation Project1', 'Industry-Academy Cooperation Project2' , 'Industry-Academy Cooperation Project3',
             'Seminar in Software', 'Software Independent Study 1', 'Software Independent Study 2', 'Software Independent Study 3', 'Software Independent Study 4', 'Software Independent Study 5',
             'SW Startup Field Practice 1', 'SW Startup Field Practice 2', 'Special Topics in Software 1', 'Special Topics in Software 2', 'Software Field Training Program 1', 'Software Field Training Program 2',
             'Software Field Training Program 3', 'Software Field Training Program 4', 'Introduction to Deep Neural Networks', 'Automata', 'Internet Service and Information Security',
             'Introduction to Embedded Software', 'Computer Security', 'Capstone Design Project', 'Introduction to Computer Engineering', 'Introduction to Computer Graphics',
             'Introduction to Computer Vision', 'Introduction to Programming', 'Probability and Random Process'], ['JAVA Programming Lab', 'Network Project',
             'Database Project', 'Mobile App Programming Lab', 'System Programming Lab', 'Open Source Software Practice', 'Web Programming Lab', 'Artificial Intelligence Project', 'Embedded System Project']]
newEnSoft = [['Introduction to Database', 'Introduction to Software Engineering', 'System Program', 'Algorithms', 'Operating Systems', 'Data Structures',
             'Introduction to Computer Architectures', 'Computer Networks', 'Programming Languages', 'Fundamentals of machine learning', 'Problem Solving Techniques', 'Introduction to Artificial Intelligence'],
             ['AI Capstone Design', 'Introduction to Human Computer Interaction', 'ICT Business Management', 'ICT Startup', 'Digital Logic Circuits', 'Multicore Computing', 'Multicore Computing',
             'Modeling Simulation', 'Introduction to Big Data Analytics', 'Industry-Academy Cooperation Project1', 'Industry-Academy Cooperation Project2', 'Industry-Academy Cooperation Project3',
             'Seminar in Software', 'Software Independent Study 1', 'Software Independent Study 2', 'Software Independent Study 3', 'Software Independent Study 4', 'Software Independent Study 5',
             'SW Startup Field Practice 1', 'SW Startup Field Practice 2', 'Special Topics in Software 1', 'Special Topics in Software 2', 'Software Field Training Program 1', 'Software Field Training Program 2',
             'Software Field Training Program 3', 'Software Field Training Program 4', 'Introduction to Deep Neural Networks', 'Automata', 'Internet Service and Information Security',
             'Introduction to Embedded Software', 'Computer Security', 'Capstone Design Project', 'Introduction to Computer Engineering', 'Introduction to Computer Graphics',
             'Introduction to Computer Vision', 'Introduction to Programming', 'Probability and Random Process'], ['JAVA Programming Lab', 'Network Project',
             'Database Project', 'Mobile App Programming Lab', 'System Programming Lab', 'Open Source Software Practice', 'Web Programming Lab', 'Artificial Intelligence Project', 'Embedded System Project']]
