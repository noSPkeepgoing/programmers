# 숨어있는 숫자의 덧셈 (2)
# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    nums = ''.join([c if c.isdigit() else ' ' for c in my_string]).split()
    return sum(map(int, nums))
