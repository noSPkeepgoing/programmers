// 다항식 더하기
// 문제 설명
// 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
// 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
// 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

function solution(polynomial) {
  const answer = [];
  [x, c] = [0, 0];
  for (i of polynomial.split(' + ')) {
    if (i.includes('x')) {
      x += i.replace('x', '') ? Number(i.replace('x', '')) : 1;
    } else {
      c += Number(i);
    }
  }
  if (x != 0) {
    xnum = x == 1 ? 'x' : x + 'x';
    answer.push(xnum);
  }
  if (c != 0) {
    answer.push(c);
  }
  return answer.join(' + ');
}
