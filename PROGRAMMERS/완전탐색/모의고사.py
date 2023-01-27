def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    result = []

    for i,answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            cnt1 += 1
        if answer == pattern2[i % len(pattern2)]:
            cnt2 += 1
        if answer == pattern3[i % len(pattern3)]:
            cnt3 += 1

    if max(cnt1, cnt2, cnt3) == cnt1:
        result.append(1)
    if max(cnt1, cnt2, cnt3) == cnt2:
        result.append(2)
    if max(cnt1, cnt2, cnt3) == cnt3:
        result.append(3)

    return result