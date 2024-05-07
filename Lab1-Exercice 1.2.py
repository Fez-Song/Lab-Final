score = int(input("Enter a number: "))


def grade_checker(mark):
    if mark >= 50:
        return 'Pass'
    else:
        return 'Fail'


print(grade_checker(score))