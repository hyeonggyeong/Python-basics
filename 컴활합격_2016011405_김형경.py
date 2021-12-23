'''
컴활시험결과 출력하기
산업시스템공학과 / 2016011405 / 김형경
'''

print("컴활 1급 시험결과 확인 프로그램입니다.")

com = int(input("컴퓨터 일반 성적을 입력하세요 : "))
sp = int(input("스프레드시트 성적을 입력하세요 : "))
db = int(input("데이터베이스 성적을 입력하세요 : "))

avg = (com + sp +db) / 3
print("===================================")
if com >= 40 and sp >=40 and db >= 40 and avg >= 60 :
    print(" 합격입니다. 축하드립니다.")
else :
    print(" 불합격입니다.")
print("===================================")

if com >= 40 :
    com = "합격"
else :
    com = "과락"
    
if sp >= 40 :
    sp = "합격"
else :
    sp = "과락"
    
if db >= 40 :
    db = "합격"
else :
    db = "과락"
    
if avg >= 60 :
    avg = "60점 이상(합격)"
else :
    avg = "60점 미만(불합격)"
    
print(" 컴퓨터 일반 :", com)
print(" 스프레드시트 :", sp)
print(" 데이터베이스 :", db)
print(" 평균 :", avg)
    
