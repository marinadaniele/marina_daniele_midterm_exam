################## Question 1
a = 19

print(a+3)

print(a // 2)

################### Qestion 2
print(2+3*6/2)

################### Question 3

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

print(c // 3)

################### Question 4

# numbers to check=
#  1. 6593036601359343374664733439531066303956
#  2. 5485839837501070045005400701057389385845
#  3. 8025833559061079503003059701609553385208
#  4. 7489617719749244646336564429479177169847
def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

number_to_check = 7489617719749244646336564429479177169847
result = is_palindrome(number_to_check)

print(f"The number {number_to_check} is a palindrome: {result}")

##################### Question 5

text = "The unhuman alien walked down the street"
def find_pattern_occurrences(text):
    words = text.split()
    match_count = 0
    for word in words:
        if (word.startswith('un') and word.endswith('an')):
            match_count += 1
    return match_count
print(find_pattern_occurrences(text))

##################### Question 7
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)

for number in random_numbers[:]:
    if number > 50:
        random_numbers.remove(number)
    else:
        random_numbers[random_numbers.index(number)] = "XX"

print("Modified list:", random_numbers)
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)

for number in random_numbers[:]:
    if number > 50:
        random_numbers.remove(number)
    else:
        random_numbers[random_numbers.index(number)] = "XX"

print("Modified list:", random_numbers)

###################### Question 8
def is_valid_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        if ':' in url:
            return True
    else:
        return False

############################ Question 9

def days_since_birthday(birthday):

    birth_year = int(birthday[-4:])
    current_year = 2024

    years_passed = current_year - birth_year - 1

    days_passed = years_passed * 365

    return days_passed

# Test
birthday = "29-07-2005"
print("Days since birthday:", days_since_birthday(birthday))