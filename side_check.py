#2016~2019
#인성2, 리더십2, 의사소통4, 창의와 사유2, 기본영어4, 전문글로벌2, 인간문화3, 사회역사3, 과학기술3, 기초자연과학24
#2016은 소프트웨어기초 4학점  듣고 기초자연과학 21학점 들어야함
#firstVersion 내부 리스트 순서는 인성(0), 리더십(1), 의사소통(2), 창의와 사유(3), SW기초(4), 기본영어(5)
#전문글로벌(6), 인간/문화(7), 사회/역사(8), 과학/기술(9), 기초자연과학(10)
firstVersion = [['성균논어'], ['실천리더십', '앙트레프레너십과리더십'], ['과학기술글쓰기', '담화와언어', '미디어글쓰기', '발표와매체언어', '발표와토의',
'스피치와토론', '시민법정토론', '의사소통1', '의사소통2', '의사소통3', '의사소통4', '창의적글쓰기', '학술적글쓰기', '한국어말소리와언어예절', '한국어매체읽기',
'한국어문서작성'], ['사고와표현', '창의와사유의기초', '창의적사고', '창의적융합디자인'], ['공학컴퓨터프로그래밍', '프로그래밍기초와실습', '컴퓨팅사고와SW코딩',
'문제해결과알고리즘', 'AI기초와활용'], ['영어쓰기', '영어발표'], ['고급영어쓰기', '과학영어', '글로벌시대의문화이해', '글로벌영어', '글로벌화와21세기중국',
'뉴스와미디어의이해', '동아시아역사와문화', '문예영어', '미국사회와법', '법률영어', '비즈니스영어', '스페인어문화권의사회와문화', '스포츠영어', '앙트레프레너십영어',
'영어토론', '유럽사회와문화', '이슬람세계의사상과문화', '인도문명권의사상과문화', '커리어영어', '한국문화와언어', '현대사회의인권과평등', '현대세계와글로벌시각', '현대중국사회의이해'], 
['MBSR명상', '게임과인문학 ', '고전속의자유', '고전속의행복', '그리스로마신화의이해', '기후변화와인문학', '노벨문학상과인문융합',
'논어와인생', '다큐멘터리영화비평', '대중예술의이해', '대중음악의이해', '독일문화의이해', '동서양의세계유산', '동서양인문전통속의감정과윤리',
'동서양지식문화의이해', '동아시아문학의이해', '동아시아의상호소통과한자문명', '동아시아의전통사상', '동양의예술과삶', '동양의지혜',
'디지털시대의융합예술', '러시아문화의이해', '명상과치유', '문예창작의이해', '문화사와철학사상', '문화인류학', '뮤지컬과오페라', '북유럽신화의이해', '비교종교학의이해', '사랑과문학',
'사랑의심리', '생명의료윤리', '성의심리학', '세계의정원과문화', '시문학과예술가곡', '아동의심리와교육', '여성의역사와문학,예술', '연극과문화',
'영미문화의이해', '예술과4차산업혁명', '예술로보는동아시아', '예술사', '예술사와철학사상', '예술의말과생각', '유럽고도의역사와문화', '음악의이해',
'인문학고전읽기', '일본문화의이해', '종교와유럽문화', '죽음과문화', '중국문화의이해', '지식정보학', '프랑스문화의이해', '프로이트와현대문화', '한국고전문학',
'한국과중국', '한국문화의이해', '한국사상과문화의이해', '한국사회와미디어', '한국의문화유산과공간', '한국현대문학', '한시의이해', '한자와한문의세계'],
['4차산업혁명과법의이해', 'AI와경영의사결정', 'ESG경영', '경제학의고전과현대적이슈', '고전속의미디어와언론의자유', '고전속의정의', '공학경제', '근대성과현대문화',
'글로벌무역의이해', '기술시대의회계', '기업가정신', '기업과증권시장의이해', '나와역사', '다문화사회의이해', '대격변의시대', '대중매체의이해', '동양의역사와문명', '미디어와윤리',
'미래사회와창의혁신인재', '민주사회와행정', '북한경제의이해', '사회과학고전읽기', '서양의역사와문명', '성격과적응', '세계사속의중국', '소비와윤리', '여성과사회', '유교자본주의의이해', '인간과토지의문명사', '인구와가족의역사',
'일상생활의역사', '전쟁과문화', '정치경제학의이해', '직업생활과법', '통일문제의이해', '한국경제의이해', '한국사개설', '한국사회풍속사', '한국역사의이해', '한국전통사회의정치문화', '현대가족의이해',
'현대동아시아정치경제변동', '현대민주주의의이해', '현대사회와법', '현대사회와법의정신', '현대사회와복지', '현대사회와헌법의이해', '현대사회유학의이해', '현대사회의문제', '현대중국사회와문화', '현대한국정치의쟁점'],
['4차산업혁명과과학문화', '테크놀러지의철학적이해', '특허와창업', '산업혁명과사회문화', '우주론', '문명과자연환경', '과학기술과사회윤리', '과학기술산업화의역사', '약과건강', '생활속의양자',
'생태계와환경', '생활속의화학', '암의과학', '인간-컴퓨터상호작용의이해', '과학기술과창업경영', '현대천문학개론', '스포츠마케팅과미디어', '과학사', '화학과생명현상', '생명진화의철학', '환경과건강',
'기후와문화', '자연과학고전읽기', '융복합시대의창업', '생활속의에너지', '운동과건강', '유전자재조합의이해', '인공지능을위한기초수학', '생명의기원과본질', '지속가능에너지화학', '생명공학의이해',
'생명과음식의과학', '생명의과학', '법의학으로보는사회의이해', '핵과학과핵에너지'], ['고급미분적분학1', '고급미분적분학2', '고급생명과학1', '고급생명과학2', '공학수학1', '공학수학2', '미분적분학1',
'미분적분학2', '빅데이터와통계학', '생명과학1', '생명과학2', '선형대수학', '이산수학', '일반물리학1', '일반물리학2', '일반화학1', '일반화학2', '확률및통계', '미분적분학실습1', '미분적분학실습2', '생명과학실험1',
'생명과학실험2', '일반물리학실험1', '일반물리학실험2', '일반화학실험1', '일반화학실험2']]

