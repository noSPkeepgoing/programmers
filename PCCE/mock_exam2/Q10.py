# [PCCE 모의고사 2] 10번
# 문제 설명
# 머쓱이는 '생명 게임'이라고 알려진 프로그램을 만들려고 합니다. 생명 게임은 2차원 보드에서 이루어지며, 각각의 칸은 0이 저장된 죽은 칸이거나 1이 저장된 살아있는 칸입니다. 이때 자기 자신의 값과 주변 이웃한 칸들의 값에 따라 다음 세대에서 각 칸의 값이 정해집니다.

# 머쓱이가 만든 생명 게임의 규칙은 다음과 같습니다.

# 살아있는 칸 주변에 이웃이 2명 이하로 존재하면 그 칸은 다음 세대에 죽는다
# 살아있는 칸 주변에 이웃이 5명 이상 존재하면 그 칸은 다음 세대에 죽는다
# 죽어있는 칸 주변에 이웃이 정확히 2명 존재하면 그 칸은 다음 세대에 살아난다.
# 그 이외의 경우에는 살아있거나 죽은 상태가 유지된다.

# 검사 할 점의 개수n과 처음 보드의 상태 board, 점의 좌표를 나타내는 정수쌍 [a,b]가 n개 담긴 리스트 position이 주어졌을 때, 한세대 뒤에 board[a][b] 칸의 상태 리스트를 return하는 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 40
# 3 ≤ board의 길이 ≤ 20
# 3 ≤ board[i]의 길이 ≤ 20
# board[i][j]의 값은 0 또는 1
# board는 직사각형 모양입니다.
# position의 길이 = n
# position[i]는 [a, b] 형태로 칸의 좌표를 나타냅니다.
# 0 ≤ a < board의 길이
# 0 ≤ b < board[0]의 길이

def solution(n, board, position):
    answer = []
    for _ in range(n):
        n = 0
        x, y = position[_]
        for i in range(max(0, x-1), min(len(board), x+2)):
            for j in range(max(0, y-1), min(len(board[0]), y+2)):
                if i == x and j == y:
                    continue
                else:
                    if board[i][j] == 1:
                        n += 1
        if board[x][y] == 1 and n <= 2:
            answer.append(0)
        elif board[x][y] == 1 and n >= 5:
            answer.append(0)
        elif board[x][y] == 0 and n == 2:
            answer.append(1)
        else:
            answer.append(board[x][y])
    return answer
