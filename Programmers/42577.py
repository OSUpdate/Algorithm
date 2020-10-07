def solution(phone_book):
    answer = True
    length = min([len(i) for i in phone_book])
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))