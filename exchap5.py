#5.1
list_ex=[10,20,30,40,50,60,70]
high=5
low=3
print(list_ex=[low])
print(list_ex=[low+2])
print(list_ex=[high-low])
print(list_ex=[low-high])
print(list_ex=[-1])
print(list_ex=[-low])
print(list_ex=[2*3])
print(list_ex=[2]*3)
print(list_ex=[5%4])
print(list_ex)

#5.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for a in list1:
    for b in list2:
        print(a," *",b,"=",a*b)

#5.5
list3=["I like", "I love"]
list4=["pancakes.", "kiwi juice.",'espresso.']

for c in list3:
    for d in list4:
        print(c+" "+d)

#5.7
n_list=[10,20,30,50,60]
total=0

for a in n_list:
    total += a

print("리스트 원소들:[10,20,30,50,60]")
print("리스트 원소들의 합:",total)

#5.9
n_list=[10,20,30,50,60]
max_num=n_list[0]

for i in n_list:
    if i>max_num:
        max_num=i

print("리스트 원소들:[10,20,30,50,60]")
print("리스트 원소들 중 최댓값:",i)

#5.11
numbers=list(map(int, input("5개의 수를 입력하시오::").split()))
print("합:",sum(numbers))
print("평균:",sum(numbers)/len(numbers))
print("최댓값:",max(numbers))
print("최솟값:",min(numbers))

#5.13
nuMbers=list(map(int, input("10개의 수를 입력하시오::").split()))
print("합:",sum(nuMbers))
print("평균:",sum(nuMbers)/len(nuMbers))
sUm=sum(nuMbers)
mean=sUm/len(nuMbers)
variance = sum((x - mean) ** 2 for x in nuMbers) / len(nuMbers)
standard_deviation = variance ** 0.5
print("표준편차:", standard_deviation)

#5.15
greet="Have a beautiful day."
print(greet[0:4])
print(greet[7:16])
print(greet[17:20])

#5.17
animals=['dog','cat','tiger','lion']
#1)
print(animals)
#2)
an=animals[1:]
an.append(animals[0])
print(an)
#3)
for i in animals:
    print("I love", i)

#5.19
s_list=['abc','bcd','abc','abba','cddc','opq','opq']
new_s_list=[]

for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)
print("s_list =",s_list)
print("new_s_list =",new_s_list)

#5.21
src='a2b3c4d51g1'

for ch in src:
        if ch.isnumeric(): #isnumeric=문자열함수
            for i in range(int(ch)):
                print(ch_old,end='')
        else:
            ch_old=ch

#5.23
person1=['온달',20,1,180.0,100,0]
person2=['이사부',25,1,170.0,70.0]
person3=['평강',22,0,169.0,60.0]
person4=['혁거세',40,1,150.0,50.0]

#1)
person_list=person1+person3+person4
print(str(len(person_list)//5),"명의 정보가 담겨있습니다.")
#2)
person_list1=person1+person2+person3+person4
total_sum = 0
count = 0
for i in range(1, len(person_list1), 5):
    if isinstance(person_list1[i], (int, float)):
        total_sum += person_list1[i]
        count += 1

average = total_sum / count
print("평균나이는", average,"세입니다.")
#3)
n_male=0
n_female=0
person_list1=person1+person2+person3+person4
for j in range(2, len(person_list1), 5):
    if person_list1[j]==1:
        n_male +=1
    else:
        n_female+=1
print("리스트에는 남자가",n_male,"명, 여자가", n_female,"명입니다.")
#4)
person1 = person_list1[:5]
person2 = person_list1[5:10]
person3 = person_list1[10:15]
person4 = person_list1[15:]

print(person1)
print( person2)
print(person3)
print(person4)
