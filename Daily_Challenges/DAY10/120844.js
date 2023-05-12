// 배열 회전시키기
// 문제 설명
// 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
// 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

function solution(numbers, direction) {
  if (direction == 'right') {
    return [numbers[numbers.length - 1]].concat(numbers.slice(0, -1));
  } else {
    return numbers.slice(1).concat([numbers[0]]);
  }
}