firstVersionEn =[['The Analects of Confucius'], ['Activity-Based Leadership', 'Entrepreneurship and Leadership'], ['Scientific & Technical Writing',
'Discourse and Language', 'Media Writing', 'Academic Presentation and Media Language', 'Academic Presentation and Discussion',
'Public Speaking and Debate', 'Introduction to Jury Trial: Mock Trial Debate', 'Understanding of Communication', 'Understanding of Advanced Communication',
'Understanding of Advanced Communication 3', 'Understanding of Advanced Communication 4', 'Creative Writing',
'Academic Writing', 'Korean Speech Sounds and Standard Language Etiquette', 'Reading in Korean Media', 'Document Writing in Korean'], ['Creative thinking and expression',
'Understanding of Creative Thinking', 'Creative Thinking', 'Creative and Interdisciplinary Design'], ['Computer Programming for Engineers', 'Basis and Practice in Programming',
'Computational Thinking and Software Coding', 'Problem Solving and Algorithm', 'AI Basics & Uses'], ['English Writing', 'English Presentation'], 
['Advanced English Writing', 'English for Science', 'Cultures of Globalization', 'Global Englishes', 'Globalization ＆ China of 21st Century', 'News and Media Literacy',
'History and culture of East Asia', 'English for Arts ＆ Literature', 'American Society and the Law', 'English for Law', 'Business English', 'The Social Life ＆ Culture in the Spanish-Speaking Regions',
'Sports English', 'Entrepreneurship English', 'Debate in English', 'European Society and Culture', 'The Thoughts ＆ Culture of Islamic World', 'The Thoughts ＆ Culture in the Area of Indian Civilization',
'Career English', 'Korean Culture and Language', 'Human Rights and Equality in Modern Society', 'Interdependent World and Global Perspectives', 'Understanding Modern Chinese Society'],
['MBSR Meditation', 'Game and Humanities', 'Freedom in the Classics', 'Happiness in the Classics', 'Understanding of Greek and Roma Mythology',
'Climate Change and the Humanities', 'Nobel Prize in Literature and Converging Humanities', 'Analects and Life', 'The Critique of Documentary Film', 'Understanding of Popular Arts',
'UNDERSTANDING POPULAR MUSIC', 'Understanding the Culture of German', 'Unesco World Heritage Exploration', 'Emotions and Ethics in Greece, Europe, and Asia',
'Understanding of the Knowledge Culture in East and West', 'East Asia in Literature', 'Cultural Exchanges in East Asia and Classical chinese Culture', 'Traditional Thoughts of East Asia',
'Art and Life in the East', 'The Wisdom of the Orient', 'Convergence Art of Digital Age', 'Understanding of Russian Culture', 'Meditation and Healing', 'Understanding of Creative Writing',
'Philosophy in Culture History', 'Cultural Anthropology', 'Musical and Opera', 'Understanding of Nordic Myth', 'Comparative Study of Religions', 'Love in Literature',
'Psychology of Love', 'Bioethics', 'Gender Psychology', 'The Worlds Garden and Culture', 'Understanding Opera', 'Child Psychology and Education', 'History, Literature and Arts of Women',
'Culture and Theatre Art', 'Approach to English Literature and Society', 'Art and Fourth Industrial Revolution', 'East Asian Art & Culture', 'History of Art', 'History of Art and Philosophy',
'Artistic Words and Thinking', 'The Culture and History of European Old Town', 'Understanding of Music', 'Reading Classics in Humanities', 'Understanding of Japanese Culture',
'Religion and European Culture', 'Death and Culture', 'Basic Studies in Chinese Culture', 'Knowledge information studies', 'Understanding of French Culture', 'Freud and Modern Culture',
'Korean Classical Literature', 'Korea and China', 'Understanding of Korean Culture', 'Understanding of Korean Thought and Culture', 'Korean Society and Media',
'Cultural heritage and places of Korea', 'Korean Modern Literature', 'Understanding the Classical Chinese Poetry', 'The World of Korean words compound by Chinese Character and Traditional Classical Chinese Sentence'],
['Understanding of Law on 4th Industrial Revolution', 'AI & Business Decision-making', 'ESG Management', 'New Ideas from Giant Economists', 'Media & Freedom of Press in the Classics',
'Justice in the Classics', 'Engineering Economy', 'Modernity and Modern Culture', 'Understanding of Global Trade', 'The Account in the Age of Technology', 'Entrepreneurship in Action',
'Understanding Corporations and Stock Market', 'History and I', 'Understanding of Multicultural Society', 'The Age of Upheaval', 'Understanding of Mass Media', 'Oriental History and Civilization',
'Media and Ethics', 'Creative and Innovation Talents of the Future Society', 'Democracy and Public Administration', 'Introduction to North Korean Economy', 'Reading Classics in Social Sciences',
'Western History and Civilization', 'Personality and Adjustment', 'China in world history', 'Consumption and Ethics', 'Women and Society', 'Understanding of Confucian Capitalism', 'Civilazation of Human and Land',
'History of population and family', 'History of Everyday Life', 'War and Culture', 'Understanding of Political Economy', 'Occupational life and law', 'Understanding Korean Reunification', 'Introduction to Korea Economy',
'Introduction to Korean History', 'History of Korean Society and Folk Culture', 'Understanding of Korean History', 'The Political culture of the traditional korea',
'Understanding the Modern Family', 'Contemporary East Asian Politics and Economy', 'Theories of Modern Democracy', 'Modern Society and Law', 'Modern society and the spirit of laws', 'Modern Society and Welfare',
'Understanding of Constitutional Law in Modern Society', 'Understanding of Confucianism in Modern society', 'Problems of Contemporary Society', 'Contemporary Chinese Society and Culture', 'Political Issues in Contemporary Korean Politics'],
['4th Industrial Revolution and Science Culture', 'The Philosophy of Technology', 'Patents and Ideas-to-Products', 'Industrial Revolution with its Social and Cultural Impact', 'Cosmology', 'Civilization and the Natural Environment',
'Science, Technology and Social Ethics', 'History of Industrialization of Science', 'Drug and Health', 'Quanta in Everyday Life', 'Ecosystem and Environments', 'Chemistry in Everyday Life', 'Science of Cancer',
'Understanding of Human-Computer Interaction', 'Science Technology and Start-up Management', 'Introduction to Modern Astronomy', 'Sports Marketing and Media', 'History of Science', 'Chemistry and Biological System', 'Philosophy of the Life Evolution',
'Life-Environment and the Health Effect', 'Climate and Culture', 'Reading Classics in Natural Sciences', 'Start up in Convergence Era', 'Energy in Everyday Life', 'Exercise and Health', 'Understanding Gene Manipulation',
'Basic Mathematics for Artificial Intelligence', 'The Origin and Nature of Life', 'Sustainability Energy Chemistry', 'Understanding of Biotechnoloy', 'Science of Foods and Life', 'Science of Life',
'Society in view of Forensic Medicine', 'Nuclear Science and Nuclear Energy'], ['Honor Calculus 1', 'Honor Calculus Ⅱ', 'Advanced General Biology 1', 'Advanced General Biology Ⅱ', 'Engineering Mathematics 1', 'Engineering Mathematics 2', 'Calculus 1',
'Calculus 2', 'Big Data and Statistics', 'Biological Science I', 'Biological science II', 'Linear Algebra', 'Discrete Mathematics', 'General Physics 1', 'General Physics 2', 'General Chemistry 1', 'General Chemistry 2', 'Probability and Statistics',
'Calculus Laboratory1', 'Calculus Laboratory2', 'Biological Science Laboratory I', 'Biological Science Laboratory II', 'General Physics Laboratory 1', 'General Physics Laboratory 2', 'General Chemistry Laboratory 1', 'General Chemistry Laboratory 2']]

