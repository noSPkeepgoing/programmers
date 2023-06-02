# 직사각형 넓이 구하기
# 문제 설명
# 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다.
# 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때,
# 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

def solution(dots):
    x1, x2 = max(dots)[0], min(dots)[0]
    y1, y2 = max(dots)[1], min(dots)[1]

    return (x1 - x2) * (y1 - y2)
