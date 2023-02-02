def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            binary = bin(number)[2:]
            binary = "0" + binary
            r = binary.rfind("0")
            binary = list(binary)
            binary[r] = "1"
            binary[r+1] = "0"
            answer.append(int("".join(binary),2))    
            
    return answer