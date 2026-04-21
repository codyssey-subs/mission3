#input_utils.py

from utils import *

def input_matrix(size, name):
    matrix = []

    print((f"\n{name} ({size}줄 입력, 공백 구분)"))

    # 3줄 입력 받기
    for i in range(size):
        while True:
            try:
                row = input().split() # 공백 분리
                if len(row) != size: #개수 검증
                    print(f"입력 형식 오류 : 각 줄에 {size}개의 숫자를 입력하세요.")
                    continue
                row = [float(x) for x in row] # 숫자 변환
                                            #float(sdf)등 터질 수도?   
                matrix.append(row)
                break

            except ValueError:
            #숫자 변환 실패, ex) 23a
                print("\n⚠️ 잘못된 입력입니다. \n숫자를 입력하세요!")
            except TypeError:
                #숫자 변환 실패 ex) sdfs
                print("\n⚠️ 잘못된 입력입니다. \n숫자를 입력하세요!")
            except KeyboardInterrupt:
                #Ctrl + C
                print("\n⚠️ 잘못된 입력입니다. \nCtrl + C로 종료되지 않습니다!")
            except EOFError:
                #Ctrl + D
                print("\n⚠️ 잘못된 입력입니다. \nCtrl + D로 안전 종료합니다!")

    return matrix