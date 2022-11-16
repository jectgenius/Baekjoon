n = int(input()) # 표준 입력 함수 input() 호출하여 과목의 수를 문자열로 입력 받아 리턴한 뒤 int() 함수 호출하여 정수로 변환 한 뒤 변수 m에 대입
a = list(map(int, input().split())) # input() 함수 호출하여 과목의 점수를 공백으로 구분한 문자열로 입력받은 뒤 리턴하여 split() 메소드 호출하여 인자로 전달한 뒤 공백을 구분자로 하여 분리된 문자열로 리턴한 뒤 map() 함수 호출하여 int() 함수와 맵핑하여 정수호 각각 변환 한 뒤 list() 함수 호출하여 리스트로 만들어 변수 a에 대입
m = max(a) # max() 함수 호출하여 리스트 a의 요소 중에서 최댓값 찾아 리턴하여 변수 m에 대입
sum = 0 # 변수 sum에 0대입

for i in a: # 변수 i에 리스트 a의 모든 요소가 순서대로 하나씩 할당될 동안 반복
    sum += i # 변수 sum에 i 합함

print(sum*100/m/len(a)) # 표준 출력 함수 print() 호출하여 새로운 평균을 구한뒤 출력

# 각 점수마다 하나씩 따로 계산하는 것이 아니라, 규칙성을 발견하여 한 번만 계산하도록 하자!