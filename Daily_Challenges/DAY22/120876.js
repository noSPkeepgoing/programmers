// 겹치는 선분의 길이
// 문제 설명
// 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

// lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

// line_2.png

// 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

function solution(lines) {
  line1 = new Set();
  line2 = new Set();
  line3 = new Set();

  for (let i = lines[0][0]; i <= lines[0][1]; i++) line1.add(i);
  for (let i = lines[1][0]; i <= lines[1][1]; i++) line2.add(i);
  for (let i = lines[2][0]; i <= lines[2][1]; i++) line3.add(i);

  a1 = Math.max([...line1].filter((e) => line2.has(e)).length - 1, 0);
  a2 = Math.max([...line1].filter((e) => line3.has(e)).length - 1, 0);
  a3 = Math.max([...line2].filter((e) => line3.has(e)).length - 1, 0);
  a4 = Math.max(
    [...line1].filter((e) => line2.has(e) && line3.has(e)).length - 1,
    0
  );

  return a1 + a2 + a3 - 2 * a4;
}
