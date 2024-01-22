def solution(land):
    maxDP = land[0]
    
    for l in land[1:]:
        maxDP = [l[0] + max(maxDP[1:]), l[1] + max(maxDP[0], maxDP[2], maxDP[3]), l[2] + max(maxDP[0], maxDP[1], maxDP[3]), l[3] + max(maxDP[:-1])]

    return max(maxDP)