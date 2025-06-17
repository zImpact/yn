label yn_act2_scene8:
    $ yn_onload("lock")
    $ renpy.block_rollback()
    $ persistent.timeofday = "day"
    $ persistent.sprite_time = "day"
    $ renpy.pause(3, hard=True)
    $ yn_chapter_intro(
        "Действие восьмое.",
        "bg yn_ext_camp_entrance_day_blurred",
        "camp_entrance_day",
        "yn_yana smile2",
        "yn_play_eighth_intro_text"
    )
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard=True)
    $ yn_onload("unlock")
    $ yn_set_timeofday_cursor_var = True
    $ renpy.block_rollback()
    $ persistent.yn_protagonist = "yana"
    # $ yn_rename_character("yn_yana", "Яна")
    $ persistent.timeofday = "sunset"
    $ persistent.sprite_time = "sunset"
    scene bg yn_ext_houses_backyard_sunset
    show yn_slon normal at center
    show yn_us normal at left
    play ambience ambience_camp_center_evening fadein 2
    play music yn_advance fadein 2
    with Dissolve(2)
    yn_narrator "И снова мы сидим за кустами, где обустроен небольшой пункт наблюдения."
    yn_th "Идея мне не нравится, но чего не сделаешь ради... товарищей."
    yn_slon "Короче, повторю план. {w}{i}Для. {w}Особо. {w}Забывчивых.{/i}"
    yn_narrator "Протянул он, явно намекая на самую младшую из нашего диверсионного отряда."
    show yn_us dontlike with dspr
    yn_us "Да помню я всё. Помню."
    yn_slon "Хорошо. Озвучь."
    show yn_us upset with dspr
    yn_narrator "Ульяна замялась. Какое-то время колебалась, перебирая все известные ей вводные слова."
    show yn_us normal with dspr
    yn_us "Ладно. Повтори."
    yn_slon "Наша цель: Найти любой компромат в домике Ежа. Если мы этого не сделаем, то последствия могут оказаться плачевными."
    yn_slon "Ты, Кузнечик, играешь главную роль."
    yn_yana "Раз уж с постановкой не срослось."
    yn_slon "Тебе нужно будет зайти в домик и порыться в его вещах. Уверен, ты найдёшь там много чего интересного."
    yn_slon "Всё, что найдёшь хватаешь и валишь через окно. Делаешь крюк для верности и возвращаешься сюда. Поняла?"
    yn_us "Раз плюнуть."
    yn_narrator "Слон смерил её придирчивым взглядом."
    yn_slon "Ящерица, ты будешь нашим последним рубежом. Если всё пойдёт не по плану, то тебе нужно будет отвлечь Ежа, чтобы Кузнечик успела слинять. Тебя он шугаться не станет в отличии от Мельпы."
    yn_slon "Да и я уверен, что она ему в глаз двинет практически сразу как только он с ней заговорит. Вопросы?"

    $ yn_act2_scene7_slon_first_dialogue_variants_d = {
        1: ["{b}Всё понятно.{/b}", "yn_act2_scene7_slon_dialogue_understand", False],
        3: ["Что будешь делать ты?", "yn_act2_scene7_slon_dialogue_slon", False, 350],
        4: ["Где Мельпа?", "yn_act2_scene7_slon_dialogue_dv", False, 500],
        5: ["Что делают Хаер и Кот?", "yn_act2_scene7_slon_dialogue_haer_and_kot", False, 370]
    }

    $ yn_act2_scene7_slon_second_dialogue_variants_d = {
        1: ["{b}Плохой план.{/b}", "yn_act2_scene7_slon_dialogue_bad_plan", False],
        4: ["{b}Хороший план.{/b}", "yn_act2_scene7_slon_dialogue_good_plan", False, 465]
    }

label yn_act2_scene7_slon_first_dialogue_wh:
    $ renpy.block_rollback()
    $ yn_act2_scene7_slon_first_dialogue_wheel = YnDialogueWheel(yn_act2_scene7_slon_first_dialogue_variants_d)
    $ yn_act2_scene7_slon_first_dialogue_wheel.yn_dw_call()

label yn_act2_scene7_slon_second_dialogue_wh:
    $ renpy.block_rollback()
    $ yn_act2_scene7_slon_second_dialogue_wheel = YnDialogueWheel(yn_act2_scene7_slon_second_dialogue_variants_d)
    $ yn_act2_scene7_slon_second_dialogue_wheel.yn_dw_call()

label yn_act2_scene7_slon_dialogue_haer_and_kot:
    $ renpy.block_rollback()
    yn_slon "Они отслеживают передвижения Ежа по Лагерю. Хаер явно не хочет, чтобы он пошёл в художку, поэтому Кот с ним."
    yn_slon "В случае чего, охладит пыл нашего патлатого героя любовника своими проповедями."
    jump yn_act2_scene7_slon_first_dialogue_wh

label yn_act2_scene7_slon_dialogue_dv:
    $ renpy.block_rollback()
    yn_slon "Да вон она."
    yn_narrator "Слон указа на дальние кусты, что находились как раз возле поворота с Площади."
    yn_slon "Если Ёж пойдёт сюда, Кот прибежит и предупредит Мельпу, а она даст условный знак."
    yn_slon "У неё очень хорошо получается имитировать звуки, что издаёт кукушка. Вообще не отличить от реальной кукушки."
    yn_slon "Если услышишь звонкое «ку-ку» дважды, то приготовься. {w}Придётся отвлекать."
    jump yn_act2_scene7_slon_first_dialogue_wh

label yn_act2_scene7_slon_dialogue_slon:
    $ renpy.block_rollback()
    yn_slon "Останусь здесь и буду следить за ходом операции."
    yn_yana "Если говорить прямо, то ты просто всё придумал и теперь считаешь, что свою часть выполнил."
    yn_slon "Ну... можно и так сказать. Мне вообще нельзя светиться. Уж простите."
    yn_us "Пф. Важная птица ты наша."
    jump yn_act2_scene7_slon_first_dialogue_wh

label yn_act2_scene7_slon_dialogue_understand:
    $ renpy.block_rollback()
    yn_slon "Отлично!"
    yn_narrator "Дверь домика распахнулась и Ёж вышел на улицу."
    yn_narrator "Он вальяжно потянулся, захлопнул дверь не закрывая её и пошёл шаркающей походкой в сторону площади."
    jump yn_act2_scene7_slon_second_dialogue_wh

label yn_act2_scene7_slon_dialogue_good_plan:
    $ renpy.block_rollback()
    $ yn_sparrows_group_ending += 1
    $ yn_slon_ending += 1
    show yn_slon smile with dspr
    yn_slon "Спасибо."
    yn_narrator "Моя похвала действительно тронула Слона. Ему было приятно, что его старания оценили."
    jump yn_act2_scene7_after_slon_dialogue

