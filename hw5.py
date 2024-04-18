def read_single_digit(digit):
    korean_digits = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return korean_digits[digit]

def read_number(number):
    
    hundreds = number // 100
    tens = (number % 100) // 10
    units = number % 10
    
    result = ""
    if hundreds != 0:
        result += read_single_digit(hundreds) + " "
    if tens != 0:
        result += read_single_digit(tens) + " "
    if units != 0 or (hundreds == 0 and tens == 0):
        result += read_single_digit(units)
    
    return result

def main():
  
    while True:
        try:
            num = int(input("세 자리수 이하의 10진 정수를 입력하세요: "))
            if num < 0 or num > 999:
                raise ValueError
            break
        except ValueError:
            print("잘못된 입력입니다. 다시 입력하세요.")

    result = read_number(num)
    print("한글로 읽은 결과:", result)

if __name__ == "__main__":
    main()
