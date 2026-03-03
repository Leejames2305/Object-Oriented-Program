# ===== 3.1 ======
# list1 = list(range(4))
# list2 = list(range(1, 10))
# list3 = list(range(1, 10, 2))

# # Pairing 2 lists (Zip)
# p = list(zip([1, 2, 3], ['a', 'b', 'c']))
# print(p)

# A, B = zip(*p)
# print(A)
# print(B)


# ===== 3.2 ======
# words = ['Python', 'is', 'a', 'programming', 'language']
# for e in words:
#     print(e)

# for i in range(len(words)):
#     print(i, words[i])

# for i, e in enumerate(words):
#     print(i, e)


# ===== 3.3 ======
# L1 = ['a,', 'b,', 'c,']
# L2 = [1, 2, 3]
# for x, y in zip(L1, L2):
#     print(x, y)

# # Fix the following
# '''
# for i, x, y in enumerate(zip(L1, L2)):
#     print(i, x, y)
# '''
# for i, (x, y) in enumerate(zip(L1, L2)):
#     print(i, x, y)

# a = []
# for i in range(5):
#     data = input('Enter data: ')
#     a.append(data)
# print(a)


# ===== 3.4 ======
# array = [1,2,3]
# print([x for x in array])
# print([3*x for x in array])
# print([x for x in array if x%2==1])
# print([x+y for x in [1,2] for y in [.1,.2]])
# print([(x,y) for x in [1,2] for y in ['a','b']])
# array = [[1,2],[3,4],[5,6]]
# print([y for x in array for y in x])


# ===== Exercise 1 ======
'''Provide solutions to classify strings from list X into i,o,e lists based on starting character
let X = ['i2','o4','23','\te5','e7\t']
i_list = ['i2']
o_list = ['o4']
e_list = ['e5','e7']
other_list = ['23']
'''
# X = [' i2', 'o4', '23 ', '\te5', '99', 'e7\t', '  o9', 'i1', 'e7']
# i_list = []
# o_list = []
# e_list = []
# other_list = []

# for s in X:
#     s = s.strip()  # Remove leading and trailing whitespace
#     # print(s)
#     if s.startswith('i'):
#         i_list.append(s)
#     elif s.startswith('o'):
#         o_list.append(s)
#     elif s.startswith('e'):
#         e_list.append(s)
#     else:
#         other_list.append(s)

# print("i_list:", i_list)
# print("o_list:", o_list)
# print("e_list:", e_list)
# print("other_list:", other_list)

# ===== 3.5 ======
# # Without exception handling
# file = 'data.txt'
# with open(file, 'r') as f:
#     data = f.read()
#     print(data)

# # With exception handling
# try:
#     file = 'data.txt'
#     with open(file, 'r') as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print(f"Error: The file '{file}' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# ===== Exercise 2 ======
'''Please study the exception handling below:
import time

def do_something():
    print("Doing something..., press Ctrl+C to stop")
    time.sleep(0.5)
while True:
    try:
        do_something()
    except KeyboardInterrupt:
        print("Ctrl+C detected, stop!")
        break
print('End')

Modify the code to use KeyboardInterrupts (Ctrl+C) to produce following outputs.
Counting from 1 to 10, code prints out if not interrupted.
Program terminate whenever KeyboardInterrupt occurs. 
'''
import time

def count():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

while True:
    try:
        count()
        break  # Exit the loop after counting to 10
    except KeyboardInterrupt:
        print("Ctrl+C detected, stop!")
        break
print('End')