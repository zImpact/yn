init:
    transform zomzom(x):#==========================================================================================
        zoom x
    transform zomrot(x,y):#========================================================================================
        zoom x
        rotate y

init python:
    import time
    import random
    from copy import deepcopy
    from itertools import chain
    UIC=ui.callsinnewcontext
    UIC2=renpy.call_in_new_context
    rand,ranc,rant,ransh,ranu,rans=random.randint,random.choice,random.triangular,random.shuffle,random.uniform,random.sample
    pauza=renpy.pause
    remusplay=renpy.music.play

    class Karta(object):#======================== КЛАСС КАРТ =======================================
        __slots__ ="num","img"
        def __init__(self,num=0,img="yn/images/mini_games/durak/0.png",suit=1):
            self.num=num   #НОМЕР
            self.img=img   #КАРТИНКА
            self.suit=suit #МАСТЬ

    base_koloda_durak36=[Karta(6,"yn/images/mini_games/durak/106.jpg",1),Karta(7,"yn/images/mini_games/durak/107.jpg",1),Karta(8,"yn/images/mini_games/durak/108.jpg",1),Karta(9,"yn/images/mini_games/durak/109.jpg",1),
        Karta(10,"yn/images/mini_games/durak/110.jpg",1),Karta(11,"yn/images/mini_games/durak/110a.jpg",1),Karta(12,"yn/images/mini_games/durak/110b.jpg",1),Karta(13,"yn/images/mini_games/durak/110c.jpg",1),Karta(14,"yn/images/mini_games/durak/111.jpg",1),
        Karta(6,"yn/images/mini_games/durak/206.jpg",2),Karta(7,"yn/images/mini_games/durak/207.jpg",2),Karta(8,"yn/images/mini_games/durak/208.jpg",2),Karta(9,"yn/images/mini_games/durak/209.jpg",2),
        Karta(10,"yn/images/mini_games/durak/210.jpg",2),Karta(11,"yn/images/mini_games/durak/210a.jpg",2),Karta(12,"yn/images/mini_games/durak/210b.jpg",2),Karta(13,"yn/images/mini_games/durak/210c.jpg",2),Karta(14,"yn/images/mini_games/durak/211.jpg",2),
        Karta(6,"yn/images/mini_games/durak/306.jpg",3),Karta(7,"yn/images/mini_games/durak/307.jpg",3),Karta(8,"yn/images/mini_games/durak/308.jpg",3),Karta(9,"yn/images/mini_games/durak/309.jpg",3),
        Karta(10,"yn/images/mini_games/durak/310.jpg",3),Karta(11,"yn/images/mini_games/durak/310a.jpg",3),Karta(12,"yn/images/mini_games/durak/310b.jpg",3),Karta(13,"yn/images/mini_games/durak/310c.jpg",3),Karta(14,"yn/images/mini_games/durak/311.jpg",3),
        Karta(6,"yn/images/mini_games/durak/406.jpg",4),Karta(7,"yn/images/mini_games/durak/407.jpg",4),Karta(8,"yn/images/mini_games/durak/408.jpg",4),Karta(9,"yn/images/mini_games/durak/409.jpg",4),
        Karta(10,"yn/images/mini_games/durak/410.jpg",4),Karta(11,"yn/images/mini_games/durak/410a.jpg",4),Karta(12,"yn/images/mini_games/durak/410b.jpg",4),Karta(13,"yn/images/mini_games/durak/410c.jpg",4),Karta(14,"yn/images/mini_games/durak/411.jpg",4)]

    def playdurak(kolodatip=52):#============================== ЗАПУСКАЮЩАЯ ИГРУ ФУНКЦИЯ ==============================
        global quick_menu
        quick_menu=False
        renpy.choice_for_skipping()
        playdurak2(kolodatip)
        renpy.call("durak78")
        quick_menu=True
    def playdurak2(kolodatip=52):#============================== ПЕРЕМЕШИВАНИЕ И РАЗДАЧА КАРТ =========================
        global iwin21,cpucards,playercards,zerocard,intergames,koloda52,cpu_walk,trump_suit,atkcards,defcards
        iwin21=0
        atkcards=[]
        defcards=[]
        zerocard=Karta(0,"yn/images/mini_games/durak/0.png")
        zerocardkrb=Karta(0,"yn/images/mini_games/durak/k.jpg")
        if kolodatip is 52:
            koloda52=deepcopy(base_koloda_durak)
        elif kolodatip is 36:
            koloda52=deepcopy(base_koloda_durak36)
        ransh(koloda52)
        cpucards=[koloda52.pop(),koloda52.pop(),koloda52.pop(),koloda52.pop(),koloda52.pop(),koloda52.pop()]
        playercards=[koloda52.pop(),koloda52.pop(),koloda52.pop(),koloda52.pop(),koloda52.pop(),koloda52.pop()]
        trump_suit=koloda52[0].suit
        intergames=1
        cpu_walk=durak_whostart()
        if cpu_walk:
            durak_cpuai()
    def durak_mine(card,num=0):#===================== ОСНОВНАЯ ФУНКЦИЯ ДУРАКА =======================================
        if card is 1:                               # ИГРОК ЗАБИРАЕТ КАРТЫ
            playercards.extend(atkcards)
            playercards.extend(defcards)
            durak_endround(1)
        elif card is 2:                             # ИГРОК ЗАВЕРШАЕТ ХОД
            durak_endround(1)
        else:                                       # ИГРОК ИСПОЛЬЗУЕТ КАРТУ
            if not atkcards:
                atkcards.append(playercards.pop(num))
                durak_cpuai(card)
                return
            atk=atkcards[-1]
            if cpu_walk:                            # КОГДА ИГРОК ОТБИВАЕТСЯ
                if atk.suit==trump_suit==card.suit:
                    if atk.num<card.num:
                        defcards.append(playercards.pop(num))
                        durak_cpuai(2)
                else:
                    if card.suit is trump_suit:
                        defcards.append(playercards.pop(num))
                        durak_cpuai(2)
                    elif atk.num<card.num and atk.suit is card.suit:
                        defcards.append(playercards.pop(num))
                        durak_cpuai(2)
            else:                                    # КОГДА ИГРОК АТАКУЕТ
                if not atkcards or card.num in durak_getnums(): #
                    atkcards.append(playercards.pop(num))
                    durak_cpuai(card)
    def durak_endround(x):#================== ЗАВЕРШЕНИЕ РАУНДА ======================================
        global atkcards,defcards,cpu_walk
        atkcards,defcards,cpu_walk=[],[],x
        durak_getcards()
        if cpu_walk:
            durak_cpuai()
    def durak_getcards():#============= УЧАСТНИКИ ДОБИРАЮТ ИЗ КОЛОДЫ ПО ОДНОЙ КАРТЕ ДО 6 =====================
        for i in koloda52:
            u=0
            if len(cpucards)<6:
                cpucards.append(koloda52.pop())
                u=1
            if len(playercards)<6 and koloda52:
                playercards.append(koloda52.pop())
                u=1
            if not u:
                return
    def durak_getnums():#========================================================================================
        nums=[]
        for i in chain(atkcards,defcards):
            nums.append(i.num)
        return nums
    def durak_winchk():#========================== ПРОВЕРКА НА ПОБЕДУ ================================================
        global intergames,iwin21
        if not cpucards or not playercards:
            intergames=0
            if not cpucards and not playercards:
                iwin21=2
            elif not playercards:
                iwin21=1
            else:
                iwin21=0
            return 1
    def durak_cpuai(card=1):#============================ РАБОТА ИИ ================================================
        if durak_winchk():
            return
        if card is 1:                           #ПЕРВЫЙ АТАКУЮЩИЙ ХОД ИИ
            minicard=0
            for n,i in enumerate(cpucards):
                if i.suit!=trump_suit:
                    numofcard=n
                    minicard=i.num
            if minicard:
                for n,i in enumerate(cpucards):
                    if i.suit!=trump_suit:
                        if i.num<minicard:
                            minicard=i.num
                            numofcard=n
            else:
                numofcard=0
                minicard=cpucards[0].num
                for n,i in enumerate(cpucards):
                    if i.num<minicard:
                        minicard=i.num
                        numofcard=n
            atkcards.append(cpucards.pop(numofcard))
        elif card is 2:                         #СЛЕДУЮЩИЕ АТАКУЮЩИЕ ХОДЫ ИИ
            for n,i in enumerate(cpucards):
                if i.num in durak_getnums():
                    atkcards.append(cpucards.pop(n))
                    return
            durak_endround(0)
        else:                                   #ЗАЩИЩАЮЩИЕСЯ ХOДЫ ИИ(ОТВЕТ НА ХОД ИГРОКА)
            if card.suit is trump_suit:         #ПОХОДИЛ ЛИ ИГРОК С КОЗЫРНОЙ КАРТЫ?
                for n,i in enumerate(cpucards):
                    if i.suit is trump_suit and i.num>card.num:
                        defcards.append(cpucards.pop(n))
                        return
            else:
                for n,i in enumerate(cpucards): #ПОХОДИЛ ЛИ ИГРОК С ОБЫЧНОЙ КАРТЫ
                    if card.suit is i.suit:
                        if i.num>card.num:
                            defcards.append(cpucards.pop(n))
                            return
                trumpnum=99
                for n,i in enumerate(cpucards): #КРЫТЬ НЕЧЕМ ищем козыря
                    if i.suit is trump_suit:
                        if i.num<trumpnum:
                            trumpnew=n
                            trumpnum=i.num
                if trumpnum<20:                 #КАГДА НАЙДЕН ПОДХОДЯЩИЙ КОЗЫРЬ
                    defcards.append(cpucards.pop(trumpnew))
                    return
            cpucards.extend(atkcards)            #НЕЧЕМ КРЫТЬ ИИ ЗАБИРАЕТ КАРТЫ
            cpucards.extend(defcards)
            durak_endround(0)
    def durak_whostart():#=========================== ОПРЕДЕЛЯЯЕМ КТО ХОДИТ ПЕРВЫМ ============================
        cpulist=[98]
        for i in cpucards:
            if i.suit is trump_suit:
                cpulist.append(i.num)
        playerlist=[99]
        for i in playercards:
            if i.suit is trump_suit:
                playerlist.append(i.num)
        if min(playerlist)<min(cpulist):
            return 0
        return 1
