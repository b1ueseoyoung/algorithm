def solution(order):
    # 숫자를 문자열로 변환합니다. (예: 29423 -> "29423")
    order_str = str(order)
    
    # '3', '6', '9'의 개수를 각각 세어서 모두 더한 값을 반환합니다.
    return order_str.count('3') + order_str.count('6') + order_str.count('9')