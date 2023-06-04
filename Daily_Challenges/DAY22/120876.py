# 겹치는 선분의 길이
# 문제 설명
# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

# line_2.png

# 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

def solution(lines):
    line1 = set(i for i in range(lines[0][0], lines[0][1] + 1))
    line2 = set(i for i in range(lines[1][0], lines[1][1] + 1))
    line3 = set(i for i in range(lines[2][0], lines[2][1] + 1))

    s1 = max(0, len(line1 & line2) - 1)
    s2 = max(0, len(line1 & line3) - 1)
    s3 = max(0, len(line2 & line3) - 1)
    s4 = max(0, len(line1 & line2 & line3) - 1)

    return s1 + s2 + s3 - s4*2
