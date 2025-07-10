

# import random

# # rom colorama import init, Fore, Style
# # init(autoreset=True)  # 色を自動でリセット


# goal = 30
# turn = 1


# # プレイヤーの初期状態（辞書で管理）
# players = {
#     "P1": {"name": "プレイヤー1", "pos": 0, "money": 1000, "job": "無職"},
#     "P2": {"name": "プレイヤー2", "pos": 0, "money": 1000, "job": "無職"},
# }



# # イベント設定（あなたのオリジナルイベント）
# events = {
#     0: {"type": "money", "amount": 1000, "desc": "スタート地点！所持金1000円"},
#     1: {"type": "money", "amount": 200, "desc": "お小遣いをもらった！"},
#     2: {"type": "money", "amount": -100, "desc": "お菓子を買いすぎた..."},
#     3: {"type": "money", "amount": -200, "desc": "飲みすぎてしまった..."},
#     4: {"type": "job", "job": "営業", "salary": 1500, "desc": "営業の仕事に就いた！初給料1500円ゲット！"},
#     5: {"type": "money", "amount": 500, "desc": "宝くじが当たった！"},
#     6: {"type": "money", "amount": -300, "desc": "友達におごった..."},
#     7: {"type": "money", "amount": -500, "desc": "友達にお金を貸した..."},
#     8: {"type": "job", "job": "教師", "salary": 1800, "desc": "教師の仕事に転職！初給料1800円ゲット！"},
#     9: {"type": "money", "amount": -400, "desc": "急な出費があった..."},
#     10: {"type": "money", "amount": -300, "desc": "詐欺にあった..."},
#     11: {"type": "money", "amount": 800, "desc": "臨時収入があった！"},
#     12: {"type": "money", "amount": 2000, "desc": "株で大儲け！"},
#     13: {"type": "money", "amount": -1000, "desc": "大きな買い物をしてしまった..."},
#     14: {"type": "money", "amount": -600, "desc": "旅行に行ってしまった..."},
#     15: {"type": "job", "job": "エンジニア", "salary": 2000, "desc": "エンジニアの仕事に就いた！"},
#     16: {"type": "money", "amount": 1500, "desc": "ボーナスが出た！"},
#     17: {"type": "money", "amount": -800, "desc": "車の修理代がかかった..."},
#     18: {"type": "money", "amount": 1200, "desc": "副業で収入があった！"},
#     19: {"type": "money", "amount": -700, "desc": "急な医療費がかかった..."},
#     20: {"type": "money", "amount": -1000, "desc": "大きな買い物をしてしまった..."},
#     21: {"type": "money", "amount": 3000, "desc": "遺産相続で大金ゲット！"},
#     22: {"type": "money", "amount": -500, "desc": "友達におごった..."},
#     23: {"type": "money", "amount": 1000, "desc": "宝くじが当たった！"},
#     24: {"type": "money", "amount": -2000, "desc": "大きな買い物をしてしまった..."},
#     25: {"type": "job", "job": "デザイナー", "salary": 2500, "desc": "デザイナーの仕事に転職！"},
#     26: {"type": "money", "amount": 500, "desc": "副業で収入があった！"},
#     27: {"type": "money", "amount": -1500, "desc": "急な出費があった..."},
#     28: {"type": "money", "amount": 2000, "desc": "株で大儲け！"},
#     29: {"type": "money", "amount": -1200, "desc": "大きな買い物をしてしまった..."},
# }

# # print("=== 2人プレイ 人生スゴロクゲーム 開始！ ===")

# # winner = None

# # turn = 1  # ターンカウントを追加
# # # プレイヤーの初期状態を表示
# # for pid, player in players.items():
# #     print(f"{player['name']} の初期状態: 所持金 {player['money']}円, 仕事: {player['job']}, 現在地: {player['pos']}マス目")

# players = {}
# num_players = int(input("何人でプレイしますか？（2以上の数字）: "))
# for i in range(num_players):
#     name = input(f"{i+1}人目の名前を入力してください: ")
#     pid = f"P{i+1}"
#     players[pid] = {"name": name, "pos": 0, "money": 1000, "job": "無職"}

