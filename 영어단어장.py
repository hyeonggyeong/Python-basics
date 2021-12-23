'''
영어 단어장 만들기
산업시스템공학과 / 2016011405 / 김형경
'''

eng = {'international':'국제적인', 'attraction':'관광명소', 'itinerary':'여행일정', 'exotic':'이국적인',
       'diverse':'다양한', 'superb':'최고의', 'baggage':'수화물', 'destination':'목적지',
       'missing':'분실된', 'duty':'관세'}

word = input("단어를 입력하시오 : ")
print(eng.get(word,'없음'))
