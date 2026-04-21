#mode_two.py

def load_filters(raw_filters):
    filters_by_size = {}

    for size_key, filter_group in raw_filters.items():
        size = int(size_key.split("_")[1])

        cross_filter = None
        x_filter = None
        
        for raw_label, matrix in filter_group.items():
            label = normalize_label(raw_label)

            if label == "Cross":
                cross_filter = matrix
            elif label == "X":
                x_filter = matrix
        
        if cross_filter is None or x_filter is None:
            raise ValueError(f"{size_key} 필터에 Cross 또는 X 필터가 없습니다.")

        filters_by_size[size] = {
            "Cross": cross_filter,
            "X": x_filter
        }

    return filters_by_size

def mode_two():
    # filters 먼저 읽기
        data = load_json("data.json")
        raw_filters = data["filters"]
        raw_patters = data["patterns"]
    
    # size 별로 filter 정리
    filters_by_size = load_filters(raw_filters)

    print("\n#---------------------------------------")
    print("# [2] 패턴 분석 (라벨 정규화 적용)")
    print("#---------------------------------------")

    total_cnt = 0
    pass_cnt = 0
    fail_cnt = 0
    fail_cases = []

    for p_key, p_data in raw_patters.items():
        total_cnt += 1

        try:
            analysis_result = analyze_pattern(p_key, p_data, filters_by_size)
            # print_pattern_result(p_key, analysis_result)

            if analysis_result["passed"]:
                pass_cnt += 1
            else:
                fail_cnt += 1
                fail_cases.append({
                    "key": p_key,
                    "reason": f"expected = {analysis_result['expected']}, result = {analysis_result['result']}"
                })
        except Exception as e:
            fail_cnt += 1
            reason = str(e)
            print_pattern_result(p_key, reason)
            fail_cases.append({
                "key": p_key,
                "reason": reason
            })
    
    try:
        run_performance_analysis(filters_by_size)
    except Exception as e:
        print("성능 분석 중 오류 발생")
        exception_value_handler(e)

    print_summary(total_cnt, pass_cnt, fail_cnt, fail_cases)