# print("\n=== 人生スゴロクゲーム 開始！ ===")
# for player in players.values():
#     print(f"{player['name']} の初期状態: 所持金 {player['money']}円, 仕事: {player['job']}")

# winner = None
# turn = 1

# # ゲームループ
# while not winner:
#     for pid in ["P1", "P2"]:
#         player = players[pid]

#         input(f"\n{player['name']} の番です。Enterでサイコロを振る...")
#         dice = random.randint(1, 6)
#         print(f"サイコロの目は {dice} です！")

#         player["pos"] += dice
#         if player["pos"] > goal:
#             player["pos"] = goal

#         print(f"{player['name']} は {player['pos']}マス目です（{player['pos']} / {goal}）")

#         # ゴールチェック
#         if player["pos"] >= goal:
#             print(f"\n🎉 {player['name']} がゴールしました！")
#             winner = player
#             break

#         # イベントチェック
#         if player["pos"] in events:
#             ev = events[player["pos"]]
#             if ev["type"] == "money":
#                 player["money"] += ev["amount"]
#                 print(f"イベント発生：{ev['desc']} お金が{ev['amount']}円 {'増えた' if ev['amount'] > 0 else '減った'}！")
#             elif ev["type"] == "job":
#                 player["job"] = ev["job"]
#                 player["money"] += ev["salary"]
#                 print(f"イベント発生：{ev['desc']} 初給料{ev['salary']}円ゲット！")

#         print(f"現在の所持金: {player['money']}円, 仕事: {player['job']}")

#         # 勝っているプレイヤーの表示（所持金ベース）
#         p1_money = players["P1"]["money"]
#         p2_money = players["P2"]["money"]

#         if p1_money > p2_money:
#             diff = p1_money - p2_money
#             print(f"💰 現在は {players['P1']['name']} がリード！（+{diff}円）")
#         elif p2_money > p1_money:
#             diff = p2_money - p1_money
#             print(f"💰 現在は {players['P2']['name']} がリード！（+{diff}円）")
#         else:
#             print("🤝 現在は引き分けです！")
#         print(f"{player['name']} の現在地: {player['pos']}マス, 所持金: {player['money']}円, 職業: {player['job']}")     

# # ゲーム終了表示
# print("\n=== ゲーム終了 ===")
# print(f"🏆 勝者: {winner['name']}")
# print(f"最終所持金: {winner['money']}円, 職業: {winner['job']}")
# # 敗者を表示
# loser = players["P1"] if winner["name"] != players["P1"]["name"] else players["P2"]
# print(f"💸 敗者: {loser['name']}")
# print(f"最終所持金: {loser['money']}円, 職業: {loser['job']}")
# # 勝者と敗者の所持金差を表示
# money_diff = abs(winner["money"] - loser["money"])


# import random

# # ------------------ ゲーム設定 ------------------
# goal = 30
# job_scores = {
#     "無職": 0,
#     "営業": 1500,
#     "教師": 1800,
#     "エンジニア": 2000,
#     "デザイナー": 2500,
#     "医者": 3000,
#     "アーティスト": 1700,
#     "ゲームクリエイター": 2600
# }

# items = {
#     "ラッキーチャーム": {"price": 500, "effect": "next_bonus", "desc": "次のターン、お金が+500円！"},
#     "ドリームカード": {"price": 1000, "effect": "change_job", "desc": "職業がランダムで変更！"}
# }

# bonus_table = [3000, 2000, 1000]  # ゴール順位ごとのボーナス

