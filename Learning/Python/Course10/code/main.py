from konlpy.tag import Okt

ok = Okt()
test = "안녕하세요. 저는 문성재입니다. #패스트캠퍼스 #패캠 #인강"
for i in ok.pos(test, norm=True):
    print(i)
for i in ok.pos(test):
    if i[1] == 'Hashtag':
        print(i)
test = "패스트캠퍼스 패캠 문성재 코딩 프로그래밍"
for i in ok.nouns(test):
    print(i)