label yn_act2_scene7_slon_dialogue_bad_plan:
    $ renpy.block_rollback()
    yn_us "Да! Мне то залезть вообще проблем не составит, но ты и сам мог бы поучаствовать, а не отсиживаться здесь."
    yn_narrator "Слон ничего не ответил, а только повёл плечами."
    jump yn_act2_scene7_after_slon_dialogue

label yn_act2_scene7_after_slon_dialogue:
    $ renpy.block_rollback()
    yn_yana "Если всё закончится плохо, я подожгу кусты возле вашего с Хаером домика и скажу, что это ты курил."
    yn_narrator "Я подмигнула."
    show yn_us grin with dspr
    yn_us "Ха! Вот этот план мне нравится куда больше."
    yn_slon "Да уж. Мельпа оказывает на тебя куда большее влияние, чем я думал. Ладно. Начали."
    scene bg ext_houses_sunset
    show yn_us normal
    with dissolve
    yn_narrator "Мы с Кузнечиком быстро направились к домику Ежа."
    yn_narrator "Насколько мне известно, он сейчас живёт один, ибо его сосед настоятельно попросил переселения. {w}Очень настоятельно попросил."
    yn_narrator "Ульяна юркнула к двери, бегло огляделась по сторонам и дёрнула за ручку. Потом ещё раз. Дверь не поддалась."
    yn_us "Это ещё что за новости? Захлопнулась."
    yn_yana "Дёрни сильнее."
    show yn_us dontlike with dspr
    yn_narrator "Ульяна закатила глаза."
    yn_us "Да ну? Помоги лучше."
    yn_narrator "Мы потянули вместе. Спустя пару минут безрезультатных попыток, нам всё же удалось распахнуть злосчастную дверь."
    show yn_us normal with dspr
    yn_us "Я пошла. Оставлю дверь полуоткрытой. Если что, зови."
    hide yn_us
    yn_narrator "Ульяна скрылась в домике. Послышалось шебуршание и скрип открывающейся дверцы шкафа."
    yn_th "Ох, какая же это всё-таки паршивая идея!"
    yn_yana "Не наследи там."
    yn_narrator "В ответ послышалось приглушёное и неразборчивое бормотание."
    yn_narrator "Я начала медленно прохаживаться взад-вперед, пытаясь сделать максимально беззаботный вид."
    yn_narrator "Правда, тот факт, что я нахожусь возле домика довольно известной в плохом смысле Лагерной личности и словно бы его ожидаю, явно выглядит подозрительно."
    yn_narrator "Ульяна роется там уже несколько минут. Неужели, у него там так много вещей?"
    yn_th "Неужели, я действительно верила, что всё пройдёт гладко?"
    yn_narrator "После очередного поворота в своей бессмысленной прогулке кругами, я увидела вдалеке Ежа."
    yn_narrator "Он уже прошёл кусты, где находилась Алиса, но никакого предупреждающего сигнала не прозвучало."
    yn_narrator "Парень уже заметил меня, на его лице появилась фирменная похабная улыбочка."
    yn_yana "Ёж идёт! Уходи!"
    yn_narrator "Быстрый топот. Ульяна подошла к двери и вполголоса сказала:"
    yn_us "Отвлеки его насколько сможешь. Мне чуть-чуть осталось. Тут тайник за фанерой походу. Тяни время, короче."
    yn_narrator "Сказала и закрыла дверь."
    yn_th "Во что же я вляпалась?"

    if yn_act2_scene5_video_get_way == "flirt":
        yn_th "Опять мне приходится это делать. Сначала Шурик, теперь ОН. Ну уж нет. С Ежом я точно флиртовать не буду. Лучше сразу сквозь землю провалиться."

    yn_narrator "Пришлось идти навстречу Ежу."
    yn_th "«Тяни время!» О чём мне с ним говорить? О погоде?"
    show yn_wuk smile pos1 at center with dissolve
    yn_wuk "О! Ящерица, а чего это ты меня тут караулишь?"

    $ yn_act2_scene7_wuk_first_dialogue_variants_d = {
        1: ["{b}Я хотела кое о чём поговорить.{/b}", "yn_act2_scene7_wuk_dialogue_talk", False],
        3: ["Погода сегодня хорошая...", "yn_act2_scene7_wuk_dialogue_weather", False, 270],
        4: ["А ты откуда?", "yn_act2_scene7_wuk_dialogue_whence", False, 520]
    }

    $ yn_act2_scene7_wuk_second_dialogue_variants_d = {
        1: ["{b}Отстань от Красавицы.{/b}", "yn_act2_scene7_wuk_dialogue_kras", False],
        3: ["А это правда то, что о тебе говорят?", "yn_act2_scene7_wuk_dialogue_gossip", False, 100],
        4: ["Что ты не поделил с Воробьями?", "yn_act2_scene7_wuk_dialogue_pigeons", False, 150]
    }

label yn_act2_scene7_wuk_first_dialogue_wh:
    $ renpy.block_rollback()
    $ yn_act2_scene7_wuk_first_dialogue_wheel = YnDialogueWheel(yn_act2_scene7_wuk_first_dialogue_variants_d)
    $ yn_act2_scene7_wuk_first_dialogue_wheel.yn_dw_call()

label yn_act2_scene7_wuk_second_dialogue_wh:
    $ renpy.block_rollback()

    if yn_act2_scene7_wuk_compromosing_time_points >= 3:
        $ yn_act2_scene7_wuk_second_dialogue_variants_d[2] = ["{b}Прости, кажется меня зовут.{/b}", "yn_act2_scene7_wuk_dialogue_leave", False]

    $ yn_act2_scene7_wuk_second_dialogue_wheel = YnDialogueWheel(yn_act2_scene7_wuk_second_dialogue_variants_d)
    $ yn_act2_scene7_wuk_second_dialogue_wheel.yn_dw_call()

label yn_act2_scene7_wuk_dialogue_weather:
    $ renpy.block_rollback()
    $ yn_act2_scene7_wuk_compromosing_time_points += 1
    show yn_wuk smile pos2 with dspr
    yn_wuk "Да не скажи. Жарит не по-детски... или это просто рядом с тобой так жарко."
    yn_narrator "Он подмигнул."
    yn_th "Держись, Яна. Сдерживай рвотные позывы. Это для общего блага."
    show yn_wuk surprised pos2 with dspr
    if yn_act2_scene7_wuk_dialogue_question_number == 1:
        yn_wuk "Так ты что-то хотела?"
        $ yn_act2_scene7_wuk_dialogue_question_number = 2

    else:
        yn_wuk "Ну, не тяни. Что случилось то?"

    jump yn_act2_scene7_wuk_first_dialogue_wh

