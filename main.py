#main.py

from utils import *

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
        except Exception as e:
                exception_input_handler(e)


def main():
    mode = select_mode()

    if mode == 1:
        # mode_one()
        print("mode_one()")
    elif mode == 2:
        # mode_two()
        print("mode_two()")

if __name__ == "__main__":
    main()