def solution(babbling):
    answer = 0
    for word in babbling:
        for sound in ["aya", "ye", "woo", "ma"]:
            word = word.replace(sound, " ", 1)  # 최대 1번만 교체
        if word.strip() == "":  # 남는 글자가 없으면
            answer += 1
    return answer