label yn_act2_scene7_wuk_dialogue_whence:
    $ renpy.block_rollback()
    $ yn_act2_scene7_wuk_compromosing_time_points += 1
    yn_wuk "Да..."
    show yn_wuk think pos1 with dspr
    yn_narrator "Ёж задумывается стоит ли ему говорить, где он был на самом деле."
    yn_narrator "Смерив меня необычным для него взглядом, в котором читалось подозрение, он ответил:"
    yn_wuk "Прогуливался."
    yn_yana "Понятно..."
    show yn_wuk surprised pos2 with dspr
    if yn_act2_scene7_wuk_dialogue_question_number == 1:
        yn_wuk "Так ты что-то хотела?"
        $ yn_act2_scene7_wuk_dialogue_question_number = 2

    else:
        yn_wuk "Ну, не тяни. Что случилось то?"

    jump yn_act2_scene7_wuk_first_dialogue_wh

label yn_act2_scene7_wuk_dialogue_talk:
    $ renpy.block_rollback()
    show yn_wuk smile pos2 with dspr
    yn_wuk "О чём же?"
    yn_narrator "Он пытается подойти ближе, я отступаю."
    yn_th "Ульяна, пожалуйста, быстрее."
    jump yn_act2_scene7_wuk_second_dialogue_wh

label yn_act2_scene7_wuk_dialogue_pigeons:
    $ renpy.block_rollback()
    $ yn_act2_scene7_wuk_compromosing_time_points += 1
    show yn_wuk surprised pos2 with dspr
    yn_narrator "Ёж якобы удивился."
    yn_wuk "У меня с ними всё нормально. Это у них со мной какие-то проблемы. Хаер, вон, вообще моросящий какой-то."
    yn_wuk "Требует, чтобы я отвалил от Красавицы. Они же не встречаются. Чего мне отваливать?"
    yn_wuk "А с конкуренцией оно всяко интереснее."
    yn_narrator "Ёж остановил взгляд на моём галстуке, что был повязан на руку."
    yn_wuk "Ой, забыл, что ты с ними трёшься."
    show yn_wuk smile pos2 with dspr
    yn_wuk "Ты это лучше давай к нам. У нас круче, а твой стиль явно станет жемчужиной Павлинов!"
    yn_yana "Нет, спасибо."
    jump yn_act2_scene7_wuk_second_dialogue_wh

label yn_act2_scene7_wuk_dialogue_gossip:
    $ renpy.block_rollback()
    $ yn_act2_scene7_wuk_compromosing_time_points += 1
    yn_wuk "А ты о чём? Много всяких слухов ходит знаешь ли. И про меня, и про тебя тоже. Это же Лагерь."
    yn_wuk "Та же Журналистка постоянно какие-то дешёвые сплетни распускает, а ей все верят."
    yn_yana "Значит, то что про тебя бают - не правда?"
    yn_wuk "Конечно нет. Тебе нужно узнать меня получше и мы обязательно подружимся."
    yn_narrator "И снова подмигивает."
    jump yn_act2_scene7_wuk_second_dialogue_wh

label yn_act2_scene7_wuk_dialogue_kras:
    $ renpy.block_rollback()
    show yn_wuk surprised2 pos2 with dspr
    yn_narrator "Это заявление явно вызвало раздражение у Ежа, но при этом в его глазах загорелись огоньки азарта, которые мне уже доводилось видеть."
    yn_wuk "И ты туда же? Что этот ваш Хаер сейчас, что ты. Сговорились что ли? Отвалите. {w}Это не ваше дело."
    hide yn_wuk with dissolve
    yn_narrator "Он быстро обошёл меня и резко открыл дверь домика."
    yn_narrator "Сердце ушло в пятки."
    yn_narrator "Но никакого крика не послышалось. Ёж просто зашёл и демонстративно захлопнул дверь."
    yn_th "Ушла! Повезло!"
    yn_narrator "Ладно. Теперь нужно возвращаться и узнать успела ли Ульяна что-то найти. А ещё стоит поинтересоваться, почему Алиса нас не предупредила."
    jump yn_act2_scene7_after_wuk_dialogue

label yn_act2_scene7_wuk_dialogue_leave:
    $ renpy.block_rollback()
    yn_th "Думаю, времени Кузнечику должно было хватить."
    show yn_wuk surprised pos2 with dspr
    yn_wuk "Разве? Я ничего не слышал."
    yn_yana "Да. Мельпа позвала."
    yn_narrator "Ежа аж передёрнуло от одной только её клички."
    yn_yana "Всё. Пока. Мне пора."
    yn_narrator "Я произнесла прощание нарочито громко, чтобы на всякий случай предупредить Ульяну, если она всё ещё в домике."
    yn_wuk "Ладно. Пока. Приходи на дискотеку. Потанцуем. Только в этот раз без мелкой."
    hide yn_wuk with dissolve
    yn_narrator "Я ничего не ответила, продолжая медленно удаляться."
    yn_narrator "Как только Ёж зашёл в домик и я убедилась, что никаких признаков поимки нашего диверсанта нет, я свернула в сторону кустов."
    yn_narrator "Посмотрим, что Ульяне удалось найти. А ещё стоит поинтересоваться почему Алиса нас не предупредила."
    jump yn_act2_scene7_after_wuk_dialogue

