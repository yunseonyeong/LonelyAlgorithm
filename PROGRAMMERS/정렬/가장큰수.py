def solution(numbers):
    nums = []
    for number in numbers:
        nums.append(str(number))

    nums.sort(key=lambda x:x*3, reverse=True)
    answer = ''
    for num in nums:
        answer+=num
        
    return str(int(answer))