# # ------------------ イベント定義 ------------------
# shop_items = list(items.keys())
# events = {
#     0: {"type": "money", "amount": 1000, "desc": "スタート地点！所持金1000円"},
#     1: {"type": "money", "amount": 200, "desc": "お小遣いをもらった！"},
#     2: {"type": "money", "amount": -100, "desc": "お菓子を買いすぎた..."},
#     3: {"type": "money", "amount": -200, "desc": "飲みすぎてしまった..."},
#     4: {"type": "job", "job": "営業", "salary": 1500, "desc": "営業に就職！"},
#     5: {"type": "money", "amount": 500, "desc": "宝くじが当たった！"},
#     6: {"type": "money", "amount": -300, "desc": "友達におごった..."},
#     7: {"type": "money", "amount": -500, "desc": "友達にお金を貸した..."},
#     8: {"type": "job", "job": "教師", "salary": 1800, "desc": "教師に転職！"},
#     9: {"type": "money", "amount": -400, "desc": "急な出費があった..."},
#     10: {"type": "money", "amount": -300, "desc": "詐欺にあった..."},
#     11: {"type": "money", "amount": 800, "desc": "臨時収入があった！"},
#     12: {"type": "shop", "desc": "アイテムショップへようこそ！"},
#     13: {"type": "money", "amount": -1000, "desc": "大きな買い物をしてしまった..."},    
#     14: {"type": "money", "amount": -600, "desc": "旅行に行ってしまった..."},   
#     15: {"type": "job", "job": "エンジニア", "salary": 2000, "desc": "エンジニアに転職！"},
#     16: {"type": "money", "amount": 1500, "desc": "ボーナスが出た！"},
#     17: {"type": "money", "amount": -800, "desc": "車の修理代がかかった..."},
#     18: {"type": "mini_game", "desc": "ミニゲームに挑戦！"},
#     19: {"type": "money", "amount": -700, "desc": "急な医療費がかかった..."},
#     20: {"type": "job", "job": "医者", "salary": 3000, "desc": "医者に転職！"},
#     21: {"type": "money", "amount": 3000, "desc": "遺産相続で大金ゲット！"},
#     22: {"type": "money", "amount": -500, "desc": "友達におごった..."},
#     23: {"type": "money", "amount": 1000, "desc": "宝くじが当たった！"},
#     24: {"type": "money", "amount": -2000, "desc": "大きな買い物をしてしまった..."},
#     25: {"type": "job", "job": "デザイナー", "salary": 2500, "desc": "デザイナーに転職！"},
#     26: {"type": "money", "amount": 500, "desc": "副業で収入があった！"},
#     27: {"type": "money", "amount": -1500, "desc": "急な出費があった..."},
#     28: {"type": "money", "amount": 2000, "desc": "株で大儲け！"},
#     29: {"type": "money", "amount": -1200, "desc": "大きな買い物をしてしまった..."},
#     30: {"type": "money", "amount": 0, "desc": "ゴール！お疲れ様でした！"}
# }

# # ------------------ ミニゲーム定義 ------------------
# def mini_game():
#     print("🎯 ミニゲーム：1〜5の数字を当てよう！")
#     ans = random.randint(1, 5)
#     guess = int(input("あなたの予想は？: "))
#     if guess == ans:
#         print("🎉 正解！ボーナス1000円！")
#         return 1000
#     else:
#         print(f"残念！正解は {ans} でした。")
#         return 0

# # ------------------ プレイヤー登録 ------------------
# players = {}
# num_players = int(input("何人でプレイしますか？（2人以上）: "))
# for i in range(num_players):
#     name = input(f"{i+1}人目の名前を入力してください: ")
#     pid = f"P{i+1}"
#     players[pid] = {
#         "name": name, "pos": 0, "money": 1000, "job": "無職",
#         "inventory": [], "history": [], "bonus": 0, "final_score": 0,
#         "next_bonus": False
#     }

# # ------------------ ゲームスタート ------------------
# goal_order = []
# print("\n=== 人生スゴロクゲーム 開始！ ===")
# turn = 1

# while len(goal_order) < num_players:
#     print(f"\n========== ターン {turn} ==========")
#     for pid, p in players.items():
#         if pid in goal_order:
#             continue

#         input(f"\n🎲 {p['name']} の番です。Enterでサイコロを振る...")
#         dice = random.randint(1, 6)
#         print(f"→ サイコロの目: {dice}")

#         p['pos'] += dice
#         if p['pos'] > goal:
#             p['pos'] = goal

#         print(f"→ {p['name']} は {p['pos']} マス目に到着！")

#         # ラッキーチャーム効果
#         if p.get("next_bonus"):
#             print("💸 ラッキーチャーム効果発動！ +500円！")
#             p['money'] += 500
#             p['next_bonus'] = False

