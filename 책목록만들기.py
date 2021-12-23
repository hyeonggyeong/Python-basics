'''
35,36_내가 읽은 책 목록 만들기
산업시스템공학과 / 2016011405 / 김형경
'''

books = []

books.append({"제목" : "개발자의 코드","출판연도":"2013.02.28","출판사":"A", "쪽수" :200,"추천유무" : False})
books.append({"제목" : "클린 코드","출판연도":"2010.03.04","출판사":"B", "쪽수" :584,"추천유무" : True})
books.append({"제목" : "빅데이터마케팅","출판연도":"2014.07.02","출판사":"A", "쪽수" :296,"추천유무" : True})
books.append({"제목" : "구글드","출판연도":"2010.02.10","출판사":"B", "쪽수" :526,"추천유무" : False})
books.append({"제목" : "강의력","출판연도":"2013.12.12","출판사":"A", "쪽수" :248,"추천유무" : True})

many_page = []
recommends = []
all_pages = 0
pub_company = set()

print("전체 책 목록")

for x in books :
    print(x)

    if x.get("쪽수") > 250 :
        many_page.append(x.get("제목"))
        
    if x.get("추천유무")==True :
        recommends.append(x.get("제목"))
        
    all_pages += x.get("쪽수")

    pub_company.add(x.get("출판사"))
    
print()    
print("쪽수가 250쪽이 넘는 책 리스트 : ",many_page)
print("내가 추천하는 책 리스트 : ",recommends)
print("내가 읽은 책 전체 쪽수 :", all_pages)
print("내가 읽은 책의 출판사 목록 :",pub_company)

print()
many_page2 = [x.get("제목") for x in books if x.get("쪽수") > 250 ]
print("한 줄로 만든 쪽수가 250쪽이 넘는 책 리스트 :",many_page2)

recommends2 = [x.get("제목") for x in books if x.get("추천유무") == True]
print("한 줄로 만든 추천하는 책 리스트 :", recommends2)

pub_company2 = set(x.get("출판사") for x in books)
print("한 줄로 만든 책의 출판사 목록 :", pub_company2)

      

