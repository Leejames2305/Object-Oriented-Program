# ====== 2.1 ======
# num = int(input("Enter a number: ")) 
# mod = num % 2 
# if mod > 0: 
#     print("This is an odd number.") 
# else: 
#     print("This is an even number.")


# if 'c' in 'abcde': 
#     print('Found c') 
# elif 'C' in 'abcde': 
#     print('Found C') 
# else: 
#     print('Cannot find C or c')

# if 2 in [1,2,3]:  
#     print('Yes')

# ====== 2.2 ======
# for x in range(10): 
#     print(x) 
# for x in range(1,11): 
#     print(x) 
# for x in range(1,11,2): #skip by 2 
#     print(x) 
# for x in range(10,0,-1): #move in reverse 
#     print(x) 
 
# # Nested loops 
# for x in range(3): 
#     for y in range(3): 
#         print(x,y)

# ====== Lists - Extra ======
# list1 = [1,2,3]
# otherlist = [4,5,6]

# # Pointing to the same list
# list1 = otherlist

# print(id(list1))
# print(id(otherlist))

# # Modifying list1 will also modify otherlist as they point to the same list
# list1[0] = 100

# print(list1)
# print(otherlist)
# print(id(list1))
# print(id(otherlist))

# # If creating list with copy, they will point to different lists
# anotherlist = list1.copy()
# anotherlist[0] = 200
# print(anotherlist)
# print(id(anotherlist))

# ===== 2.3 ======
# a, b = 0, 1 
# n = int(input("Size of Fibonacci sequence: "))
# i = 0
# while i < n: 
#     print(a) 
#     a, b = b, a+b
#     i += 1

# ===== 2.4 ======
# def f(a, b): 
#     return a/2, 2*b 
 
# x, y = f(1, 2)
# print(x, y)
# x, _ = f(1, 2)
# print(_)
# x, *_ = f(1, 2)
# print(_)

# def isDivisor(x):
#     if num % x == 0: 
#         return True 
#     else: 
#         return False

# num = int(input("Enter a number: ")) 
# for x in range(1,num+1):
#     if isDivisor(x): 
#         print(x)

# ===== 2.5 ======
# Create/append/size/concatenate 
# array = [] 
# array.append(1) 
# array.append('2') 
# array = array + [3] 
# array += ['4'] 
# print(len(array)) 
# vector=[5,6] 
# array = array + vector
# print(array)
# print('2' in array) 
# print(5 in array) 
 
# # Index and slice
# print() 
# print(array[0]) 
# print(array[:2]) 
# print(array[2:]) 
# print(array[1:2]) 
 
# List of lists 
# array = [[1, 2], [3, 4]] 
# array = [] 
# array.append([]) #[[]] 
# array.append([]) #[[],[]] 
# array[0].append('a') #[['a'],[]] 
# array[0].append('b') #[['a', 'b'],[]] 
# array[1].append('c') #[['a', 'b'],['c']] 
# array[1].append('d') #[['a', 'b'],['c', 'd']] 
# array[1]    #['c', 'd'] 
# array[1][0] #'c' 
 
# Converting string to list 
# str = '12345678' 
# print(list(str)) 
# print([list('12'), list('34')]) 
 
# Look up for all functionalities, e.g. remove/sort/count, of list by: 
# dir(list) 
# help(list)

# ===== 2.6 ======
# words = ['Python', 'is', 'cool'] 
# for e in words: 
#     print(e)

# words = ['Python', 'is', 'cool'] 
# for e in range(len(words)): 
#     print(words[e])

# data = [ ['A',1,2], ['B',3,4], ['C',5,6] ] 
# for a in data: 
#     for b in a: 
#         print(b)

# ===== Excercise ======
'''
Program read A2_input.csv, store data in list of lists, and display analysis described below:
0. List of lists should look something like this: 
[['Alan Tan', 'M', 39, 2000], 
 ['Bradley', 'm', 34, 5448], 
 ['Zoe Yap', 'f', 25, 5769]]

1. Print out entries of table
Alan Tan M 39 2000
...

2. Print out all female names with their index number
[2] Catherine
[24] Zoe Yap

3. Find richest man and woman in the list
The richest man is ...
The richest woman is ...

4. Find the mean average of age and incomes in the list
Mean Age: ...
Mean Income: ...

5. Find the median average of incomes, if even number of items, take average if 2 middle items. Do also for max and min incomes.
Median Income: ...
Max Income: ..., Min Income: ...
'''
import csv
with open('Practical_2/A2_input.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

data = data[1:]  # Remove header
# print(data)

# 1. Print out entries of table
print("Entries of table:")
for row in data:
    # Remove redundant spaces (front/end/middle) and convert age and income to integers
    name = ' '.join(row[0].split())
    gender = row[1].strip().upper()
    age = int(row[2].strip())
    income = int(row[3].strip())

    # Print the entry with fixed width for better alignment
    print(f"{name:15} {gender:1} {age:3} {income:6}")


# 2. Print out all female names with their index number
print("\nFemale names with index number:")
for row in data:
    if row[1].strip().upper() == 'F':
        index = data.index(row)
        name = ' '.join(row[0].split())
        print(f"[{index}] {name}")


# 3. Find richest man and women
print("\nFinding Richest person ...")
incomelistM = []
incomelistF = []
personinfo = []

for row in data:
    name = ' '.join(row[0].split())
    gender = row[1].strip().upper()
    income = int(row[3].strip())

    if gender == 'M':
        personinfo.append(name)
        personinfo.append(income)  # Person info is [name, income]
        incomelistM.append(personinfo)  # incomelist is [[name, income], [name, income], ...]
    
    if gender == 'F':
        personinfo.append(name)
        personinfo.append(income)
        incomelistF.append(personinfo)
    
    personinfo = []  # Clear personinfo for next iteration

for person in incomelistM:
    if person[1] == max(incomelistM, key=lambda x: x[1])[1]:  # If person income = max of entire list
        richestman = person[0]

for person in incomelistF:
    if person[1] == max(incomelistF, key=lambda x: x[1])[1]:
        richestwoman = person[0]
    
print(f"The richest man is {richestman}")  # type: ignore
print(f"The richest woman is {richestwoman}")  # type: ignore


# 4. Find the mean average of age and incomes in the list
print("\nFinding mean average of age and income ...")
agelist = []
incomelist = []

for row in data:
    age = int(row[2].strip())
    income = int(row[3].strip())
    agelist.append(age)
    incomelist.append(income)

meanAge = sum(agelist) / len(agelist)
meanIncome = sum(incomelist) / len(incomelist)

print(f"Mean Age: {meanAge:.2f}")
print(f"Mean Income: {meanIncome:.2f}")


# 5. Find median of incomes, and min/max as well
print("\nFinding median, max and min of incomes ...")
incomelist.sort()
if len(incomelist) % 2 == 0:
    index1 = int(len(incomelist)/2)
    index2 = index1 + 1
    medianIncome = (incomelist[index1] + incomelist[index2]) / 2
else:
    index = int((len(incomelist)-1)/2)
    medianIncome = incomelist[index]

print(f"Median Income: {medianIncome}")
print(f"Max Income: {max(incomelist)}")
print(f"Min Income: {min(incomelist)}")