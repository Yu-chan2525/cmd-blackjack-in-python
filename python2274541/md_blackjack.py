from array import array
import random
import time

#頭文字　大文字がありますがクラスは使っていません
#印字　== print のことです
"""
苦戦したやつ、まだ完全に理解してない
https://dev.classmethod.jp/articles/python-function-nest-variable/
#---------------
"""
#動作確認や　挙動確認の際、64行のdef(time_sleep)内のtime.sleepの値を小さくすると多少は効果的です...。default = 0.5
#または、'time.sleep(' を選択、右クリック全ての出現場所を変更で　#付けのコメントアウト化など こっちは処理が速すぎて追えなくなるかも

def blackjack():
    #blackjack()でのローカススコープ変数を定義
    Burst = False
    Natural = False
    Blackjack = False
    FiveCard = False 
    Ace = 0
    #-------------------------------------

    """
    if __name__ == '__main__':
        #global variable
        global Burst,Natural,Blackjack,FiveCard,Ace
        Burst = False
        Natural = False
        Blackjack = False
        FiveCard = False
        Ace = 0
        #---------------
    """

    def nonlocal_reset():
        #RESET nonlocal variable---------------------
        nonlocal Burst,Natural,Blackjack,FiveCard,Ace
        Burst = False
        Natural = False
        Blackjack = False
        FiveCard = False
        Ace = 0
        #--------------------------------------------

    def upper_ten(random_num:int)->int:
        """11以上の数を10にして返します"""
        return 10 if random_num > 10 else random_num

    def card_sum(card_array:array)->int:
        """引数配列の合計sumを(1を1)として左の返り値、(1を11)として計算して右の返り値でreturnします"""
        last_add = 0
        for n in card_array:
            if n == 1:
                last_add += 10
        return sum(card_array),sum(card_array)+last_add

    def card_disp(card_array:array,sleep:float)->None:
        """引数配列の値を順に'[' int ']'形式で印字します。順にprintしていく間隔(時間)をsleep引数に渡してください'改行なしend=''"""
        for n in card_array:
            time.sleep(sleep)
            print('[',n,']',end='')

    def time_sleep():
        """呼ぶと印字が始まります--'空白1マス' '>' t0.5 '>' t0.5 '>' t0.5 #tはtime.sleepのことです 3つめの'>'まで改行なしend=''"""
        print(' ',end='')
        print('>',end='')
        time.sleep(0.5)
        print('>',end='')
        time.sleep(0.5)
        print('>')
        time.sleep(0.5)


    def judge_num_disp(card_array:array,low_val:int,hi_val:int):
        """
        --基本的にBLACKJACKでのみ有効な関数です--
        引数3つ:要素数6以下の配列,配列のsum(1を1として計算),配列のsum(1を11として計算)
        下記のBurst,Natural,Blackjack,FiveCard,Aceはノンローカル変数です、judge_num_disp()内で、blackjack()の変数の値を書き換えます

        ☆返り値の　Trueは(BURSTやBLACKJACKになっておらず)まだカードを引いても大丈夫を表します
        ★        Falseは             "          おり    もうカードを引くことができないを表します      
        まず印字で--ハンドx枚-と表示します x == 配列の要素数lenです、次に
        *配列のなかにAce(1のこと)が含まれないとき↓
            *1 |1点計算と11点計算は同じ値になります
            *2 |値が22点以上->配列のsumの値とBURSTの文字を印字し BurstにTrueを代入 返り値はFalse
            *3 |値が21点    ->配列のsumの値とBLACKJACKの文字を印字し BlackjackにTrueを 返り値はFalse
            *4 |値が21点以下->配列のsumの値を印字し 返り値は　True
        *配列のなかにAce(1のこと)が含まれるとき↓
        基本的に上と同様に、自動的に22以上で戻り値False,BurstをTrue::21点で戻り値False,BlackjackをTrueになります
        *Aceが1枚のとき
            *5|1点計算と11点計算の場合を踏まえて*2,*3の処理を行います (11点計算BURST 1点計算21点以下などがあるため)
            *6|Aceを11点計算しBURSTする場合 1点計算を適用した配列のsumを印字 返り値はTrue
            *6|↑BURSTしない場合、1点計算のsum配列 と 文字列'OR' 11点計算のsum配列を印字 返り値はTrue
        *Aceが2枚以上のとき
            *7|2枚以上を11点計算すると必ずBURSTになるので、(Aceを全て1点計算と)、(1枚のみ11点、その他は1点計算)
            *7|全て1点計算がBURSTの場合*2の処理、(1*Ace枚数 点)(11+1*Ace枚数 点)の場合で*3の処理
            *8|(11+1*Ace枚数 点)がBURSTしない場合 (1*Ace枚数 点)のsum配列 と 文字列'OR' (11+1*Ace枚数 点)のsum配列を印字 返り値はTrue
        *BURSTしていない、配列の要素数が5のとき(5枚)のとき 5CARDの文字 が印字と global FiveCard = Trueに
        返り値はないので、関数外で5枚なのでもうカードを引けないようにする必要があるかもしれません
        """

        def five_card_disp(card_array:array):
            if len(card_array) == 5:
                nonlocal FiveCard
                FiveCard = True
                print('!-☆彡-★彡-- 5 CARD --☆彡-★彡')

        if low_val > 21:
            nonlocal Burst
            Burst = True
            time.sleep(1.5)
            print(f'--ハンド-{len(card_array)}枚-(合計:[{low_val}])')
            time.sleep(0.5)
            print('!-X-X-BURST-X-X-')
            return False
        elif low_val == 21 or hi_val == 21:
            nonlocal Blackjack
            Blackjack = True
            time.sleep(1.5)
            print(f'--ハンド-{len(card_array)}枚-(合計:[21])')
            time.sleep(0.7)
            print('!-★-☆-BLACKJACK-★-☆-')
            five_card_disp(card_array)
            return False
        else:                                                     #     low:high
            if min(card_array) == 1: #ハンド配列にAce(1)が含まれるとき　例(1,2[3]:[13]1+10,2)
                nonlocal Ace
                Ace = 0
                for n in card_array:
                    if n == 1:
                        Ace += 1
                if Ace == 1: #含まれるかつ1枚のとき
                    if hi_val > 21: #11点計算が21を超えた時点で 1点計算の方のみを表示する
                        time.sleep(1.5)
                        print(f'--ハンド-{len(card_array)}枚-(合計:[{low_val}])')
                        five_card_disp(card_array)
                        return True
                    else: #11点計算が21以下のとき Aceを1で加算した場合と11で加算の場合を表示
                        time.sleep(1.5)
                        print(f'--ハンド-{len(card_array)}枚-(合計:[{low_val}] OR [{hi_val}])')
                        five_card_disp(card_array)
                        return True

                def mid_val_disp(mid_val):
                    if mid_val == 21: #1+11点計算の結果 Blackjack
                        nonlocal Blackjack
                        Blackjack = True
                        time.sleep(1.5)
                        print(f'--ハンド-{len(card_array)}枚-(合計:[21])')
                        time.sleep(0.7)
                        print('!-★-☆-BLACKJACK-★-☆-')
                        five_card_disp(card_array)
                        return False
                    #11+11のhi_valは即バーストのため気にしなくていい
                    elif mid_val > 21: #1+11計算が22以上になってしまっている場合 lowのみ
                        time.sleep(1.5)
                        print(f'--ハンド-{len(card_array)}枚-(合計:[{low_val}])')
                        five_card_disp(card_array)
                        return True
                    else: #1+11計算で21以下の場合　lowとmidを表示
                        time.sleep(1.5)
                        print(f'--ハンド-{len(card_array)}枚-(合計:[{low_val}] OR [{mid_val}])')
                        five_card_disp(card_array)
                        return True
                                                                                            #low  mid high 
                if Ace == 2: #含まれるかつ２枚のとき　例(1,3,1[5]or[15]:[15]or[25]1,3,1) (1,9,1[11],[21]:[31]1,9,1)
                    #すこしややこしいので無駄な処理も書きます
                    low_val = low_val #1点と1点で計算　21点以上は排除済み
                    mid_val = hi_val-10 #1点と11点で計算
                    hi_val = hi_val #11点と11点で計算しているもの
                    tmp_bool = mid_val_disp(mid_val)
                    return tmp_bool
                if Ace == 3:
                    mid_val = hi_val-20
                    tmp_bool = mid_val_disp(mid_val)
                    return tmp_bool
                if Ace == 4:
                    mid_val = hi_val-30
                    tmp_bool = mid_val_disp(mid_val)
                    return tmp_bool
                if Ace == 5:
                    mid_val = hi_val-40
                    tmp_bool = mid_val_disp(mid_val)
                    return tmp_bool
                        
            else: #ハンド配列にAce(1)が含まれないとき　low == high
                time.sleep(1.5)
                print(f'--ハンド-{len(card_array)}枚-(合計:[{low_val}])') #hi low どっちでもいい
                five_card_disp(card_array)
                return True


    print('#Dealer:カードを2枚配ります',end='')
    print(' ',end='') #半角スペース
    time_sleep()
    d_card = [] #dealerのハンドになります
    d_card.append(upper_ten(random.randint(1,13))) #1-13でランダムな値を生成->11以上を10にハンドに追加
    d_card.append(upper_ten(random.randint(1,13))) #1-13でランダムな値を生成->11以上を10にハンドに追加
    print('#Dealer:',end='')
    time.sleep(1.2)
    print('[',d_card[0],']',end='')
    time.sleep(1.7)
    print('[-?-]',end='') #dealerの2枚目は最初伏せます
    time.sleep(1.5)
    print('--ハンド-2枚-(1枚目:[',d_card[0],'])',sep='')
    time.sleep(1)
    p_card = [] #playerのハンドになります
    p_card.append(upper_ten(random.randint(1,13))) #1-13でランダムな値を生成->11以上を10にハンドに追加
    p_card.append(upper_ten(random.randint(1,13))) #1-13でランダムな値を生成->11以上を10にハンドに追加

    time_sleep()
    print('*Player:--PLAYER TURN--')
    time.sleep(1.5)
    print('*Player:始めるよ、私のターン!')
    time_sleep()

    print('*Player:',end='')
    card_disp(p_card,1.7)
    low,high = card_sum(p_card)
    judge_num_disp(p_card,low,high)

    flag = True
    while flag  and len(p_card) < 5:
        if len(p_card) == 2 and high == 21: #最初の2枚で21
            Natural = True
            time.sleep(0.9)
            print('!-☆-★- NATURAL -☆-★-')
            flag = False
            break

        hit_stand = input('*ヒット(引く)--> 1\n*スタンド(これ以上引かない)--> 2\n*入力してください:')
        if hit_stand == '1' or hit_stand == '１': #hit 選択時
            time_sleep()
            append_card = upper_ten(random.randint(1,13)) #一枚引く 値を代入
            print('*Hit-->[',append_card,']です') #引いた値を表示
            p_card.append(append_card)  #ハンドの配列にappend
            print('*Player:',end='')
            card_disp(p_card,0.7)   #ハンドを表示
            low,high = card_sum(p_card) #ハンド配列の要素を合計した値　low<--Aceを1として  high<--Aceを11として
            flag = judge_num_disp(p_card,low,high) #ハンドの合計値を表示 flagに返り値を代入

        elif hit_stand == '2' or hit_stand ==  '２':
            flag = False
        else:
            time_sleep()
            print('*---入力が正しくありません---*')
            print('*Player:',end='')
            card_disp(p_card,0.7)
            judge_num_disp(p_card,low,high)
            #continue
    time_sleep()
    print('*Player:うまくできたかな、ターンを終了するよ!')
    time.sleep(1.2)
    print('*Player:--TURN END--')
    time_sleep()
    time.sleep(0.5)

    #値を退避----------------
    P_BURST = Burst
    P_NATURAL = Natural
    P_BLACKJACK = Blackjack
    P_FIVECARD = FiveCard
    P_ACE = Ace
    #------------------------

    nonlocal_reset() #退避させたローカル変数をリセット、最初の宣言の状態に戻します

    print('')
    print('#Dealer:では、私が引いていきます')

    print('#Dealer:',end='')
    time.sleep(1.2)
    print('[',d_card[0],']',end='')
    time.sleep(1.7)
    print('[-?-]',end='')
    time.sleep(1.5)
    print('--ハンド-2枚-(1枚目:[',d_card[0],'])',sep='')
    time_sleep()
    print('#Dealer:',end='')
    print('私の2枚目のカードは、{}でした'.format(d_card[1]))
    time.sleep(1)
    time_sleep()
    print('#Dealer:',end='')
    card_disp(d_card,0.7)
    low,high = card_sum(d_card)
    judge_num_disp(d_card,low,high)

    flag = True
    while flag and len(d_card) < 5:
        if len(d_card) == 2 and high == 21: #最初の2枚で21
            Natural = True
            time.sleep(0.9)
            print('!-☆-★- NATURAL -☆-★-')
            flag = False
            break

        fifty_percent = random.randint(1,2) #cpuなので2分の1(50%)の確率で17点以上でhit,枚数4で残り1枚で5カードの時hitを実装するための準備

        while len(d_card) < 5 and (low < 17 or high < 17): #17点以下なので絶対に引く(cpu想定なので例:5+1+11で17などの特殊な計算は考慮しないでおく(例の場合:(5+1+1)でTrueを返す))
            time_sleep()
            append_card = upper_ten(random.randint(1,13)) #一枚引く 値を代入
            print('#Hit-->[',append_card,']です') #引いた値を表示
            d_card.append(append_card)  #ハンドの配列にappend
            print('#Dealer:',end='')
            card_disp(d_card,0.7)   #ハンドを表示
            low,high = card_sum(d_card) #ハンド配列の要素を合計した値　low<--Aceを1として  high<--Aceを11として
            flag = judge_num_disp(d_card,low,high) #ハンドの合計値を表示 flagに返り値を代入

        if flag and (not Burst) and len(d_card) == 4 and fifty_percent == 1: #BURSTしてない残り1枚hitで5カードが見えるとき,50%の確率でhitさせる
            time_sleep()
            append_card = upper_ten(random.randint(1,13)) #一枚引く 値を代入
            print('*Hit-->[',append_card,']です') #引いた値を表示
            d_card.append(append_card)  #ハンドの配列にappend
            print('#Dealer:',end='')
            card_disp(d_card,0.7)   #ハンドを表示
            low,high = card_sum(d_card) #ハンド配列の要素を合計した値　low<--Aceを1として  high<--Aceを11として
            flag = judge_num_disp(d_card,low,high) #ハンドの合計値を表示 flagに返り値を代入
        else:
            break

        if flag and (not Burst) and fifty_percent == 1: #17点以上でも50%の確率でhitさせる
            time_sleep()
            append_card = upper_ten(random.randint(1,13)) #一枚引く 値を代入
            print('#Hit-->[',append_card,']です') #引いた値を表示
            d_card.append(append_card)  #ハンドの配列にappend
            print('#Dealer:',end='')
            card_disp(d_card,0.7)   #ハンドを表示
            low,high = card_sum(d_card) #ハンド配列の要素を合計した値　low<--Aceを1として  high<--Aceを11として
            flag = judge_num_disp(d_card,low,high) #ハンドの合計値を表示 flagに返り値を代入
        else:
            break

    time_sleep()
    print('#Dealer:私のターンは終わりです')
    time.sleep(1.2)
    print('#Dealer:--TURN END--')
    time_sleep()

    #ローカル変数をそのまま使ってもいいけど、わかりやすいように
    D_BURST = Burst
    D_NATURAL = Natural
    D_BLACKJACK = Blackjack
    D_FIVECARD = FiveCard
    D_ACE = Ace
    #---------------------------------------------------

    def decoration_line(n,t):
        for _ in range(n):
            time.sleep(t)
            print('-',end='')
        print('') #end=を無効

    decoration_line(50,0.01)
    print('☆  結果発表  ☆')

    #                        1          3       2        2         ハイカード
    def result_disp(name,burst:bool,natu:bool,bj:bool,five:bool,ace:int,hand:array)->int:
        if natu:
            print(f'{name}:ナチュラルブラックジャック[☆★ ]')
            return 103
        elif bj:
            print(f'{name}:ブラックジャック[★ ]')
            return 102
        elif five:
            print(f'{name}:ファイブカード[◎ ]')
            return 102
        elif burst:
            print(f'{name}:バースト[X]')
            return 1
        elif ace == 0:
            low,high = card_sum(hand)
            print(f'{name}:ハイカード[{high}点]')
            return sum(hand)
        else:
            low,high = card_sum(hand)
            if high < 21:
                print(f'{name}:ハイカード[{high}点]')
                return high
            else:
                for _ in range(ace):
                    high = high - 10
                    if high < 21:
                        print(f'{name}:ハイカード[{high}点]')
                        return high
                else:
                    print(f'{name}:ハイカード[{low}点]')
                    return low

    print('*',end='')
    p_result = result_disp('Player',P_BURST,P_NATURAL,P_BLACKJACK,P_FIVECARD,P_ACE,p_card)
    print('#',end='')
    d_result = result_disp('Dealer',D_BURST,D_NATURAL,D_BLACKJACK,D_FIVECARD,D_ACE,d_card)

    if p_result == d_result:
        print('---引き分け---')
    elif p_result > d_result:
        print('☆★☆  Playerの勝利 ☆★☆')
    else:
        print('☆★☆  Dealerの勝利 ☆★☆')

if __name__ == '__main__':

    blackjack()

"""
dealer rule
    17以上になるまで hit ~16
    17以上で stand 17~

winner
ナチュラルブラックジャック > ブラックジャック == 5カード > ハイカード[20] > ハイカード[17] > バースト
上の例ではハイカードに[20]と[17]が入っていますが、もちろん同じ値の場合、引き分けです
"""
