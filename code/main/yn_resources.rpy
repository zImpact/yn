init python:
    import time
    from os import path

    for file_name in renpy.list_files():
        if 'yana' in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith('yana/images/bg/'):
                if file_name.endswith('.ogv'):
                    renpy.image('bg ' + file_path, Movie(fps=45, play=file_name))

                else:
                    renpy.image('bg ' + file_path, file_name)

            elif file_name.startswith('yana/images/gui/'):
                renpy.image(file_path, file_name)

            elif file_name.startswith('yana/images/sprites/'):
                renpy.image(file_path, ConditionSwitch('persistent.sprite_time=="sunset"', im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), 'persistent.sprite_time=="night"', im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith('yana/sounds/'):
                globals()[file_path] = file_name

    yn_std_set_for_preview = {}
    yn_std_set = {}
    store.yn_colors = {}
    store.yn_names = {}
    store.yn_names_list = []
    yn_speaker_color = 'speaker_color'

    store.yn_names_list.append('yn_narrator')

    store.yn_names_list.append('yn_th')

    yn_colors['yn_yana'] = {'speaker_color': 'ff852a'}
    yn_names['yn_yana'] = 'Яна'
    store.yn_names_list.append('yn_yana')

    yn_colors['yn_mom'] = {'speaker_color': '#FFC0CB'} 
    yn_names['yn_mom'] = 'Мама'
    store.yn_names_list.append('yn_mom')

    yn_colors['yn_dad'] = {'speaker_color': '#CD5C5C'}
    yn_names['yn_dad'] = 'Папа'
    store.yn_names_list.append('yn_dad')

    yn_colors['yn_mi'] = {'speaker_color': '#00b4cf'}
    yn_names['yn_mi'] = 'Циановая'
    store.yn_names_list.append('yn_mi')

    yn_colors['yn_cs'] = {'speaker_color': '#8686e6'}
    yn_names['yn_cs'] = 'Медработник'
    store.yn_names_list.append('yn_cs')

    yn_colors['yn_mz'] = {'speaker_color': '#4a86ff'}
    yn_names['yn_mz'] = 'Женя'
    store.yn_names_list.append('yn_mz')

    yn_colors['yn_sl'] = {'speaker_color': '#ffd200'}
    yn_names['yn_sl'] = 'Блондинка'
    store.yn_names_list.append('yn_sl')

    yn_colors['yn_mt'] = {'speaker_color': '#00ea32'}
    yn_names['yn_mt'] = 'Ольга'
    store.yn_names_list.append('yn_mt')

    yn_colors['yn_us'] = {'speaker_color': '#ff3200'}
    yn_names['yn_us'] = 'Девчушка'
    store.yn_names_list.append('yn_us')

    yn_colors['yn_haer'] = {'speaker_color': '#004979'}
    yn_names['yn_haer'] = 'Хаер'
    store.yn_names_list.append('yn_haer')

    yn_colors['yn_kot'] = {'speaker_color': '#efbf88'}
    yn_names['yn_kot'] = 'Кот'
    store.yn_names_list.append('yn_kot')

    yn_colors['yn_kras'] = {'speaker_color': '#b4151a'}
    yn_names['yn_kras'] = 'Красавица'
    store.yn_names_list.append('yn_kras')

    yn_colors['yn_slon'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon'] = 'Полноватый'
    store.yn_names_list.append('yn_slon')

    yn_colors['yn_slon_willpower'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_willpower'] = 'Сила воли'
    store.yn_names_list.append('yn_slon_willpower')

    yn_colors['yn_slon_laziness'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_laziness'] = 'Лень'
    store.yn_names_list.append('yn_slon_laziness')

    yn_colors['yn_slon_irritability'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_irritability'] = 'Раздражительность'
    store.yn_names_list.append('yn_slon_irritability')

    yn_colors['yn_slon_unrest'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_unrest'] = 'Переживания'
    store.yn_names_list.append('yn_slon_unrest')

    yn_colors['yn_slon_friendliness'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_friendliness'] = 'Дружелюбие'
    store.yn_names_list.append('yn_slon_friendliness')

    yn_colors['yn_slon_instincts'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_instincts'] = 'Инстинкты'
    store.yn_names_list.append('yn_slon_instincts')

    yn_colors['yn_slon_spontaneity'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_spontaneity'] = 'Спонтанность'
    store.yn_names_list.append('yn_slon_spontaneity')

    yn_colors['yn_slon_observations'] = {'speaker_color': '#2f2f2f'}
    yn_names['yn_slon_observations'] = 'Наблюдения'
    store.yn_names_list.append('yn_slon_observations')

    yn_colors['yn_sh'] = {'speaker_color': '#fff226'}
    yn_names['yn_sh'] = 'Шурик'
    store.yn_names_list.append('yn_sh')

    yn_colors['yn_el'] = {'speaker_color': '#fff226'}
    yn_names['yn_el'] = 'Шурик'
    store.yn_names_list.append('yn_el')

    yn_colors['yn_erika'] = {'speaker_color': '#efe2d9'}
    yn_names['yn_erika'] = 'Светловолосая'
    store.yn_names_list.append('yn_erika')

    yn_colors['yn_un'] = {'speaker_color': '#aa64d9'}
    yn_names['yn_un'] = 'Лена'
    store.yn_names_list.append('yn_un')

    yn_colors['yn_dv'] = {'speaker_color': '#ffaa00'}
    yn_names['yn_dv'] = 'Алиса'
    store.yn_names_list.append('yn_dv')

    yn_colors['yn_jurn'] = {'speaker_color': '#45933f'}
    yn_names['yn_jurn'] = 'Девушка в берете'
    store.yn_names_list.append('yn_jurn')

    yn_colors['yn_san'] = {'speaker_color': '#466d7b'}
    yn_names['yn_san'] = 'Физрук'
    store.yn_names_list.append('yn_san')

    # yn_colors['yn_kris'] = {'speaker_color': '#aa64d9'}
    # yn_names['yn_kris'] = 'Кристина'
    # store.yn_names_list.append('yn_kris')

    yn_colors['yn_wuk'] = {'speaker_color': '#c33736'}
    yn_names['yn_wuk'] = 'Ёж'
    store.yn_names_list.append('yn_wuk')

    yn_colors['yn_skaz'] = {'speaker_color': '#eda593'}
    yn_names['yn_skaz'] = 'Сказочница'
    store.yn_names_list.append('yn_skaz')

    yn_colors['yn_medz'] = {'speaker_color': '#cac894'}
    yn_names['yn_medz'] = 'Медуза'
    store.yn_names_list.append('yn_medz')

    yn_colors['yn_julya'] = {'speaker_color': '#cac894'}
    yn_names['yn_julya'] = 'Жуля'
    store.yn_names_list.append('yn_julya')

    yn_colors['yn_sparrows_g'] = {'speaker_color': '#c9c9c9'}
    yn_names['yn_sparrows_g'] = 'Воробьи'
    store.yn_names_list.append('yn_sparrows_g')

    yn_colors['yn_slon_and_us'] = {'speaker_color': '#c9c9c9'}
    yn_names['yn_slon_and_us'] = 'Слон и Кузнечик'
    store.yn_names_list.append('yn_slon_and_us')

    yn_colors['yn_haer_and_dv'] = {'speaker_color': '#c9c9c9'}
    yn_names['yn_haer_and_dv'] = 'Хаер и Алиса'
    store.yn_names_list.append('yn_haer_and_dv')

    def yn_char_define(character_name, is_nvl = False):
        global DynamicCharacter
        global nvl
        global yn_store
        global yn_speaker_color
        yn_gl = globals()
        
        if character_name == 'yn_narrator':
            if is_nvl:
                yn_gl['yn_narrator'] = Character(None, kind=nvl, what_style='yn_text_style', what_suffix='\n')
            
            else:
                yn_gl['yn_narrator'] = Character(None, what_style='yn_text_style')
            
            return
        
        if character_name == 'yn_th':
            if is_nvl:
                yn_gl['yn_th'] = Character(None, kind=nvl, what_style='yn_text_style', what_prefix='~ ', what_suffix=' ~\n')
            
            else:
                yn_gl['yn_th'] = Character(None, what_style='yn_text_style', what_prefix='~ ', what_suffix=' ~')
            
            return
        
        if is_nvl:
            yn_gl[character_name] = DynamicCharacter('%s_name' % character_name, color=store.yn_colors[character_name][yn_speaker_color], kind=nvl, what_style='yn_text_style', who_suffix=':', what_suffix='\n')
            yn_gl['%s_name' % character_name] = store.yn_names[character_name]
        
        else:
            yn_gl[character_name] = DynamicCharacter('%s_name' % character_name, color=store.yn_colors[character_name][yn_speaker_color], what_style='yn_text_style')
            yn_gl['%s_name' % character_name] = store.yn_names[character_name]

    def yn_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global yn_store
        
        for character_name in store.yn_names_list:
            yn_char_define(character_name)

    def yn_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global yn_narrator
        global yn_th
        yn_narrator_nvl = yn_narrator
        th_nvl = yn_th
        
        global yn_store
        
        for character_name in store.yn_names_list:
            yn_char_define(character_name, True)

    def yn_reload_names():
        global yn_store
        
        for character_name in store.yn_names_list:
            yn_char_define(character_name)

    yn_reload_names()

    def yn_rename_character(character_id, new_name):
        store.yn_names_list.remove(character_id)
        yn_names[character_id] = new_name
        store.yn_names_list.append(character_id)
        yn_reload_names()

    def yn_frame_animation(image_name, frames_quantity, retention, loop, transition, start = 1, **properties):
        anim_args = []
        
        for i in range(start, start + frames_quantity):
            anim_args.append(renpy.display.im.image(image_name + '_' + str(i) + '.png'))
            
            if loop:
                anim_args.append(retention)
                anim_args.append(transition)
        
        return anim.TransitionAnimation(*anim_args, **properties)

    def yn_blink(blink_pause):
        renpy.show('blink')
        renpy.pause(blink_pause, hard=True)

    def yn_unblink(scene_name, unblink_pause):
        renpy.hide('blink')
        renpy.scene()
        renpy.show(scene_name)
        renpy.show('unblink')
        renpy.pause(unblink_pause, hard=True)

    class YnTimingMemorization():
        def __init__(self, channel, fade):
            self.channel = channel
            self.fade = fade            

        def pause(self):
            self.file_name = renpy.music.get_playing(self.channel)
            self.pause_time = renpy.music.get_pos(self.channel)
            renpy.music.stop(self.channel, fadeout = self.fade)

        def resume(self):
            self.resume_params = '<from 0>' + self.file_name if self.pause_time == None else '<from {}>'.format(self.pause_time) + self.file_name
            renpy.music.play(self.resume_params, channel=self.channel, fadein=self.fade)

    def yn_set_main_menu_cursor():
        config.mouse_displayable = MouseDisplayable(yn_gui_path + 'misc/cursor.png', 0, 0)

    yn_set_main_menu_cursor_curried = renpy.curry(yn_set_main_menu_cursor)

    def yn_set_timeofday_cursor():
        global yn_set_timeofday_cursor_var

        if yn_set_timeofday_cursor_var:
            config.mouse_displayable = MouseDisplayable(yn_gui_path + 'dialogue_box/' + persistent.timeofday + '/cursor.png', 0, 0)

    yn_set_timeofday_cursor_curried = renpy.curry(yn_set_timeofday_cursor)

    def yn_set_null_cursor():
        config.mouse_displayable = MouseDisplayable(yn_gui_path + 'misc/yn_none.png', 0, 0)

    yn_set_null_cursor_curried = renpy.curry(yn_set_null_cursor)
        
    def yn_chapter_intro(_save_name, background, ambience, sprite, text, intermedia_phrase=None):
        global save_name

        save_name = _save_name
        renpy.music.play('sound/ambiences/{}.ogg'.format(ambience), 'ambience', fadein=2)
        renpy.show(background, at_list = [yn_chapter_intro_background_moving()])
        renpy.show(sprite, at_list = [yn_chapter_intro_sprite_moving()])
        renpy.show(text, at_list = [yn_chapter_intro_text_pos(text)])

        if intermedia_phrase:
            renpy.show(intermedia_phrase, at_list = [yn_intermedia_phrase_pos(intermedia_phrase)])

        renpy.transition(dissolve)
        renpy.pause(4, hard=True)
        renpy.music.stop('ambience', 2)

    yn_music_list = {
        yn_follow_the_compass_be_near: 'Follow The Compass — Be Near',
        yn_master_of_spirits_failure: 'Master Of Spirits — Failure',
        yn_master_of_spirits_theatreclub_theme: 'Master Of Spirits — Спектакль',
        'sound/music/raindrops.ogg': 'Sergey Eybog — Raindrops',
        'sound/music/get_to_know_me_better.ogg': 'Sergey Eybog — Get To Know Me Better',
        'sound/music/silhouette_in_sunset.ogg': 'Sergey Eybog — Silhouette In Sunset'
    }

    yn_keyboard_help_list = {
        'TAB, LCTRL — пропуск': 200, 
        'H, колесо мыши — скрыть интерфейс': 400,
        'Скроллинг вверх — история': 600
    }

    def yn_chapter_text_pos(text):
        return 1920 - renpy.image_size(yn_gui_path + 'misc/' + text + '.png')[0]

    def yn_predict_screens():
        for screen_name in yn_screens_list:
            renpy.start_predict_screen(screen_name)

    def yn_predict_resources():
        for folder_name in yn_folders_list:
            renpy.start_predict(folder_name)

    def yn_stop_predict_screens():
        for screen_name in yn_screens_list:
            renpy.stop_predict_screen(screen_name)

    def yn_stop_predict_resources():
        for folder_name in yn_folders_list:
            renpy.stop_predict(folder_name)

    def yn_onload(type):
        global yn_lock_quit
        global yn_lock_quick_menu

        if type == 'lock':
            renpy.config.skipping = None
            yn_lock_quit = True
            yn_lock_quick_menu = True
            config.allow_skipping = False

        elif type == 'unlock':
            yn_lock_quit = False
            yn_lock_quick_menu = False
            config.allow_skipping = True

    class YnDustParticles(renpy.Displayable, NoRollback):   
        def __init__(self, particle):
            super(YnDustParticles, self).__init__()
            self.particle = renpy.displayable(particle)           
            self.parts_cache = []
            
            if self.parts_cache:
                self.__init__()
            
            self.max_parts = 125
            self.oldst = None                    
        
        def yn_dust_create_cache(self):     
            self.parts_cache = [self.yn_dust_get_anim() for i in xrange(self.max_parts)]
        
        def yn_dust_get_anim(self):
            part = self.particle
            pos = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
            pos2 = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
            dist = [pos2[0] - pos[0], pos2[1] - pos[1]]
            speed = random.uniform(45, 55)
            alpha = random.uniform(.25, 1.0)
            zoom = random.uniform(.25, .75)
            time = math.sqrt(dist[0] ** 2 + dist[1] ** 2) / speed
            elapsed_time = time
            birth_time = time - random.uniform(.5, 3.5)
            death_time = random.uniform(.5, 3.5)
            current_zoom = .0
            current_alpha = .0
            return [part, pos, pos2, dist, speed, alpha, zoom, time, elapsed_time, birth_time, death_time, current_zoom, current_alpha]      
        
        def yn_dust_visit(self):
            return [i[0] for i in self.parts_cache]
        
        def yn_dust_update(self, st):            
            if self.oldst == None:
                self.oldst = st
            
            self.tick = st - self.oldst
            self.oldst = st     
            
            for part in self.parts_cache:   
                if part[8] <= part[7]:
                    part[8] -= self.tick
                
                else:
                    part[8] = 0
                    self.tick = 0     
                
                if part[8] <= .0:
                    upd_val = self.yn_dust_get_anim()

                    for i in xrange(1, 13):
                        part[i] = upd_val[i]

                try:        
                    path_progress = part[8] / part[7]           
                    xdist_now = part[3][0] * path_progress
                    part[1][0] = part[2][0] - xdist_now
                    
                    ydist_now = part[3][1] * path_progress
                    part[1][1] = part[2][1] - ydist_now
                    
                    alpha_time = part[7] - part[9]
                    alpha_el_time = alpha_time
                    alpha_el_time -= self.tick
                    alpha_progress = alpha_el_time / alpha_time
                    alpha_now = part[5] * (1.0 - alpha_progress)
                    zoom_now = part[6] * (1.0 - alpha_progress)
                    
                    if part[8] >= part[9]:
                        if part[12] < part[5] and part[11] < part[6]:
                            part[12] += alpha_now
                            part[11] += zoom_now
                        
                        elif part[12] > part[5] and part[11] > part[6]:
                            part[12] = part[5]
                            part[11] = part[6]
                    
                    if part[8] <= part[10]:
                        if part[12] > .0 and part[11] > .0:
                            part[12] -= alpha_now
                            part[11] -= zoom_now
                        
                        elif part[12] <= .001 and part[11] <= .001:
                            part[12] = .0
                            part[11] = .0
                
                except ZeroDivisionError:
                    pass
        
        def render(self, width, height, st, at):               
            if not self.parts_cache:
                self.yn_dust_create_cache()
            
            renderObj = renpy.Render(config.screen_width, config.screen_height)
            
            for part in self.parts_cache:
                xpos, ypos = part[1]
                alpha, zoom = part[12], part[11]
                t = Transform(child = part[0], zoom = zoom, alpha = alpha)
                cp_render = renpy.render(t, width, height, st, at)
                renderObj.blit(cp_render, (xpos, ypos))
            
            self.yn_dust_update(st)              
            renpy.redraw(self, 0)
            return renderObj     

init:
    $ yn_titles_text_act_one_good_end = '''{b}КОНЕЦ ПЕРВОГО АКТА{/b}
    Благодарим вас за прочтение первого акта нашей модификации. Второй акт в процессе разработки.


    {b}СОЗДАТЕЛИ{/b}
    Человек, который непонятно зачем всё это придумал\nи написал - Ева Миронова.

    Гений - Андрей Катаев.

    Как же долго мы ждали её рисунки - Рина Анисимова.

    Те, благодаря кому вы видели красивые задники,\nа не пустоту - Александр Герасимов и Лена Тихонова.

    Он сделал многое, но вы этого не оцените - Егор Бобков.

    Он сделал с десяток треков, но подошло только два - Алан Кокоев.

    Ребятки тоже кое-что рисовали - Aizan Drag, Егор Козаченко,
    Максим Сацукевич.


    {b}ТЕСТЕРЫ{/b}
    Родион Егоров - Успешный человек, который первым\n опробовал сей «шедевр».

    Ева Миронова - Да, сценарий мой, но вы бы знали, сколько ошибок было мной найдено!

    Инори Милованова - Третий, кто опробовал сей «шедевр».

    Александр Милютин - красавчик.


    {b}ДОНАТЕРЫ{/b}
    Запрещённая на территории летосферы группировка FJ (500р) - Sorry, but I drank your beer while I was holding.

    Илья Можайкин (200р) - Мы очень быстро ждали и дождались! 

    Максим Миронов (1000р) - Он пришёл безмолвно, только и кинув кошель шекелей на стол.

    Дмитрий Алексеев (50р) - Тоже пришёл безмолвно.

    Януля Савченко (25р) - Не извиняйся)

    Алексей Макаров (426р) - Спасибо за бутылку ликёра. Она очень помогла при написании текста.

    Ваня Коваленко (375р)  - Андрей реально еврей, а хентай пока не намечается :3

    Семён Персунов (20р) - Ну, мод вышел относительно быстро.

    Алексей Хмель (25р) - Смотри выше.

    Владик Хисматуллин (15р) - Я с первого раза смог прочитать твою фамилию.

    Андрей Пупышев (370р) - Двигаем как можем.

    Абдулкадыр Курбанов (50р) - Ну, тут уже не с первого раза.

    Максим Сацукевич (10р) - Зачем ты задонатил, если состоишь в команде? 

    Герман Медведев (38р) - Вот ты и в титрах, бро, как и хотел.

    Александр Милютин (70р) - Блин, а можешь повторить? Тогда точно попробую Крушовицу!

    Инори Милованова (21р) - Тут ты как-нибудь сам.

    Сергей столбов (10р) - Слишком мало ты выделил на юри. 

    Даниэль Маринюк (200р) - Мы всё ещё перспективные и в том же духе!

    Евгений Портов (10р) - Да, мы все заметили, что ты сделал опечатку в слове «коммунизм».


    {b}ОТДЕЛЬНЫЕ БЛАГОДАРНОСТИ{/b}
    Яночке, нашему маскоту, за то, что согласилась взять на себя\n главную роль (правда, мы её и не спрашивали).

    {i}Тебе, дорогой читатель.{/i} Молодец, что не скипнул титры.'''

    $ yn_titles_text_act_one_bad_end = '''{b}КОНЕЦ ПЕРВОГО АКТА{/b}
    Благодарим вас за прочтение первого акта нашей модификации. Второй акт в процессе разработки.


    {b}СОЗДАТЕЛИ{/b}
    Ева Миронова - автор идеи, сценарист.

    Андрей Катаев - программист, дизайнер интерфейсов.

    Рина Анисимова - художник спрайтов и CG.

    Александр Герасимов и Лена Тихонова - художники фонов.

    Егор Бобков - работа над визуальной состовляющей модификации в целом.

    Алан Кокоев - композитор.

    Aizan Drag, Егор Козаченко, Максим Сацукевич - художники.


    {b}ТЕСТЕРЫ{/b}
    Родион Егоров.

    Инори Милованова.

    Александр Милютин


    {b}ДОНАТЕРЫ{/b}
    FJ - 500р. 

    Илья Можайкин - 200р.

    Максим Миронов - 1000р.

    Дмитрий Алексеев - 50р.

    Януля Савченко - 25р.

    Алексей Макаров - 426р.

    Ваня Коваленко - 375р.

    Семён Персунов - 20р.

    Алексей Хмель - 25р.

    Владик Хисматуллин - 15р.

    Андрей Пупышев - 370р.

    Абдулкадыр Курбанов - 50р.

    Максим Сацукевич - 10р.

    Герман Медведев - 38р.

    Александр Милютин - 70р.

    Инори Милованова - 21р.

    Сергей столбов - 10р.

    Даниэль Маринюк - 200р.

    Евгений Портов - 10р.


    {b}ОТДЕЛЬНЫЕ БЛАГОДАРНОСТИ{/b}
    Яне, нашему маскоту, за то, что согласилась взять на себя\n главную роль.

    {i}Тебе, дорогой читатель.{/i} Спасибо, что не скипнул титры.'''

    image yn_titles_final = ParameterizedText(style='yn_titles_style', size=40, xalign=0.5)

    image yn_int_library_sunset_rain = 'yana/images/bg/yn_rain_library/yn_int_library_sunset_rain.png'
    image yn_curtains = 'yana/images/bg/yn_rain_library/yn_curtains.png'
    image yn_forest = 'yana/images/bg/yn_rain_library/yn_forest.png'
    image yn_glass = 'yana/images/bg/yn_rain_library/yn_glass.png'

    image yn_rain_anim:
        'yana/images/bg/yn_rain_library/yn_rain_1.png'
        0.1
        'yana/images/bg/yn_rain_library/yn_rain_2.png'
        0.1
        'yana/images/bg/yn_rain_library/yn_rain_3.png'
        0.1
        repeat

    image bg yn_int_library_sunset_rain_anim:
        contains:
            'yn_forest'
        contains:
            'yn_curtains'
        contains:
            'yn_glass'
        contains:
            'yn_rain_anim'
        contains:
            'yn_int_library_sunset_rain'

    $ yn_tomtits_group = 0 #синицы
    $ yn_sparrows_group = 0 #воробьи
    $ yn_sparrows_group_ending = 0
    $ yn_peacocks_group = 0 #павлины
    $ yn_pigeons_group = 0 #голуби

    $ yn_morality = 0

    $ yn_set_timeofday_cursor_var = False
    $ yn_lock_quit = False
    $ yn_lock_quick_menu = False
    $ yn_lock_quit_game_main_menu_var = True

    $ yn_act_one_play_two_lunch_us_hoax = False
    $ yn_act_one_play_two_library_mz_play_along = False
    $ yn_act_two_totmits_group_song = None
    $ yn_act_two_play_fourth_dv_card_game_win = False
    $ yn_act_two_play_fourth_haer_ask_about_bf = False
    $ yn_act_two_play_fourth_haer_told_about_jurn_newspaper = False
    $ yn_act_two_play_fourth_yn_help_haer = False
    $ yn_act_two_play_fourth_meduza_dialogue_sarcasm_v = False
    $ yn_act_two_play_fourth_dv_disco = False
    $ yn_act_two_play_fifth_yn_help_get_video = False
    $ yn_act_two_play_fifth_slon_dialogue_variants = 0
    $ yn_act_two_play_fifth_slon_dialogue_ask_tomtits_help = False
    $ yn_act_two_play_fifth_slon_dialogue_ask_pigeons_help = False
    $ yn_act_two_play_fifth_yn_ask_jurn_about_newspaper = False
    $ yn_act_two_play_fifth_map_visit_library = False
    $ yn_act_two_play_fifth_get_us_apple = False
    $ yn_act_two_play_fifth_jurn_succes = False
    $ yn_act_two_play_fifth_mz_succes = False
    $ yn_act_two_play_fifth_sh_dialogue_flirt_counter = 1
    $ yn_act_two_play_fifth_video_get_way = None
    $ yn_act_two_play_fifth_video_get = False
    $ yn_act_two_play_sixth_note_fix = False
    $ yn_act_two_play_seventh_wuk_dialogue_question_number = 1
    $ yn_act_two_play_seventh_wuk_compromosing_time_points = 0

    $ yn_haer_good_ending = False
    $ yn_us_ending = 0
    $ yn_dv_good_ending = False
    $ yn_slon_ending = 0

    $ yn_sl_play_two_dialogue_about_library = False
    $ yn_sl_play_two_dialogue_about_yourself = False
    $ yn_sl_play_two_dialogue_about_miku = False
    $ yn_sl_play_two_dialogue_counter = 0

    $ yn_act_one_play_two_bypass_counter = 0

    $ yn_act_one_play_two_bypass_places = {
        'yn_act_one_play_two_bypass_library_completed': False,
        'yn_act_one_play_two_bypass_medic_house_completed': False,
        'yn_act_one_play_two_bypass_radio_engineering_club_completed': False,
        'yn_act_one_play_two_bypass_music_club_completed': False,
        'yn_act_one_play_two_bypass_art_club_completed': False,
        'yn_act_one_play_two_bypass_theatre_club_completed': False  
    }
    
    $ yn_act_one_play_two_bypass_assignment = {
        'yn_act_one_play_two_bypass_library_completed': ['yn_mz_sign', (1708, 585)],
        'yn_act_one_play_two_bypass_medic_house_completed': ['yn_cs_sign', (1718, 616)],
        'yn_act_one_play_two_bypass_radio_engineering_club_completed': ['yn_sh_sign', (1714, 543)],
        'yn_act_one_play_two_bypass_music_club_completed': ['yn_mi_sign', (1724, 568)],
        'yn_act_one_play_two_bypass_art_club_completed': ['yn_kras_sign', (1732, 493)],
        'yn_act_one_play_two_bypass_theatre_club_completed': ['yn_haer_sign', (1723, 516)]
    }

    $ yn_act_one_play_two_amb = YnTimingMemorization('ambience', 1)
    $ yn_act_one_play_two_mus = YnTimingMemorization('music', 2)

    $ yn_us_sepia = Character('Кузнечик', what_style='yn_text_style', ctc='yn_none', ctc_position='fixed', color='#fbd195', what_color='#fbd195')
    $ yn_yana_sepia = Character('Яна', what_style='yn_text_style', ctc='yn_none', ctc_position='fixed', color='#fbd195', what_color='#fbd195')

    $ yn_screens_list = ['yn_main_menu', 'yn_notes_main_menu', 'yn_preferences_main_menu', 'yn_load_main_menu', 'yn_quit_main_menu', 'yn_preferences', 'yn_save', 
        'yn_load', 'yn_say', 'yn_nvl', 'yn_game_menu_selector', 'yn_quit', 'yn_yesno_prompt', 'yn_text_history', 'yn_choice', 'yn_help']

    $ yn_folders_list = ['yana/images/bg*.*', 'yana/images/sprites*.*']

    $ yn_lines_transition = ImageDissolve('yana/images/gui/misc/yn_lines.jpg', 1.0, 8)

    $ yn_timeskip = ImageDissolve('yana/images/gui/misc/yn_timeskip.png', 1.0, ramplen=0, reverse=False, alpha=True)

    image yn_epilogue_intro_text = 'yana/images/gui/misc/yn_epilogue_intro_text.png'

    image yn_dusts = YnDustParticles('yana/images/gui/misc/yn_dust_particle.png')

    image bg yn_table = 'yana/images/mini_games/durak/tb.png'

    image bg yn_ext_square_lenin_night_party_blurred = im.Blur('yana/images/bg/yn_ext_square_lenin_night_party.png', 2)
    image bg yn_ext_square_lenin_day_blurred = im.Blur('yana/images/bg/yn_ext_square_lenin_day.png', 2)
    image bg yn_int_dining_hall_people_sunset_blurred = im.Blur('yana/images/bg/yn_int_dining_hall_people_sunset.png', 2)
    image bg yn_int_theatreclub_day_blurred = im.Blur('yana/images/bg/yn_int_theatreclub_day.png', 2)
    image bg yn_int_yana_room_blurred = im.Blur('yana/images/bg/yn_int_yana_room.png', 1)
    image bg yn_ext_busstop_summer_blurred = im.Blur('yana/images/bg/yn_ext_busstop_summer.png', 2)
    image bg yn_int_dining_hall_people_day_blurred = im.Blur('images/bg/int_dining_hall_people_day.jpg', 2)
    image bg yn_ext_camp_entrance_day_blurred = im.Blur('images/bg/ext_camp_entrance_day.jpg', 2)
    image bg yn_ext_beach_day_blurred = im.Blur('images/bg/ext_beach_day.jpg', 2)
    image bg yn_ext_playground_day_blurred = im.Blur('images/bg/ext_playground_day.jpg', 2)
    image bg yn_ext_beach_sunset_blurred = im.Blur('images/bg/ext_beach_sunset.jpg', 2)
    image bg yn_int_old_building_night_blurred = im.Blur('images/bg/int_old_building_night.jpg', 2)

    image yn_int_old_building_wall = 'yana/images/bg/yn_wall/yn_int_old_building_wall.png'
    image yn_int_old_building_wall_yana_name = 'yana/images/bg/yn_wall/yn_int_old_building_wall_yana_name.png'

    image yn_static_noise_anim = yn_frame_animation('yana/images/bg/yn_static_noise_anim/yn_static_noise', 5, 0.2, True, Dissolve(0.2))
    image yn_interferences_anim = yn_frame_animation('yana/images/bg/yn_interferences_anim/yn_interferences', 3, 0.2, True, Dissolve(0.2))

    if persistent.yn_notes_variables == None:
        $ persistent.yn_notes_variables = {
            'yn_int_yana_room_photo_note': False,
            'yn_ext_bus_station_photo_note': False,
            'yn_int_house_of_yana_photo_note': False,
            'yn_int_theatreclub_photo_note': False,
            'yn_int_artclub_photo_note': False,
            'yn_haer_note': False,
            'yn_kot_note': False,
            'yn_slon_note': False,
            'yn_jurn_note': False,
            'yn_kras_note': False,
            'yn_erika_note': False,
            'yn_tomtits_group_note': False,
            'yn_sparrows_group_note': False,
            'yn_peacocks_group_note': False,
            'yn_pigeons_group_note': False
        }

    $ yn_place_var = None
    $ yn_character_var = None
    $ yn_group_var = None

    $ yn_notes_all = {
        'yn_int_yana_room': ['Комната Яны', 'yn_int_yana_room_photo', 'yn_int_yana_room_photo_text'],
        'yn_ext_bus_station': ['Автобусная\nстанция', 'yn_ext_bus_station_photo', 'yn_ext_bus_station_photo_text'],
        'yn_int_house_of_yana_day_2': ['Домик Яны', 'yn_int_house_of_yana_photo', 'yn_int_house_of_yana_photo_text'],
        'yn_int_theatreclub_day': ['Театральный\nклуб', 'yn_int_theatreclub_photo', 'yn_int_theatreclub_photo_text'],
        'yn_int_artclub_day': ['Художественный\nклуб', 'yn_int_artclub_photo', 'yn_int_artclub_photo_text'],
        'yn_haer': ['Хаер', 'yn_haer_photo', 'yn_haer_photo_text'],
        'yn_kot': ['Кот', 'yn_kot_photo', 'yn_kot_photo_text'],
        'yn_slon': ['Слон', 'yn_slon_photo', 'yn_slon_photo_text'],
        'yn_jurn': ['Журналистка', 'yn_jurn_photo', 'yn_jurn_photo_text'],
        'yn_kras': ['Красавица', 'yn_kras_photo', 'yn_kras_photo_text'],
        'yn_erika': ['Эрика', 'yn_erika_photo', 'yn_erika_photo_text'],
        'yn_tomtits_group': ['Синицы', 'yn_tomtits_group_logo', 'yn_tomtits_group_text', 'yn_tomtits_group_roster'],
        'yn_sparrows_group': ['Воробьи', 'yn_sparrows_group_logo', 'yn_sparrows_group_text', 'yn_sparrows_group_roster'],
        'yn_peacocks_group': ['Павлины', 'yn_peacocks_group_logo', 'yn_peacocks_group_text', None],
        'yn_pigeons_group': ['Голуби', 'yn_pigeons_group_logo', 'yn_pigeons_group_text', 'yn_pigeons_group_roster']
    }

    image bg yn_loading_background:
        contains:
            'bg yn_int_yana_room_night_blurred'
            xalign 0.5 yalign 0.5 zoom 1.0
            pause 2.0
            linear 20 zoom 2.0 xalign 0.5 yalign 0.5

        contains:
            'yn_dusts'
        
        contains:
            'yn_loading_screen_header'
            xpos 770
            ypos 46

        contains:
            'yn_resources_loading'
            xpos 557
            ypos 831

    image bg yn_int_dining_hall_people_sunset_sparrows:
        contains:
            'bg yn_int_dining_hall_people_sunset_blurred_and_zoomed_center'

        contains:
            'yn_erika normal hands_behind'
            xpos 20
            ypos 0

        contains:
            'mz bukal glasses pioneer'
            xpos 460
            ypos 0

        contains:
            'un normal pioneer'
            xpos 870
            ypos 0

    image bg yn_int_dining_hall_people_sunset_tomtits:
        contains:
            'bg yn_int_dining_hall_people_sunset_blurred_and_zoomed_left'

        contains:
            'yn_mi grin'
            xpos 20
            ypos -40

        contains:
            'yn_jurn smirk'
            xpos 500
            ypos -40

        contains:
            'yn_kras normal'
            xpos 900
            ypos -40

    image bg yn_int_dining_hall_people_sunset_pigeons:
        contains:
            'bg yn_int_dining_hall_people_sunset_blurred_and_zoomed_right'

        contains:
            'yn_us grin'
            xpos -300
            ypos 0

        contains:
            'yn_haer normal'
            xpos 514
            ypos 27

        contains:
            'yn_kot normal'
            xpos 140
            ypos 0

        contains:
            'dv grin pioneer2'
            xpos 900
            ypos 0

        contains:
            'yn_slon normal'
            xpos 1230
            ypos 0
            
    transform yn_chapter_intro_background_moving():
        zoom 1.4
        anchor(0.5, 0.5)
        ypos 0.5
        xpos 0.35
        linear 19 xpos 0.7
        
    transform yn_chapter_intro_sprite_moving():
        ypos 0.05
        xpos 0.001
        linear 20 xpos 0.7
        
    transform yn_chapter_intro_text_pos(text):
        xpos yn_chapter_text_pos(text)
        ypos 150

    transform yn_intermedia_phrase_pos(intermedia_phrase):
        xpos yn_chapter_text_pos(intermedia_phrase)
        ypos 600

    transform yn_notes_zoom_rotate():
        xpos 448
        ypos 160
        rotate_pad True
        rotate 0

        on idle:
            parallel:
                easein 0.5 zoom 1.0
                easein 0.5 rotate 0

        on hover:
            parallel:
                easein 0.5 zoom 1.04
                easein 0.5 rotate 10

    transform yn_bus_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat

        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat

    transform yn_moveinbottom():
        linear 0.8 ypos 1300

    transform yn_first_dot_pos():
        xpos 1323
        ypos 931

    transform yn_second_dot_pos():
        xpos 1336
        ypos 931

    transform yn_third_dot_pos():
        xpos 1350
        ypos 931

    transform yn_full_rotate_repeat(l, z, x, y):
        parallel:
            zoom z
            xalign x
            yalign y 
            rotate_pad True
            rotate 0
            linear l rotate 360
            repeat

    transform yn_titles_anim():
        xalign 0.5
        ypos 1.1
        linear 70 ypos -5.3