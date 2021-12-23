
#산업시스템 공학과 / 2016011405 / 김형경
#장바구니 계산하여 내가 지불해야 할 금액 구하기


print("반갑습니다. 경상마트에 오신 것을 환영합니다.")
apple = int(input("사과는 몇 개 고르셨나요?"))
orange = int(input("오렌지는 몇 개 고르셨나요?"))
grape = int(input("포도는 몇 개 고르셨나요?"))
coupon = int(input("할인쿠폰 금액은 얼마인가요?"))

cost_total = (apple * 1000 + orange * 2000 + grape * 1500) - coupon

print()
print()

print("손님께서 지불해야 할 금액은 아래와 같습니다.")
print("===============================")
print(cost_total,"원")      

