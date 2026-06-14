def solution(s):
    answer = ''
    hi = []
    for i in s:
        if s.count(i) == 1:
            hi.append(i)
    hi = sorted(hi)
    answer = "".join(hi)
    return answer