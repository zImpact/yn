label yn_act2_scene6:
    $ yn_onload("lock")
    $ renpy.block_rollback()
    $ persistent.timeofday = "sunset"
    $ persistent.sprite_time = "sunset"
    $ renpy.pause(3, hard=True)
    $ yn_chapter_intro(
        "Действие шестое.",
        "bg yn_ext_beach_sunset_blurred",
        "lake_shore_evening",
        "yn_yana swim smile",
        "yn_play_sixth_intro_text"
    )
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard=True)
    $ yn_onload("unlock")
    $ yn_set_timeofday_cursor_var = True
    $ persistent.yn_protagonist = "yana"
    # $ yn_rename_character("yn_yana", "Яна")
    scene bg yn_ext_pier_sunset_gl with dissolve
    play ambience ambience_lake_shore_evening fadein 2
    play music yn_giaa_first_day_of_sun fadein 2
    # !голова яны в купальнике
    yn_narrator "День Нептуна - водное мероприятие, которое перекочевало в пионерлагеря от моряков."
    yn_narrator "Во время театрального представления пионеры обливаются водой, а иногда и принудительно отправляют в заплыв своего зазевавшегося товарища."
    yn_narrator "Организацией занималась Сказочница с ребятами из младших отрядов."
    yn_narrator "Она пыталась и нас завербовать в помощники, но после маниакального блеска в глазах Алисы и парочки её «зажигательных» идей, вожатая резко передумала."
    scene bg ext_beach_sunset
    show yn_us smile pirate at center
    with dissolve
    yn_us "Да ладно! Ты сняла свою железяку? Теперь точно нужно искупаться! День Нептуна как никак!"
    yn_yana "Я знала, что как только сниму протез, то вы меня в воду потащите."
    show yn_us supr1 pirate with dspr
    yn_narrator "Ульяна очень ненатурально удивилась."
    yn_us "Никто тебя в воду не кинет! Честное пионерское!"
    yn_yana "Хотелось бы верить, но верится с трудом. Ладно. Проверим насколько ты честная."
    show yn_us smile pirate:
        linear 1.0 xalign -0.3
    $ renpy.pause(1, hard=True)
    show yn_dv pirate normal:
        xalign 0.15
    show yn_slon normal:
        xalign 1.1
    with dissolve
    yn_slon "Не самая лучшая идея доверять Кузнечику."
    yn_dv "А чего это ты, Слоняра, припёрся по форме?"
    yn_slon "Да я..."
    show yn_slon normal2 with dspr
    show yn_san neptun evil:
        xalign 0.6
    with dissolve
    yn_narrator "Вдруг, на его плечо легла поражающая своими размерами ладонь. Это был Физрук в облачении Нептуна."
    yn_san "Жиром трясти, ска, не хочет."
    yn_mt "Александр Ильич, тут же дети! Можете приличнее выражаться?"
    yn_narrator "Вскинув брови и скрестив руки на груди спросила проходящая мимо Панамка."
    yn_san "Да шо вы начинаете? Какие они, ска, дети? Вона, на Слоняру поглядите - кабаняра, ска!"
    yn_th "Она из-за жары такая красная стала или?.."
    show yn_san neptun normal with dspr
    yn_narrator "Заметив накал, Физрук сделал серьёзное лицо."
    yn_san "Всё. Молчу."
    yn_narrator "Недовольно зыркнув, Панамка ещё какое-то время постояла на месте, словно действительно хотела удостовериться, что Физрук больше не говорит."
    yn_narrator "Тот стоически держался."
    yn_narrator "Наконец фыркнув, она направилась к компании ребят, что собирались искупать приятеля против его воли."
    yn_san "Годы идут, а всё такая же, ска, правильная. {w}Ну, не везде..."
    show yn_san neptun smile with dspr
    yn_narrator "Физрук заговорщицки подмигнул."
    yn_us "А вы о чём?"
    show yn_san neptun normal with dspr
    yn_narrator "Александр Ильич сделал вид, что вопрос был адресован не ему."
    show yn_san neptun smile with dspr
    yn_san "Это, Ящерица, у нас тут трёшь-мнёшь возник. Неудобняк, ска."
    yn_san "Ты на меня зла не держи. Я же по факту говорил. Добро?"
    yn_th "Извиняться он не умеет от слова совсем. Зато искренне."
    yn_yana "Всё в порядке. Я понимаю."
    yn_san "Вот и славненько!"
    yn_narrator "Тем временем, на пляж пришёл Хаер и направился к нам. {w}Но стоило ему заметить Физрука, как пионер резко сделал поворот и попытался ретироваться."
    yn_narrator "Александр Ильич даже не оглянулся."
    show yn_san neptun evil with dspr
    yn_san "Хаер! Сто-оять!"
    yn_th "Да как он это делает?"
    yn_narrator "Хаер послушно замер в пол-оборота. Лицо его походило на гримасу приговорённого к смертной казни."
    yn_san "Где то, шо я просил?"
    yn_haer "Я не нашёл..."
    yn_san "Рожай! Шо ты тогда, ска, припёрся? На Красавицу в купальнике позырить пришёл? Нема её тут. Выполняй уговор или я тебя за жабры в воду утащу! Своим лясем-трясем не отделаешься."
    yn_narrator "Это хоть и была угроза, но всё же довольно добродушная по меркам Физрука."
    yn_haer "Так точно!"
    yn_narrator "И исчез, словно его тут никогда и не было."
    yn_yana "А в чём он провинился?"
    yn_san "Та... Нечё спорить. {w}Ишь ты, ска, на слабо меня взять удумал патлатый."
    yn_san "Ладно, молодёжь. Развлекайтесь."
    hide yn_san
    hide yn_slon
    with dissolve
    show yn_dv pirate normal:
        linear 1.0 xalign 0.8
    show yn_us smile pirate:
        linear 1.0 xalign 0.2
    $ renpy.pause(1, hard=True)
    yn_narrator "Слон вместе с Физруком ушли к остальным «актёрам». Ну, точнее к Русалке, которая на удивление была сегодня... {w}Русалкой."
    yn_narrator "Чем та явно была недовольна, судя по её раздражённому виду."
    play sound sfx_draw_water
    yn_narrator "Как и стоило ожидать, Ульяна и честность - вещи несовместимые. Девчушка окатила меня водой из ведра. {w}Теперь от прилипшего песка я вряд ли отделаюсь."
    yn_yana "Кузнечик!"
    show yn_us grin pirate with dspr
    yn_us "А я что? Обещано было в воду тебя не тащить, но про воду к тебе мы не обговаривали. Вы сюда загорать пришли что ли? Пошли купаться!"
    yn_dv "Пас. Если попытаешься меня облить - тебе конец."
    yn_th "А пойду-ка я и правда искупаюсь. До ужина осталось не так много времени. Солнце уже заходит."
    scene bg yn_act2_scene6_swim with dissolve
    yn_narrator "Вода оказалась тёплой."
    yn_narrator "Кругом резвилась ребятня."
    yn_narrator "Они окатывали друг-друга брызгами, звонко смеялись и явно были счастливы."
    yn_narrator "Я всматриваюсь в горизонт."
    yn_narrator "Ровно на границе между водой и небом снова плывёт электричка."
    yn_narrator "Эта закатная {yn_tip_tag=suita}сюита{/yn_tip_tag} рифмуется с пением птиц, гвалтом всеобщего веселья и очень умиротворяет."
    yn_narrator "Раньше мне очень часто казалось, что я вижу себя со стороны, словно наблюдаю за собой из зазеркалья."
    yn_narrator "Когда радовалась или сердилась - это словно делала кто-то другая, а не я."
    yn_narrator "Теперь, смотря в зеркальную гладь воды, я понимаю, что наконец-то перестала видеть себя со стороны."
    yn_narrator "Отражение на своём месте."
    yn_th "{i}Неужели всё взаправду?{/i}"
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard=True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "day"
    $ persistent.sprite_time = "day"
    scene bg yn_int_theatreclub_day
    show yn_us normal:
        xpos -240

    show dv normal pioneer2:
        xpos 160

    show yn_haer pity longhair:
        xpos 850

    show yn_kot normal:
        xpos 470

    show yn_slon normal2:
        xpos 1200
    with Dissolve(2)
    play ambience ambience_int_cabin_day fadein 2
    play music yn_everyday_theme fadein 5
    yn_yana "В смысле, вы подожгли дерево?"
    yn_us "Не подожгли! Оно само загорелось..."
    yn_yana "Скажи мне на милость, как дерево может загореться само?"
    show yn_kot think with dspr
    yn_kot "Ну... Был же один горящий куст..."
    yn_haer "Это к теме не относится."
    yn_narrator "Отрезал Хаер попытки Кота перевести разговор в другое русло."
    yn_dv "Кузнечик, ты когда-нибудь находила свою одежду приклеенной к потолку?"
    yn_us "Нет..."
    yn_dv "А хочешь?"
    show yn_us fear with dspr
    yn_us "Точно нет."
    show yn_us normal with dspr
    yn_dv "Тогда не тяни кота за..."
    yn_narrator "Алиса запнулась. Оценивающе глянула на Кота."
    show yn_kot normal with dspr
    yn_narrator "Он, в свою очередь рефлекторно на всякий случай перекрестился."
    yn_dv "Рассказывайте давайте!"
    yn_kot "Ну, Кузнечик нашла лупу и мы решили поэкспериментировать."
    yn_haer "Нашли? Это где?"
    yn_us "Ну, одолжили в библиотеке..."
    yn_haer "Если Мегера заметит пропажу, то примчится сюда."
    yn_dv "И что дальше?"
    yn_kot "Мы хотели проверить, правда ли с помощью лупы можно что-нибудь поджечь. Оказалось, что можно..."
    yn_yana "Я ума не приложу, каким образом то вы дерево подожгли."
    yn_us "Мы сами без понятия."
    yn_dv "Кто-нибудь вас видел?"
    yn_us "Да нет. Если бы нас заметили, то Панамка с Медузой уже были бы здесь."
    yn_haer "Благо хоть додумались подальше от Лагеря свои эксперименты проводить. Но ладно. Это, вроде, нечет."
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    scene bg ext_houses_day
    show dv normal pioneer2 at center
    with yn_timeskip
    play ambience ambience_camp_center_day fadein 2
    yn_yana "Кажется, у нас проблемы. У нас, в смысле у тебя."
    yn_dv "Что случилось?"
    yn_yana "Откуда у тебя вообще дымовая шашка?"
    show dv smile pioneer2 with dspr
    yn_dv "Ха! Немного «Правды», бутылочка селитры, щепотка любви и огромный талант. Вот и весь секрет."
    yn_yana "Но зачем ты всё это богатство в уборную кинула, когда там один из Голубей был?"
    show dv laugh pioneer2 with dspr
    yn_dv "Он назвал меня дурой необразованной. Я ему и показала свои навыки юного химика."
    yn_dv "Ишь ты, «необразованная». Я ещё взрыв-пакеты им не показывала!"
    yn_yana "Медуза тебя убьёт. Совсем. Насмерть."
    stop ambience fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    scene bg yn_int_theatreclub_day
    show yn_us normal:
        xpos -240

    show dv normal pioneer2:
        xpos 160

    show yn_haer pity longhair:
        xpos 850

    show yn_kot normal:
        xpos 470

    show yn_slon normal2:
        xpos 1200
    with yn_timeskip
    play ambience ambience_int_cabin_day fadein 2
    play music yn_videoplayer_theme fadein 2
    yn_slon "Как и обещал, нарыл кое-что на Ежа! Не малая часть Павлинов его недолюбливает. В основном женская, конечно."
    yn_slon "Короче, Малая где-то нашла очередную «любовную» записку Ежа. К сожалению, разорванную."
    yn_slon "Без понятия, за каким фигом она хранила эти клочки бумаги, но там может оказаться нормальный такой компромат."
    yn_narrator "Алиса смерила Слона разочарованным взглядом и уныло вздохнула."
    yn_dv "Я то думала, ты что-то реальное надыбал, а тут какие-то бесполезные обрывки."
    yn_dv "Сама могу по Лагерю пройтись и собрать несколько таких Ежовых писем. При этом целые."
    yn_haer "Да не гони ты раньше времени. Можно попробовать сложить кусочки. Всё равно ничего не теряем."
    yn_dv "{i}Теряем. {w}Моё. {w}Терпение.{/i}"
    yn_narrator "Процедила она каждое слово сквозь зубы."
    yn_dv "Я могу сделать так, что он даже не поймёт из-за чего у него волосы загорелись. {w}И да, Хаер. Напомню, это и в твоих интересах тоже."
    yn_haer "Да я при любом удачном случае познакомил бы свой кулак с его лицом и устроил им первый поцелуй. Но настучит же. И всё. Пока, Лагерь."
    yn_yana "Может, займёмся этой злосчастной запиской? Попробуем собрать."
    yn_slon "Я притащил клейкую ленту. Можно будет с обратной стороны потом склеить. Если спереди, то с его куриным почерком и мятой бумагой ничего разобрать уже не выйдет. Аккуратно надо."

    menu:
        "Попробовать самой":
            $ yn_sparrows_group_ending += 1
            $ yn_act2_scene6_note_fix = True
            $ yn_slon_ending += 1
            scene bg yn_table with dissolve
            yn_narrator "Я склонилась над столом и принялась кропотливо перекладывать фрагменты записки по столу. Слон помогал."
            yn_narrator "Брал кусочек, разглаживал и приклеивал к нему небольшую полоску скотча."
            call screen yn_note_picking_minigame with Dissolve(0.5)
            show yn_note_full with Dissolve(0.5)
            yn_narrator "Спустя несколько минут, нам всё же удалось собрать полезную улику."
            yn_haer "Ну? Что там? Читай!"
            yn_yana "Дорогуша, я понимаю, что мы в немного разной весовой категории, но ты настолько красива, что я не могу молчать."
            yn_yana "Твои волосы пахнут любовью, а глаза явно видят больше, чем у других. Прошу, Косая, приходи сегодня вечером на причал. Буду ждать."
            hide yn_note_full
            scene bg yn_int_theatreclub_day
            with dissolve
            $ renpy.pause(0.5, hard=True)
            show yn_us normal:
                xpos -240

            show dv normal pioneer2:
                xpos 160

            show yn_haer pity longhair:
                xpos 850

            show yn_kot normal:
                xpos 470

            show yn_slon normal2:
                xpos 1200
            with dissolve
            yn_narrator "Молчание. Всеобщий глубокий вдох."
            yn_dv "Пфф..."
            show dv laugh pioneer2
            show yn_us grin
            show yn_slon smile
            show yn_haer smile2_longhair
            show yn_kot smile
            with dspr
            yn_narrator "Мы одновременно засмеялись протяжным, неумолчным и непрерывным смехом. Хаер вообще хохотал так, словно впал в какой-то припадок."
            yn_narrator "Нам потребовалось много времени, чтобы успокоиться."
            yn_dv "Вот и реальные доказательства, что он шары к Сказочнице катил. Журналистка из этой бумажки сможет такое состряпать..."
            yn_slon "Да, но чтобы закопать Ежа этого будет мало. Все и так знали, что он к ней подкатывал. Нужно что-то ещё."

        "Позволить кому-нибудь другому":
            yn_haer "Давай я попробую собрать."
            yn_dv "Ты и тут накосячить умудришься."
            yn_haer "Не нагнетай."
            yn_narrator "Хаер склонился над столом и принялся кропотливо перекладывать фрагменты записки по столу."
            yn_narrator "Брал один кусочек, разглаживал, приклеивал к нему небольшой полоску скотча и так по кругу. Вот такой странный пазл."
            yn_narrator "Спустя десять минут пионер тихо выругался."
            yn_haer "Тут не хватает двух фра..."
            yn_slon "Фрагментов?"
            yn_haer "Ага. Прям по центру. Нифига не понятно. Прочитать можно только «Твои волосы пахнут любовью»."
            yn_narrator "Молчание. Всеобщий глубокий вдох."
            show dv laugh pioneer2
            show yn_us grin
            show yn_slon smile
            show yn_haer smile2_longhair
            show yn_kot smile
            with dspr
            yn_dv "Пфф..."
            yn_narrator "Мы одновременно засмеялись протяжным, неумолчным и непрерывным смехом. Хаер вообще хохотал так, словно впал в какой-то припадок."
            yn_slon "Это настолько тупо, что гениально."
            yn_dv "Ладно. Всё. Закончили. Записка."
            show dv normal pioneer2
            show yn_us normal
            show yn_slon normal
            show yn_haer pity longhair
            show yn_kot normal
            with dspr
            yn_narrator "Все бросили озабоченные взгляды на стол. Прямо по центру тетрадного листа, где и была написана вся нужная нам информация, зияла большой дыра с рваными краями."
            yn_dv "И где оставшиеся кусочки?"
            yn_slon "Без понятия. Изначально вроде бы всё на месте было."
            yn_haer "Прекрасно. Просто офигенно."
            yn_slon "Ладно. Не парьтесь. Попробую ещё что-нибудь найти."

    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    scene bg ext_houses_day
    show yn_haer pity longhair at center
    with yn_timeskip
    play ambience ambience_camp_center_day fadein 2
    yn_yana "Ты же сам говорил, что хотел извинится перед Лютиком за цветы. Вот она. Лучше возможности уже не представится."
    yn_haer "Ладно-ладно. Твоя правда. Да. Пойду извинюсь. Ну, надеюсь, нечет."
    scene bg yn_ext_square_lenin_day
    show yn_haer pity longhair at left
    show yn_sl serious at right
    with dissolve
    yn_narrator "Хаер свернул на площадь и шаркающей походкой подошёл к скамейке, где по обыкновению отдыхала Славяна."
    yn_narrator "Она смерила его коротким студёным взглядом и показательно приподняла вверх подбородок."
    yn_haer "Лют, я тут извинится хотел. Некрасиво получилось. Я это не подумав. Прости меня, а? Может, я помочь чем могу?"
    show yn_sl normal with dspr
    yn_narrator "Девушка задумалась, оглядывая Воробья с головы до ног."
    yn_sl "Клумбу я уже восстановила, но помочь ты можешь. Готов?"
    yn_haer "Всегда готов!"
    yn_narrator "Карикатурно отсалютовав, сказал он."
    yn_sl "Ну, пошли, Казанова."
    yn_narrator "Она встала с лавочки и пальцем поманила длинноволосого за собой."
    yn_narrator "Хаер бросил на меня вопросительный взгляд, а мне только и оставалось, что неопределённо пожать плечами."
    hide yn_sl
    hide yn_haer
    with dissolve
    yn_narrator "Оставшуюся часть дня Хаеру в добровольно-принудительном порядке пришлось участвовать в чём-то вроде реконструкции времён крепостного права."
    scene bg yn_ext_admins_day
    show yn_haer pity longhair at left
    show yn_sl normal at right
    with fade
    yn_narrator "Сначала он под пристальным надзором Славяны подметал на площади, перед зданием администрации и в «жилых кварталах»."
    scene bg yn_ext_booth_day
    show yn_haer pity longhair at left
    show yn_sl smile2 at right
    with fade
    yn_narrator "Затем убирался на складе и лодочном причале."
    yn_narrator "Комсомолка осталась довольна."
    scene bg yn_ext_square_lenin_day with fade
    yn_narrator "Уже ближе к вечеру, продемонстрировав работу Панамке и получив похвалу за организацию уборочных работ (Хаер тоже без добрых слов в свой адрес не остался), отпустила моего товарища с миром на все четыре стороны."
    yn_narrator "Он потом жуть как ворчал из-за того, что послушал меня и пошёл извинятся."
    stop ambience fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "sunset"
    $ persistent.sprite_time = "sunset"
    scene bg yn_ext_musclub_sunset_video_rain with yn_timeskip
    play ambience yn_rain fadein 2
    play music music_list["dance_of_fireflies"] fadein 2
    yn_narrator "Алиса попросила меня прийти в библиотеку после ужина."
    yn_narrator "Сперва я решила заглянуть в музыкальный клуб, чтобы отдать Мику одолженную на днях заколку. Уже на подходе к зданию клуба начался лёгкий летний дождь."
    yn_narrator "На крыльце я заметила высокую рыжеволосую девушку. Ей оказалась вожатая по прозвищу Жуля."
    yn_narrator "За всё время моего пребывания в Лагере мы сталкивались всего пару раз, но я наслышана о ней, как о отличной художнице. В принципе, это всё, что я о ней знаю."
    show yn_julya normal at center with dissolve
    yn_julya "О! Привет, Ящерица!"
    yn_narrator "С лёгкой улыбкой крикнула она мне."
    yn_julya "Давай сюда, быстрее! Чего мокнешь?"
    scene bg yn_ext_musclub_verandah_sunset_video_rain
    show yn_julya happy at center
    with dissolve
    yn_narrator "Когда я поднялась по ступенькам, её улыбка стала ещё шире."
    yn_yana "Здравствуйте!"
    yn_narrator "Я начала с формальностей, потому что не знала как стоит себя с ней вести. На это она лишь отмахнулась."
    yn_julya "Перестань. Я не Медуза и не такая взрослая, как Панамка. Можешь обращаться на «Ты»."
    yn_yana "Хорошо. Спасибо. Так будет проще."
    yn_julya "Да без проблем. Обращайся!"
    yn_narrator "Она подмигнула."
    yn_julya "А ты тут чего? Тоже к Мику?"
    yn_narrator "Дождь мелкой дробью барабанил по крыше навеса, мелодично сливаюсь с шелестом крон деревьев."
    yn_narrator "Иногда мне кажется, что само это место создаёт вокруг себя музыку."
    yn_yana "Да. Хотела кое-что вернуть. А вы... ты тут зачем?"
    yn_julya "Ну, считай, цели у нас схожи, но альтернативны."
    yn_julya "Хотела у неё гитару одолжить, да вот не ко времени пришла. Закрыто."
    yn_yana "Есть идеи, где она может быть?"
    yn_julya "Вполне. Скорее всего она сейчас в художественном кружке вместе с доброй половиной Голубей. У них там какие-то обсуждения. Я, честно сказать, не вникала."
    yn_yana "А зачем ты тогда пришла сюда, если знаешь, что она в другом месте?"
    yn_julya "Ну... я об этом задумалась только после того как ты спросила."
    yn_narrator "Странно. А зачем Алиса вообще позвала меня в библиотеку? Это же явно как-то связано с тем, что Голуби сейчас в другом месте!"
    yn_yana "Я тогда пойду. Мне ещё кое-куда нужно успеть заскочить."
    show yn_julya normal with dspr
    yn_narrator "Жуля в это мгновение словно бы ушла в себя, не сразу отреагировав на моё прощание."
    yn_julya "А. Да. Бывай! Было приятно пообщаться!"
    stop ambience fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    scene bg yn_int_library_sunset_rain_anim with yn_timeskip
    play ambience ambience_library_day fadein 2
    play sound_loop yn_rain2 fadein 2
    yn_narrator "В библиотеке царило мертвенное молчание, изредка прерываемое шуршанием где-то на переферии."
    yn_yana "Ты здесь?"
    yn_narrator "Из-за книжных стеллажей показалось очень недовольное лицо."
    show dv sad pioneer2 at center with dissolve
    yn_dv "Чего так долго? Тебя только за смертью посылать."
    yn_yana "Дождь застал меня врасплох. Что ты тут вообще делаешь?"
    hide dv with dissolve
    yn_narrator "Рыжая голова исчезла за книжными полками, лишь буркнув:"
    yn_dv "Давай сюда."
    yn_narrator "Я заглянула за книжные полки."
    scene bg yn_int_library_books_dv with dissolve
    yn_narrator "Среди хаоса из разбросанных повсюду книг сидела Алиса и смотрела на меня неправдоподобно невинными для её тона глазами."
    yn_dv "Помоги."
    yn_yana "Я бы помогла, только не могу понять с чем. Раскидать книги? Ты что, заначку здесь оставила?"
    yn_dv "Схватываешь на ходу! В одной из книг лежит... кое-что, что мне сейчас очень нужно. Только я не могу вспомнить в какой именно."
    yn_yana "Ты серьёзно спрятала что-то ценное в логове тех, кто тебя и на пушечный выстрел к себе подпускать не пожелает?"
    yn_dv "Эти полки - самое надёжное место. Голуби на дух не переносят Зощенко. Они никогда в жизни сюда не полезут."
    yn_yana "Всё ещё звучит не очень убедительно. Ты точно меня на пособничество в воровстве не подбиваешь?"
    yn_dv "Расслабься. Я тут заначку уже несколько смен подряд делаю."
    yn_yana "А что искать то?"
    yn_dv "Вообще, я тебя позвала, чтобы ты на шухере постояла. Ребята сейчас другим делом заняты. Просто постой на входе. Если кто-то пойдёт, начни его громко забалтывать."
    scene bg yn_int_library_sunset_rain_anim
    show dv sad pioneer2 at center
    with dissolve
    yn_narrator "Она на мгновение замешкалась, перестав перебирать страницы очередной книги. Подняла на меня пронзительный взгляд и немного стушевавшись сказала:"
    yn_dv "Пожалуйста."
    yn_yana "Ну, если пожалуйста, то конечно. В следующий раз предупреждай на что подбиваешь."
    yn_dv "А так неинтересно."
    stop ambience fadeout 2
    stop music fadeout 2
    stop sound_loop fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)

    if yn_act2_scene5_video_get:
        $ renpy.block_rollback()
        $ persistent.timeofday = "night"
        $ persistent.sprite_time = "night"
        scene bg int_clubs_male2_night
        show yn_us normal:
            xpos -240

        show dv normal pioneer2:
            xpos 160

        show yn_haer smile2_longhair:
            xpos 850

        show yn_kot normal:
            xpos 470

        show yn_slon normal2:
            xpos 1200
        with yn_timeskip
        play ambience ambience_int_cabin_night fadein 2
        play music yn_raw_deal_lamanski_chase_lamanski_syn fadein 2
        yn_haer "Ну и фильмец, конечно. Шварц - шикарен. Боевичок, что доктор прописал!"
        show yn_us laugh with dspr
        yn_us "До сих пор не могу перестать смеяться от этого ломанного русского языка."
        show yn_kot sad2 with dspr
        yn_kot "Мне Кэт жалко."
        show yn_kot angry with dspr
        yn_kot "А этот Рост - гад, конечно. По делам ему!"
        show yn_kot normal with dspr
        yn_kot "Как говорится, нашла коса на камень!"
        yn_haer "Да! Видели, как они его? Ух!"
        yn_narrator "Замахал руками довольный Хаер, пытаясь повторить движения из фильма."
        yn_dv "А мне не понравилось. Лучше другое кинцо глянуть."
        yn_dv "Я тут порылась и нашла занимательную такую кассету. {w}Ток мы женским составом её посмотрим. {w}Без вас, парни."
        yn_dv "Кузнечик, ты тоже извиняй."
        yn_slon "Что это за фильм то такой?"
        yn_narrator "Мельпа повернулась так, чтобы её лицо могла видеть только я и подмигнула, мол «подыграй». Затем выдержав паузу ещё немного, а потом закинув ногу на ногу сказала:"
        show dv smile pioneer2 with dspr
        yn_dv "Эммануэль."
        yn_narrator "Алиса явно играла на Слона, видимо зная или догадываясь, что тот знает, о чём этот фильм."
        yn_th "Да... Нашла я как-то эту кассету под кроватью родителей. Познавательное кино. Ничего не скажешь."
        show yn_slon normal with dspr
        yn_narrator "План Мельпы сработал. На щеках Слона появился румянец и он отвёл взгляд."
        yn_haer "А о чём фильм? Кто снимался? Ван Дамм? Сталлоне?"
        show yn_us upset with dspr
        yn_us "Так не честно! Мы тоже хотим посмотреть!"
        show dv laugh pioneer2 with dspr
        yn_narrator "Алиса лишь ехидно улыбалась, довольная собой."
        yn_slon "Ребят, действительно, пошли. Пусть смотрят."
        yn_slon "Я вам потом всё расскажу. Нечего шуметь."
        show yn_us dontlike with dspr
        yn_us "У-у. Опять всё веселье испортили. Нельзя нам смотреть. Какие важные."
        yn_us "Ну и тухните здесь. Не больно то и хотелось."
        hide yn_us
        hide yn_kot
        hide yn_haer
        hide yn_slon
        with dissolve
        yn_narrator "Ребята медленно вышли из кладовой, стараясь ничего не задеть, попутно присматривая за Кузнечиком, чтобы она {b}нарочно{/b} ничего не задела."
        yn_narrator "Алиса всё так же молчала смотря на меня испытывающим взглядом и с всё той же ехидной улыбкой."
        show dv normal pioneer2 with dspr
        yn_narrator "Затем достала из нагрудного кармана сигареты и закурила. Это только придало ещё большей пикантности ситуации. {w}Становилось неловко."
        yn_narrator "Девушка ожидала моей реакции."
        yn_yana "Ты серьёзно эротику решила посмотреть?"
        yn_dv "Коне..."
        show dv laugh pioneer2 with dspr
        yn_narrator "Она запнулась и надрывно засмеялась, размахивая зажённой сигаретой."
        yn_dv "Прости, не сдержалась. Ты бы видела своё лицо. А морды ребят - вообще."
        yn_dv "Слон, как помидор стал. Я и не сомневалась, что он такое смотрит."
        yn_yana "Шурик же просил здесь не курить."
        show dv normal pioneer2 with dspr
        yn_narrator "Алиса закатила глаза и громко вздохнула. Ей было не по нраву, что я испортила весь момент."
        yn_dv "Забей. {w}Они не заметят. {w}Выветрится. {w}Пошли наших догонять, а то обидятся же."
        show dv laugh pioneer2 with dspr
        yn_narrator "Уже на выходе она легонько толкнула меня в бок. И заулыбалась."
        yn_dv "А оказывается ещё кое-кто у нас смотрит {i}такие{/i} фильмы. {w}Ай, да Ящерица."
        yn_yana "Да я..."
        stop music fadeout 2
        stop ambience fadeout 2

    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    $ renpy.block_rollback()
    $ persistent.timeofday = "day"
    $ persistent.sprite_time = "day"
    scene bg ext_playground_day
    show us angry sport at center
    with yn_timeskip
    play ambience ambience_soccer_play_background fadein 2
    play music yn_proton4_eto_chudesnoe_leto fadein 2
    yn_yana "И долго ты ещё собираешься кидаться на ветряные мельницы?"
    yn_us "Я понять не могу, ты за меня болеть пришла или непонятными фразами кидаться?"
    scene bg yn_ext_playground_us_football with dissolve
    yn_narrator "Пот струится по лицу Ульяны, она тяжело дышит, прижимая к себе футбольный мяч."
    yn_yana "Ну не сможешь ты Физруку забить. Он сам, как все ворота. Там мячу протиснуться некуда."
    yn_us "Я забью! Это дело принципа!"
    yn_yana "Ты уже минут тридцать пытаешься это сделать. Он в последние твои попытки даже не двигался. Мяч ему в грудь или в руку прилетает."
    yn_san "Эй, Кузнечик, у тебя ещё три попытки! Не забьёшь - десять кругов вокруг поля, ска!"
    yn_narrator "Я не смогла сдерживать улыбки, наблюдая за озадаченным лицом девочки."
    yn_us "Чего ты улыбаешься?"
    yn_yana "Тебе и я, и Слон говорили, что не стоит спорить с Физруком. Хаер в прошлый раз после подобного спора отжимался, пока Физрук не устал."
    yn_us "Маловерная ты. Сейчас всё будет. Смотри и записывай. Все потом будут говорить, как я спор у Физрука выиграла!"
    scene bg ext_playground_day with fade
    yn_narrator "А я смотрела и записывала. Как Кузнечик спустя три очевидно провальные попытки уже и так вымотанная и уставшая, наматывала круги вокруг футбольного поля. Под улюлюканье и хлопки Физрука."
    scene bg black with yn_timeskip
    stop ambience fadeout 2
    stop music fadeout 2
    $ renpy.block_rollback()
    $ persistent.timeofday = "night"
    $ persistent.sprite_time = "night"
    $ renpy.pause(1, hard=True)
    scene bg yn_ext_houses_night
    show yn_haer pity longhair at fleft
    show yn_slon normal at center
    show dv normal pioneer2 at fright
    play ambience ambience_camp_center_night fadein 2
    play music music_list["eternal_longing"] fadein 2
    with yn_timeskip
    yn_yana "Вы уверены, что быть соглядатаями хорошая идея?"
    show yn_haer smile2_longhair with dspr
    yn_haer "Не дрейфь, Ящерица. Физрук после отбоя идёт куда-то со звенящим пакетом."
    yn_haer "Тебе самой не интересно?"
    yn_slon "Тише будьте. Услышит же."
    yn_dv "Где он вообще алкашку достал? Неужели, с собой привёз?"
    yn_haer "Да не. Я видел, как он во время дискотеки из Лагеря уходил."
    yn_haer "По-любому в деревню уходил, в хозмаг. {w}Там по слухам из под прилавка водку с вином продают."
    yn_dv "И кому это интересно, он высокоградусный романтический вечер устроить решил?"
    yn_yana "А почему вы Кота с Кузнечиком не позвали?"
    yn_dv "Это им в наказание. Нечего деревья поджигать."
    yn_haer "Ой, какая ты справ..."
    show yn_haer pity longhair with dspr
    yn_narrator "Хаер замолчал. Вновь на его лице отразилось уже знакомое всем замешательство."
    yn_slon "Справедливая?"
    yn_haer "Да! Спасибо. Какая ты справедливая, Мельпа. Может, в угол ещё их поставишь?"
    yn_dv "Во-первых, не нарывайся. Во-вторых, эта острота выглядит нелепой из-за того, что ты забыл слово."
    scene bg yn_ext_house_of_mt_night_san with fade
    yn_narrator "Вдруг Физрук остановился возле домика Панамки. {w}Придерживая предательски выдающий звоном содержимое пакет, он оглянулся."
    yn_narrator "Все мы инстинктивно пригнулись, чтобы не быть замеченными."
    yn_narrator "Из-за резкого движения Хаер начал терять равновесие, чуть не наступив на сухую ветку, но Слон успел ухватить товарища."
    yn_dv "Если она хрустнет, следом такой же звук издаст твой позвоночник."
    yn_narrator "Шёпотом сказала крайне заинтригованная происходящим Алиса."
    yn_narrator "В окнах домика вожатой тем временем подрагивал слабый огонёк. По всей видимости, от свечей."
    yn_narrator "Физрук, убедившись, что в радиусе его видимости никого нет, трижды постучал в дверь."
    scene bg ext_house_of_mt_night
    show yn_haer pity longhair at fleft
    show yn_slon normal at center
    show dv normal pioneer2 at fright
    with fade
    yn_narrator "Спустя пару мгновений она распахнулась и он спешно зашёл внутрь. Послышался щелчок закрывающегося замка."
    yn_dv "Чтоб меня. Журналистка бы удавилась за такой материал."
    show yn_haer smile2_longhair with dspr
    yn_haer "Ну, Саныч, конечно, мужик. Я даже и не подумал бы."
    yn_dv "Да ты вообще редко это делаешь."
    yn_slon "Может пошли уже, пока не услышали чего лишнего? Нам же потом ещё им в глаза смотреть."
    yn_dv "Эх, лучше бы Физрук Медузу захомутал. Может, подобрела бы."
    yn_haer "У Саныча голова на плечах есть, вряд ли бы он добровольно её на каменную сменил."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with yn_timeskip
    $ renpy.pause(1, hard=True)
    scene bg yn_ext_square_lenin_night
    show yn_kras normal at center
    play ambience ambience_camp_center_night fadein 2
    with yn_timeskip
    yn_kras "Как и просили, вот ваш логотип Голубей на простыне."
    hide yn_kras
    show yn_kot laugh at center
    with dissolve
    yn_kot "Дай Бог тебе здоровья!"
    hide yn_kot
    show yn_haer smile2_longhair at center
    with dissolve
    yn_haer "Спасибо! Выглядит супер! Ты молодец!"
    hide yn_haer
    show dv normal pioneer2 at center
    with dissolve
    yn_dv "Даже не спросишь зачем мне это или уже знаешь?"
    hide dv with dissolve
    yn_narrator "Алиса с подозрением покосилась на Хаера, который в это время не сводил взгляда с Красавицы."
    yn_narrator "Прошло какое-то время, а он всё разглядывал пионерку в упор с застывшей улыбкой на тонких бледных губах, размышляя о чём-то своём."
    show yn_kras smile at center with dissolve
    yn_kras "Не знаю. А даже, если и знаю, то знать не хочу. {w}Ладно. Удачи."
    hide yn_kras
    show yn_us grin at center
    with dissolve
    yn_us "Бывай, сестрёнка."
    hide yn_us with dissolve
    yn_narrator "Прозвучало вовсе недружелюбно, а даже с какой-то долей сарказма, но Красавица даже бровью не повела."
    show yn_haer smile2_longhair at center with dissolve
    yn_haer "Пока!"
    hide yn_haer
    show yn_slon normal at center
    with dissolve
    yn_slon "До сих пор не могу поверить, что эту идею предложила Ящерица."
    hide yn_slon
    show dv laugh pioneer2 at center
    with dissolve
    yn_dv "Обвыкаться начала, молодец!"
    yn_yana "Ну, это как бы была просто невинная шутка. {w}Я же не думала, что вы всерьёз решитесь взяться за такое."
    hide dv
    show yn_us laugh at center
    with dissolve
    yn_us "Да ладно тебе! Покажем этим очкарикам!"
    hide yn_us
    show dv normal pioneer2 at center
    with dissolve
    yn_dv "Тише будь. Хаер, помоги флаг снять и тащи сюда новый."
    hide dv with dissolve
    yn_narrator "Алиса и Хаер завозились перед флагштоком. Они о чём-то тихо спорили, но разобрать слов не получалось."
    yn_narrator "Слышался звук рвущийся ткани и металлический скрежет."
    yn_narrator "Спустя пару минут они закончили и принялись за трос поднимать новый, белый флаг."
    scene bg yn_ext_square_lenin_night_pigeons_flag with dissolve
    yn_narrator "Закончив, Алиса отступила назад и задрала голову вверх."
    yn_narrator "На флаге из оборванной простыни красовался аккуратно нарисованный логотип Голубей, который мне уже довелось увидеть в Первом."
    scene bg yn_ext_square_lenin_night_pigeons_flag_zoomed with fade
    #yn_narrator "Чуть ниже уже менее аккуратно была выведена подпись «Всезнайки»."
    yn_dv "Красота-а-а."
    yn_narrator "Нараспев протянула она, явно довольная результатом."
    yn_haer "Будут знать, как на нас гнать."
    yn_yana "Видимо, я одна считаю, что после такого можно не ждать указаний Медузы, где нам могилки рыть, а уже самим приступать."
    yn_slon "Да не. Все, конечно, поймут, что это мы, но доказать никак не смогут."
    yn_dv "Ладно. Валим, пока нас не заметили."
    stop ambience fadeout 2
    scene bg black with Dissolve(1)
    jump yn_act2_scene7
