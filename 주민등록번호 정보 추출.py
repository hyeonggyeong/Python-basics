#산업시스템공학과 / 2016011405 / 김형경
# 주민등록번호 정보 추출하기


ssn = input("주민등록번호 13자리를 입력해 주세요 : ")

year = "19" + ssn[0:2]
print("출생년도 : ",year)

month = ssn[2:4]
print("출생 월 : ",month)

day = ssn[4:6]
print("출생 일 : ",day)

print("성별 : ",ssn[7])
print("출생지역 : ",ssn[8])
