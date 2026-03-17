# ===== 4.1 =====
# price = {}
# price = {'orange': 0.80, 'apple': 0.50, 'pear': 1.20}

# price.keys()
# min(price.keys())
# max(price.keys())

# price.values()
# price['banana'] = 0.20
# price.update({'durian': 200})
# del price['orange']

# if 'orange' in price:
#     print(price['orange'])
# if 0.5 in price.values():
#     print('selling cheap')

# for x in sorted(price.keys()):
#     print(x)

# for y in price.values():
#     print(y)


# ===== 4.2 =====
# B = ['Alan', 'Age', 23, 'Gender', 'Male',
#      'Bobby', 'Age', 28, 'Gender', 'Male',
#      'Catherine', 'Age', 21, 'Gender', 'Female']

# A = {}
# for i in range(0, len(B), 5):
#     A[B[i]] = {'Age': B[i+2], 'Gender': B[i+4]}
# print(A)


# ===== 4.3 =====
students = {
    'id1':
    {'name': ['Sarah'],
     'class': ['A'],
     'courses': ['english, math, science']
    },
    'id2':
    {'name': ['Ivan'],
     'class': ['B'],
     'courses': ['english, math, science']
    },
    'id3':
    {'name': ['Sarah'],
     'class': ['A'],
     'courses': ['english, math, science']
    },
    'id4':
    {'name': ['Lee'],
     'class': ['A'],
     'courses': ['english, math, science']
    },
    'id5':
    {'name': ['Zoe'],
     'class': ['B'],
     'courses': ['english, math, science']
    },
}

# Remove duplicate students while keeping id
uniq_students = {}

for student_id, student_info in students.items():
    name = student_info['name'][0]
    if name not in [student_info['name'][0] for student_id, student_info in uniq_students.items()]:
        uniq_students[student_id] = student_info


print(uniq_students)
print()

# Sort students by name while keeping id
sorted_students = dict(sorted(uniq_students.items(), key=lambda item: item[1]['name'][0]))
print(sorted_students)
print()

# Update dict with score
scores = {
    'id1': 70,
    'id2': 75,
    'id3': 70,
    'id4': 80,
    'id5': 60,
}

for student_id in students.keys():
    if student_id in scores:
        students[student_id]['score'] = scores[student_id]  # type: ignore

print(students)