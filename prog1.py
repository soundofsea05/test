import random

def number_guessing_game():
    #ランダムに正解の数字を決定（3桁：100〜999）
    secret_number = random.randint(100, 999)
    
    #回答回数の制限（ここでは7回に設定）
    max_attempts = 7
    
    print("【3桁の数当てゲーム】")
    print(f"100から999までの数字を当てよう．チャンスは{max_attempts}回．\n")
    
    
                
    #回数制限に達した場合の処理
    print("ゲームオーバーだ．制限回数を超えた．")
    print(f"正解は {secret_number} だった．")

if __name__ == "__main__":
    number_guessing_game()