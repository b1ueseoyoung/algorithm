def solution(my_string):
    tokens = my_string.split()
    
    answer = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        next_num = int(tokens[i+1])
        
        if operator == '+':
            answer += next_num
        elif operator == '-':
            answer -= next_num
            
    return answer