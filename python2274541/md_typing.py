

import csv
import time
import random

def typing(csvfile):
    """
    最初が word_len,word で始まり、その後順番に
    左側に単語の文字数,右側に単語が記載されているCSVファイル('example.csv')を引数としてください
    (例--example.csv--)
    word_len,word
    5,あいうえお
    3,やゆよ
    """
    with open(csvfile, encoding="utf-8", mode="r") as f:
        lst = list(csv.DictReader(f))

            #DictReader(colum名で指定可能)word_lenとword
            #Dictionary(辞書、辞典)

    flag = True

    while flag:

        print('難易度を選択\nかんたん--> 1\nふつう----> 2\n難しい----> 3')

        level = input('入力してください・・・:')

        #levelに合わせた変数への代入

        if level == '1' or level == '１':
            #1 level
            lev_info = 'かんたん'
                    #出題する
            lower_limit = 1 #文字数の下限
            upper_limit = 4 #文字数の上限
            que_times = 10  #問題数

            flag = False

        elif level == '2'or level == '２':
            #2 level
            lev_info = 'ふつう'
            lower_limit = 4
            upper_limit = 7
            que_times = 20

            flag = False

        elif level == '3' or level == '３':
            #3 level
            lev_info = '難しい'
            lower_limit = 8
            upper_limit = 20
            que_times = 20
            
            flag = False

        else:
            print('\n\n* 難易度の選択は1または2もしくは3で入力してください *\n')
            flag = True
            continue


        quebox = []

        for i in range(len(lst)):
            if lower_limit <= int(lst[i]["word_len"]) <= upper_limit:
                quebox.append([(lst[i]["word_len"]),lst[i]["word"]])

        #出題する問題が格納されたリストを表示できる
        #print(quebox)

        print("complete")

        print(f'*難易度：{lev_info}')
        print(f'出題文字数:{lower_limit}～{upper_limit}文字です')
        print(f'問題数:{que_times}回です')
        print('難易度を変更する場合や、途中で中断するときは end もしくは　えんｄ と入力してください!!')

        chk = input('(全角にして)Enterキーでスタート(end入力で難易度選択へ)::')
        if chk == 'end' or chk == 'えんｄ':
            flag = True
            continue
        else:
            print('3')
            time.sleep(0.7)
            print('2')
            time.sleep(0.7)
            print('1')
            time.sleep(0.7)
            print('start')
            time.sleep(0.2)

            i_count = 0
            flg = True
            distinct = None #タイプミスの場合同じ問題が続けて出題なので、勘違いしないように、同じ単語を連続させないための変数
            timelog = [] #正確に打ち終わるまでの経過時間(このプログラムではprogress)と、出題単語を記録していくためのもの

            while True:
                randnum = random.randint(0,len(quebox)-1) #配列数の　ランダムな整数を取得
                if randnum == distinct: #一つ前の問題と同じだったら再抽選させる
                    continue
                else:
                    que_word = quebox[randnum][1]             #ランダムな値の添え字番目の単語を取得
                    flg = True
                    
                    start = time.perf_counter() #開始時間

                    while flg:
                        print('{:>2d} '.format(i_count+1),end='') 
                        print(f'問目  {que_word}',end='')
                        ans_word = input(':')
                        if ans_word == 'end' or ans_word == 'えんｄ': #end入力で
                            flag = False
                            break #134行目に移動
                        if ans_word == que_word: #正確に打てたとき

                            finish = time.perf_counter() #終了時間

                            progress = finish - start #経過時間の計測
                            progress = round(progress,1) #経過時間の四捨五入

                            timelog.append([i_count,ans_word,progress]) #timelogリストの中にリストをいれる

                            distinct = randnum
                            i_count += 1
                            flg = False #134行目に移動
                        else: #打てなかったとき、i_countの値は変わらないので同じ出題がされる
                            flg = True
                            continue
                    if ans_word == 'end' or ans_word == 'えんｄ' or i_count >= que_times: #end入力もしくは、出題数の数だけ終了したとき
                        break
        print('-----------------------------------------')
        print('お疲れ様でした')
        print(f'難易度:{lev_info}\n')
        
        total_time = 0
        w_length = 0

        for i,w,t in timelog:
            w_length += len(w)
            total_time += t
        print(f'{i_count}問打つのにかかった時間は{round(total_time,1)}秒でした')
        try:
            print(f'一文字あたり{round((total_time/w_length),1)}秒でした')
            print('-----------------------------------------')
        except ZeroDivisionError:
            print(f'end または　えんｄ　が入力されました...中断します')

        while True:
            change = input('-タイピングが終了しました-\nもっと詳細な結果を見る---> 1\n難易度を選択してもう一度プレイ--> 2\nタイピングを終了する--> 3\n入力してください:')

            if change == '1' or change =='１':
                print('-----------------------------------------')
                if bool(timelog): #list空かチェック
                    for i,w,t in timelog:
                        print('{:>2d}問目:'.format(i+1),end='')
                        print(f'{w}--',end='')
                        print(f'{t}秒')
                else:
                    print('1問もタイピングできていませんでした')
                print('-----------------------------------------')
                continue

            elif change == '2' or change =='２':
                flag = True
                break

            elif change == '3' or change =='３':
                flag = False
                break 

            else:
                print('\n\n* 難易度の選択は1または2もしくは3で入力してください *\n')
                continue
        
        continue

    print('タイピングを終了します')

if __name__ == '__main__':
    
    typing('tango.csv')

"""
#4文字#https://jp.wazap.com/cheat/%E3%81%93%E3%81%A8%E3%81%B0%E3%81%95%E3%81%8C%E3%81%97%E3%80%80%E4%B8%80%E8%A6%A7%E8%A1%A8%EF%BC%88%EF%BC%94%E6%96%87%E5%AD%97%EF%BC%89/550363/
#8,9文字#https://jp.wazap.com/cheat/%E3%81%93%E3%81%A8%E3%81%B0%E3%81%95%E3%81%8C%E3%81%97%E3%80%80%E4%B8%80%E8%A6%A7%E8%A1%A8%EF%BC%88%EF%BC%98%2C%EF%BC%99%E6%96%87%E5%AD%97%EF%BC%89/550354/
#他、5,6,7文字なども同サイトなどからコピー
"""