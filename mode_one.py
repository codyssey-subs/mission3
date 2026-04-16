#mode_one.py

def mode_one():
    #필터A입력
    filter_a = input_matrix(3, "filter_a")
    #필터B입력
    filter_a = input_matrix(3, "filter_b")
    #패턴 입력
    pattern = input_matrix(3, "pattern")
    #MAC 계산
    try:
        score_a = mac_operation(pattern, filter_a)
        score_b = mac_operation(pattern, filter_b)
    except Exception as e:
        exception_value_handler(e)
    #판정 출력
    result = decide(score_a, score_b)
    #시간 측정
    try:
        avg_time_a = measure_average_time(pattern, filter_a, repeat=10)
        avg_time_b = measure_average_time(pattern, filter_b, repeat=10)
        avg_time = (avg_time_a + avg_time_b) / 2
    except Exception as e:
        #성능 측정 실패
        return
    #결과 출력
    print("\n#---------------------------------------")
    print("# [결과]")
    print("#---------------------------------------")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"판정: {result}")
    print(f"연산 시간(평균/10회): {avg_time:.6f} ms")
