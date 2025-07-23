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
    
    r = random.random()

    if r < 0.01:
        num1 = num2 = num3 = 7
        print(f"結果：{num1} | {num2} | {num3}")
        print("超大当たり！")
        a += 1

    elif r < 0.05:
        # 次の10%で「大当たり」＝同じ数字3つ（ただし7以外）
        n = random.choice([1, 2, 3, 4, 5, 6, 8, 9])  # 7は除く
        num1 = num2 = num3 = n
        print(f"結果：{num1} | {num2} | {num3}")
        print("大当たり！")
        b += 1

    elif r < 0.25:
        # 次の20%で「リーチ」＝2つだけ同じ
        n = random.randint(1, 9)
        m = random.randint(1, 9)
        while m == n:
            m = random.randint(1, 9)  # nと違う数字にする

        # どの2つを同じにするかランダムに決める
        pattern = random.choice([(n, n, m), (n, m, n), (m, n, n)])
        num1, num2, num3 = pattern
        print(f"結果：{num1} | {num2} | {num3}")
        print("リーチ！")
        c += 1

    else:
        # 残り65%で「ハズレ」＝全部バラバラ
        nums = random.sample(range(1, 10), 3)  # 重複なしで3つ選ぶ
        num1, num2, num3 = nums
        print(f"結果：{num1} | {num2} | {num3}")
        print("ハズレ！")
        d += 1


# 最終結果
print("//ゲーム結果まとめ//")
print(f"超大当たり：{a} ")
print(f"大当たり：{b} 回")
print(f"リーチ：{c} 回")
print(f"ハズレ：{d} 回")
print("Thank you")