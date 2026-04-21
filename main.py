#main.py

from mode_one import *
from utils import *
from input_utils import *

def select_mode():
    print("\n=== Mini NPU Simulator ===")
    print("\n[모드 선택]")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")
    while True:
        try:
            mode = input("선택: ").strip()

            if mode == "1":
                return 1
            elif mode == "2":
                return 2
            else:
                print("\n⚠️ 잘못된 입력입니다!\n")
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


def main():
    while True:
        mode = select_mode()

        if mode == 1:
            mode_one()
            # print("mode_one()")
        elif mode == 2:
            # mode_two()
            print("mode_two()")

if __name__ == "__main__":
    main()