#2020
#인성/리더십2, 고전/명저3, 의사소통4, 창의3, 미래(SW)8, 글로벌6, 인간문화3, 사회역사3, 과학기술3, 자연과학18
#secondVersion 내부 리스트 순서는 인성(0), 고전(1), 의사소통(2), 창의(3), 미래(SW)(4), 글로벌(5), 인간/문화(6), 사회/역사(7), 과학/기술(8), 기초자연과학(9)
secondVersion = [['성균논어', '실천리더십', '앙트레프레너십과리더십'], ['고전명저북클럽'], ['과학기술글쓰기', '담화와언어', '미디어글쓰기', '발표와매체언어', '발표와토의', '스피치와토론', '시민법정토론',
'의사소통1', '의사소통2', '의사소통3', '의사소통4', '창의적글쓰기', '학술적글쓰기', '한국어말소리와언어예절', '한국어매체읽기', '한국어문서작성'], ['사고와표현', '창의와사유의기초', '창의적사고', '창의적융합디자인'],
['공학컴퓨터프로그래밍', '프로그래밍기초와실습', '컴퓨팅사고와SW코딩', '문제해결과알고리즘', 'AI기초와활용'], ['고급영어쓰기', '과학영어', '글로벌시대의문화이해', '글로벌영어', '글로벌화와21세기중국', '뉴스와미디어의이해',
'동아시아역사와문화', '문예영어', '미국사회와법', '법률영어', '비즈니스영어', '스페인어문화권의사회와문화', '스포츠영어', '앙트레프레너십영어', '영어토론', '영어발표', '유럽사회와문화', '이슬람세계의사상과문화',
'인도문명권의사상과문화', '커리어영어', '한국문화와언어', '현대사회의인권과평등', '현대세계와글로벌시각', '현대중국사회의이해', '영어쓰기'], ['MBSR명상', '게임과인문학 ', '고전속의자유', '고전속의행복', '그리스로마신화의이해',
'기후변화와인문학', '노벨문학상과인문융합', '논어와인생', '다큐멘터리영화비평', '대중예술의이해', '대중음악의이해', '독일문화의이해', '동서양의세계유산', '동서양인문전통속의감정과윤리',
'동서양지식문화의이해', '동아시아문학의이해', '동아시아의상호소통과한자문명', '동아시아의전통사상', '동양의예술과삶', '동양의지혜', '디지털시대의융합예술', '러시아문화의이해', '명상과치유', '문예창작의이해',
'문화사와철학사상', '문화인류학', '뮤지컬과오페라', '북유럽신화의이해', '비교종교학의이해', '사랑과문학', '사랑의심리', '생명의료윤리', '성의심리학', '세계의정원과문화', '시문학과예술가곡', '아동의심리와교육',
'여성의역사와문학,예술', '연극과문화', '영미문화의이해', '예술과4차산업혁명', '예술로보는동아시아', '예술사', '예술사와철학사상', '예술의말과생각', '유럽고도의역사와문화', '음악의이해',
'인문학고전읽기', '일본문화의이해', '종교와유럽문화', '죽음과문화', '중국문화의이해', '지식정보학', '프랑스문화의이해', '프로이트와현대문화', '한국고전문학',
'한국과중국', '한국문화의이해', '한국사상과문화의이해', '한국사회와미디어', '한국의문화유산과공간', '한국현대문학', '한시의이해', '한자와한문의세계'],
['4차산업혁명과법의이해', 'AI와경영의사결정', 'ESG경영', '경제학의고전과현대적이슈', '고전속의미디어와언론의자유', '고전속의정의', '공학경제', '근대성과현대문화',
'글로벌무역의이해', '기술시대의회계', '기업가정신', '기업과증권시장의이해', '나와역사', '다문화사회의이해', '대격변의시대', '대중매체의이해', '동양의역사와문명', '미디어와윤리',
'미래사회와창의혁신인재', '민주사회와행정', '북한경제의이해', '사회과학고전읽기', '서양의역사와문명', '성격과적응', '세계사속의중국', '소비와윤리', '여성과사회', '유교자본주의의이해', '인간과토지의문명사', '인구와가족의역사',
'일상생활의역사', '전쟁과문화', '정치경제학의이해', '직업생활과법', '통일문제의이해', '한국경제의이해', '한국사개설', '한국사회풍속사', '한국역사의이해', '한국전통사회의정치문화', '현대가족의이해',
'현대동아시아정치경제변동', '현대민주주의의이해', '현대사회와법', '현대사회와법의정신', '현대사회와복지', '현대사회와헌법의이해', '현대사회유학의이해', '현대사회의문제', '현대중국사회와문화', '현대한국정치의쟁점'],
['4차산업혁명과과학문화', '테크놀러지의철학적이해', '특허와창업', '산업혁명과사회문화', '우주론', '문명과자연환경', '과학기술과사회윤리', '과학기술산업화의역사', '약과건강', '생활속의양자',
'생태계와환경', '생활속의화학', '암의과학', '인간-컴퓨터상호작용의이해', '과학기술과창업경영', '현대천문학개론', '스포츠마케팅과미디어', '과학사', '화학과생명현상', '생명진화의철학', '환경과건강',
'기후와문화', '자연과학고전읽기', '융복합시대의창업', '생활속의에너지', '운동과건강', '유전자재조합의이해', '인공지능을위한기초수학', '생명의기원과본질', '지속가능에너지화학', '생명공학의이해',
'생명과음식의과학', '생명의과학', '법의학으로보는사회의이해', '핵과학과핵에너지'], ['고급미분적분학1', '고급미분적분학2', '고급생명과학1', '고급생명과학2', '공학수학1', '공학수학2', '미분적분학1', '미분적분학2', '빅데이터와통계학', '생명과학1', '생명과학2', '선형대수학',
'이산수학', '일반물리학1', '일반물리학2', '일반화학1', '일반화학2', '확률및통계', '미분적분학실습1', '미분적분학실습2', '생명과학실험1', '생명과학실험2', '일반물리학실험1', '일반물리학실험2', '일반화학실험1', '일반화학실험2']]

