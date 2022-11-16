n = input() # 표준출력함수 input() 호출하여 숫자의 개수를 문자열로 입력받아 변수 n에 대입
numbers = list(input()) # 표준 입력 함수 input() 호출하여 n개의 숫자 나열을 문자열로 입력받아 list() 함수 호출하여 인자로 전달하여 문자열의 각 문자가 요소인 리스트 만들어 변수 numbers에 대입
sum = 0 # 변수 sum에 0 대입하여 초기화

for i in numbers: # 변수 i에 리스트 numbers의 모든 요소가 순서대로 하나씩 할당될 동안 반복
    sum += int(i) # int() 함수 호출하여 문자열 i를 정수로 변환하여 리턴한 뒤 변수 sum에 합함

print(sum) # 표준 출력 함수 print() 호출하여 변수 sum에 저장된 각 자리 숫자의 합 출력