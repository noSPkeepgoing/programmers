# 등수 매기기
# 문제 설명
# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다.
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때,
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(score):
    avg = [sum(x)/2 for x in score]
    idx = sorted(avg, reverse=True)

    return [idx.index(i) + 1 for i in avg]
