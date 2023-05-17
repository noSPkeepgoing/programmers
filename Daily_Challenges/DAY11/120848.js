// 팩토리얼
// 문제 설명
// i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
// 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
// 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

// i! ≤ n

function solution(n) {
  for (let i = 0, temp = 0; i <= n + 1; i++) {
    if (factorial(i) <= n) {
      temp = i;
      continue;
    } else {
      return temp;
    }
  }
}

function factorial(n) {
  if (n == 0 || n == 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
