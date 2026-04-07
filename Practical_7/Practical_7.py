# ===== 7.1 =====
# class employee: 
#     def __init__(self, name, sal): 
#         self._name=name   # protected attribute; use one underscore 
#         self.__salary=sal # private attribute
    
#     def get_salary(self): 
#         return self.__salary
    
#     def info(self): 
#         print('{}: salary is {}'.format(self._name, self.__salary))

# class engineer(employee): 
#     def info(self): 
#         print('{}: salary is {}'.format(self._name, self.get_salary()))

# person = engineer('Bob', 4000) 
# person.info()  # Cannot access salary using __salary, must go through get_salary() method
# person = employee('Steve', 8000) 
# person.info()


# ===== 7.2 =====
# import math

# class Point:   
#     def __init__(self, xCoord, yCoord): 
#         self.__xCoord = xCoord 
#         self.__yCoord = yCoord 
#         self.__len = math.sqrt(xCoord ** 2 + yCoord ** 2) 
#         self.__angle = math.atan(yCoord / xCoord) 
 
#     def __str__(self): # overload the builtin function str()   
#         return ('point @ ({}, {}), |A| = {}, θ = {}'.format(                 
#             self.__xCoord, self.__yCoord, self.__len, self.__angle)) 
 
#     def __add__(self, y): 
#         x = self.__xCoord + y.__xCoord 
#         y = self.__yCoord + y.__yCoord 
#         return Point(x, y)
    
#     def __eq__(self, others):
#         return (self.__xCoord, self.__yCoord) == (others.__xCoord, others.__yCoord)

# x = Point(math.sqrt(3), 3) 
# y = Point(1, 1) 
# print('x =', str(x)) 
# print('y =', str(y)) 
# z = x + y 
# print('z =', str(z))

# a = Point(1, 2)
# b = Point(4, 3)
# c = Point(4, 3)
# print('Check b = a:', b == a)
# print('Check b = c:', b == c)


# ===== 7.3 =====
# Base Class: Person  
class Person: 
    def __init__(self, person_id, name, age): 
        self.person_id = person_id 
        self.name = name 
        self.age = int(age) 
 
    def display_info(self): 
        print(f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}") 
 
# Subclass: Student 
class Student(Person): 
    def __init__(self, student_id, name, age, major, cgpa): 
        super().__init__(student_id, name, age) 
        self.major = major 
        self.cgpa = float(cgpa) if cgpa else 0.0  # Convert to float 
 
    def display_info(self): 
        print(f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Role: Student, " 
              f"Major: {self.major}, CGPA: {self.cgpa:.2f}") 
 
# Subclass: Staff 
class Staff(Person): 
    def __init__(self, staff_id, name, age, major, years_experience): 
        super().__init__(staff_id, name, age) 
        self.major = major 
        self.years_experience = int(years_experience) if years_experience else 0  # Convert to int 
 
    def display_info(self): 
        print(f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Role: Staff, " 
              f"Major: {self.major}, Experience: {self.years_experience} years") 
 
# Function to load data from CSV file 
def load_data(filename): 
    people = [] 
    try: 
        with open(filename, mode='r', encoding='utf-8') as file: 
            lines = file.readlines() 
            headers = lines[0].strip().split(",")  # Extract headers 
            for line in lines[1:]: 
                data = line.strip().split(",")  # Read each row 
                person_data = dict(zip(headers, data))  # Map headers 

                major = person_data["Major"] 
                cgpa = person_data["CGPA"] 
                years_experience = person_data["YearsExperience"]
                if cgpa: 
                    person = Student(person_data["ID"], person_data["Name"], person_data["Age"], major, cgpa) 
                elif years_experience: 
                    person = Staff(person_data["ID"], person_data["Name"], person_data["Age"], major, years_experience) 
                else: 
                    person = Person(person_data["ID"], person_data["Name"], person_data["Age"]) 
                people.append(person)
        print("Data successfully loaded from", filename) 
    except FileNotFoundError: 
        print(f"File '{filename}' not found.") 
    return people

# Function to display all people 
def display_people(people): 
    print("\nPeople List:") 
    for person in people: 
        person.display_info() 
 
# Function to get students with CGPA < 2.0 
def get_students_below_2_cgpa(people): 
    print("\nStudents with CGPA < 2.0:") 
    for person in people: 
        if isinstance(person, Student) and person.cgpa < 2.0: 
            person.display_info() 
 
# Function to get staff with ≥10 years experience 
def get_staff_with_10_plus_years(people): 
    print("\nStaff with >= 10 years of experience:") 
    for person in people: 
        if isinstance(person, Staff) and person.years_experience >= 10: 
            person.display_info() 
 
# Main Execution 
people = load_data("Practical_7/persons.csv") 
display_people(people) 
get_students_below_2_cgpa(people) 
get_staff_with_10_plus_years(people)