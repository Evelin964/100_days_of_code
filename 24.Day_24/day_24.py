"""This is a mail merge challenge.
    For dr Angela Yu course 100 days of code with python course.
    """
import os

current_directory = os.getcwd()

file_name = "List_of_names.txt"

filepath = os.path.join(current_directory, file_name)


with open(filepath, "r") as file:
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        date, name, address = line.split("|")
        with open("Congragulate.txt", "r") as file:
            file.write(
                f"Dear {name},\nYou are cordially invited to a dinner on {date}. Please come to {address}.\n\n"
            )
            file.close()
