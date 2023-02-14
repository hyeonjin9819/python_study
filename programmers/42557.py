def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book) - 1):
        # 지금 데이터랑 다음 차례 접두사가 같을때
        print(phone_book[i], phone_book[i + 1][:len(phone_book[i])])
        if (phone_book[i] == phone_book[i + 1][:len(phone_book[i])]):
            answer = False
            return answer

    answer = True
    return answer