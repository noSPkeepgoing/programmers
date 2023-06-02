// 안전지대
// 문제 설명
// 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
// image.png
// 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
// 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

function solution(board) {
  let answer = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] == 1) {
        let x = i - 1 < 0 ? 0 : i - 1;
        let y = j - 1 < 0 ? 0 : j - 1;
        while (x < board.length) {
          if (x == i + 2) {
            break;
          }
          while (y < board.length) {
            if (y == j + 2) {
              break;
            }
            board[x][y] = board[x][y] == 1 ? 1 : 2;
            y++;
          }
          y = j - 1 < 0 ? 0 : j - 1;
          x++;
        }
      }
    }
  }
  for (arr of board) {
    answer += arr.filter((e) => e == 0).length;
  }
  return answer;
}
