# 약수 구하기
# 문제 설명
# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    for i in range(1, int(n**(1/2)) + 1) :
        if n % i == 0 :
            if(i != n**(1/2)) :
                answer.append(n // i)
            answer.append(i)
    return sorted(answer)