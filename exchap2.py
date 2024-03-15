#2.1
print(200,'+',300,'+',400,'+','=', 200+300+400)

#2.3
width = 30
height = 60
print("사각형의 면적 :",width*height)

#2.5
q=int(input("정사각형의 밑변을 입력하시오 :"))
print("정사각형의 면적 :", q*q)

#2.7
print("10! =", 10*9*8*7*6*5*4*3*2*1)

#2.9 어떻게 하는지 잘 모르겠으므로 나중에 다시 해볼것
fahrenheit = (9/5) * celsius + 32

#2.11
t=int(input("화씨 온도를 입력하세요 :"))
print("화씨", t, "도는 섭씨", (t-32)*(5/9), "도 입니다.")

#2.13
PI=3.141592
r=int(input("원의 반지름을 입력하세요"))
print("원의 둘레 =", 2*PI*r, ", 원의 면적 =", PI*r*r)

#2.15
a=int(input("밑변의 길이를 입력하세요."))
b=int(input("높이의 길이를 입력하세요."))
print("빗변의 길이 :", (a**2 + b**2)**0.5)

#2.17
print(2 << 0,2 << 1, 2 << 2, 2 << 3, 2 << 4, 2 << 5, 2 << 6, 2 << 7, 2 << 8, 2 << 9)

#2.19
A=int(input("정수를 입력하세요 :"))
if (A < 0 or A <= 100) and A/2!=1.0 :
 print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False")
else :
 print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? True")


#2.21
number=int(input("정수를 입력하시오 :"))
print(number, "의 2진수 값 :", bin(number))
print(number, "의 2진수 값에 대한 비트 단위 부정값 : ", bin(~number))

#2.23
nUmber=int(input("세 자리 정수를 입력하시오 :"))
hun = nUmber // 100
ten = (nUmber %100) // 10
one = nUmber % 10

print("백의 자리 :", hun)
print("십의 자리 :", ten)
print("일의 자리 :", one)
