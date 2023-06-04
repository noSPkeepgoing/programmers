# 평행
# 문제 설명
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def solution(dots):
    a, b, c, d = dots
    if slop(a, b) == slop(c, d):
        return 1
    elif slop(a, c) == slop(b, d):
        return 1
    elif slop(b, c) == slop(a, d):
        return 1
    return 0


def slop(a, b):
    return abs(a[0]-b[0]) / abs(a[1]-b[1])
