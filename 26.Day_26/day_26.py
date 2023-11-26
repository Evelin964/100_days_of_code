#code ex 1

# numbers = [1,1,2,3,5,8,13,21,34,55]


# squared = [num*num for num in numbers]

# print(squared)

#code ex 2


# list_of_string = input("Give me a list of strings: ").split()

# int_list_of_string = [int(num) for num in list_of_string]

# even_numbers = [num for num in int_list_of_string if num % 2 == 0]

# print(even_numbers)

# with open(r'26.Day_26/numbers1.txt', mode='r') as file:
#     numbers = file.readlines()
#     int_numbers_1 = [int(num) for num in numbers]

# with open(r'26.Day_26/numbers2.txt', mode='r') as file:
#     numbers = file.readlines()
#     int_numbers_2 = [int(num) for num in numbers]


# distinct_numbers = [num for num in int_numbers_1 if num in int_numbers_2]

# print(distinct_numbers)


# list_of_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# import random

# score_names = {student:random.randint(1,100) for student in list_of_names}

# print(score_names )

# passed_students = {student:score for (student,score) in score_names.items() if score > 50}

# print(passed_students)

# list_of_words =["Python", "data", "scientist", "learning", "problem", "trial", "job", "SQL", "skills", "opinion"]

# dict_of_letters = {value:len(value) for value in list_of_words}

# print(dict_of_letters)

# temperature_in_celcius = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# #temp_f = (temp_c * 9/5) + 32

# temperature_in_fahrenheit = {day:((temp_c * 9/5) + 32) for (day,temp_c) in temperature_in_celcius.items()}

# # print(temperature_in_fahrenheit)
# import pandas as pd
# file_data = pd.read_csv(r'26.Day_26/nato_phonetic_alphabet.csv')


# nato_dict = {row.letter:row.code for (index,row) in file_data.iterrows()}

# code_word = input("Give me a word: ").upper()

# nato_code = [nato_dict[letter] for letter in code_word]
# print(nato_code)

