def calculate_result(marks):

    total = sum(marks)

    percentage = total / len(marks)

    if percentage >= 90:

        grade = "A+"

    elif percentage >= 80:

        grade = "A"

    elif percentage >= 70:

        grade = "B"

    elif percentage >= 60:

        grade = "C"

    elif percentage >= 50:

        grade = "D"

    else:

        grade = "Fail"

    return total, percentage, grade