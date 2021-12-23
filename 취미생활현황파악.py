'''
취미 생활 현황 파악하기
산업시스템공학과 / 2016011405 / 김형경
'''
count = int(input('입력하는 학생수가 총 몇명인가요? : '))
                  
print('학생의 이름과 취미를 차례대로 입력하세요! ')
student = []
x = 1

while x <= count :
    print(x,"번째 학생 =====")
    name = input("* 이름 : ")
    hobby = input("* 취미 : ")
    a = (name,hobby)
    student.append(a)
    x += 1

name_list = []
hobby_set = set()

for x,y in student :
    name_list.append(x)
    hobby_set.add(y)
    
print(" == 전체 학생 리스트 정보 : ", name_list)
print(" == 전체 취미 세트 정보 : ",hobby_set )


   