#         # イベント処理
#         if p['pos'] in events:
#             ev = events[p['pos']]
#             print(f"🌀 イベント: {ev['desc']}")
#             if ev["type"] == "money":
#                 p['money'] += ev['amount']
#                 p['history'].append(f"{turn}ターン目: {ev['desc']} お金{ev['amount']}円")
#             elif ev["type"] == "job":
#                 p['job'] = ev['job']
#                 p['money'] += ev['salary']
#                 p['history'].append(f"{turn}ターン目: {ev['desc']} 初給料{ev['salary']}円")
#             elif ev["type"] == "shop":
#                 for idx, item in enumerate(shop_items):
#                     print(f"{idx+1}. {item} - {items[item]['price']}円 : {items[item]['desc']}")
#                 choice = input("購入したい番号（スキップはEnter）: ")
#                 if choice.isdigit():
#                     item = shop_items[int(choice)-1]
#                     if p['money'] >= items[item]['price']:
#                         p['money'] -= items[item]['price']
#                         p['inventory'].append(item)
#                         p['history'].append(f"{turn}ターン目: {item} を購入")
#                         print(f"✅ {item} を購入しました！")
#                     else:
#                         print("❌ お金が足りません。")
#             elif ev["type"] == "mini_game":
#                 reward = mini_game()
#                 p['money'] += reward
#                 p['history'].append(f"{turn}ターン目: ミニゲーム報酬 +{reward}円")

#         # アイテム効果発動（1回限り）
#         for item in p['inventory']:
#             if items[item]['effect'] == "next_bonus":
#                 p['next_bonus'] = True
#             elif items[item]['effect'] == "change_job":
#                 new_job = random.choice(list(job_scores.keys()))
#                 p['job'] = new_job
#                 p['history'].append(f"{turn}ターン目: {item}で職業が {new_job} に変更")

#         # 現在の状態表示
#         print(f"\n📌 {p['name']} の状態")
#         print(f"・現在地: {p['pos']} / {goal}マス")
#         print(f"・所持金: {p['money']}円")
#         print(f"・職業: {p['job']}")
#         print(f"・アイテム: {p['inventory']}")

#         if p['pos'] >= goal:
#             goal_order.append(pid)
#             print(f"🎉 ゴール！順位: {len(goal_order)}位\n")

#     turn += 1

# # ------------------ 結果発表 ------------------
# print("\n=== 🎊 最終結果発表 🎊 ===")
# for i, pid in enumerate(goal_order):
#     bonus = bonus_table[i] if i < len(bonus_table) else 500
#     p = players[pid]
#     p['bonus'] = bonus
#     p['final_score'] = p['money'] + job_scores.get(p['job'], 0) + bonus

# # スコア順にソート
# ranked = sorted(players.values(), key=lambda p: p['final_score'], reverse=True)
# for idx, p in enumerate(ranked):
#     print(f"\n🏅 第{idx+1}位: {p['name']}")
#     print(f"・所持金: {p['money']}円")
#     print(f"・職業: {p['job']}（価値: {job_scores.get(p['job'], 0)}円）")
#     print(f"・ゴールボーナス: {p['bonus']}円")
#     print(f"・最終スコア: {p['final_score']}円")
#     print("・イベント履歴:")
#     for h in p['history']:
#         print(f"  - {h}")

# print(f"\n🏆 優勝者: {ranked[0]['name']}（スコア: {ranked[0]['final_score']}円）")
# print(f"🥈 準優勝者: {ranked[1]['name']}（スコア: {ranked[1]['final_score']}円）")




import random

# ------------------ ゲーム設定 ------------------
goal = 30
job_scores = {
    "無職": 0,
    "営業": 65358,
    "教師": 48738,
    "エンジニア": 53756,
    "デザイナー": 33567,
    "医者": 67357,
    "アーティスト": 27667,
    "ゲームクリエイター": 27635,
}

items = {
    "ラッキーチャーム": {
        "price": 50000,
        "effect": "next_bonus",
        "desc": "次のターン、お金が+50000円！"
    },
    "ドリームカード": {"price": 100000, "effect": "change_job", "desc": "職業がランダムで変更！"}
}

bonus_table = [36847, 38677, 40754]  # ゴール順位ごとのボーナス

