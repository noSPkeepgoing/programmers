// 가까운 수
// 문제 설명
// 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

function solution(array, n) {
  array.sort((a, b) => a - b);
  answer = array.map((e) => Math.abs(n - e));
  return array[answer.findIndex((e) => e == Math.min(...answer))];
}
