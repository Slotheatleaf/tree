


#4.1
def my_greet():
    print("환영합니다.")

my_greet()
my_greet()

#4.3
def max2(m,n):
    if m>n:
        return m
    else:
        return n

def min2(m,n):
    if m<n:
        return m
    else:
        return n
print("100과 200중 큰 수는 :", max2(100,200))
print("100과 200중 작은 수는 :", min2(100,200))

#4.5
def inch2cm(inch):
    return inch*2.54

print("1인치 = ",inch2cm(1), "센티미터")
print("2인치 = ",inch2cm(2), "센티미터")
print("3인치 = ",inch2cm(3), "센티미터")
print("4인치 = ",inch2cm(4), "센티미터")
print("5인치 = ",inch2cm(5), "센티미터")

#4.7
def mean3(a,b,c):
    return (a+b+c)/3
def max3(a,b,c):
    return max(a,b,c)
def min3(a,b,c):
    return min(a,b,c)

a,b,c=map(int, input("세 수를 입력하시오:").split())
print(a,b,c, "의 평균값은", mean3(a,b,c))
print(a,b,c, "의 최댓값은", max3(a,b,c))
print(a,b,c, "의 최소값은", min3(a,b,c))
          
#4.9
def mean_of_n(nums):
    return sum(nums)/len(nums)
def max_of_n(nums):
    return max(nums)
def min_of_n(nums):
    return min(nums)

nums=list(map(int, input("정수를 여러 개 입력하시오:").split()))
print("평균값은",mean_of_n(nums))
print("최댓값은",max_of_n(nums))
print("최솟값은",min_of_n(nums))

#4.11
def area(x1,y1,x2,y2):
    width=x2-x1
    height=y2-y1
    return (width*height)/2
x1=int(input("x1 좌표를 입력하시오:"))
y1=int(input("y1 좌표를 입력하시오:"))
x2=int(input("x2 좌표를 입력하시오:"))
y2=int(input("y2 좌표를 입력하시오:"))
print("직각삼각형의 면적은 :",area(x1,y1,x2,y2))

#4.13
def cube_vol(s):
    return s*s*s
def squ_vol(w,h,l):
    return l*w*h
def con_vol(r,h2):
    return (1/3)*3.14*r*r*h2
def cir_vol(r1):
    return (4/3)*3.14*r1*r1*r1
def cyl_vol(r2,h3):
    return 3.14*r2*r2*h3

print("정육면체 부피:", cube_vol(12))
print("정육면체 부피:", cube_vol(20))
print("직육면체 부피:", squ_vol(3,5,6))
print("원뿔 부피:", con_vol(20,10))
print("구 부피:", cir_vol(15))
print("원기둥 부피:", cyl_vol(20,10))

#4.15
def my_sort(*nums):
    numbers = list(nums)
    
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers
print(my_sort(1, 4, 6, 7))

#4.17
def sum_range(n1, n2):
    return sum(range(n1, n2 + 1))
    
print("10에서 20 까지의 정수의 합:",sum_range(10,20))
print("40에서 100 까지의 정수의 합:",sum_range(40,100))

#4.19
def fibo(n):
    if n <=1 :
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("fobo(n)의 n을 입력하세요:"))
print("fibo(",n,") =",fibo(n))

#4.21
def my_birth(input_str):
    year = int(input_str[:2])
    month = int(input_str[2:4])
    day = int(input_str[4:])
    
    if year >= 50:
        year += 1900
    else:
        year += 2000
    return year, month, day

input_str=input("주민등록번호 첫 6숫자 형식 입력:")
year, month, day=my_birth(input_str)
print(year, "년", month, "월", day,"일")

#4.23
import numpy as np
def area_and_circumference(r):
    area=r*r*np.pi
    cir=2*r*np.pi
    return area, cir

while True:
    r = float(input("반지름을 입력하세요: "))
    if r > 0:
        area, cir = area_and_circumference(r)
        print("원의 넓이:",area, "원의 둘레:",cir)
    else:
        print("프로그램을 종료합니다.")
        break

#4.25
s1='Kang Young Min'
s2='Kang Youn-Min'
s3='Park Dong Min'
s4='Park Don-Yun'

def remov_hi_and_sp(name):
    return name.replace(" ", "").replace("-","").upper()
print(remov_hi_and_sp(s1))

def count_N(name1):
    return name1.count("N")
print(count_N(remov_hi_and_sp(s1)))

print("Kang Young Min은(는)", remov_hi_and_sp(s1),"(으)로 수정됨")
print(remov_hi_and_sp(s1),":",count_N(remov_hi_and_sp(s1)),"개의 N이 나타남")

#4.27(다시하기...진짜 모르겠음...ㅠㅠㅠ)
def unit_fraction(frac):
