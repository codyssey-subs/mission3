#utils.py

def exception_value_handler(e):
    if isinstance(e, ValueError):
        #숫자 변환 실패, ex) 23a
        print("\n⚠️ 잘못된 입력입니다!")
    elif isinstance(e, TypeError):
        #숫자 변환 실패 ex) sdfs
        print("\n⚠️ 잘못된 입력입니다!")