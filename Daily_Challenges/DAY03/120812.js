// 최빈값 구하기
// 문제 설명
// 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
// 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

function solution(array) {
  set = new Set(array);
  setArray = Array.from(set);
  countArray = [];
  for (let i = 0; i < setArray.length; i++) {
    let cnt = 0;
    array.map((num) => {
      if (num == setArray[i]) cnt++;
    });
    countArray.push(cnt);
  }

  findIdx = (i) => i == Math.max(...countArray);
  filterCountArray = countArray.filter((i) => i == Math.max(...countArray));

  idx = countArray.findIndex(findIdx);
  answer = filterCountArray.length == 1 ? setArray[idx] : -1;

  return answer;
}