# ------------------ イベント定義 ------------------
shop_items = list(items.keys())
events = {
    1: {"type": "money", "amount": 72814, "desc": "お小遣いをもらった！"},
    2: {"type": "money", "amount": -9634, "desc": "お菓子を買いすぎた..."},
    3: {"type": "money", "amount": -10843, "desc": "飲みすぎてしまった..."},
    4: {"type": "job", "job": "営業", "salary": 65358, "desc": "営業に就職！"},
    5: {"type": "money", "amount": 146452, "desc": "宝くじが当たった！"},
    6: {"type": "money", "amount": -96750, "desc": "友達におごった..."},
    7: {"type": "money", "amount": -100000, "desc": "友達にお金を貸した..."},
    8: {"type": "job", "job": "教師", "salary": 48738, "desc": "教師に転職！"},
    9: {"type": "money", "amount": -56865, "desc": "急な出費があった..."},
    10: {"type": "money", "amount": -99999, "desc": "詐欺にあった..."},
    11: {"type": "money", "amount": 190868, "desc": "臨時収入があった！"},
    12: {"type": "shop", "desc": "アイテムショップへようこそ！"},
    13: {"type": "money", "amount": -54555, "desc": "大きな買い物をしてしまった..."},
    14: {"type": "money", "amount": -9876, "desc": "旅行に行ってしまった..."},
    15: {"type": "job", "job": "エンジニア", "salary": 53756, "desc": "エンジニアに転職！"},
    16: {"type": "money", "amount": 157659, "desc": "ボーナスが出た！"},
    17: {"type": "money", "amount": -10987, "desc": "車の修理代がかかった..."},
    18: {"type": "mini_game", "desc": "ミニゲームに挑戦！"},
    19: {"type": "money", "amount": -9999, "desc": "急な医療費がかかった..."},
    20: {"type": "job", "job": "医者", "salary": 67357, "desc": "医者に転職！"},
    21: {"type": "money", "amount": 215675, "desc": "遺産相続で大金ゲット！"},
    22: {"type": "money", "amount": -35686, "desc": "友達におごった..."},
    23: {"type": "money", "amount": 100000, "desc": "宝くじが当たった！"},
    24: {"type": "money", "amount": -56756, "desc": "大きな買い物をしてしまった..."},
    25: {"type": "job", "job": "デザイナー", "salary": 33567, "desc": "デザイナーに転職！"},
    26: {"type": "money", "amount": 75312, "desc": "副業で収入があった！"},
    27: {"type": "money", "amount": -86743, "desc": "急な出費があった..."},
    28: {"type": "money", "amount": 97514, "desc": "株で大儲け！"},
    29: {"type": "money", "amount": -57641, "desc": "大きな買い物をしてしまった..."},
    30: {"type": "money", "amount": 777, "desc": "ゴール！お疲れ様でした！"}
}

# ------------------ ミニゲーム定義 ------------------


def mini_game():
    print("🎯 ミニゲーム：1〜5の数字を当てよう！")
    ans = random.randint(1, 5)
    guess = int(input("あなたの予想は？: "))
    if guess == ans:
        print("🎉 正解！ボーナス675380円！")
        return 675380
    else:
        print(f"残念！正解は {ans} でした。")
        return 0


# ------------------ プレイヤー登録 ------------------
players = {}
num_players = int(input("何人でプレイしますか？（2人以上）: "))
for i in range(num_players):
    name = input(f"{i+1}人目の名前を入力してください: ")
    pid = f"P{i+1}"
    players[pid] = {
        "name": name, "pos": 0, "money": 10000, "job": "無職",
        "inventory": [], "history": [], "bonus": 0, "final_score": 0,
        "next_bonus": False
    }

# ------------------ ゲームスタート ------------------
goal_order = []
print("\n=== 人生スゴロクゲーム 開始！ ===")
turn = 1

