def validate_student_presence(student_presence):
    if (
        student_presence[0] is None
        or student_presence[1] is None
        or type(student_presence[0]) is not int
        or type(student_presence[1]) is not int
    ):
        raise ValueError


def is_target_time(student_presence, target_time):
    validate_student_presence(student_presence)
    most_people = 0
    for student_hour in range(student_presence[0], (student_presence[1] + 1)):
        if student_hour == target_time:
            most_people += 1
    return most_people


def study_schedule(permanence_period, target_time):
    try:
        most_people = 0
        if target_time is None:
            return None
        for student_presence in permanence_period:
            most_people += is_target_time(student_presence, target_time)
        return most_people
    except ValueError:
        return None
