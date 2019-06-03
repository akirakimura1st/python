age = int(input("年齢を入力してください"))
while age > 120:
    age = int(input("エラーです、年齢を入力してください"))

print("あなたは" + str(age) + "歳です")