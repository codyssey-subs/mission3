#normalize_label.py

def normalize_label(labe):
    label = label.lower()

    mapping = {
        "+" : "Cross",
        "cross" : "Cross",
        "x" : "X"
    }

    return mapping.get(label, label)

#mapping.get(label, label)
#mapping 딕셔너리 안에 label이 key로 있으면 -> 그 value반환
#없으면 -> 두번째 인자인 label 그대로 반환