label yn_act2_scene7_after_wuk_dialogue:
    $ renpy.block_rollback()
    stop music fadeout 2
    scene bg yn_ext_houses_backyard_sunset
    show yn_slon normal at center
    show yn_us normal at left
    with dissolve

    if yn_act2_scene7_wuk_compromosing_time_points >= 3:
        $ yn_sparrows_group_ending += 1
        $ yn_us_ending += 1
        $ yn_slon_ending += 1
        yn_narrator "Ульяна вернулась довольная собой и с добычей."
        yn_narrator "Причём очень неожиданной. Два лифчика и эротический журнал."
        yn_th "Вот ведь извращенец!"
        yn_narrator "Слон на некоторое время застыл с открытым ртом."
        yn_slon "Это чьи?"
        yn_narrator "Спросил он, указывая на лифчики лежащие в траве и символично обрамляющие непристойное чтиво."
        yn_us "Этот точно Мельпы. Он пропал, когда она одежду после стирки сушила."
        yn_yana "Если она узнает..."
        yn_slon "...то убьёт его."
        yn_us "Ага..."
        show yn_us grin with dspr
        yn_us "Расскажем ей?"
        yn_slon "Сдурела что ли? Хочешь, чтобы традиция по «Покойничку» на поколение продолжилась?"
        yn_narrator "Ульяна отрицательно покачала головой."
        yn_slon "Как-нибудь незаметно закинь его потом ей в шкафчик."
        yn_yana "Кстати о Мельпе. Где она? Почему не было сигнала?"
        yn_slon "Я без понятия."
        show yn_us normal with dspr
        yn_us "Тоже хотелось бы узнать. Если бы не Ящерица, то я бы по полной влетела."
        yn_us "Всё из-за нашей заводилы. И да. План твой - туфта."
        yn_narrator "Слова Ульяны совсем не задели Слона. {w}Он только отмахнулся, а затем вперил странный взгляд в журнал. Тот был помятым и замызганным."
        yn_slon "Кузнечик, я тебе настоятельно рекомендую прямо сейчас быстро пойти помыть руки. Прям тщательно. С мочалкой."
        yn_us "А что такое?"
        yn_slon "Как бы тебе сказать..."
        yn_narrator "Слон замялся."
        yn_slon "Тут страницы липкие похоже."
        show yn_us fear with dspr
        yn_narrator "Ульяна сначала покраснела, а потом прямо на глазах побелела."
        hide yn_us with dissolve
        yn_narrator "Издав громкий визг, сопровождаемый множеством нецензурных междометий и даже целых предложений, она умчалась в сторону умывальников."
        yn_th "Ого. А дед-сторитель её многому научил. Это надо иметь недюжий талант, чтобы придумывать такие заковыристые выражения."

    else:
        yn_narrator "Ульяна вернулась ни с чем."
        show yn_us dontlike with dspr
        yn_us "Ящерица, из-за тебя я чуть не спалилась. Это же надо было такую фигню ему начать затирать!"
        yn_yana "Уж извини. Это как бы Мельпа должна была нас предупредить."
        yn_us "Это тоже. Слон, твой план - полнейшая туфта."
        yn_narrator "Кузнечик раздражённо замахала руками, выражая всё своё недовольство."
        yn_slon "Признаю, всё прошло не так как ожидалось. Но ничего не попишешь. {w}Мы хотя бы попытались."
        yn_slon "Ёж нас не заметил, значит это как минимум не провал."
        yn_yana "Оптимистично, конечно. Только вот без компромата мы с Ежом ничего не сделаем."
        yn_us "Я туда больше не полезу. {w}Сами разбирайтесь, короче!"
        hide yn_us with dissolve
        yn_narrator "Она для большей наглядности сильно топнула ногой, скрестила руки на груди и ушла."
        yn_slon "Ох и не нравится мне всё это. {w}Готов поспорить, что у Хаера точно было дежавю."

    stop ambience fadeout 2
    scene bg black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    scene bg yn_int_musclub_mattresses_sunset
    show yn_us dontlike:
        xpos -240

    show dv angry pioneer2:
        xpos 160

    show yn_haer pity longhair:
        xpos 850

    show yn_kot sad2:
        xpos 470

    show yn_slon normal2:
        xpos 1200
    with Dissolve(1)
    play ambience ambience_music_club_day fadein 2
    yn_yana "И зачем вы решили тут устроить собрание?"
    yn_narrator "Я пришла последней. Остальные Воробьи уже были в сборе."
    yn_narrator "Кузнечик пыталась предъявлять претензии Алисе, она же просто игнорировала подругу, злобно поглядывая на Хаера."
    yn_slon "Нужно обсудить с Синицами вопрос обновления Стены. На старой уже не хватает места. Сказали ждать их тут. Скоро начнут подтягиваться."
    hide yn_us
    hide dv
    hide yn_kot
    hide yn_haer
    hide yn_slon
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show yn_slon normal at center with dissolve
    yn_narrator "Я подошла к Слону и наклонилась ближе, чтобы услышать меня мог только он."
    yn_yana "Что случилось?"
    yn_narrator "Слон ответил шепотом."
    yn_slon "Да всё то же. Выяснилось, что Ежа спугнул Хаер, начав выяснять с ним отношения."
    yn_slon "Кот прибежал предупредить Мельпу, а той на месте не оказалось. Как-то так."
    show yn_kot sad:
        xpos 100
    with dissolve
    yn_kot "Всё у нас не слава Богу."
    hide yn_kot with dissolve
    yn_narrator "Неожиданно прошептал непонятно откуда взявшийся Кот."
    yn_yana "Мельпа сказала, куда она пропала?"
    yn_slon "Не-а."
    hide yn_slon with dissolve
    yn_narrator "Тем временем уже потихоньку начиналась перебранка. Алиса соизволила ответить Ульяне, но как и следовало ожидать, это была просто едкая острота."
    yn_th "Нет смысла влезать во всё это и выяснять отношения. Что случилось, то случилось."
    yn_narrator "Решив не обращать внимание на небольшую склоку, которая явно не перерастёт в сильную ссору, я подошла к роялю."
    yn_narrator "Порой даже не верится, что музыка это нечто земное и довольно привычное, что её вообще создали и заточили в музыкальные инструменты люди."
    yn_narrator "Сам по себе человек мелок, но чувства огромны. Им тесно внутри, они хотят выйти наружу, выплеснуться за края чаши человеческого тела."
    yn_narrator "Так рождается музыка, да и всё настоящее творчество в целом."
    yn_narrator "Я аккуратно подняла крышку рояля и села на неудобный стул-вертушку."
    yn_narrator "Вспомнилась одна простенькая, но красивая мелодия, которую я успела выучить до попадания в больницу."
    yn_narrator "При должной сноровке хватит и одной руки."
    yn_narrator "Ребята к этому времени всё ещё не успокоились."
    show dv angry pioneer2 at left
    show yn_us dontlike at right
    with dissolve
    yn_dv "Конечно-конечно. Ты права. Ты у нас всегда права, мелкая всезнайка."
    yn_narrator "Слон уже было хотел что-то сказать. Даже поднял руку, для привлечения внимания."
    scene bg yn_act_two_musclub_piano with dissolve
    play music yn_wolfgang_vivaldi_moonlight_sonata fadein 2
    yn_narrator "Я провела пальцами по клавишам. Гам прекратился. Все замолчали. Слон так и застыл с поднятой рукой."
    yn_narrator "Родилась мелодия. Мои руки стали проводниками, которые разрывая обыденность приносили в это место истинную красоту звуков."
    yn_narrator "Получалось не очень ровно, с перепадами. Левая грабля всё никак не хотела вовремя нажимать на клавиши, но это было не так страшно."
    yn_narrator "Даже если эта музыка только мне кажется чарующей и красивой, то я всё равно довольна."
    $ renpy.pause()
    stop music fadeout 2
    scene bg yn_int_musclub_mattresses_sunset
    show yn_mi grin at center
    with dissolve
    yn_narrator "Стоило мне доиграть, как тут же в музыкальный клуб вошла Мику. Она была в восторге и улыбалась."
    yn_narrator "Улыбка у неё была не такая, как у других людей, а какая-то по-детски наивная и глупая, но очень очаровывающая."
    yn_mi "{yn_tip_tag=totemo}Тотемо утскаси!{/yn_tip_tag} Я знала, что ты рано или поздно сыграешь на рояле!"
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard=True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "night"
    $ persistent.sprite_time = "night"
    scene bg ext_dining_hall_near_night with Dissolve(2)
    play ambience ambience_camp_center_night fadein 2
    play music music_list["that_s_our_madhouse"] fadein 2
    yn_yana "А я надеялась, что про проникновение со взломом вы пошутили..."
    show yn_slon normal at center with dissolve
    yn_slon "В данный момент эта идея мне тоже кажется очень тупой. Мы с Ежом чуть не прокололись, а тут дело более серьёзное."
    hide yn_slon
    show dv normal pioneer2 at center
    with dissolve
    yn_dv "Забей. Не неси чепуху. Всё нормально будет. Не в первый раз же."
    hide dv
    show yn_slon normal at center
    with dissolve
    yn_slon "Не неси чепуху..."
    hide yn_slon with dissolve
    yn_narrator "Сказал Слон с какой-то непонятной иронией в голосе."
    yn_narrator "Вероятно, он повторил её слова только по инерции, но даже беспристрастный человек мог бы принять это за издёвку, а уж Алиса едва не взвилась как ужаленная."
    yn_narrator "Но затем пристально всмотревшись в лицо Слона, успокоилась."
    yn_narrator "Тот даже бровями не повёл, а лишь с озабоченным видом что-то обдумывал."
    show yn_kot sad at center with dissolve
    yn_kot "А ведь воровать - грех."
    hide yn_kot
    show yn_haer pity longhair at center
    with dissolve
    yn_haer "А у кого мы воруем? Харчи то казённые, государственные."
    hide yn_haer
    show yn_kot sad at center
    with dissolve
    yn_kot "Так у государства и воруем."
    hide yn_kot
    show yn_haer pity longhair at center
    with dissolve
    yn_haer "А мы что, не часть государства по твоему?"
    hide yn_haer
    show yn_kot think at center
    with dissolve
    yn_narrator "Кот задумался."
    yn_kot "Ну... часть, конечно."
    hide yn_kot
    show yn_haer pity longhair at center
    with dissolve
    yn_haer "Вот и не парься, Кошак. Сам у себя не украдёшь."
    hide yn_haer
    show dv normal pioneer2 at center
    with dissolve
    yn_dv "Всё тихо. Ящерица, пошли. Остальные на шухере."
    hide dv
    show yn_us upset
    with dissolve
    yn_us "Ты только в этот раз нас не кинь."
    hide yn_us with dissolve
    yn_narrator "Мельпа остановилась, сжала кулаки."
    show dv angry pioneer2 at center with dissolve
    yn_dv "Молчи, мелкая. Я и твои косяки напомнить могу."
    hide dv with dissolve
    yn_narrator "Мельпа выжидающе зыркнула через плечо на Ульяну и поняв, что продолжения перепалки не будет, молча пошла к крыльцу столовой."
    yn_narrator "Кузнечик благоразумно ничего не ответила, а возможно, просто эдаким чудным способом дразнила Алису."
    # yn_dv "У меня три шпильки. Ящерица, не хочешь попробовать открыть Сезам?"
    # yn_th "На удивление я почему-то была не против поучаствовать в этой авантюре."
    # yn_th "Ведь, если в действительности посмотреть на всё это не через призму «правильности», то это чертовски весело и захватывающе. Не за этими ли эмоциями я сюда ехала?"
    # yn_yana "Ты серьёзно? Я же не взломщик тебе какой-то. Это умеючи надо."
    # yn_kot "Попытка - не пытка."
    # yn_dv "Во! Дело говорит. Тут то и сложного ничего нет. Просовываешь шпильку в верхнюю часть скважины, снизу медленно и аккуратно проворачиваешь отверткой. Когда услышишь щелчок - дело сделано. Нужно просто попасть в нужную позицию и не давить слишком сильно. Осилишь?"
    # yn_yana "Давай попробуем. Отвёртка, я так понимаю тоже краденная? Из радио кружка."
    # yn_narrator "Алиса осклабилась."
    # yn_dv "Обижаешь. Я её обменяла. Нельзя же просто так брать. Мена должна быть."
    # yn_yana "Но мена была без ведома хозяев?"
    # yn_dv "А это необязательное условие так то. Ладно. Поехали!"

    # show screen lockpicking
    # #*Мини-игра. Взлом.*
    # #*Подсказка*

    # #"Вращайте шпильку при помощи мышки. Попытка проворота активируется на левую кнопку мыши. Чем меньше диапазон проворота, тем дальше замок от точки открытия.
    # #При слишком длительном нажатии в неверном положении шпилька сломается."

    # #*Провал (1)*
    # yn_narrator "Я попыталась провернуть шпильку, но та с характерным звуком сломалась."
    # yn_dv "М-да... Я же сказала: аккуратно поворачиваешь."
    # yn_narrator "Алиса достала из нагрудного кармана щипцы и вытащила обломок из замочной скважины."
    # yn_dv "Давай ещё раз. Но это последняя попытка. Нечё отмычки зазря переводить."

    # #*Мини-игра. Взлом.*
    # #*Провал (2)*
    # yn_narrator "И снова я сделала что-то не так. Накатило чувство неоправданного доверия, что не осталось незамеченным."
    # yn_dv "Не парься. Не во всём же быть талантливой. Давай теперь мамочка этим займётся."
    # yn_narrator "Я отошла, пропуская «мамочку» к двери."
    yn_narrator "Я даже не успела и глазом моргнуть, как Мельпа парой ловких движений провернула шпильку в замке и раздался щелчок."
    show dv smile pioneer2 at center with dissolve
    yn_dv "Учись пока я не в «покойничках»."
    hide dv with dissolve
    yn_narrator "Девушка приоткрыла дверь и дала отмашку остальным Воробьям."

    # #Успех*
    # yn_narrator "Я аккуратно провернула замок, послышался невероятно желанный щелчок."
    # yn_th "Доверие оправданно."
    # yn_dv "Маладца! Горжусь!"
    # yn_narrator "Девушка приоткрыла дверь и дала отмашку остальным Воробьям."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg int_dining_hall_night
    show yn_us normal:
        xpos -240

    show dv normal pioneer2:
        xpos 160

    show yn_haer pity longhair:
        xpos 850

    show yn_kot sad:
        xpos 470

    show yn_slon normal2:
        xpos 1200
    with dissolve
    play ambience yn_fridge_ambient fadein 2
    yn_narrator "Непривычная тишина, которую нарушает только гул работающих холодильников."
    yn_yana "Кстати, забыла спросить. А зачем мы собственно сюда забрались?"
    yn_haer "Это больше Мельпе надо. Хочет свое... это самое... потешить, короче."
    yn_slon "Эго."
    yn_haer "Да, спасибо."
    yn_th "Кажется, ситуация вот-вот накалится до предела. Сначала Кузнечик, теперь Хаер."
    yn_narrator "За тот короткий промежуток времени, что мы находились в столовой, Ульяна уже успела присвоить себе пару банок сгущёнки."
    yn_narrator "Она встала чуть в стороне и теперь внимательно, словно ювелир, рассматривающий драгоценный камень, изучала этикетки."
    show dv angry pioneer2 with dspr
    yn_dv "Ты мне что-то предъявить хочешь?"
    yn_narrator "Алиса уже завелась на на шутку."
    yn_haer "Много чего накопилось. Да. Много."
    yn_narrator "Неожиданно Хаер прищурился и окинул взглядом помещение."
    yn_slon "Дежавю."
    yn_narrator "Прошептал мне Слон."
    yn_dv "Это не я, как ревнивая идиотка караулила у художки, лишь бы этот озабоченный не припёрся к моей ненаглядой!"
    yn_dv "Из-за тебя всё пошло не по плану! Да и план фиговый был на самом деле."
    yn_haer "А другие хочешь сказать не переживают за тех, кто им дорог? Вот ты..."
    show dv rage pioneer2 with dspr
    yn_narrator "Алиса оскалилась."
    yn_dv "Не смей!"
    yn_narrator "Прошипела она."
    yn_narrator "Все безропотно молчали. Наблюдали и не рисковали вмешаться."
    yn_narrator "Даже Кузнечик не торопилась вставить свои пять копеек."
    yn_narrator "Хаер сперва действительно поумерил свой пыл, он был в замешательстве."
    yn_narrator "Но затем всё же собрался и закончил то, что начал."
    yn_haer "Ты тоже чуть не отметелила ту девчонку, когда она полезла к твоему..."
    yn_narrator "Алиса уже казалось, была готова броситься на товарища, когда неожиданно между ними материализовался Слон."
    yn_slon "Оба успокойтесь. Не место здесь разборки устраивать. Предлагаю снова устроить то самое собрание."
    yn_narrator "Алиса прерывисто и тяжело дышала. Она была ужасно зла."
    yn_narrator "Хаер, удивлённый собственной дерзостью, всё же пытался сохранять самообладание."
    yn_dv "Пошли."
    hide dv with dissolve
    yn_narrator "Кротко бросила она и, развернувшись, пошла прочь из столовой."
    hide yn_haer with dissolve
    yn_narrator "Немного замешкавшись, Хаер пошёл следом."
    yn_slon "Чувствую, разговор будет очень жарким."
    yn_narrator "Слон окинул оценивающим взглядом меня, Кузнечика и Кота."

    if yn_sparrows_group_ending < 5:
        yn_slon "Так, ребят, вам лучше не идти. Мельпа злая, Хаер тоже не в духе. Ещё и вам прилетит."
        yn_slon "Я же прослежу, чтобы они там друг друга не поубивали."
        yn_narrator "Кузнечик нахмурилась, но возражать не решилась."
        yn_narrator "Кот же до сих пор находясь под впечатлением от произошедшего и совершенно никак не отреагировал."
        yn_th "Слон прав. Не стоит нам сейчас лезть в их прения. Ему явно виднее."
        yn_yana "Хорошо. Мы тогда подождём снаружи?"
        yn_slon "Да. Так будет лучше, извините."
        yn_yana "Всё в порядке. Удачи тебе там."
        stop ambience fadeout 2
        scene bg black with Dissolve(1)
        $ renpy.pause(2, hard=True)
        $ renpy.block_rollback()
        $ persistent.timeofday = "day"
        $ persistent.sprite_time = "day"
        scene bg yn_int_theatreclub_day with Dissolve(1)
        play ambience ambience_int_cabin_day fadein 2
        play music yn_sad_piano fadein 2
        $ yn_diary_say.page = 2
        $ yn_diary_say("После того вечера с ссорой Хаера и Алисы всё пошло заметно хуже. Боюсь, всё просто ужасно. {w}Слон сказал, что тем же вечером Хаер пересёкся с Ежом и они подрались. {w}Говорит, что скоро Хаера вызовут на Кладбище (к администрации). В Лагере многие шепчутся о новом «покойнике» в рядах Воробьёв.")
        $ yn_diary_say("Сам Хаер ничего внятного не рассказывает. {w}Просто извиняется и говорит, что ему жаль и он не смог сдержаться. {w}Воцарилась атмосфера уныния. Хотелось бы верить, что всё обойдётся.")

    else:
        $ yn_us_ending += 1
        yn_slon "Ладно. Пошли в театральный."
        stop ambience fadeout 2
        scene bg black with Dissolve(1)
        $ renpy.pause(1, hard=True)
        scene bg yn_int_theatreclub_night_smoke
        show yn_us normal:
            xpos -240

        show dv angry pioneer2:
            xpos 160

        show yn_haer pity longhair:
            xpos 850

        show yn_kot sad:
            xpos 470

        show yn_slon normal2:
            xpos 1200
        with Dissolve(1)
        play ambience ambience_int_cabin_night fadein 2
        play music music_list["you_lost_me"] fadein 2
        yn_narrator "Обстановка действительно была жаркая."
        yn_narrator "Воздух уплотнился и табачный дым, всегда сопровождавший ночные посиделки Воробьёв, стал настолько всеобъемлющим, что начал душить."
        yn_narrator "Ребятам хотелось выговориться. Нет, дело явно не в обычной обиде. Тут нечто куда более важное, чем мелкая ссора."
        yn_narrator "И по всей видимости, подобное собрание уже когда-то случалось."
        yn_haer "Что, Мельпа, поговорим по существу?"
        yn_dv "Давай, удиви, патлатый. Скажи, что обо мне думаешь, а я тебе это верну и накину сверху с процентами."
        yn_slon "Хаер, ты только не перегибай или она напихает тебе похлеще, чем досталось Усманову за «Хлопковое дело»."
        yn_dv "Не лезь. Я и до тебя доберусь, если у нас сегодня такой вечер откровений."
        yn_narrator "В ответ Слон только неопределённо развёл руками."
        yn_haer "Ну, хорошо. Держи: самовлюблённая, ци..."
        yn_narrator "Он запнулся, снова забыв нужное слово."
        yn_slon "Циничная."
        yn_haer "Да, спасибо. Самовлюблённая, циничная стерва с недостатком внимания и страхом быть отверженной!"
        yn_dv "По живому режешь, гад? Ладно."
        yn_dv "Неуверенный и зашуганный понторез, оправдывающий свои проколы достоинствами других, который даже не пытается взять себя в руки, а только и продолжающий ныть о том, что он безнадёжный неудачник!"
        yn_slon "Ну, теперь моя очередь. Давай. Добивай."
        yn_dv "Скрытный и скользкий, как мыло в душе тип, которым руководят только изворотливость и инстинкт самосохранения."
        yn_dv "Всё про всех знаешь, а сам раскрыться боишься, хоть и понимаешь, что мы тебя только поддержим."
        yn_slon "Убила. Четырёхпалубник."
        show yn_us dontlike with dspr
        yn_us "О! О! А про меня можно?"
        yn_dv "Сама напросилась! Несамостоятельный застрявший в детстве ребёнок, который пытается казаться взрослым, повторяя за мной."
        yn_dv "Нашла, чтоб тебя, пример для подражания. Курить она решила начать!"
        yn_dv "Запомни, ребёнка от взрослого отличает готовность признавать и исправлять свои ошибки! Ты же этого делать не хочешь!"
        yn_yana "Ну и меня тогда стороной не обходи. Я хоть и рыжая, но не белая ворона."
        yn_dv "Да пожалуйста! Выросшая в богатой семье душная избалованная девчонка. Даже притеревшись, продолжаешь смотреть сверху вниз."
        yn_dv "Ты не можешь принять себя такой, какая ты есть. В своих страхах и сомнениях сидишь, как в скорлупе, даже не пытаясь от туда вылезти и просто банально попросить у кого-то помощи."
        yn_dv "Гордость не позволяет или доверять не умеешь?"
        show yn_kot think with dspr
        yn_narrator "В стороне остался только крайне удивлённый Кот. Смотрит на нас ошарашенно приоткрыв рот, как на идиотов, что решили ни с того ни с сего перемыть друг другу кости."
        yn_haer "А про Кота что скажешь?"
        show yn_haer smile2_longhair with dspr
        yn_narrator "С ухмылкой спросил Хаер, торжествующе смотря на потерявшую запал Алису."
        show dv laugh pioneer2 with dspr
        yn_narrator "Уловив на себе этот взгляд, она приосанилась и, злорадно подмигнув, сказала:"
        yn_dv "Славный малый. Хоть и слишком ведомый из-за своей наивности, но это мы со временем поправим."
        stop music fadeout 7
        yn_narrator "Напряжённая атмосфера быстро рассеялась. Стало понятно, что никто ни на кого зла не держит."
        yn_th "Я ожидала чего-то более... масштабного."
        yn_slon "Все выговорились и услышали то, что хотели?"
        show dv normal pioneer2
        show yn_kot sad
        show yn_us normal
        show yn_haer pity longhair
        with dspr
        yn_narrator "Все неуверенно кивнули всё ещё находясь под впечатлением от случившегося."
        yn_slon "Ну и славно. Давайте примем всё вышесказанное к сведению и постараемся переступить через свои недостатки, чтобы стать лучшими версиями себя. Надеюсь, конфликт исчерпан?"
        yn_haer_and_dv "Вполне."
        show dv smile pioneer2
        show yn_haer smile2_longhair
        with dspr
        yn_narrator "Затем эти двое улыбнувшись друг другу в жест примиренения пожали руки."
        yn_th "А из Алисы бы получился отличный психолог. Отличный агрессивно настроенный психолог. Она говорила прямо и остро, но попала точно в «яблочко»."
        yn_narrator "Немного неприятно, когда тебя выворачивают наизнанку всем на показ, но ведь для того и нужны друзья. Люди, что без утаивания скажут тебе о том, что ты и сам прекрасно знаешь."
        yn_narrator "О том, зудящем и разъедающем изнутри, что ты хочешь закопать поглубже, смириться с этим и сделать вид, что всё в порядке, что всё так и должно быть."
        yn_narrator "Ведь именно друзья делают это не для того, чтобы сделать тебе больно, откапывая то, что ты так тщательно пытался спрятать, а для того, чтобы помочь, ведь ты им не безразличен."
        yn_narrator "Да. Думаю, я теперь понимаю, кем стали для меня Воробьи. Настоящими друзьями."
        scene bg black with Dissolve(1)
        $ renpy.pause(1, hard=True)
        scene bg yn_int_theatreclub_night_smoke
        show dv smile pioneer2 at center
        with Dissolve(1)
        yn_narrator "Алиса предложила мне остаться после собрания, мол хочет поговорить. Я согласилась."
        yn_narrator "И вот, мы сидим за столом в молчании. Спустя какое-то время, она достаёт подаренные Marlboro и закуривает."
        yn_yana "Мы кого-то ждём?"
        yn_dv "Так точно! Сейчас Слон с заказом прийти должен."
        yn_yana "Заказом?"
        yn_narrator "Алиса сперва долго затягивается, медленно, с наслаждением выпускает дым и только тогда кивает."
        yn_dv "Да. С заказом."
        yn_th "Понятно. Дальше можно не расспрашивать. Лучше просто дождаться Слона."
        show yn_slon normal at fright with dissolve
        yn_narrator "Он пришёл через несколько минут, пряча что-то большое под рубашкой."
        yn_dv "Тебя только за смертью посылать."
        yn_slon "Там Павлины везде шкандыбали. Кое-как незамеченным проскочил."
        yn_dv "Ну да. Тебя сложно не заметить. Ладно. Доставай уж."
        hide dv with dissolve
        yn_narrator "Алиса уходит к шкафчику, где хранился реквизит, а Слон достаёт из-под рубашки бутылку вина с выпирающей пробкой."
        yn_th "Они серьёзно? Вино?!"
        show dv normal pioneer2 at center with dissolve
        yn_narrator "Мельпа вернулась и поставила на стол два фужера."
        yn_yana "Вы собираетесь пить?"
        yn_th "Нет, конечно, я понимаю, что второй бокал для меня, но всё же пытаюсь хотя бы чуть-чуть отойти от этого."
        show yn_slon normal2 with dspr
        yn_narrator "Слон скривился."
        yn_slon "Я это пить не буду {yn_tip_tag=covrig}ни за какие коврижки.{/yn_tip_tag}"
        yn_dv "Это для нас. Чтобы разговор мягче шёл."
        yn_yana "А это обязательно?"
        yn_dv "Да."
        yn_th "Ладно. От половины бокала ничего страшного не случится. К тому же, за семейными застольями мне уже доводилось пару раз пробовать сей напиток."
        yn_narrator "Впервые я выпила вино на юбилей дедушки по его настоянию, мол за здоровье. Он аргументировал это тем, что раз уж у меня есть рот, значит можно."
        yn_yana "Эх, если только половину бокала."
        show dv smile pioneer2 with dspr
        yn_narrator "Алиса улыбнулась и добродушно пожала плечами."
        yn_narrator "Ей понравилось, что я не стала жеманничать."
        yn_dv "Хорошо."
        yn_slon "Когда судьба наливает, ты выпиваешь до дна."
        yn_narrator "Сказал Слон, открывая бутылку. Раздался характерный хлопок."
        yn_dv "Не паясничай или с нами сейчас пить будешь."
        yn_slon "Понял. Пойду, закрою дверь с той стороны. Хорошего вечера."
        hide yn_slon with dissolve
        yn_narrator "Слон ушёл, а Мельпа разлила вино по фужерам."
        scene bg yn_dv_thinking_smoke with fade
        play music music_list["waltz_of_doubts"] fadein 10
        yn_dv "Знаешь, давно уже думала поговорить с кем-нибудь об этом чтобы душу отвести, да не с кем было."
        yn_narrator "С бокалом в руке Алиса выглядит довольно кокетливо, хоть и взгляд её излучает глубокую задумчивость."
        yn_yana "Дай угадаю. Разговор пойдёт про любовь?"
        scene bg yn_dv_smiling_smoke with dissolve
        yn_narrator "Алиса улыбается."
        yn_dv "Я же говорила, что ты довольно проницательная."
        yn_dv "Вот смотрю я на тупые попытки Хаера ухаживать за Красавицей и понимаю, что он делает не так, но вот помочь с этим не могу. Никак."
        yn_dv "Тошно только от одной мысли становится. Хорошо, что ты тут преуспела. Спасибо."
        yn_yana "А как давно вы знакомы с Хаером?"
        yn_dv "С самого детства. Он в деревне у бабушки жил до тринадцати лет, а я туда на лето с родителями каждый год приезжала. Так и сдружились."
        yn_dv "Даже семьи наши потом дружбу водить начали. Отцы сработались, так сказать..."
        yn_narrator "Мельпа осеклась. Окинула меня внимательным взглядом, а затем, решившись, продолжила."
        yn_dv "Мой раньше военным лётчиком был, а сейчас на таможне работает. Отец Хаера же фарцой занимается."
        yn_th "Так вот откуда у этих обоих дефицитные вещи."
        yn_narrator "Я тоже сделала глоток из своего бокала. Вино оказалось кислым и не особо вкусным."
        yn_dv "Да. Знаю, что кислятина, но другого тут не достанешь. Пить вообще дело сложное. Если бы было иначе, то все бы пили беспробудно."
        yn_yana "А где вы его взяли?"
        yn_dv "От туда же, откуда его брал Физрук. Из деревни, что неподалёку."
        scene bg yn_dv_thinking_smoke with dissolve
        yn_yana "Слушай, а что у тебя такого случилось, что тебя воротит от любви?"
        yn_narrator "Алиса сделала большой глоток вина. Потянулась к пачке сигарет. Закурила."
        yn_dv "Один мудак год назад сломал мне эту красивую картинку, что вы называете любовью. Ваней его зовут. Из моего города."
        yn_dv "Водил в кино, читал стихи, дарил цветы, клялся в любви. А я, дура, повелась. Втюрилась в него по уши."
        yn_dv "Вот можешь меня представить влюблённой? Даже самой не верится."
        yn_narrator "Алиса замолчала. Огонёк её сигареты алеет в полумраке."
        yn_dv "Через два месяца он посмеялся мне прямо в лицо и бросил. Оказалось, это он на спор всё это делал."
        yn_dv "Типа, ему не слабо даже такой, как я голову вскружить. С кривым носом он теперь, правда, не такой симпатичный, как раньше."
        yn_dv "Понимаю, что это всё тупо. Наивная подростковая влюблённость. Но что-то во мне сломалось. Просто плевать стало почти на всё."
        yn_narrator "Она снова замолчала. Выпила. Потушила тлеющую сигарету, которой так ни разу и не затянулась."
        yn_narrator "Вот она. Гордая, несгибаемая и... одинокая."
        yn_narrator "Словно, забытая в музейной коллекции потрескавшаяся мраморная статуя прекрасной музы. В глазах плещется печаль, а слова полны смеха."
        yn_dv "Вот послушала от Хаера, сама тебе выговорилась и как-то легче стало. А ты когда-нибудь любила?"
        yn_yana "Наверное, скорее да, чем нет."
        yn_dv "И как оно?"
        yn_yana "Там всё сложно было. Я бы даже сказала: ненормально. Но это было давно и не правда."
        scene bg yn_dv_smiling_smoke with dissolve
        yn_narrator "Сейчас это кислое вино показалось самым вкусным напитком на земле. Театральный кружок стал очень уютным. От резких движений немного шла кругом голова."
        yn_narrator "Алиса снова заулыбалась."
        yn_th "Сегодня она явно побила рекорд по искренним улыбкам. Я то думала, что Мельпа искренне улыбается только тогда, когда кто-то умудряется провалиться в уличный туалет или по глупости потерять что-то ценное."
        yn_dv "Ого. Что же там такое было?"
        yn_yana "Позволь мне немного побыть Слоном?"
        yn_dv "В смысле?"
        yn_yana "Это маленький се-крет."
        stop music fadeout 2
        stop ambience fadeout 2
        scene bg black with Dissolve(2)
        $ renpy.block_rollback()
        $ renpy.pause(2, hard=True)
        $ persistent.timeofday = "day"
        $ persistent.sprite_time = "day"
        scene bg yn_int_theatreclub_day with Dissolve(2)
        play ambience ambience_int_cabin_day fadein 2
        play music music_list["memories"] fadein 5
        $ yn_diary_say.page = 2
        $ yn_diary_say("После того собрания в театральном Воробьи заметно переменились. {w}Мельпа стала более сдержанной. {w}Её подколки теперь звучат куда более мягко да и реже. {w}Она даже перестала грубить Медузе во время репетиций.")
        $ yn_diary_say("Наш разговор открыл её для меня совершенно с другой стороны и заметно сблизил, что уж говорить. {w}Никогда бы не подумала, что она человек столь тонкой душевной организации. {w}Не такая я и проницательная на самом деле.")
        $ yn_diary_say("Кузнечик перестала устраивать концерты по любому поводу. Детская непосредственность сменилась задумчивостью. Забавно, конечно, но она даже пошла в библиотеку и взяла «Преступление и наказание» (у Жени, наверное, глаза на лоб полезли).")
        $ yn_diary_say("Сказала, что хочет прочитать оригинал и надеется, что там роль, которая ей досталась расписана куда больше и лучше. Я не стала её расстраивать.")
        $ yn_diary_say("Слон рассказал о своей семье. У них там целая династия военных, а он получился пятой колонной. {w}Как Слон шутил, в его военном билете написано не «не годен», а «годен до». Ещё он показал несколько своих тайников.")
        $ yn_diary_say("Никогда не думала, что подобное сможет меня удивить, но они были спрятаны так хорошо и незаметно, что даже стой ты прямо перед этим схроном ни за что не догадаешься о его существовании, если тебе не скажут.")
        $ yn_diary_say("Хаер всё же записался в художественный кружок. Теперь он не просто навязчиво приходит туда донимая Красавицу, а учится рисовать. Да и сама Красавица как-то оттаяла. Стала больше улыбаться, особенно рядом с Хаером и говорит теперь менее односложно.")
        $ yn_diary_say("На Ежа просто перестали обращать внимание. Скоро выйдет газета Журналистки и он окончательно отстанет.")
        $ yn_diary_say("А ещё мой потлатый товарищ перестал забывать слова. Слон говорит, что такого никогда раньше не случалось. А Кот... Ну, теперь Кот всем говорит, что он славный парень.")
        $ yn_diary_say("Что же касается меня... Стало заметно легче. Все те озарения, что случались со мной на протяжении всей Лагерной смены и вечер откровений окончательно сложились в единый пазл. {w}Мой. {w}Личный. {w}Мрачное будущее уже не кажется таким страшным. Туман со временем осядет. Нужно просто не бояться в него всматриваться и идти вперёд.")

    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with Dissolve(2)
    jump yn_act3_scene9
