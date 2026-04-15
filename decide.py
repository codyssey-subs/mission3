#decide.py

def decide(score_a, score_b, epsilon=1e-9):
    if abs(score_a - score_b) < epsilon:
        return "UNDECIDED"
    elif score_a > score_b:
        return "Cross"
    elif score_b > score_a:
        return "X"

#부동소수점
#epsilon