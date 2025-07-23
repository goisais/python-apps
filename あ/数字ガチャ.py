# import random

# print("数字ガチャゲーム")
# print("Enterで回す/pで終了")

# # カウント用の変数
# a = 0    # 超大当たり回数
# b = 0    # 大当たり回数
# c = 0    # リーチ回数
# d = 0    # ハズレ回数

# while True:
#     z = input("▶ ガチャを回しますか？：")

#     if z == "p":
#         break
    
#     r = random.random()

#     if r < 0.01:
#         num1 = num2 = num3 = 7
#         print(f"結果：{num1} | {num2} | {num3}")
#         print("超大当たり！")
#         a += 1

#     elif r < 0.05:
#         # 次の10%で「大当たり」＝同じ数字3つ（ただし7以外）
#         n = random.choice([1, 2, 3, 4, 5, 6, 8, 9])  # 7は除く
#         num1 = num2 = num3 = n
#         print(f"結果：{num1} | {num2} | {num3}")
#         print("大当たり！")
#         b += 1

#     elif r < 0.25:
#         # 次の20%で「リーチ」＝2つだけ同じ
#         n = random.randint(1, 9)
#         m = random.randint(1, 9)
#         while m == n:
#             m = random.randint(1, 9)  # nと違う数字にする

#         # どの2つを同じにするかランダムに決める
#         pattern = random.choice([(n, n, m), (n, m, n), (m, n, n)])
#         num1, num2, num3 = pattern
#         print(f"結果：{num1} | {num2} | {num3}")
#         print("リーチ！")
#         c += 1

#     else:
#         # 残り65%で「ハズレ」＝全部バラバラ
#         nums = random.sample(range(1, 10), 3)  # 重複なしで3つ選ぶ
#         num1, num2, num3 = nums
#         print(f"結果：{num1} | {num2} | {num3}")
#         print("ハズレ！")
#         d += 1


# # 最終結果
# print("//ゲーム結果まとめ//")
# print(f"超大当たり：{a} ")
# print(f"大当たり：{b} 回")
# print(f"リーチ：{c} 回")
# print(f"ハズレ：{d} 回")
# print("Thank you")






import random  # 発表：まずはrandomモジュールを使うことで、乱数を扱えるようにしています。

print("数字ガチャゲーム")  # 発表：このプログラムは、数字ガチャゲームです。
print("Enterで回す/pで終了")  # 発表：プレイヤーはEnterキーでガチャを回し、pで終了できます。

# 発表：当たりの種類ごとにカウントを記録するため、4つの変数を用意しました。
a = 0    # 超大当たり
b = 0    # 大当たり
c = 0    # リーチ
d = 0    # ハズレ

# 発表：では、ガチャを繰り返し回せるように、while文で無限ループを作っています。
while True:
    z = input("▶ ガチャを回しますか？：")

    # 発表：「p」が入力されたら、ループを終了し、結果表示に進みます。
    if z == "p":
        break

    # 発表：random.random()で0〜1未満の乱数を作ります。
    # 発表：この値によって結果を振り分けることで、全体の確率をコントロールしています。
    r = random.random()

    # 発表：まずrが0.01未満、つまり1%の確率で「超大当たり」です。
    if r < 0.01:
        num1 = num2 = num3 = 7  # 発表：全部7に揃えて特別感を出しました。
        print(f"結果：{num1} | {num2} | {num3}")
        print("🎉 超大当たり！ 🎉")
        a += 1

    # 発表：次にrが0.05未満（つまり4%）なら「大当たり」です。
    elif r < 0.05:
        # 発表：7は超大当たり専用にして除外しました。他の数字をランダムに選びます。
        n = random.choice([1, 2, 3, 4, 5, 6, 8, 9])
        num1 = num2 = num3 = n  # 発表：同じ数字3つにして当たり感を演出しました。
        print(f"結果：{num1} | {num2} | {num3}")
        print("🎯 大当たり！")
        b += 1

    # 発表：rが0.25未満（つまり20%）のときは「リーチ」です。
    elif r < 0.25:
        # 発表：同じ数字2つと、違う数字1つを組み合わせます。
        n = random.randint(1, 9)
        m = random.randint(1, 9)
        while m == n:
            m = random.randint(1, 9)  # 発表：mがnと同じにならないように再抽選します。

        # 発表：どの位置に同じ数字を置くかもランダムで決めて、パターンに変化を持たせています。
        pattern = random.choice([(n, n, m), (n, m, n), (m, n, n)])
        num1, num2, num3 = pattern
        print(f"結果：{num1} | {num2} | {num3}")
        print("📶 リーチ！")
        c += 1

    # 発表：それ以外の確率（約75%）ではハズレになります。
    else:
        # 発表：重複しない3つの数字を選ぶために、random.sampleを使っています。
        nums = random.sample(range(1, 10), 3)
        num1, num2, num3 = nums
        print(f"結果：{num1} | {num2} | {num3}")
        print("💨 ハズレ...")
        d += 1

# 発表：ゲームが終了したら、各結果の回数を表示してまとめています。
print("//ゲーム結果まとめ//")
print(f"超大当たり：{a} 回")
print(f"大当たり ：{b} 回")
print(f"リーチ  ：{c} 回")
print(f"ハズレ  ：{d} 回")
print("🎊 Thank you for playing 🎊")

# 発表：このゲームでは、乱数の値で確率をコントロールする方法を学びながら、
# 発表：当たりパターンの演出や工夫も取り入れて、楽しく動くアプリを作りました。
