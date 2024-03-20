#3.1
print(100>200);print(100>=200);print(100<200);print(100<=200);
print(100==200); print(100!=200); print(200==200); print(200!=200);
print(True or True); print(True or False); print(True and False); print(True and True);
print('Morning'<'morning'); print('A'>'B')

#3.3
age=int(input("나이를 입력하시오 :"))
tall=int(input("키를 입력하시오(단위cm) :"))
if age>=19 and tall>=150:
    print("입장할 수 있습니다.")
else :
    print("입장할 수 없습니다.")

#3.5
a,b=map(int,input("두 정수를 입력하시오 :").split())
if a>b:
    print(b,a)
else :
    print(a,b)

#3.7
game_score=int(input("게임 점수를 입력하시오 :"))
if game_score>=1000:
    print("고수입니다.")
else:
    print("입문자입니다.")

#3.9
num=int(input("정수를 입력하시오 :"))
if num%2==0:
    print(num, "는(은) 2로 나누어집니다.")
else :
    print(num, "는(은) 2로 나누어지지 않습니다.")

if num%3==0:
    print(num, "는(은) 3로 나누어집니다.")
else :
    print(num, "는(은) 3로 나누어지지 않습니다.")

if num%2==0 and num%3==0:
    print(num, "는(은) 2와 3 모두로 나누어집니다.")
else :
    print(num, "는(은) 2와 3 모두로 나누어지지 않습니다.")

#3.11 (다시하기)
def check_lottery_numbers(user_numbers, winning_numbers):
    num_correct = len(set(user_numbers) & set(winning_numbers))
    
    if num_correct == 3:
        return "1억 원"
    elif num_correct == 2:
        return "1천만원"
    elif num_correct == 1:
        return "1만 원"
    else:
        return "다음 기회에..."

# 이번 회차의 복권 당첨 번호
winning_numbers = [2, 3, 9]

# 사용자로부터 3개의 정수를 입력 받음
user_input = input("복권 번호 3개를 입력하세요 : ")
user_numbers = list(map(int, user_input.split()))

# 복권 번호와 당첨 번호를 비교하여 상금 결정
prize = check_lottery_numbers(user_numbers, winning_numbers)

# 결과 출력
print("당첨 결과:", prize)

#3.13
x,y=map(int,input("점의 좌표 x,y를 입력하시오 :").split())
if ((x-3)**2+(y-4)**2)**0.5 <=10:
    print("원의 내부에 있음")
else :
    print("원의 외부에 있음")

#3.15 (다시하기...)
for i in range(1,10):
    print("2*", i, "=", 2*i)
num=int(input("1에서 9까지의 숫자를 입력하세요: "))
if 1<= num <= 9:
    i=1
    while i <=9:
        print("2*", i, "=", 2*i)
        i+=1
else:
    print("1에서 9까지의 수를 다시 입력하세요.")


#3.17
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')

for i in range(3):
    print('Python' )
    print('is ')
print('FUN! ')

for i in range(3):
    print('Python' )
print('is ')
print('FUN! ')

#3.19
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")

while True:
    order = input("메뉴를 선택하세요(알파벳 b,c,p 입력) :")
    if order == 'b':
        print("버거를 선택하였습니다.")
        break
    if order == 'c':
        print("치킨을 선택하였습니다.")
        break
    if order == 'p':
        print("피자를 선택하였습니다.")
        break
    else:
        print("메뉴를 다시 입력하세요.")

#3.21(다시하기)
num=int(input("숫자를 입력하세요.")
def is_prime(num):
    if num <=1:
        return False
    elif num <=3:
        return True
    elif num%2==0:
        return False
    else:
        divisor=3
        while divisor*divisor <= num:
            if num % divisor ==0:
                return False
            divisor +=2
        return True

if num ==2 or (num %2 !=0 and is_prime(num)):
    print(num, "은(는) 소수입니다.")
else:
    print(num, "은(는) 소수가 아닙니다.")

#3.23
for i in range(1,n+1):
    result +=i**2
 return result

n=int(input("양의 정수 n을 입력하세요 :"))
print("결과는",  "입니다.")

#3.25(다시하기)
depth_of_well = 30  # 우물의 깊이
climb_per_day = 7   # 달팽이가 하루에 기어올라가는 거리
slide_per_night = 5  # 달팽이가 밤에 미끄러지는 거리
snail_position = 0   # 달팽이의 현재 위치

days = 0  # 걸린 날짜 초기화

while snail_position < depth_of_well:
    days += 1
    snail_position += climb_per_day  # 낮에 올라감
    print("day:", days, "달팽이의 위치:", snail_position, "미터")
    
    if snail_position >= depth_of_well:
        break  # 우물을 벗어났으면 while 루프를 종료
    
    snail_position -= slide_per_night  # 밤에 미끄러짐

print("달팽이가 우물을 벗어나는데 걸리는 날짜:", days, "일")

#3.27(다시하기)
def is_armstrong_number(num):
    num_str = str(num)
    num_length = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    
    return sum_of_powers == num

for number in range(100, 1000):
    if is_armstrong_number(number):
        print("세 자리의 암스트롱 수:" number)
    
#3.29(다시하기)
fuel_tank_capacity = 500  # 초기 연료 탱크 용량
fuel_level = fuel_tank_capacity  # 초기 연료 양

while fuel_level > 0:
    print("현재 연료 양:", fuel_level)
    
    # 연료 사용 또는 충전 입력 받기
    action = input("사용한 연료(-) 또는 충전한 연료(+)를 입력하세요: ")
    
    # 사용자 입력에 따라 연료 양 갱신
    if action == '-':
        fuel_used = int(input("사용한 연료 양을 입력하세요: "))
        fuel_level -= fuel_used
    elif action == '+':
        fuel_added = int(input("충전한 연료 양을 입력하세요: "))
        fuel_level += fuel_added
    else:
        print("잘못된 입력입니다. - 또는 + 기호만 입력하세요.")
        continue
    
    # 연료 양이 10% 미만이면 경고 메시지 출력 후 종료
    if fuel_level < 0.1 * fuel_tank_capacity:
        print("경고: 연료가 10% 미만이니 충전하세요!")
        break

#3.31(다시하기)
    def sum_of_divisors(n):
    # 자기 자신을 제외한 약수의 합 계산
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

def find_amicable_numbers(start, end):
    amicable_pairs = []
    for num1 in range(start, end + 1):
        num2 = sum_of_divisors(num1)
        if num1 != num2 and num2 <= end and sum_of_divisors(num2) == num1:
            # 친화수를 찾았을 때 리스트에 추가
            amicable_pairs.append((num1, num2))
    return amicable_pairs

# 1에서 20000 사이의 친화수 찾기
start_range = 1
end_range = 20000
amicable_numbers = find_amicable_numbers(start_range, end_range)

# 결과 출력
print("1에서 20000 사이의 모든 친화수:")
for pair in amicable_numbers:
    print(pair)
