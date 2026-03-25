

def round_scores(student_scores):
    new_list = []
    for i in range(len(student_scores)):
        student_scores[i] = round(student_scores[i])
        new_list.append(student_scores[i])

    print(new_list)

def count_failed_students(student_scores):
    count = 0
    for index in range(len(student_scores)):
        if student_scores[index] <= 40:
            count += 1

    print count

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    for index in range(len(student_scores)):
        name = 0
        new_list = []
        new_list.append(f'''{index + 1}.{student_names[name]} :    
                       {student_scores[index]}''' )
        name += 1

    print new_list

student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
output1 = round_scores(student_scores)
output2 = count_failed_students(student_scores)