screen key_off():#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    key"game_menu"action NullAction()
    key"rollback"action NullAction()
    key"viewport_wheelup"action NullAction()
    key"viewport_wheeldown"action NullAction()
    key"viewport_up"action NullAction()
    key"viewport_down"action NullAction()
    key"hide_windows"action NullAction()
    key"skip"action NullAction()
    key"stop_skipping"action NullAction()
    key"toggle_skip"action NullAction()
    key"fast_skip"action NullAction()
    key"accessibility"action NullAction()
screen durak78():#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    use key_off

    add"yn/images/mini_games/durak/tb.png"

    textbutton ["Сдаться"]:
        align(.8, .5)
        style "yn_dw_info_text_style"
        text_style "yn_dw_info_text_style"
        action [Return(), Jump("yn_act_two_play_fourth_card_game_loose")]

    if intergames:
        if len(koloda52)>1:
            if koloda52:
                add koloda52[0].img align(0.,.5) at zomrot(.7,90)
            add"yn/images/mini_games/durak/s.png"align(0.,.5)at zomzom(.7)
        if cpu_walk:
            if len(atkcards):
                textbutton ["Забрать"]:
                    align(.5,.7)
                    style "yn_dw_info_text_style"
                    text_style "yn_dw_info_text_style"
                    action Function(durak_mine,1)

            hbox xpos.15 yalign.4:#--------------АТАКУЮЩИЕ КАРТЫ
                spacing 3
                for i in atkcards:
                    add i.img at zomzom(.7)
            hbox xpos.142 yalign.502:#--------------ЗАЩИЩАЮЩИЕСЯ КАРТЫ
                spacing 3
                for i in defcards:
                    add"yn/images/mini_games/durak/shadow.png"at zomzom(.7)
            hbox xpos.14 yalign.5:#--------------ЗАЩИЩАЮЩИЕСЯ КАРТЫ
                spacing 3
                for i in defcards:
                    add i.img at zomzom(.7)
        else:
            if len(atkcards):
                textbutton ["Завершить ход"]:
                    align(.5,.7)
                    style "yn_dw_info_text_style"
                    text_style "yn_dw_info_text_style"
                    action Function(durak_mine,2)
            hbox xpos.14 yalign.5:#--------------АТАКУЮЩИЕ КАРТЫ
                spacing 3
                for i in atkcards:
                    add i.img at zomzom(.7)
            hbox xpos.152 yalign.402:#--------------ЗАЩИЩАЮЩИЕСЯ КАРТЫ
                spacing 3
                for i in defcards:
                    add"yn/images/mini_games/durak/shadow.png"at zomzom(.7)
            hbox xpos.15 yalign.4:#--------------ЗАЩИЩАЮЩИЕСЯ КАРТЫ
                spacing 3
                for i in defcards:
                    add i.img at zomzom(.7)
        hbox align(.5,0.):#-------------------КАРТЫ В РУКАХ ИИ
            spacing 3
            for i in cpucards:
                add"yn/images/mini_games/durak/k.jpg"at zomzom(.7)#"yn/images/mini_games/durak/k.jpg"
        hbox align(.5,1.):#------------------КАРТЫ В РУКАХ ИГРОКА
            spacing 3
            for n,i in enumerate(playercards):
                imagebutton idle i.img at zomzom(.7)action Function(durak_mine,i,n)
    else:
        if iwin21 is 1:
            textbutton ["Победа"]:
                align(.5,.5)
                style "yn_dw_info_text_style"
                text_style "yn_dw_info_text_style"
                action [Return(), Jump("yn_act_two_play_fourth_card_game_win")]

        elif iwin21 is 2:
            textbutton ["Ничья"]:
                align(.5,.5)
                style "yn_dw_info_text_style"
                text_style "yn_dw_info_text_style"
                action [Return(), Jump("yn_act_two_play_fourth_card_game_draw")]

        else:
            textbutton ["Проигрыш"]:
                align(.5,.5)
                style "yn_dw_info_text_style"
                text_style "yn_dw_info_text_style"
                action [Return(), Jump("yn_act_two_play_fourth_card_game_loose")]
label durak78:################################################################################################
    call screen durak78
    return