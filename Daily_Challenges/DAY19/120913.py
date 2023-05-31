# 잘라서 배열로 저장하기
# 문제 설명
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(my_str, n):
    answer = []
    while my_str != '':
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer
