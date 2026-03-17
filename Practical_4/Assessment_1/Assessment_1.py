# ========== Assesment 1 ==========
# Student Name 1    : Lee Xin Yi
# Student ID 1      : 2103307
# Student Programme : MH
#  
# Student Name 2    : Chua Yun Juan
# Student ID 2      : 2103232
# Student Programme : MH
# ====================================

import csv


# ========== (a) Read CSV ==========
# Read CSV file and get: Employee ID, Name, Department, Sales
with open('Practical_4/Assessment_1/employee_performance.csv', mode='r') as file:  # Update the path to your CSV file
    csv_reader = csv.DictReader(file)
    employee_data = {}
    for row in csv_reader:
        employee_data[row['Employee ID']] = {
            'Name': row['Name'].strip(),
            'Department': row['Department'].strip(),
            'Sales': float(row['Sales'].strip())
        }


# ========== (b) Performance Rating ==========
# Count the number of employees in each ratings
for employee_id, details in employee_data.items():
    sales = details['Sales']
    if sales >= 100000:
        details['Rating'] = 'Excellent'
    elif 80000 <= sales < 100000:
        details['Rating'] = 'Good'
    elif 60000 <= sales < 80000:
        details['Rating'] = 'Average'
    else:
        details['Rating'] = 'Poor'

rating_counts = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Poor': 0}
rating_sales = {'Excellent': 0.0, 'Good': 0.0, 'Average': 0.0, 'Poor': 0.0}

# Count the total number of rating & sales of each ratings
for details in employee_data.values():
    rating = details['Rating']
    sales = details['Sales']
    rating_counts[rating] += 1
    rating_sales[rating] += sales

# Count the average sales
average_sales_by_rating = {rating: (rating_sales[rating] / rating_counts[rating]) for rating in rating_counts}


# ========== (c) Total sales for each Department ==========
# Determine the total sales for each department
department_sales = {}
for details in employee_data.values():
    department = details['Department']
    sales = details['Sales']
    if department in department_sales:
        department_sales[department] += sales
    else:
        department_sales[department] = sales


# ========== Printout results ==========
print('\nPerformance Rating Summary:')
for rating in rating_counts:
    print("{:<10}: {:<3} employees".format(rating, rating_counts[rating]))

print('\nAverage Sales by Rating:')
for rating in average_sales_by_rating:
    print("{:<10}: RM {:.2f}".format(rating, average_sales_by_rating[rating]))

print('\nDepartment Sales Summary:')
for department, total_sales in department_sales.items():
    print("{:<22}: RM {:.2f}".format(department, total_sales))