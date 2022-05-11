# Name, Grade
# Assignment
# Description

### START - DO NOT EDIT ###
import sys

# list of dictionaries of employee data
# (gender_code must be only 'M' for male or 'F' for female)
employees = [
    {
        'first_name': 'John',
        'last_name': 'Smith',
        'age': 23,
        'gender_code': 'M'
    },
    {
        'first_name': 'Joe',
        'last_name': 'Ruddy',
        'age': 33,
        'gender_code': 'M'
    },
    {
        'first_name': 'Jenny',
        'last_name': 'McPherson',
        'age': 24,
        'gender_code': 'F'
    },
    {
        'first_name': 'Janice',
        'last_name': 'Johnson',
        'age': 33,
        'gender_code': 'F'
    },
    {
        'first_name': 'Jill',
        'last_name': 'Lancaster',
        'age': 46,
        'gender_code': 'F'
    }
]

engineers = ['Joe', 'Jenny']
managers = ['Joe', 'Jill']

# return the dictionary for an employee if exists, or None
def employee_data(first_name):
    for data in employees:
        if data['first_name'] == first_name:
            return data
    return None

### END - DO NOT EDIT ###

### EDIT HERE ###

if len(sys.argv) != 2:
    print("usage: job-title.py <first_name>", file=sys.stderr)
    sys.exit(1)

first_name = sys.argv[1]
data = employee_data(first_name)
