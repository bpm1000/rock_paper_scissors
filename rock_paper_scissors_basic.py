import random

print("じゃんけんゲームへようこそ!")

hands = ["グー", "チョキ", "パー"]

# コンピューターの手をランダムに選ぶ
computer_hand = random.choice(hands)

# ユーザーの手を選択
user_input = (
    int(input("1:グー 2:チョキ 3:パー の中から選んでください: ")) - 1
)  # 入力から1引いてリストのインデックスに合わせる

# ユーザーの手をリストから取得
user_hand = hands[user_input]

# コンピューターとユーザーの手を表示
print(f"コンピュータの手: {computer_hand}")
print(f"あなたの手: {user_hand}")

# 勝敗の判定
if user_hand == computer_hand:
    print("引き分けです!")
elif user_hand == "グー" and computer_hand == "チョキ":
    print("あなたの勝ち!")
elif user_hand == "チョキ" and computer_hand == "パー":
    print("あなたの勝ち!")
elif user_hand == "パー" and computer_hand == "グー":
    print("あなたの勝ち!")
else:
    print("コンピューターの勝ち!")
