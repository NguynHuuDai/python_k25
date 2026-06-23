def calculate_average(scores):
    valid_scores = []

    for score in scores:
        if isinstance(score, (int, float)):
            valid_scores.append(score)

    if len(valid_scores) == 0:
        return 0

    return sum(valid_scores) / len(valid_scores)


def classify_student(average):
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    else:
        return "Yếu"
