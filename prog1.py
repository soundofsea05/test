import random

def number_guessing_game():
    #ランダムに正解の数字を決定（3桁：100〜999）
    secret_number = random.randint(100, 999)
    
    #回答回数の制限
    max_attempts = 7
    
    print("【3桁の数当てゲーム】")
    print(f"100から999までの数字を当てよう．チャンスは{max_attempts}回．\n")
    
    for attempt in range(1, max_attempts + 1):
        #キーボード入力で回答を受け取る
        guess_input = input(f"[{attempt}/{max_attempts}回目] 3桁の数字を入力: ")
        
        #入力された値が本当に3桁の数字かチェック
        if not guess_input.isdigit() or len(guess_input) != 3:
            print("無効な入力だ．3桁の数字（数字のみ）を入力しよう．\n")
            continue
            
        guess = int(guess_input)
        
        #正解・不正解のフィードバック
        if guess == secret_number:
            print(f"正解だ！ {attempt} 回目で {secret_number} を当てた！")
            return  #正解したらプログラムを終了する
        else:
            print("不正解！")
            #不正解時にヒントを出力
            if guess < secret_number:
                print("ヒント: 正解はもっと大きな数字だ．\n")
            else:
                print("ヒント: 正解はもっと小さな数字だ．\n")
            
            #残り2回のときに、1の位を提示する
            if attempt == max_attempts - 2:
                ones_place = secret_number % 10
                print(f"★ヒント: 正解の1の位は 「{ones_place}」 だ！")
            #残り1回のときに、10の位を提示する
            elif attempt == max_attempts - 1:
                tens_place = (secret_number // 10) % 10
                print(f"★最後のヒント: 正解の10の位は 「{tens_place}」 だ！")

                
    #回数制限に達した場合の処理
    print("ゲームオーバーだ．制限回数を超えた．")
    print(f"正解は {secret_number} だった．")

if __name__ == "__main__":
    number_guessing_game()