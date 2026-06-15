# [level 0] 영어가 싫어요 - 120894 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120894) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 06월 16일 00:00:00

### 문제 설명

<p>매개변수 <code>numbers</code>는 영어로 표현된 숫자가 공백 없이 이어 붙여진 문자열입니다. <code>numbers</code>를 정수로 변환해 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 50</li>
<li><code>numbers</code>는 소문자로만 이루어져 있습니다.</li>
<li><code>numbers</code>는 zero, one, two, three, four, five, six, seven, eight, nine 중 하나 이상을 이어 붙여서 만들어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"onetwothree"</td>
<td>123</td>
</tr>
<tr>
<td>"onefourzero"</td>
<td>140</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>onetwothree는 one, two, three로 이루어져 있으므로 1, 2, 3으로 변환해 이어 붙이면 123을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>onefourzero는 one, four, zero로 이루어져 있으므로 1, 4, 0으로 변환해 이어 붙이면 140을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges