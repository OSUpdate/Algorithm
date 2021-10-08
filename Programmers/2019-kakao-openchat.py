record = [
    "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
    "Enter uid1234 Prodo", "Change uid4567 Ryan"
]
table = {}
tmp = []
res = []
for data in record:
    if data.startswith("Enter"):
        command, uid, nick = data.split()
        table[uid] = nick
        tmp.append((f"{uid}", "님이 들어왔습니다."))
    elif data.startswith("Leave"):
        command, uid = data.split()
        tmp.append((f"{uid}", "님이 나갔습니다."))
    elif data.startswith("Change"):
        command, uid, nick = data.split()
        table[uid] = nick
for uid, text in tmp:
    res.append(f"{table[uid]}{text}")

print(res)
