#utils.py

def exception_value_handler(e):
    except ValueError:
        #숫자 변환 실패, ex) 23a
        print("\n⚠️ 잘못된 입력입니다!")
    except TypeError:
        #숫자 변환 실패 ex) sdfs
        print("\n⚠️ 잘못된 입력입니다!")