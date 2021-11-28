def solution(numbers,target):
    answer = 0
    def dfs(numbers,target,cur_idx,cur_sum):
        nonlocal answer
        
        if cur_idx == len(numbers):
            if cur_sum == target :
                answer +=1
        else:
            dfs(numbers, target, cur_idx+1, cur_sum+numbers[cur_idx])
            dfs(numbers, target, cur_idx+1, cur_sum-numbers[cur_idx])
        return answer
    
    dfs(numbers,target,0,0)
    return answer