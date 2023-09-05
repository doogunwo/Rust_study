def solution(name, yearning, photo):
    # name = 사람 명단
    # yearning = 그리움 수치
    # photo = 사진 2차원 배열
    answer = []
    dict2 = dict(zip(name,yearning))
    for i in photo:
        sum = 0
        for j in i:
            if j  in name:
                sum = sum +dict2[j]
            else:
                pass

        answer.append(sum) 

    print(answer)

    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

solution(name,yearning,photo)