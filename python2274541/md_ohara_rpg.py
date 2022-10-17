
import math
import time
import random

def rpg():
    #基底クラス Player_Enemy
    class Player_Enemy:
        #クラス変数
        #コンストラクタ、イニシャライザ
        #init == initialize（イニシャライズ)初期化
        def __init__(self,name,hit_point,pw_limit) -> None:
            #インスタンス変数---------
            #Player_Enemy
            self.__name = name
            self.__hp = hit_point
            self.__pw = pw_limit
            #------------------------

        def name_disp(self):
            return self.__name

        def test(self):
            print(self.__name)
            print(self.__hp)
            print(self.__pw)
        #-Player用----------------------------------------------------
        def hp_disp(self):
            print(f' {self.__name}:',end='')
            if self.__hp <= 0:
                print('◇◇◇◇◇◇◇◇◇◇',end='') #10
            elif self.__hp < wariai_and_lowlimit:
                print('◆',end='')
                print('◇◇◇◇◇◇◇◇◇',end='') #9
            else:
                hp_gauge = math.floor(self.__hp / wariai_and_lowlimit) #せっかくなのでround以外も使ってみる 切り捨て
                if hp_gauge > 10:
                    hp_gauge = 10 #最大10
                    
                for _ in range(hp_gauge):
                    print('◆',end='')
                for _ in range(10 - hp_gauge):
                    print('◇',end='')
            print(f' [HP:{self.__hp}]')

        def buff_hp_limit(self,bairitu):
            """主人公のHPのみ難易度に合わせて上げます"""
            self.__hp *= bairitu

        def p_damege(self,num):
            print(f'{self.__name}に{num}ダメージ')
            self.__hp -= num

        def p_heal(self,num):
            print(f'{self.__name}の体力が{num}回復')
            self.__hp += num

        def hp_check(self):
            if self.__hp <= 0:
                print(f'{self.__name}が倒れた')
                return False
            else:
                return True
        #-------------------------------------------------------------
        #セイレーン用からの回復用
        def s_heal(self,num):
            print(f'{self.__name}の体力が{num}回復')
            self.__hp += num


    class Enemy(Player_Enemy):
        def __init__(self,name,hit_point,pw_limit) -> None:
            super().__init__(name,hit_point,pw_limit)
            self.__name = name
            self.__hp = hit_point
            self.__pw = pw_limit

        def release_limit(self,bairitu): #normal-1x hard-2x ex-3xとか予定
            """敵のHPとPWを難易度に合わせて上げます"""
            self.__hp *= bairitu
            self.__pw *= bairitu

        def test(self):
            print(self.__name)
            print(self.__hp)
            print(self.__pw)
        #-Enemy用---------------------------------------------
        def hp_disp(self):
            print(f' {self.__name}:',end='')
            if self.__hp <= 0:
                print('◇◇◇◇◇◇◇◇◇◇',end='') #10
            elif self.__hp < wariai_and_lowlimit:
                print('◆',end='')
                print('◇◇◇◇◇◇◇◇◇',end='') #9
            else:
                hp_gauge = math.floor(self.__hp / wariai_and_lowlimit) #せっかくなのでround以外も使ってみる 切り捨て
                for _ in range(hp_gauge):
                    print('◆',end='')
                for _ in range(10 - hp_gauge):
                    print('◇',end='')
            print(f' [HP:{self.__hp}]')

        def e_damage(self,num):
            print(f'{self.__name}に{num}ダメージ')
            self.__hp -= num

        def hp_check(self):
            if self.__hp <= 0:
                print(f'{self.__name}を倒した')
                return False
            else:
                return True

        def e_randint(self):
            return random.randint(0,self.__pw)
        #------------------------------------------------------
        #セイレーン用
        def s_heal(self,num):
            print(f'{self.__name}の体力が{num}回復')
            self.__hp += num

    class Job_Card:
        def __init__(self,name,numeric) -> None:
            self.name = name
            self.action_limit = numeric
        
        def use_card(self):
            return random.randint(wariai_and_lowlimit,self.action_limit)

    class Kenshi(Job_Card):
        def __init__(self, name, numeric) -> None:
            super().__init__(name, numeric)
            self.name = name
            self.numeric = numeric

        def use_card(self):
            return random.randint(wariai_and_lowlimit,self.action_limit)

    class Magic(Job_Card):
        def __init__(self, name, numeric) -> None:
            super().__init__(name, numeric)
            self.name = name
            self.numeric = numeric
            
        def use_card(self):
            return random.randint(0,self.action_limit)

    class Healer(Job_Card):
        def __init__(self, name, numeric) -> None:
            super().__init__(name, numeric)
            self.name = name
            self.numeric = numeric

        def use_card(self):
            return random.randint(wariai_and_lowlimit,self.action_limit)

    def decoration_line(n,t):
        for _ in range(n):
            time.sleep(t)
            print('-',end='')
        print('') #end=を無効

    def decoration(kigou,kaisuu,kankaku):
        for _ in range(kaisuu):
            time.sleep(kankaku)
            print(str(kigou),end='')
        time.sleep(kankaku)
        print(str(kigou))



    while True:
        p_name = input('主人公の名前を入力:')
        if len(p_name) != 0 and p_name[0] != ' ': #入力が0文字じゃない、かつ１文字目が空白じゃない
            break
        else:
            print('空白の名前は使用できません')
            #continue
    decoration_line(30,0.05)
    wariai_and_lowlimit = 10
    player = Player_Enemy(p_name,100,50)

    print(f'O-HARAの世界へようこそ {player.name_disp()}!')

    player.hp_disp()
    while True:
        print('難易度を選択してね!')
        #decoration_line(30,0.01)
        get_tmp = input('EASY---- 1\nNORMAL-- 2\nHARD---- 3\n入力してください:')
        if len(get_tmp) == 1 and get_tmp in ['1','2','3','１','２','３']: #1文字　and inで含まれている
            break
        else:
            print('入力が正しくありません')
            #continue

    #インスタンス化-----------------------------------------------------------
    kensi = Kenshi('剣士カード',50) #下限-50までのランダムな値    |      減らす
    magic = Magic('魔法カード',100)# 0 - 100 までのランダムな値   |HPから減らす
    healer = Healer('回復カード',50)   #下限-50までのランダムな値 |      増やす

    #分かりやすいように　綴り間違えてます
    sulime = Enemy('-敵-スライム',10,10) #バランス
    golem = Enemy('-敵-ゴーレム',40,20) #バランス
    minotaur = Enemy('-強敵-ミノタウロス',60,30) #攻撃的
    seiren = Enemy('-強敵-セイレーン',80,50) #回復多めにしたい
    doragon = Enemy('-BOSS-ドラゴン',100,70) #未定
    #-------------------------------------------------------------------------
    #選んだ難易度に合わせて　上記インスタンス化した値などを調整---------------------
    if get_tmp == '1' or get_tmp == '１':
        bairitu = 1
        wariai_and_lowlimit = 10
    elif get_tmp == '2' or get_tmp == '２':
        bairitu = 2
        wariai_and_lowlimit = 20
    elif get_tmp == '3' or get_tmp == '３':
        bairitu = 3
        wariai_and_lowlimit = 30

    player.buff_hp_limit(bairitu)
    sulime.release_limit(bairitu)
    golem.release_limit(bairitu)
    minotaur.release_limit(bairitu)
    seiren.release_limit(bairitu)
    doragon.release_limit(bairitu)
    #---------------------------------------------------------------------------

    """
    sulime.test()
    golem.test()
    minotaur.test()
    seiren.test()
    doragon.test()
    """

    def toko_toko():
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('トコトコ...')
        time.sleep(1)

    def select_check():
        while True:
            decoration('--',20,0.02)
            print(f'・剣士カードを使う[{wariai_and_lowlimit}~50]- 1')
            print(f'・魔法カードを使う[0~100]- 2')
            print(f'・回復カードを使う[{wariai_and_lowlimit}~50]- 3')
            select = input('入力してください-- :')
            if select in ['1','2','3','１','２','３']:
                break
            else:
                print('入力が間違っています')
                #continue
        return select

    e_flag = True
    p_flag = True
    #-スライムSTART----------------------------------------------------------
    toko_toko()
    time.sleep(0.7)
    decoration('--',20,0.02)
    print(f'{sulime.name_disp()}が現れた!')
    sulime.hp_disp()

    while e_flag and p_flag:

        print(f'{player.name_disp()}はどうする')
        player.hp_disp()
        select = select_check()
        decoration('--',20,0.02)

        if select in ['1','１']:
            sulime.e_damage(kensi.use_card())
        elif select in ['2','２']:
            sulime.e_damage(magic.use_card())
        else:
            player.p_heal(healer.use_card())
            player.hp_disp()

        sulime.hp_disp()
        e_flag = sulime.hp_check() #敵が生きているなら True
        time.sleep(1.2)
        if e_flag:
            print(f'{sulime.name_disp()}の攻撃')
            time.sleep(1.5)
            time.sleep(1.5)
            p_flag = player.p_damege(sulime.e_randint()) #0-上限値(pw)の乱数ダメージ
            time.sleep(1)
            time.sleep(1)
        else:
            #e_flag = False
            break #敵は死んで　自分は生きているとき while外へ
        
        player.hp_disp()
        p_flag = player.hp_check()

    #次の敵の準備と状態遷移------------------------
    if e_flag == False and p_flag == True:
        toko_toko()
        e_flag = True
        time.sleep(0.7)
        decoration('--',20,0.02)
        print(f'{golem.name_disp()}が現れた!')
        golem.hp_disp()
    else:
        e_flag = True #敵は生きてる
        p_flag = False #自分は死んでる状態へ

    #-スライムEND------------------------------------------------------------

    #-ゴーレムSTART----------------------------------------------------------
    while e_flag and p_flag:

        print(f'{player.name_disp()}はどうする')
        player.hp_disp()
        select = select_check()
        decoration('--',20,0.02)

        if select in ['1','１']:
            golem.e_damage(kensi.use_card())
        elif select in ['2','２']:
            golem.e_damage(magic.use_card())
        else:
            player.p_heal(healer.use_card())
            player.hp_disp()

        golem.hp_disp()
        e_flag = golem.hp_check() #敵が生きているなら True
        time.sleep(1.2)
        if e_flag:
            print(f'{golem.name_disp()}の攻撃')
            time.sleep(1.5)
            p_flag = player.p_damege(golem.e_randint()) #0-上限値(pw)の乱数ダメージ
            time.sleep(1)
        else:
            #e_flag = False
            break #敵は死んで　自分は生きているとき while外へ
        
        player.hp_disp()
        p_flag = player.hp_check()

    #次の敵の準備と状態遷移--------------------------
    if e_flag == False and p_flag == True:
        toko_toko()
        e_flag = True
        time.sleep(0.7)
        decoration('--',20,0.02)
        print(f'{minotaur.name_disp()}が現れた!')
        print(f'気を付けて、{minotaur.name_disp()}は、先行攻撃をしてくるぞ!')
        time.sleep(1.3)
        minotaur.hp_disp()
    else:
        e_flag = True #敵は生きてる
        p_flag = False #自分は死んでる状態へ

    #-ゴーレムEND--------------------------------------------------------

    #-ミノタウロスSTART----------------------------------------------------------
    while e_flag and p_flag:

        if e_flag:
            print(f'{minotaur.name_disp()}の攻撃')
            time.sleep(1.5)
            p_flag = player.p_damege(minotaur.e_randint()) #0-上限値(pw)の乱数ダメージ
            time.sleep(1)
        else:
            #e_flag = False
            break #敵は死んで　自分は生きているとき while外へ

        player.hp_disp()
        p_flag = player.hp_check()

        if p_flag: #生きてるなら
            print(f'{player.name_disp()}はどうする')
            player.hp_disp()
            select = select_check()
            decoration('--',20,0.02)

            if select in ['1','１']:
                minotaur.e_damage(kensi.use_card())
            elif select in ['2','２']:
                minotaur.e_damage(magic.use_card())
            else:
                player.p_heal(healer.use_card())
                player.hp_disp()

            minotaur.hp_disp()
            e_flag = minotaur.hp_check() #敵が生きているなら True
            time.sleep(1.2)

    #次の敵の準備と状態遷移--------------------------
    if e_flag == False and p_flag == True:
        toko_toko()
        e_flag = True
        time.sleep(0.7)
        decoration('--',20,0.02)
        print(f'{seiren.name_disp()}が現れた!')
        print(f'{seiren.name_disp()}は、回復をしてくる厄介な相手..でも気まぐれで冒険者も回復してくるかも')
        seiren.hp_disp()
    else:
        e_flag = True #敵は生きてる
        p_flag = False #自分は死んでる状態へ

    #-ミノタウロスEND--------------------------------------------------------------

    #-セイレーンSTART--------------------------------------------------------------
    while e_flag and p_flag:

        print(f'{player.name_disp()}はどうする')
        player.hp_disp()
        select = select_check()
        decoration('--',20,0.02)

        if select in ['1','１']:
            seiren.e_damage(kensi.use_card())
        elif select in ['2','２']:
            seiren.e_damage(magic.use_card())
        else:
            player.p_heal(healer.use_card())
            player.hp_disp()

        seiren.hp_disp()
        e_flag = seiren.hp_check() #敵が生きているなら True
        time.sleep(1.2)
        if e_flag:
            persent = random.randint(1,3)
            if persent == 1:
                print(f'{seiren.name_disp()}の攻撃')
                time.sleep(1.5)
                p_flag = player.p_damege(seiren.e_randint()) #0-上限値(pw)の乱数ダメージ
                time.sleep(1)
                player.hp_disp()
            elif persent == 2:
                print(f'{seiren.name_disp()}の回復の歌')
                time.sleep(1.5)
                seiren.s_heal(wariai_and_lowlimit)
                time.sleep(1.2)
                seiren.hp_disp()
                time.sleep(1)
            else: #3
                print(f'{seiren.name_disp()}の癒しの歌')
                time.sleep(1.5)
                print(f'あなたも回復してあげる')
                time.sleep(1)
                player.s_heal(wariai_and_lowlimit + 17)
                time.sleep(1.2)
                seiren.s_heal(wariai_and_lowlimit + 17)
                time.sleep(1.2)
                seiren.hp_disp()
                time.sleep(1)
        else:
            #e_flag = False
            break #敵は死んで　自分は生きているとき while外へ
        
        p_flag = player.hp_check()

    #次の敵の準備と状態遷移--------------------------
    if e_flag == False and p_flag == True:
        toko_toko()
        e_flag = True
        time.sleep(0.7)
        decoration('--',20,0.02)
        print(f'{doragon.name_disp()}が現れた!')
        print(f'最後の敵だ、{doragon.name_disp()}は、攻撃と回復を同時にしてくるぞ!')
        doragon.hp_disp()
    else:
        e_flag = True #敵は生きてる
        p_flag = False #自分は死んでる状態へ

    #-セイレーンEND-------------------------------------------------------------

    #-ドラゴンSTART-------------------------------------------------------------
    while e_flag and p_flag:
        print(f'{player.name_disp()}はどうする')
        player.hp_disp()
        select = select_check()
        decoration('--',20,0.02)

        if select in ['1','１']:
            doragon.e_damage(kensi.use_card())
        elif select in ['2','２']:
            doragon.e_damage(magic.use_card())
        else:
            player.p_heal(healer.use_card())
            player.hp_disp()

        doragon.hp_disp()
        e_flag = doragon.hp_check() #敵が生きているなら True
        time.sleep(1.2)

        if e_flag:
            print(f'{doragon.name_disp()}の治癒のウロコ')
            doragon.s_heal(wariai_and_lowlimit * (random.randint(1,3))) #セイレーン用に作ったやつ使います
            doragon.hp_disp()
        if e_flag:
            fifty_persent = random.randint(1,2) #2パターンの攻撃メッセージを用意
            if fifty_persent == 1:
                print(f'{doragon.name_disp()}の攻撃')
                time.sleep(1.5)
            elif fifty_persent == 2:
                print(f'{doragon.name_disp()}の火炎弾')

            p_flag = player.p_damege(doragon.e_randint()) #0-上限値(pw)の乱数ダメージ
            time.sleep(1)
        else:
            #e_flag = False
            break #敵は死んで　自分は生きているとき while外へ
        
        player.hp_disp()
        p_flag = player.hp_check()

    #-ドラゴンEND--------------------------------------------------------

    if p_flag == False:
        time.sleep(0.8)
        print(f'{player.name_disp()}は目の前が真っ暗になった')
        time.sleep(0.8)
        print('T-t- GAMEOVER -t-T')
        time.sleep(0.8)
        print('ざんねん!!')
        decoration('--',20,0.02)
    if e_flag == False:
        time.sleep(0.8)
        print('☆★☆ GAME-CLEAR--☆ 彡★ 彡')
        time.sleep(0.8)
        print('おめでとう!!')
        decoration('--',20,0.02)

if __name__ == '__main__':
    
    rpg()

"""
bound method == ()付け忘れかも
"""