while len(goal_order) < num_players:
    print(f"\n========== ターン {turn} ==========")
    for pid, p in players.items():
        if pid in goal_order:
            continue

        input(f"\n🎲 {p['name']} の番です。Enterでサイコロを振る...")
        dice = random.randint(1, 6)
        print(f"→ サイコロの目: {dice}")

        p['pos'] += dice
        if p['pos'] > goal:
            p['pos'] = goal

        print(f"→ {p['name']} は {p['pos']} マス目に到着！")

        # ラッキーチャーム効果：所持金が0〜3倍に変動
        if p.get("next_bonus"):
            multiplier = random.randint(0, 3)
            original_money = p['money']
            p['money'] = original_money * multiplier

            if multiplier == 0:
                print(f"💸 ラッキーチャームの効果で全財産が消滅…（{original_money}円 → 0円）")
            else:
                print(
                    f"💸 ラッキーチャーム効果！所持金が{multiplier}倍に！"
                    f"（{original_money}円 → {p['money']}円）"
                )
                p['next_bonus'] = False

        # イベント処理
        if p['pos'] in events:
            ev = events[p['pos']]
            if ev["type"] == "money":
                amount = ev['amount']
                icon = "✅" if amount >= 0 else "❌"
                sign = "+" if amount >= 0 else "-"
                p['money'] += amount
                print(f"{icon} お金{sign}{abs(amount)}円")
                p['history'].append(
                    f"{turn}ターン目: {ev['desc']} お金{sign}{abs(amount)}円"
                )
            elif ev["type"] == "job":
                p['job'] = ev['job']
                p['money'] += ev['salary']
                print(f"👔 {ev['desc']} 初給料 +{ev['salary']}円")
                p['history'].append(
                    f"{turn}ターン目: {ev['desc']} 初給料 +{ev['salary']}円"
                )
            elif ev["type"] == "mini_game":
                reward = mini_game()
                sign = "+" if reward >= 0 else "-"
                icon = "✅" if reward > 0 else "❌"
                p['money'] += reward
                print(f"{icon} ミニゲーム報酬 {sign}{abs(reward)}円")
                p['history'].append(
                    f"{turn}ターン目: ミニゲーム報酬 {sign}{abs(reward)}円"
                )
            elif ev["type"] == "shop":
                for idx, item in enumerate(shop_items):
                    print(
                        f"{idx+1}. {item} - {items[item]['price']}円 : "
                        f"{items[item]['desc']}"
                    )
                choice = input("購入したい番号（スキップはEnter）: ")
                if choice.isdigit():
                    item = shop_items[int(choice)-1]
                    if p['money'] >= items[item]['price']:
                        p['money'] -= items[item]['price']
                        p['inventory'].append(item)
                        p['history'].append(f"{turn}ターン目: {item} を購入")
                        print(f"✅ {item} を購入しました！")
                    else:
                        print("❌ お金が足りません。")

        # アイテム効果発動
        for item in p['inventory']:
            if items[item]['effect'] == "next_bonus":
                p['next_bonus'] = True
            elif items[item]['effect'] == "change_job":
                new_job = random.choice(list(job_scores.keys()))
                p['job'] = new_job
                p['history'].append(f"{turn}ターン目: {item}で職業が {new_job} に変更")

        # 現在の状態表示
        print(f"\n📌 {p['name']} の状態")
        print(f"・現在地: {p['pos']} / {goal}マス")
        print(f"・所持金: {p['money']}円")
        print(f"・職業: {p['job']}")
        print(f"・アイテム: {p['inventory']}")

        if p['pos'] >= goal:
            goal_order.append(pid)
            print(f"🎉 ゴール！順位: {len(goal_order)}位\n")

    turn += 1

# ------------------ 結果発表 ------------------
print("\n=== 🎊 最終結果発表 🎊 ===")
for i, pid in enumerate(goal_order):
    bonus = bonus_table[i] if i < len(bonus_table) else 500
    p = players[pid]
    p['bonus'] = bonus
    p['final_score'] = p['money'] + job_scores.get(p['job'], 0) + bonus

ranked = sorted(players.values(), key=lambda p: p['final_score'], reverse=True)
for idx, p in enumerate(ranked):
    print(f"\n🏅 第{idx+1}位: {p['name']}")
    print(f"・所持金: {p['money']}円")
    print(f"・職業: {p['job']}（価値: {job_scores.get(p['job'], 0)}円）")
    print(f"・ゴールボーナス: {p['bonus']}円")
    print(f"・最終スコア: {p['final_score']}円")
    print("・イベント履歴:")
    for h in p['history']:
        print(f"  - {h}")

print(f"\n🏆 優勝者: {ranked[0]['name']}（スコア: {ranked[0]['final_score']}円）")
if len(ranked) > 1:
    print(f"🥈 準優勝者: {ranked[1]['name']}（スコア: {ranked[1]['final_score']}円）")
