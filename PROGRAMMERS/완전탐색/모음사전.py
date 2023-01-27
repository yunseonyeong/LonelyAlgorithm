def solution(word):
    word_obj = {
        "A": 0,
        "E": 1,
        "I": 2,
        "O": 3,
        "U": 4
    }
    cnt = [1,6,31,156,781]
    answer = len(word)
    for i,w in enumerate(word):
        answer += word_obj[w] * cnt[4-i]
    

    return answer


