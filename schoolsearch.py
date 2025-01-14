import os

def read_students_file(file_name):
    students = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                item = line.strip().split(',')
                students.append({
                    'StLastName': item[0],
                    'StFirstName': item[1],
                    'Grade': int(item[2]),
                    'Classroom': int(item[3]),
                    'Bus': int(item[4]),
                    'GPA': float(item[5]),
                    'TLastName': item[6],
                    'TFirstName': item[7]
                })
    except FileNotFoundError:
        print("Error: students.txt not found.")
        exit(1)
    except IndexError as e:
        print(f"Error: Invalid File Syntax")
        exit(1)

    return students


def search_by_lastname(lastname, number):
    if number is not None:
        our_list = search_by_bus(number)
    else:
        our_list = students

    if our_list is None:
        print("No Students Found")
        return

    found = []
    for s in our_list:
        if s['StLastName'] == lastname:
            found.append(s)
    if found == []:
        print("No Students Found")
    else:
        for item in found:
            print(", ".join(str(value) for value in item.values()))


def search_by_teacher(lastname):
    found = []
    for s in students:
        if s['TLastName'] == lastname:
            found.append(s)
    if found == []:
        print("No Teachers Found")
    else:
        for item in found:
            print(", ".join(str(value) for value in item.values()))


def search_by_bus(number):
    found = []
    for s in students:
        if s['Bus'] == int(number):
            found.append(s)

    if found == []:
        return None
    else:
        return found


def search_by_grade(Grade, option):
    found = []
    for s in students:
        if s['Grade'] == int(Grade):
            found.append(s)
    if found == []:
        print("No Students Found")
    else:
        if option is None:
            for item in found:
                print(", ".join(str(value) for value in item.values()))
        elif option[0] == 'H':
            max = found[0]
            for item in found:
                if item['GPA'] > max['GPA']:
                    max = item
            print(", ".join(str(value) for value in max.values()))
        elif option[0] == 'L':
            min = found[0]
            for item in found:
                if item['GPA'] < min['GPA']:
                    min = item
            print(", ".join(str(value) for value in min.values()))


def average(grade):
    avg = 0.0
    num = 0
    for s in students:
        if s['Grade'] == int(grade):
            avg += s['GPA']
            num += 1
    if num == 0:
        print("No Students Found")
        return

    avg = avg / num
    avg = avg // 0.01
    avg = avg / 100
    print(f"The Average GPA for Grade {grade} is: {avg}")


def get_info():
    count = 0
    for i in range(0, 7):
        for student in students:
            if student['Grade'] == i:
                count += 1
        print(f"{i}: {count}")
        count = 0


if __name__ == "__main__":
    students = read_students_file("students.txt")
    while (1):
        command = input(">").strip().split(" ")
        if command[0][0] == 'S':
            if len(command) >= 3:
                search_by_lastname(command[1], command[2])
            else:
                search_by_lastname(command[1], None)
        elif command[0][0] == 'T':
            search_by_teacher(command[1])
        elif command[0][0] == 'B':
            a = search_by_bus(command[1])
            if a is not None:
                for item in a:
                    print(", ".join(str(value) for value in item.values()))
            else:
                print("No Students Found")
        elif command[0][0] == 'G':
            if len(command) < 3:
                search_by_grade(command[1], None)
            else:
                search_by_grade(command[1], command[2])
        elif command[0][0] == 'A':
            average(command[1])
        elif command[0][0] == 'I':
            get_info()
        elif command[0][0] == 'Q':
            exit(0)
        else:
            print("Error: Invalid Command")
