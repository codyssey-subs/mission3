def input_matrix(size, name):
    matrix = []

    print((f"\n{name} ({size}줄 입력, 공백 구분)"))

    # 3줄 입력 받기
    for i in range(3):
        while True:
            try:
                row = input().split() # 공백 분리
                if lne(row) != size: #개수 검증
                    print(f"입력 형식 오류 : 각 줄에 {size}개의 숫자를 입력하세요.")
                    continue
                row = [float(x) for x in row] # 숫자 변환
                                            #float(sdf)등 터질 수도?   
                matrix.append(row)
                break

            except Exception as e:
                exception_value_handler(e)

    return matrix