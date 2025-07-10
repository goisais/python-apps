# import random
# rn=random.randint(1,100)
rn = 77

# il = input("1~100の数字を当ててください：")
for i in range(5):
    li = input(f"{i+1}回目")

    if not li.isdigit():
        print("数字を入力してください")
        continue

    a = int(li)
    if a == rn:
        print("せーかい")
        break
    elif a < rn:
        print("もっと大きい")
    else:
        print("もっと小さい")
else:
    print("ふせーかい、せーかいは", rn, "です")