secondVersionEn = [['The Analects of Confucius', 'Activity-Based Leadership', 'Entrepreneurship and Leadership'], ['Sungkyun Classics Book Club'], ['Scientific & Technical Writing', 'Discourse and Language', 'Media Writing',
'Academic Presentation and Media Language', 'Academic Presentation and Discussion', 'Public Speaking and Debate', 'Introduction to Jury Trial: Mock Trial Debate', 'Understanding of Communication', 'Understanding of Advanced Communication',
'Understanding of Advanced Communication 3', 'Understanding of Advanced Communication 4', 'Creative Writing', 'Academic Writing', 'Korean Speech Sounds and Standard Language Etiquette', 'Reading in Korean Media', 'Document Writing in Korean'],
['Creative thinking and expression', 'Understanding of Creative Thinking', 'Creative Thinking', 'Creative and Interdisciplinary Design'], ['Computer Programming for Engineers', 'Basis and Practice in Programming',
'Computational Thinking and Software Coding', 'Problem Solving and Algorithm', 'AI Basics & Uses'], ['Advanced English Writing', 'English for Science', 'Cultures of Globalization', 'Global Englishes', 'Globalization ＆ China of 21st Century', 'News and Media Literacy',
'History and culture of East Asia', 'English for Arts ＆ Literature', 'American Society and the Law', 'English for Law', 'Business English', 'The Social Life ＆ Culture in the Spanish-Speaking Regions',
'Sports English', 'Entrepreneurship English', 'Debate in English', 'English Presentation', 'European Society and Culture', 'The Thoughts ＆ Culture of Islamic World', 'The Thoughts ＆ Culture in the Area of Indian Civilization',
'Career English', 'Korean Culture and Language', 'Human Rights and Equality in Modern Society', 'Interdependent World and Global Perspectives', 'Understanding Modern Chinese Society', 'English Writing'], ['MBSR Meditation', 'Game and Humanities', 'Freedom in the Classics',
'Happiness in the Classics', 'Understanding of Greek and Roma Mythology', 'Climate Change and the Humanities', 'Nobel Prize in Literature and Converging Humanities', 'Analects and Life', 'The Critique of Documentary Film', 'Understanding of Popular Arts',
'UNDERSTANDING POPULAR MUSIC', 'Understanding the Culture of German', 'Unesco World Heritage Exploration', 'Emotions and Ethics in Greece, Europe, and Asia', 'Understanding of the Knowledge Culture in East and West', 'East Asia in Literature',
'Cultural Exchanges in East Asia and Classical chinese Culture', 'Traditional Thoughts of East Asia', 'Art and Life in the East', 'The Wisdom of the Orient', 'Convergence Art of Digital Age', 'Understanding of Russian Culture', 'Meditation and Healing', 'Understanding of Creative Writing',
'Philosophy in Culture History', 'Cultural Anthropology', 'Musical and Opera', 'Understanding of Nordic Myth', 'Comparative Study of Religions', 'Love in Literature', 'Psychology of Love', 'Bioethics', 'Gender Psychology', 'The Worlds Garden and Culture', 'Understanding Opera',
'Child Psychology and Education', 'History, Literature and Arts of Women', 'Culture and Theatre Art', 'Approach to English Literature and Society', 'Art and Fourth Industrial Revolution', 'East Asian Art & Culture', 'History of Art', 'History of Art and Philosophy',
'Artistic Words and Thinking', 'The Culture and History of European Old Town', 'Understanding of Music', 'Reading Classics in Humanities', 'Understanding of Japanese Culture', 'Religion and European Culture', 'Death and Culture', 'Basic Studies in Chinese Culture',
'Knowledge information studies', 'Understanding of French Culture', 'Freud and Modern Culture', 'Korean Classical Literature', 'Korea and China', 'Understanding of Korean Culture', 'Understanding of Korean Thought and Culture', 'Korean Society and Media',
'Cultural heritage and places of Korea', 'Korean Modern Literature', 'Understanding the Classical Chinese Poetry', 'The World of Korean words compound by Chinese Character and Traditional Classical Chinese Sentence'],
['Understanding of Law on 4th Industrial Revolution', 'AI & Business Decision-making', 'ESG Management', 'New Ideas from Giant Economists', 'Media & Freedom of Press in the Classics',
'Justice in the Classics', 'Engineering Economy', 'Modernity and Modern Culture', 'Understanding of Global Trade', 'The Account in the Age of Technology', 'Entrepreneurship in Action',
'Understanding Corporations and Stock Market', 'History and I', 'Understanding of Multicultural Society', 'The Age of Upheaval', 'Understanding of Mass Media', 'Oriental History and Civilization',
'Media and Ethics', 'Creative and Innovation Talents of the Future Society', 'Democracy and Public Administration', 'Introduction to North Korean Economy', 'Reading Classics in Social Sciences',
'Western History and Civilization', 'Personality and Adjustment', 'China in world history', 'Consumption and Ethics', 'Women and Society', 'Understanding of Confucian Capitalism', 'Civilazation of Human and Land',
'History of population and family', 'History of Everyday Life', 'War and Culture', 'Understanding of Political Economy', 'Occupational life and law', 'Understanding Korean Reunification', 'Introduction to Korea Economy',
'Introduction to Korean History', 'History of Korean Society and Folk Culture', 'Understanding of Korean History', 'The Political culture of the traditional korea',
'Understanding the Modern Family', 'Contemporary East Asian Politics and Economy', 'Theories of Modern Democracy', 'Modern Society and Law', 'Modern society and the spirit of laws', 'Modern Society and Welfare',
'Understanding of Constitutional Law in Modern Society', 'Understanding of Confucianism in Modern society', 'Problems of Contemporary Society', 'Contemporary Chinese Society and Culture', 'Political Issues in Contemporary Korean Politics'],
['4th Industrial Revolution and Science Culture', 'The Philosophy of Technology', 'Patents and Ideas-to-Products', 'Industrial Revolution with its Social and Cultural Impact', 'Cosmology', 'Civilization and the Natural Environment',
'Science, Technology and Social Ethics', 'History of Industrialization of Science', 'Drug and Health', 'Quanta in Everyday Life', 'Ecosystem and Environments', 'Chemistry in Everyday Life', 'Science of Cancer',
'Understanding of Human-Computer Interaction', 'Science Technology and Start-up Management', 'Introduction to Modern Astronomy', 'Sports Marketing and Media', 'History of Science', 'Chemistry and Biological System', 'Philosophy of the Life Evolution',
'Life-Environment and the Health Effect', 'Climate and Culture', 'Reading Classics in Natural Sciences', 'Start up in Convergence Era', 'Energy in Everyday Life', 'Exercise and Health', 'Understanding Gene Manipulation',
'Basic Mathematics for Artificial Intelligence', 'The Origin and Nature of Life', 'Sustainability Energy Chemistry', 'Understanding of Biotechnoloy', 'Science of Foods and Life', 'Science of Life',
'Society in view of Forensic Medicine', 'Nuclear Science and Nuclear Energy'], ['Honor Calculus 1', 'Honor Calculus Ⅱ', 'Advanced General Biology 1', 'Advanced General Biology Ⅱ', 'Engineering Mathematics 1', 'Engineering Mathematics 2', 'Calculus 1', 'Calculus 2', 'Big Data and Statistics',
'Biological Science I', 'Biological science II', 'Linear Algebra', 'Discrete Mathematics', 'General Physics 1', 'General Physics 2', 'General Chemistry 1', 'General Chemistry 2', 'Probability and Statistics', 'Calculus Laboratory1', 'Calculus Laboratory2', 'Biological Science Laboratory I',
'Biological Science Laboratory II', 'General Physics Laboratory 1', 'General Physics Laboratory 2', 'General Chemistry Laboratory 1', 'General Chemistry Laboratory 2']]

