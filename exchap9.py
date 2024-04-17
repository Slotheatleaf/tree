#9.1
class Prac1:
    def __init__(self,another):
        self.another=another

    def __add__(self,other):
        return self.another+other.another

a= Prac1(123)
b= Prac1(334)
result=a+b
print(result)

class Prac2:
    def __init__(self,another):
        self.another=another

    def __sub__(self,other):
        return self.another-other.another

a= Prac2(123)
b= Prac2(334)
result=a-b
print(result)

class Prac3:
    def __init__(self,another):
        self.another=another

    def __mul__(self,other):
        return self.another*other.another

a= Prac3(123)
b= Prac3(334)
result=a*b
print(result)

class Prac4:
    def __init__(self,another):
        self.another=another

    def __truediv__(self,other):
        return self.another/other.another

a= Prac4(123)
b= Prac4(3)
result=a/b
print(result)

#9.3 (????)
s='Hello World~'
's'.pop() #사용불가
's'.sort() #사용불가
's'.append() #사용불가
's'.upper() #사용가능?
's'.insert() #사용불가
's'.remove() #사용불가

#9.5
a=1
b=1
c=2
d=3
e=3

print("a와 b는 같은 객체인가?",a is b)
print("b와 c는 같은 객체인가?",b is c)
print("c와 d는 같은 객체인가?",c is d)
print("d와 e는 같은 객체인가?",d is e)

#9.7
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return "이름은 "+self.name+'이고, 나이는 '+self.age+'살입니다.'

my_dog=Dog("Mango", "3")
print(my_dog)

#9.9
class Counter:
    def __init__(self, number):
        if number >=100 or number <=-1:
            self.number=0
        else:
            self.number=number

    def reset(self):
        self.number= 0

    def inc(self):
        self.number +=1
        if self.number>=100:
            self.reset()

    def dec(self):
        self.number -=1
        if self.number<=-1:
            self.number=0

    def __str__(self):
        return f'C({self.number})'

    def __add__(self, other):
        result = self.number + other.number
        if result >= 100:
            return Counter(0)
        else:
            return Counter(result)

    def __sub__(self, other):
        result = self.number - other.number
        if result <= -1:
            return Counter(0)
        else:
            return Counter(result)

c1=Counter(10)
c2=Counter(20)
c3=c1+c2
c4=c1-c2
print('c3=',c3)
print('c4=',c4)

#9.11
class Student:
    def __init__(self,name,number,total_score=0,korean_quiz=0,math_quiz=0,science_quiz=0):
        self.name=name
        self.number=str(number).zfill(8)
        self.total_score=total_score
        self.korean_quiz=korean_quiz
        self.math_quiz=math_quiz
        self.science_quiz=science_quiz
        self.update_total_score() #업데이트용... 변수?

    def __str__(self):
        return f"이름: {self.name}, 학번: {self.number}, 국어 성적: {self.korean_quiz}, 수학 성적: {self.math_quiz}, 과학 성적: {self.science_quiz}, 합계: {self.total_score},평균: {self.total_score/3}"

    def get_name(self,name):
        return self.name

    def get_student_id(self,number):
        return self.number

    def set_korean_quiz(self,korean_quiz):
        self.korean_quiz=korean_quiz
        self.update_total_score()
        
    def get_korean_quiz(self):
        return self.korean_quiz

    def set_math_quiz(self,math_quiz):
        self.math_quiz=math_quiz
        self.update_total_score()
        
    def get_math_quiz(self):
        return self.math_quiz
    
    def set_science_quiz(self,science_quiz):
        self.science_quiz=science_quiz
        self.update_total_score()
        
    def get_science_quiz(self):
        return self.science_quiz

    def update_total_score(self):
         self.total_score=self.korean_quiz+self.math_quiz+self.science_quiz

    def get_total_score(self):
        return self.total_score

    def get_avg_score(self,total_score):
        return self.total_score/3

name=input("학생의 이름을 입력하세요:")
student_id=input("학생의 학번을 입력하세요.")

student=Student(name,student_id)
korean_quiz=int(input("학생의 국어 성적을 입력하세요:"))
math_quiz=int(input("학생의 수학 성적을 입력하세요:"))
science_quiz=int(input("학생의 과학 성적을 입력하세요:"))
student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)

#9.13
class Rectangle:
    def __init__(self, x, y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: x={self.x}, y={self.y}, w={self.width}, h={self.height},면적={self.width*self.height}"

    def set_x(self,x):
        self.x=x

    def get_x(self):
        return self.x

    def set_y(self,y):
        self.y=y

    def get_y(self):
        return self.y

    def set_width(self,width):
        self.width=width

    def get_width(self):
        return self.width

    def set_height(self,height):
        self.height=height

    def get_height(self):
        return self.height

    def area(self):
        return self.width*self.height

    def contains(self, r): #포함되어있는것... 아아아악 진짜 모르겠다...
        if (self.x <= r.x and 
            self.x + self.width >= r.x + r.width and 
            self.y <= r.y and 
            self.y - self.height <= r.y - r.height):
            return True
        else:
            return False
    
    def overlaps(self, r): #겹쳐있는것... 아아아악 더모르겠다...
        if (self.x < r.x + r.width and 
            self.x + self.width > r.x and 
            self.y < r.y + r.height and 
            self.y + self.height > r.y):
            return True
        else:
            return False

r1=Rectangle(0,0,100,100)
r2=Rectangle(0,-10,10,10)
r3=Rectangle(-100,0,120,100)

print('r1=',r1)
print('r2=',r2)
print('r3=',r3)

print('r1 contains r2:', r1.contains(r2))
print('r1 contains r3:', r1.contains(r3))
print('r1 overlaps r2:', r1.overlaps(r2))
print('r1 overlaps r3:', r1.overlaps(r3))



#상속 문제
#1)
class Car:
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car):
    def method(self):
        print("서브클래스")

myCar=Car()
mySedan=Sedan()
myCar.method()
mySedan.method()
#정답: 3 (슈퍼클래스 서브클래스)

#2)
class Car:
    speed=0

    def upSpeed(self,value):
        self.speed=sel.speed+value

class RVCar(Car):
    seatNum=0

    def getSeatNum(self):
        return self.seatNum
#정답: class RVCar(Car):
