import random

print("数字ガチャゲーム")
print("Enterで回す/pで終了")

# カウント用の変数
a = 0    # 超大当たり回数
b = 0    # 大当たり回数
c = 0    # リーチ回数
d = 0    # ハズレ回数

while True:
    z = input("▶ ガチャを回しますか？：")

    if z == "p":
        break

    # ガチャの数字を決定（1〜9）
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)

    print(f"結果：{num1} | {num2} | {num3}")

    # 結果判定
    if num1 == num2 == num3:
        if num1 == 7:
            print("超大当たり！")
            a += 1
        else:
            print("🎉 大当たり！！ 🎉")
            b += 1
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("リーチ！")
        c += 1
    else:
        print("ハズレ！")
        d += 1

# 最終結果
print("\n📊 ゲーム結果まとめ")
print(f"超大当たり：{a} 回")
print(f"大当たり：{b} 回")
print(f"リーチ：{c} 回")
print(f"ハズレ：{d} 回")
print("Thank you")