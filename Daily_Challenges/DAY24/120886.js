// A로 B 만들기
// 문제 설명
// 문자열 before와 after가 매개변수로 주어질 때,
// before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

function solution(before, after) {
  const arr_a = [...after];
  const arr_b = [...before].filter((e) => {
    if (arr_a.includes(e)) {
      arr_a.splice(arr_a.indexOf(e), 1);
      return false;
    }
    return true;
  });
  return arr_b.length ? 0 : 1;
}