#2021,2022
#인성/리더십2, 고전/명저3, 의사소통4, 창의3, DS수업11, 글로벌6, 인간문화/사회역사/과학기술6, 인문사회/자연과학18
#DS기반 수업으로 소프트웨어 학생은 필수로 공컴프, 프기실, AI기초활용,데이터분석기초를 들어야함
#thirdVersion 내부 리스트 순서는 인성(0), 고전(1), 의사소통(2), 창의(3), DS수업(4), 글로벌(5), 인간/문화,사회/역사,과학/기술(6), 인문사회/기초자연과학(7)
thirdVersion = [['성균논어', '실천리더십', '앙트레프레너십과리더십'], ['고전명저북클럽'], ['과학기술글쓰기', '담화와언어', '미디어글쓰기', '발표와매체언어', '발표와토의', '스피치와토론', '시민법정토론',
'의사소통1', '의사소통2', '의사소통3', '의사소통4', '창의적글쓰기', '학술적글쓰기', '한국어말소리와언어예절', '한국어매체읽기', '한국어문서작성'], ['사고와표현', '창의와사유의기초', '창의적사고', '창의적융합디자인'],
['공학컴퓨터프로그래밍', '프로그래밍기초와실습', 'AI기초와활용', '데이터분석기초'], ['고급영어쓰기', '과학영어', '글로벌시대의문화이해', '글로벌영어', '글로벌화와21세기중국', '뉴스와미디어의이해',
'동아시아역사와문화', '문예영어', '미국사회와법', '법률영어', '비즈니스영어', '스페인어문화권의사회와문화', '스포츠영어', '앙트레프레너십영어', '영어토론', '영어발표', '유럽사회와문화', '이슬람세계의사상과문화',
'인도문명권의사상과문화', '커리어영어', '한국문화와언어', '현대사회의인권과평등', '현대세계와글로벌시각', '현대중국사회의이해', '영어쓰기'], ['MBSR명상', '게임과인문학 ', '고전속의자유', '고전속의행복', '그리스로마신화의이해',
'기후변화와인문학', '노벨문학상과인문융합', '논어와인생', '다큐멘터리영화비평', '대중예술의이해', '대중음악의이해', '독일문화의이해', '동서양의세계유산', '동서양인문전통속의감정과윤리',
'동서양지식문화의이해', '동아시아문학의이해', '동아시아의상호소통과한자문명', '동아시아의전통사상', '동양의예술과삶', '동양의지혜', '디지털시대의융합예술', '러시아문화의이해', '명상과치유', '문예창작의이해',
'문화사와철학사상', '문화인류학', '뮤지컬과오페라', '북유럽신화의이해', '비교종교학의이해', '사랑과문학', '사랑의심리', '생명의료윤리', '성의심리학', '세계의정원과문화', '시문학과예술가곡', '아동의심리와교육', '여성의역사와문학,예술',
'연극과문화', '영미문화의이해', '예술과4차산업혁명', '예술로보는동아시아', '예술사', '예술사와철학사상', '예술의말과생각', '유럽고도의역사와문화', '음악의이해',
'인문학고전읽기', '일본문화의이해', '종교와유럽문화', '죽음과문화', '중국문화의이해', '지식정보학', '프랑스문화의이해', '프로이트와현대문화', '한국고전문학', '한국과중국', '한국문화의이해', '한국사상과문화의이해', '한국사회와미디어',
'한국의문화유산과공간', '한국현대문학', '한시의이해', '한자와한문의세계', '4차산업혁명과법의이해', 'AI와경영의사결정', 'ESG경영', '경제학의고전과현대적이슈', '고전속의미디어와언론의자유', '고전속의정의', '공학경제', '근대성과현대문화',
'글로벌무역의이해', '기술시대의회계', '기업가정신', '기업과증권시장의이해', '나와역사', '다문화사회의이해', '대격변의시대', '대중매체의이해', '동양의역사와문명', '미디어와윤리',
'미래사회와창의혁신인재', '민주사회와행정', '북한경제의이해', '사회과학고전읽기', '서양의역사와문명', '성격과적응', '세계사속의중국', '소비와윤리', '여성과사회', '유교자본주의의이해', '인간과토지의문명사', '인구와가족의역사',
'일상생활의역사', '전쟁과문화', '정치경제학의이해', '직업생활과법', '통일문제의이해', '한국경제의이해', '한국사개설', '한국사회풍속사', '한국역사의이해', '한국전통사회의정치문화', '현대가족의이해',
'현대동아시아정치경제변동', '현대민주주의의이해', '현대사회와법', '현대사회와법의정신', '현대사회와복지', '현대사회와헌법의이해', '현대사회유학의이해', '현대사회의문제', '현대중국사회와문화', '현대한국정치의쟁점',
'4차산업혁명과과학문화', '테크놀러지의철학적이해', '특허와창업', '산업혁명과사회문화', '우주론', '문명과자연환경', '과학기술과사회윤리', '과학기술산업화의역사', '약과건강', '생활속의양자',
'생태계와환경', '생활속의화학', '암의과학', '인간-컴퓨터상호작용의이해', '과학기술과창업경영', '현대천문학개론', '스포츠마케팅과미디어', '과학사', '화학과생명현상', '생명진화의철학', '환경과건강',
'기후와문화', '자연과학고전읽기', '융복합시대의창업', '생활속의에너지', '운동과건강', '유전자재조합의이해', '인공지능을위한기초수학', '생명의기원과본질', '지속가능에너지화학', '생명공학의이해',
'생명과음식의과학', '생명의과학', '법의학으로보는사회의이해', '핵과학과핵에너지'], ['경제학입문', '기초독어1', '기초독어2', '기초러시아어1', '기초러시아어2', '기초일본어1', '기초일본어2', '기초중국어1', '기초중국어2', '기초프랑스어1',
'기초프랑스어2', '기초한문', '동양사상입문', '라틴어', '문학입문', '사회과학입문', '사회학입문', '심리학입문', '언어학입문', '역사학입문', '예술학입문', '정치학입문', '철학입문', '희랍어', '고급미분적분학1', '고급미분적분학2', '고급생명과학1',
'고급생명과학2', '공학수학1', '공학수학2', '미분적분학1', '미분적분학2', '빅데이터와통계학', '생명과학1', '생명과학2', '선형대수학', '이산수학', '일반물리학1', '일반물리학2', '일반화학1', '일반화학2', '확률및통계',
'미분적분학실습1', '미분적분학실습2', '생명과학실험1', '생명과학실험2', '일반물리학실험1', '일반물리학실험2', '일반화학실험1', '일반화학실험2']]

