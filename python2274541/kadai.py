
import time
import datetime
from md_typing import typing
from md_blackjack import blackjack
from md_ohara_rpg import rpg
#global variable----
NAME = None
play_counter = 1
#-------------------

#https://note.nkmk.me/python-datetime-now-today/
dt_now = datetime.datetime.now()
#また、属性で年year、月month、日day、時間hour、分minute、秒second、マイクロ秒microsecondを整数intで取得できる。

def decoration(kigou,kaisuu,kankaku):
    for _ in range(kaisuu):
        time.sleep(kankaku)
        print(str(kigou),end='')
    time.sleep(kankaku)
    print(str(kigou))

print('準備中',end='')
decoration('・',5,0.3)

while True:
    get_tmp = input('名前を入力してください:')
    if len(get_tmp) != 0 and get_tmp[0] != ' ':
        NAME = get_tmp
        break
    else:
        print('空白の名前は使用できません')
        #continue

print('読み込み中',end='')
decoration('・',5,0.3)
print('-complete-')
print('現在の時刻[',end='')
print(f'{dt_now.year}年{dt_now.month}月{dt_now.day}日{dt_now.hour}時{dt_now.minute}分',end='')
print(']')
if 5 <= dt_now.hour and dt_now.hour <= 8: #5-8
    print(f'おはようございます、{NAME}さん')
elif 9 <= dt_now.hour and dt_now.hour <= 17: #9-17
    print(f'こんにちは、{NAME}さん')
elif 18 <= dt_now.hour and dt_now.hour <= 24: #18-24
    print(f'こんばんは、{NAME}さん')
else: #1-4
    print(f'深夜ですね、{NAME}さん、早めに寝ましょう')

get_check = None
while True:
    if get_check == '4' or get_check == '４':
        print('お疲れ様でした')
        print('遊んでくれてありがとう!')
        break
    if play_counter == 1: #1回のみ 予定
        print('今日も来てくれてありがとう')
        print('さて、今日はどのゲームをプレイする？')
    elif play_counter % 2 == 0: #2の倍数のとき
        print(f'楽しかったね、{NAME}さん')
        print('次は、どのゲームをプレイする？') #2
    elif play_counter % 3 == 0: #3の倍数のとき
        print(f'実はこのゲーム、私が全て作ったの、\n{NAME}さんのお気に入りのゲームは見つかった？') #3
        print('次はどのゲームを遊ぼうかな？')
    else: # 5 7 11 13 17とか
        print(f'そろそろ疲れて来る頃だね、{NAME}さん')
        print('まだゲームをプレイする？')
    
    flag = True
    while flag:
        decoration('--',20,0.02)
        get_check = input('Typing-- 1\nBlackJack--- 2\nO-HARA_RPG-- 3\n今日はもうゲームをやめる-- 4\n入力してください:')
        if not(get_check in ['1','2','3','4','１','２','３','４']):
            print('入力した値が間違っています、再度入力してください')
            continue
        else:
            if get_check == '1' or get_check == '１':
                decoration('--',20,0.02)
                print('タイピングを始めるよ')
                print('読み込み中',end='')
                decoration('・',5,0.3)
                print('---complete---')
                typing('tango.csv')
                decoration('--',20,0.02)
                play_counter += 1
                flag = False
            elif get_check == '2' or get_check == '２':
                decoration('--',20,0.02)
                print('ブラックジャックを始めるよ')
                print('読み込み中',end='')
                decoration('・',5,0.3)
                print('---complete---')
                time.sleep(1)
                print('それでは、いまからブラックジャックジャックを始めます!')
                print('説明は必要ですか_？')
                while True:
                    decoration('--',20,0.02)
                    get_check2 = input('説明が必要! -- 1\nはやく始めたい!! -- 2\n入力してください:')
                    if not(get_check2 in ['1','2','１','２']):
                        print('入力した値が間違っています、再度入力してください')
                        continue
                    elif get_check2 == '1' or get_check2 =='１':
                        #bjの説明 印字
                        print('bjの説明です、理解したらEnterを押してください')
                        print('|基本的なルールはすみませんが、ご自身で調べてください')
                        print('|プレイヤーとCPU(ディーラー)の一対一の勝負になります')
                        print('|トランプのカードは数字の1-10で出現します。10は3/13の確率で出現します')
                        print('|また、同じ数字が4回以上出現する可能性もあります')
                        print('|ベットやダブルベットなどの要素はなく、シンプルにヒットかスタンドのみです')
                        print('|最初にカードが2枚配られた後、プレイヤーがスタンドまたは、役ができるまで引いて')
                        print('|その後、ディーラーが引いていく流れになります。以下、役の強さ、勝敗の決め方です')
                        print('|ナチュラルブラックジャック > ブラックジャック == 5カード > ハイカード[20] > ハイカード[17] > バースト')
                        print('|上の例ではハイカードに[20]と[17]が入っていますが、もちろん同じ値の場合、引き分けです')
                        get_check3 = input('OK!-- Enter(エンターキー)') #処理を一時止める
                        break
                    else: #2の選択
                        break
                print('それでは、始めます')
                decoration('--',20,0.02)
                time.sleep(1)
                blackjack()
                decoration('--',20,0.02)
                play_counter += 1
                flag = False
            elif get_check == '3' or get_check == '３':
                decoration('--',20,0.02)
                print('O-HARA_RPGを始めるよ')
                print('読み込み中',end='')
                decoration('・',5,0.3)
                print('---complete---')
                rpg()
                play_counter += 1
                flag = False
            else: #4の選択
                flag = False