thirdVersionEn = [['The Analects of Confucius', 'Activity-Based Leadership', 'Entrepreneurship and Leadership'], ['Sungkyun Classics Book Club'], ['Scientific & Technical Writing', 'Discourse and Language', 'Media Writing',
'Academic Presentation and Media Language', 'Academic Presentation and Discussion', 'Public Speaking and Debate', 'Introduction to Jury Trial: Mock Trial Debate', 'Understanding of Communication', 'Understanding of Advanced Communication',
'Understanding of Advanced Communication 3', 'Understanding of Advanced Communication 4', 'Creative Writing', 'Academic Writing', 'Korean Speech Sounds and Standard Language Etiquette', 'Reading in Korean Media', 'Document Writing in Korean'],
['Creative thinking and expression', 'Understanding of Creative Thinking', 'Creative Thinking', 'Creative and Interdisciplinary Design'], ['Computer Programming for Engineers', 'Basis and Practice in Programming', 'AI Basics & Uses', 'Basis of Data Analysis'],
['Advanced English Writing', 'English for Science', 'Cultures of Globalization', 'Global Englishes', 'Globalization ＆ China of 21st Century', 'News and Media Literacy', 'History and culture of East Asia', 'English for Arts ＆ Literature',
'American Society and the Law', 'English for Law', 'Business English', 'The Social Life ＆ Culture in the Spanish-Speaking Regions', 'Sports English', 'Entrepreneurship English', 'Debate in English', 'English Presentation', 'European Society and Culture',
'The Thoughts ＆ Culture of Islamic World', 'The Thoughts ＆ Culture in the Area of Indian Civilization', 'Career English', 'Korean Culture and Language', 'Human Rights and Equality in Modern Society', 'Interdependent World and Global Perspectives',
'Understanding Modern Chinese Society', 'English Writing'], ['MBSR Meditation', 'Game and Humanities', 'Freedom in the Classics', 'Happiness in the Classics', 'Understanding of Greek and Roma Mythology',
'Climate Change and the Humanities', 'Nobel Prize in Literature and Converging Humanities', 'Analects and Life', 'The Critique of Documentary Film', 'Understanding of Popular Arts',
'UNDERSTANDING POPULAR MUSIC', 'Understanding the Culture of German', 'Unesco World Heritage Exploration', 'Emotions and Ethics in Greece, Europe, and Asia',
'Understanding of the Knowledge Culture in East and West', 'East Asia in Literature', 'Cultural Exchanges in East Asia and Classical chinese Culture', 'Traditional Thoughts of East Asia',
'Art and Life in the East', 'The Wisdom of the Orient', 'Convergence Art of Digital Age', 'Understanding of Russian Culture', 'Meditation and Healing', 'Understanding of Creative Writing',
'Philosophy in Culture History', 'Cultural Anthropology', 'Musical and Opera', 'Understanding of Nordic Myth', 'Comparative Study of Religions', 'Love in Literature',
'Psychology of Love', 'Bioethics', 'Gender Psychology', 'The Worlds Garden and Culture', 'Understanding Opera', 'Child Psychology and Education', 'History, Literature and Arts of Women',
'Culture and Theatre Art', 'Approach to English Literature and Society', 'Art and Fourth Industrial Revolution', 'East Asian Art & Culture', 'History of Art', 'History of Art and Philosophy',
'Artistic Words and Thinking', 'The Culture and History of European Old Town', 'Understanding of Music', 'Reading Classics in Humanities', 'Understanding of Japanese Culture',
'Religion and European Culture', 'Death and Culture', 'Basic Studies in Chinese Culture', 'Knowledge information studies', 'Understanding of French Culture', 'Freud and Modern Culture',
'Korean Classical Literature', 'Korea and China', 'Understanding of Korean Culture', 'Understanding of Korean Thought and Culture', 'Korean Society and Media',
'Cultural heritage and places of Korea', 'Korean Modern Literature', 'Understanding the Classical Chinese Poetry', 'The World of Korean words compound by Chinese Character and Traditional Classical Chinese Sentence',
'Understanding of Law on 4th Industrial Revolution', 'AI & Business Decision-making', 'ESG Management', 'New Ideas from Giant Economists', 'Media & Freedom of Press in the Classics',
'Justice in the Classics', 'Engineering Economy', 'Modernity and Modern Culture', 'Understanding of Global Trade', 'The Account in the Age of Technology', 'Entrepreneurship in Action',
'Understanding Corporations and Stock Market', 'History and I', 'Understanding of Multicultural Society', 'The Age of Upheaval', 'Understanding of Mass Media', 'Oriental History and Civilization',
'Media and Ethics', 'Creative and Innovation Talents of the Future Society', 'Democracy and Public Administration', 'Introduction to North Korean Economy', 'Reading Classics in Social Sciences',
'Western History and Civilization', 'Personality and Adjustment', 'China in world history', 'Consumption and Ethics', 'Women and Society', 'Understanding of Confucian Capitalism', 'Civilazation of Human and Land',
'History of population and family', 'History of Everyday Life', 'War and Culture', 'Understanding of Political Economy', 'Occupational life and law', 'Understanding Korean Reunification', 'Introduction to Korea Economy',
'Introduction to Korean History', 'History of Korean Society and Folk Culture', 'Understanding of Korean History', 'The Political culture of the traditional korea',
'Understanding the Modern Family', 'Contemporary East Asian Politics and Economy', 'Theories of Modern Democracy', 'Modern Society and Law', 'Modern society and the spirit of laws', 'Modern Society and Welfare',
'Understanding of Constitutional Law in Modern Society', 'Understanding of Confucianism in Modern society', 'Problems of Contemporary Society', 'Contemporary Chinese Society and Culture', 'Political Issues in Contemporary Korean Politics',
'4th Industrial Revolution and Science Culture', 'The Philosophy of Technology', 'Patents and Ideas-to-Products', 'Industrial Revolution with its Social and Cultural Impact', 'Cosmology', 'Civilization and the Natural Environment',
'Science, Technology and Social Ethics', 'History of Industrialization of Science', 'Drug and Health', 'Quanta in Everyday Life', 'Ecosystem and Environments', 'Chemistry in Everyday Life', 'Science of Cancer',
'Understanding of Human-Computer Interaction', 'Science Technology and Start-up Management', 'Introduction to Modern Astronomy', 'Sports Marketing and Media', 'History of Science', 'Chemistry and Biological System', 'Philosophy of the Life Evolution',
'Life-Environment and the Health Effect', 'Climate and Culture', 'Reading Classics in Natural Sciences', 'Start up in Convergence Era', 'Energy in Everyday Life', 'Exercise and Health', 'Understanding Gene Manipulation',
'Basic Mathematics for Artificial Intelligence', 'The Origin and Nature of Life', 'Sustainability Energy Chemistry', 'Understanding of Biotechnoloy', 'Science of Foods and Life', 'Science of Life',
'Society in view of Forensic Medicine', 'Nuclear Science and Nuclear Energy'], ['Elementary Economics', 'Elementary German Ι', 'Elementary German Ⅱ', 'Elementary Russian  I', 'Elementary Russian Ⅱ', 'Elementary Japanese Ⅰ', 'Elementary Japanese Ⅱ',
'Elementary ChineseⅠ', 'Elementary ChineseⅡ', 'Introduction to French 1', 'Introduction to French 2', 'Elementary Classical Chinese Literature', 'Introduction to Eastern Thoughts', 'Latin', 'Introduction to Literature', 'Introduction to social science ',
'Introduction to Sociology', 'Introduction to Psychology', 'Introduction to Linguistics', 'Introduction to Historiography', 'Introduction to Arts', 'Introduction to Political Science', 'Introduction to Philosophy', 'Greek',
'Honor Calculus 1', 'Honor Calculus Ⅱ', 'Advanced General Biology 1', 'Advanced General Biology Ⅱ', 'Engineering Mathematics 1', 'Engineering Mathematics 2', 'Calculus 1', 'Calculus 2', 'Big Data and Statistics',
'Biological Science I', 'Biological science II', 'Linear Algebra', 'Discrete Mathematics', 'General Physics 1', 'General Physics 2', 'General Chemistry 1', 'General Chemistry 2', 'Probability and Statistics',
'Calculus Laboratory1', 'Calculus Laboratory2', 'Biological Science Laboratory I', 'Biological Science Laboratory II', 'General Physics Laboratory 1', 'General Physics Laboratory 2', 'General Chemistry Laboratory 1', 'General Chemistry Laboratory 2']]


