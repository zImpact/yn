screen yn_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    add "yn_main_menu_picture" xpos 1146 ypos 111

    add "yn_yana_name" xpos 1428 ypos 709

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_start_%s.png"
        xpos 525
        ypos 161
        action [Hide("yn_main_menu", Dissolve(1.5)), yn_set_null_cursor_curried(), SetVariable("yn_lock_quit_game_main_menu_var", False), Start("yn_prologue")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_load_%s.png"
        xpos 525
        ypos 276
        action [Hide("yn_main_menu"), ShowMenu("yn_load_main_menu")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_preferences_%s.png"
        xpos 525
        ypos 394
        action [Hide("yn_main_menu"), ShowMenu("yn_preferences_main_menu")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_notes_%s.png"
        xpos 525
        ypos 509
        action [Hide("yn_main_menu"), ShowMenu("yn_notes_main_menu")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_authors_%s.png"
        xpos 525
        ypos 625
        action [Hide("yn_main_menu"), ShowMenu("yn_authors_main_menu")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_quit_%s.png"
        xpos 525
        ypos 743
        action [Hide("yn_main_menu"), ShowMenu("yn_quit_main_menu")]

screen yn_notes_main_menu():
    tag menu
    modal True
        
    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    add "yn_main_menu_picture" xpos 1146 ypos 111

    add "yn_yana_name" xpos 1428 ypos 709

    text "Заметки":
        size 60
        xalign 0.37
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    textbutton ["Обитатели лагеря"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 182
        action [Hide("yn_notes_main_menu"), ShowMenu("yn_notes_characters_main_menu")]

    textbutton ["Места"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 297
        action [Hide("yn_notes_main_menu"), ShowMenu("yn_notes_places_main_menu")]

    textbutton ["Группы"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 413
        action [Hide("yn_notes_main_menu"), ShowMenu("yn_notes_groups_main_menu")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_main_menu"), ShowMenu("yn_main_menu")]

screen yn_notes_characters_main_menu():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    text "Обитатели лагеря":
        size 60
        xalign 0.338
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    textbutton ["Хаер"]:
        if persistent.yn_haer_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_characters_main_menu"), SetVariable("yn_character_var", "yn_haer"), ShowMenu("yn_notes_choosen_character")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 182

    textbutton ["Кот"]:
        if persistent.yn_kot_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_characters_main_menu"), SetVariable("yn_character_var", "yn_kot"), ShowMenu("yn_notes_choosen_character")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 297

    textbutton ["Слон"]:
        if persistent.yn_slon_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_characters_main_menu"), SetVariable("yn_character_var", "yn_slon"), ShowMenu("yn_notes_choosen_character")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 413

    textbutton ["Журналистка"]:
        if persistent.yn_jurn_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_characters_main_menu"), SetVariable("yn_character_var", "yn_jurn"), ShowMenu("yn_notes_choosen_character")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 527

    textbutton ["Красавица"]:
        if persistent.yn_kras_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_characters_main_menu"), SetVariable("yn_character_var", "yn_kras"), ShowMenu("yn_notes_choosen_character")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 647

    textbutton ["Эрика"]:
        if persistent.yn_erika_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_characters_main_menu"), SetVariable("yn_character_var", "yn_erika"), ShowMenu("yn_notes_choosen_character")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 1100
        ypos 182

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_characters_main_menu"), ShowMenu("yn_notes_main_menu")]

screen yn_notes_choosen_character():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    text yn_notes_all[yn_character_var][0]:
        font yn_main_menu_font
        color "#000000"
        size 60
        xalign 0.36
        ypos 55
        antialias True
        kerning 2

    add yn_notes_all[yn_character_var][1]

    add yn_notes_all[yn_character_var][2]:
        xpos 1106
        ypos 124

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_choosen_character"), SetVariable("yn_character_var", None), ShowMenu("yn_notes_characters_main_menu")]

screen yn_notes_places_main_menu():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    add "yn_main_menu_picture" xpos 1146 ypos 111

    add "yn_yana_name" xpos 1428 ypos 709

    text "Места":
        size 60
        xalign 0.37
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    textbutton ["Комната Яны"]:
        if persistent.yn_int_yana_room_photo_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_places_main_menu"), SetVariable("yn_place_var", "yn_int_yana_room"), ShowMenu("yn_notes_choosen_place")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 182

    textbutton ["Автобусная станция"]:
        if persistent.yn_ext_bus_station_photo_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_places_main_menu"), SetVariable("yn_place_var", "yn_ext_bus_station"), ShowMenu("yn_notes_choosen_place")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 297

    textbutton ["Домик Яны"]:
        if persistent.yn_int_house_of_yana_photo_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_places_main_menu"), SetVariable("yn_place_var", "yn_int_house_of_yana_day_2"), ShowMenu("yn_notes_choosen_place")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 413

    textbutton ["Театральный клуб"]:
        if persistent.yn_int_theatreclub_photo_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_places_main_menu"), SetVariable("yn_place_var", "yn_int_theatreclub_day"), ShowMenu("yn_notes_choosen_place")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 523
        ypos 525

    textbutton ["Художественный клуб"]:
        if persistent.yn_int_artclub_photo_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_places_main_menu"), SetVariable("yn_place_var", "yn_int_artclub_day"), ShowMenu("yn_notes_choosen_place")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 523
        ypos 647

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_places_main_menu"), ShowMenu("yn_notes_main_menu")]

screen yn_notes_image_temp(image_name):
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action [Hide("yn_notes_image_temp", Dissolve(1.5)), ShowMenu("yn_notes_choosen_place")]

    add "bg {}".format(image_name)

screen yn_notes_choosen_place():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    text yn_notes_all[yn_place_var][0]:
        font yn_main_menu_font
        line_spacing -43
        color "#000000"
        size 60
        xalign 0.36
        ypos 55
        antialias True
        kerning 2

    imagebutton at yn_notes_zoom_rotate():
        idle yn_notes_all[yn_place_var][1]
        hover yn_notes_all[yn_place_var][1]
        action [Hide("yn_notes_choosen_place", Dissolve(1.5)), ShowMenu("yn_notes_image_temp", image_name=yn_place_var)]

    add yn_notes_all[yn_place_var][2]:
        xpos 1106
        ypos 124

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_choosen_place"), SetVariable("yn_place_var", None), ShowMenu("yn_notes_places_main_menu")]

screen yn_notes_groups_main_menu():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    add "yn_main_menu_picture" xpos 1146 ypos 111

    add "yn_yana_name" xpos 1428 ypos 709

    text "Группы":
        size 60
        xalign 0.37
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    textbutton ["Синицы"]:
        if persistent.yn_tomtits_group_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_groups_main_menu"), SetVariable("yn_group_var", "yn_tomtits_group"), ShowMenu("yn_notes_choosen_group")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 182

    textbutton ["Воробьи"]:
        if persistent.yn_sparrows_group_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_groups_main_menu"), SetVariable("yn_group_var", "yn_sparrows_group"), ShowMenu("yn_notes_choosen_group")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 297

    textbutton ["Павлины"]:
        if persistent.yn_peacocks_group_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_groups_main_menu"), SetVariable("yn_group_var", "yn_peacocks_group"), ShowMenu("yn_notes_choosen_group")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 413

    textbutton ["Голуби"]:
        if persistent.yn_pigeons_group_note:
            text_style "yn_settings_header_main_menu_preferences"
            action [Hide("yn_notes_groups_main_menu"), SetVariable("yn_group_var", "yn_pigeons_group"), ShowMenu("yn_notes_choosen_group")]

        else:
            text_style "yn_settings_header_main_menu_preferences_locked"
            action NullAction()

        style "yn_button_none"
        text_align 0.5
        xpos 525
        ypos 527

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_groups_main_menu"), ShowMenu("yn_notes_main_menu")]

screen yn_notes_choosen_group():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    text yn_notes_all[yn_group_var][0]:
        font yn_main_menu_font
        color "#000000"
        size 60
        xalign 0.36
        ypos 55
        antialias True
        kerning 2

    add yn_notes_all[yn_group_var][1]:
        xpos 521
        ypos 190

    add yn_notes_all[yn_group_var][2]:
        xpos 1106
        ypos 124

    add yn_notes_all[yn_group_var][3]:
        xpos 490
        ypos 508

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_notes_choosen_group"), SetVariable("yn_group_var", None), ShowMenu("yn_notes_groups_main_menu")]

screen yn_quit_main_menu():
    tag menu
    modal True
    
    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    add "yn_main_menu_picture" xpos 1146 ypos 111

    add "yn_yana_name" xpos 1428 ypos 709
    
    text "Вы действительно \nхотите выйти?":
        size 60
        xalign 0.35
        ypos 207
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2
        line_spacing -2

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_yes_%s.png"
        xpos 550
        ypos 623
        action [Hide("yn_quit_main_menu"), (Function(yn_screens_diact)), ShowMenu("main_menu")]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_no_%s.png"
        xpos 810
        ypos 623
        action [Hide("yn_quit_main_menu"), ShowMenu("yn_main_menu")]

screen yn_authors_main_menu():
    tag menu
    modal True

    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"

    text "Авторы":
        size 60
        xalign 0.37
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    textbutton ["Даниил Бухичевский"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 182
        action OpenURL("https://vk.com/bukhichevsky")

    textbutton ["Андрей Катаев"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 297
        action OpenURL("https://github.com/paych3ck")

    textbutton ["Рина Анисимова"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 413
        action OpenURL("https://vk.com/liffft_art")

    textbutton ["Егор Бобков"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"        
        text_align 0.5
        xpos 525
        ypos 527
        action OpenURL("https://vk.com/id238480098")

    textbutton ["Алан Кокоев"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 525
        ypos 647
        action OpenURL("https://vk.com/my_attic_of_this_mortal_world")

    textbutton ["Александр Герасимов"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"        
        text_align 0.5
        xpos 1100
        ypos 182
        action OpenURL("https://vk.com/kurioni_arts")

    textbutton ["Лена Тихонова"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"        
        text_align 0.5
        xpos 1100
        ypos 297
        action OpenURL("https://vk.com/kagome_art")

    textbutton ["Juria Kraiymer"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 1100
        ypos 413
        action OpenURL("https://vk.com/juriakraiymer")

    textbutton ["Мария Ракшинская"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"        
        text_align 0.5
        xpos 1100
        ypos 527
        action OpenURL("https://vk.com/marie_raksha")

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_zero_impact_logo_%s.png"
        xpos 1311
        ypos 650
        action OpenURL("https://vk.com/zeroimpact")

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_authors_main_menu"), ShowMenu("yn_main_menu")]  
        
screen yn_preferences_main_menu():
    tag menu
    modal True
    
    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"
    
    text "Настройки":
        size 60
        xalign 0.37
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    text "Режим экрана":
        size 55
        xalign 0.37
        ypos 177
        font yn_main_menu_font
        color "#000000"
        
    textbutton ["На весь экран"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 481
        ypos 296
        action Preference("display", "fullscreen")
        
    textbutton ["В окне"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 831
        ypos 296

        if not _preferences.fullscreen:
            text_style "yn_settings_header_main_menu_preferences_inverse"

        else:
            text_style "yn_settings_header_main_menu_preferences"

        action Preference("display", "window")

    text "Размер шрифта":
        size 55
        xpos 1175
        ypos 177
        font yn_main_menu_font
        color "#000000"
            
    textbutton ["Обычный"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 1100
        ypos 296
        action SetField(persistent, "font_size", "small")
            
    textbutton ["Большой"]:
        style "yn_button_none"
        text_style "yn_settings_header_main_menu_preferences"
        text_align 0.5
        xpos 1400
        ypos 296
        action SetField(persistent, "font_size", "large")
            
    text "{font=[yn_main_menu_font]}{color=#000000}Пропускать{/font}{/color}":
        size 55
        xalign 0.37
        ypos 484

    if not _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "yn_button_none"
            text_style "yn_settings_header_main_menu_preferences"
            text_align 0.5
            xpos 485
            ypos 604
            action Preference("skip", "seen")

        textbutton ["Всё"]:
            style "yn_button_none"
            text_style "yn_settings_header_main_menu_preferences"
            text_align 0.5
            xpos 880
            ypos 604
            action Preference("skip", "all")
                        
    if _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "yn_button_none"
            text_style "yn_settings_header_main_menu_preferences"
            text_align 0.5
            xpos 485
            ypos 604
            action Preference("skip", "seen")

        textbutton ["Всё"]:
            style "yn_button_none"
            text_style "yn_settings_header_main_menu_preferences"
            text_align 0.5
            xpos 880
            ypos 604
            action Preference("skip", "all")    
        
    text "Громкость музыки":
        size 55
        xpos 1150
        ypos 484
        font yn_main_menu_font
        color "#000000"

    bar:
        value Preference("music volume")
        right_bar yn_gui_path + "preferences/main_menu/yn_main_menu_bar_null.png"
        left_bar yn_gui_path + "preferences/main_menu/yn_main_menu_bar_full.png"
        thumb "yn_main_menu_thumb"
        xpos 1140
        ypos 613
        xmaximum 400
        ymaximum 85

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_preferences_main_menu"), ShowMenu("yn_main_menu")]  
        
screen yn_load_main_menu():
    tag menu
    modal True
    
    key "K_F1":
        action NullAction()

    add "yn_main_menu_background"
    
    text "Загрузка":
        size 60
        xalign 0.37
        ypos 55
        font yn_main_menu_font
        color "#000000"
        antialias True
        kerning 2

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_load_%s.png"
        xalign 0.285
        ypos 702
        action [(YnFunctionCallback(yn_on_load_callback, selected_slot), FileLoad(selected_slot, confirm = False))]

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_delete_%s.png"
        xalign 0.455
        ypos 702
        action FileDelete(selected_slot, confirm = False)

    imagebutton:
        auto yn_gui_path + "main_menu/buttons/yn_return_%s.png"
        xalign 0.37
        ypos 779
        action [Hide("yn_load_main_menu"), ShowMenu("yn_main_menu")]    
        
    grid 4 3:
        xpos 0.25
        ypos 0.17
        xmaximum 0.596
        ymaximum 0.5
        transpose False
        xfill True
        yfill True

        for slot in range(1, 13):
            fixed:
                add FileScreenshot(slot):
                    size (227, 130)
                    xpos 8
                    ypos 8

                button:
                    action SetVariable("selected_slot", slot)
                    xfill False
                    yfill False
                    style "yn_save_load_button_main_menu"

                    fixed:
                        text (FileTime(slot, format = "%d.%m.%y, %H:%M", empty = "Пусто") + "\n" + FileSaveName(slot)):
                            style "yn_text_save_load_main_menu"
                            xpos 10
                            ypos 10
        
screen yn_preferences():
    tag menu
    modal True
    
    $ yn_bar_null = Frame((yn_gui_path + "preferences/" + persistent.timeofday + "/yn_bar_null.png"), 36, 36)
    $ yn_bar_full = Frame((yn_gui_path + "preferences/" + persistent.timeofday + "/yn_bar_full.png"), 36, 36)

    window background yn_gui_path + "preferences/" + persistent.timeofday + "/preferences_bg.jpg":
        text ["Настройки"]: 
            style "yn_settings_link"
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton ["Назад"]: 
            style "yn_log_button" 
            text_style "yn_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 16 xfill True spacing 15

                text ["Режим экрана"]:
                    style "yn_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Во весь экран"]: 
                            style "yn_log_button"
                            text_style "yn_settings_text_" + persistent.timeofday
                            action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["В окне"]: 
                            style "yn_log_button"
                            text_style "yn_settings_text_" + persistent.timeofday
                            action Preference("display", "window")

                text ["Пропускать"]:
                    style "yn_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Всё"]: 
                            style "yn_log_button" 
                            text_style "yn_settings_text_" + persistent.timeofday
                            action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Виденное ранее"]: 
                            style "yn_log_button" 
                            text_style "yn_settings_text_" + persistent.timeofday
                            action Preference("skip", "seen")

                text ["Громкость"]:
                    style "yn_settings_header_" + persistent.timeofday                   
                    xalign 0.5

                grid 2 1 xfill True:
                    textbutton ["Музыка"]: 
                        style "yn_log_button"
                        text_style "yn_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("music volume")
                        left_bar yn_bar_full 
                        right_bar yn_bar_null 
                        thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                        hover_thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton ["Звуки"]: 
                        style "yn_log_button"
                        text_style "yn_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("sound volume") 
                        left_bar yn_bar_full 
                        right_bar yn_bar_null 
                        thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                        hover_thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton ["Эмбиент"]: 
                        style "yn_log_button"
                        text_style "yn_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("voice volume") 
                        left_bar yn_bar_full 
                        right_bar yn_bar_null 
                        thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                        hover_thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                text ["Скорость текста"]:
                    style "yn_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar: 
                    value Preference("text speed") 
                    left_bar yn_bar_full 
                    right_bar yn_bar_null 
                    thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                    hover_thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text ["Автопереход"]:
                    style "yn_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Включить"]: 
                            style "yn_log_button"
                            text_style "yn_settings_text_" + persistent.timeofday
                            action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Выключить"]: 
                            style "yn_log_button"
                            text_style "yn_settings_text_" + persistent.timeofday
                            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text ["Время автоперехода"]:
                    style "yn_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar: 
                    value Preference("auto-forward time") 
                    left_bar yn_bar_full 
                    right_bar yn_bar_null 
                    thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                    hover_thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text ["Размер шрифта"]:
                    style "yn_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Обычный"]:
                            style "yn_log_button"
                            text_style "yn_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add yn_gui_path + "preferences/" + persistent.timeofday + "/yn_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Крупный"]: 
                            style "yn_log_button"
                            text_style "yn_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "large")

            bar: 
                value XScrollValue("preferences") 
                left_bar "images/misc/none.png" 
                right_bar "images/misc/none.png" 
                thumb "images/misc/none.png" 
                hover_thumb "images/misc/none.png"

            vbar: 
                value YScrollValue("preferences") 
                bottom_bar "images/misc/none.png" 
                top_bar "images/misc/none.png" 
                thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_vthumb.png" 
                thumb_offset -12

screen yn_save():
    tag menu
    modal True
    
    window background yn_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text ["Сохранение"]: 
            style "yn_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton ["Назад"]: 
            style "yn_log_button" 
            text_style "yn_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton ["Сохранить"]: 
            style "yn_log_button" 
            text_style "yn_settings_link"
            yalign 0.92 
            xalign 0.5 
            action (YnFunctionCallback(yn_on_save_callback, selected_slot), FileSave(selected_slot))

        textbutton ["Удалить"]: 
            style "yn_log_button" 
            text_style "yn_settings_link" 
            yalign 0.92 
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True

            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot) xpos 10 ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "yn_save_load_button_" + persistent.timeofday
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(slot)) style "file_picker_text" xpos 15 ypos 15
    
screen yn_load():
    tag menu
    modal True
    
    window background yn_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text ["Загрузка"]: 
            style "yn_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton ["Назад"]: 
            style "yn_log_button" 
            text_style "yn_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton ["Загрузить"]: 
            style "yn_log_button" 
            text_style "yn_settings_link" 
            yalign 0.92 
            xalign 0.5 
            action (YnFunctionCallback(yn_on_load_callback, selected_slot), FileLoad(selected_slot, confirm=False))
        
        textbutton ["Удалить"]: 
            style "yn_log_button" 
            text_style "yn_settings_link"
            yalign 0.92
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True

            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot) xpos 10 ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "yn_save_load_button_" + persistent.timeofday
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(slot)) style "file_picker_text" xpos 15 ypos 15

screen yn_say(what, who):
    window background None id "window":
        # add yn_gui_path + "dialogue_box/" + persistent.timeofday + "/buttons_box.png" xpos 1670 ypos 50

        if persistent.font_size == "large":
            add yn_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png" xpos 304 ypos 866

            add yn_gui_path + "dialogue_box/" + persistent.timeofday + "/side_box_large.png" xpos 52 ypos 866

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/hide_%s.png"
                xpos 1648 
                ypos 883
                action HideInterface()

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/save_%s.png"
                xpos 1707
                ypos 883
                action ShowMenu("yn_save")

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/menu_%s.png"
                xpos 1765
                ypos 883
                action ShowMenu("yn_game_menu_selector")

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/load_%s.png"
                xpos 1822
                ypos 883
                action ShowMenu("yn_load")

            if persistent.timeofday == "sepia":
                add "yn_" + persistent.yn_protagonist + "_emote_" + persistent.yn_protagonist_mood + "_sepia" xpos 72 ypos 871

            else:
                add "yn_" + persistent.yn_protagonist + "_emote_" + persistent.yn_protagonist_mood xpos 72 ypos 871

            text what:
                id "what" 
                xpos 315 
                ypos 907 
                xmaximum 1550 
                size 29
                line_spacing 1

            if who:
                text who:
                    id "who" 
                    xpos 315
                    ypos 873
                    size 35 
                    line_spacing 1

        elif persistent.font_size == "small":
            add yn_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png" xpos 285 ypos 916

            add yn_gui_path + "dialogue_box/" + persistent.timeofday + "/side_box.png" xpos 69 ypos 916

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/hide_%s.png"
                xpos 1629 
                ypos 933
                action HideInterface()

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/save_%s.png"
                xpos 1688
                ypos 933
                action ShowMenu("yn_save")

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/menu_%s.png"
                xpos 1746
                ypos 933 
                action ShowMenu("yn_game_menu_selector")

            imagebutton:
                auto yn_gui_path + "dialogue_box/" +persistent.timeofday + "/load_%s.png"
                xpos 1803
                ypos 933
                action ShowMenu("yn_load")

            if persistent.timeofday == "sepia":
                add "yn_" + persistent.yn_protagonist + "_emote_" + persistent.yn_protagonist_mood + "_sepia":
                    size (121, 137)
                    xpos 83
                    ypos 918

            else:
                add "yn_" + persistent.yn_protagonist + "_emote_" + persistent.yn_protagonist_mood:
                    size (121, 137)
                    xpos 83
                    ypos 918

            text what:
                id "what" 
                xpos 298
                ypos 956
                xmaximum 1541 
                size 24
                line_spacing 2

            if who:
                text who:
                    id "who" 
                    xpos 298
                    ypos 925 
                    size 28 
                    line_spacing 2

screen yn_nvl(items, dialogue):
    window background Frame((yn_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox

        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10

                if persistent.font_size == "large":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 35

                    text what:
                        id what_id 
                        size 32

                elif persistent.font_size == "small":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 30

                    text what:
                        id what_id 
                        size 28
        if items:
            vbox:
                id "menu"

                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"

                    else:
                        text caption style "nvl_dialogue"

screen yn_game_menu_selector():
    tag menu
    modal True

    if yn_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

        add yn_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png" xalign 0.5 yalign 0.5

        # $ yn_current_music = renpy.music.get_playing()

        # if yn_current_music == None:
        #     text "Сейчас ничего не играет"

        # else:
        #     text "Сейчас играет: " + yn_music_list[yn_current_music]

        # imagebutton:
        #     auto yn_gui_path + "quick_menu/" + persistent.timeofday + "/help_%s.png"
        #     xpos 1780
        #     ypos 30
        #     action ShowMenu("yn_keyboard_help")

        imagemap:
            auto yn_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_%s.png" xalign 0.5 yalign 0.5

            hotspot(0, 70, 660, 65) focus_mask None clicked [yn_set_main_menu_cursor_curried(), MainMenu(confirm=False)]

            hotspot(0, 135, 660, 65) focus_mask None clicked ShowMenu("yn_save")

            hotspot(0, 200, 660, 65) focus_mask None clicked ShowMenu("yn_load")

            hotspot(0, 265, 660, 65) focus_mask None clicked ShowMenu("yn_text_history")

            hotspot(0, 330, 660, 65) focus_mask None clicked ShowMenu("yn_preferences")

            hotspot(0, 395, 660, 65) focus_mask None action [(Function(yn_screens_diact)), ShowMenu("main_menu")]

screen yn_keyboard_help():
    tag menu
    modal True

    add yn_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"

    text ["Помощь"]: 
        style "yn_settings_link" 
        xalign 0.5 
        yalign 0.08 
        color "#ffffff"

    viewport id "vp":
        for _text, _ypos in yn_keyboard_help_list.items():
            text _text:
                xpos 200
                ypos _ypos

    textbutton ["Назад"]: 
        style "yn_log_button" 
        text_style "yn_settings_link" 
        xalign 0.015 
        yalign 0.92 
        action Return()

screen yn_quit():
    tag menu
    modal True
    
    if yn_lock_quit:
        timer 0.01 action Return()

    elif yn_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm = False)

    else:
        add yn_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
            
        text "Вы действительно \nхотите выйти?":
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            font yn_link_font
            antialias True
            kerning 2
            
        textbutton ["Да"]:
            style "yn_settings_header_main_menu_quit"
            text_style "yn_settings_header_main_menu_quit"
            xpos 493
            ypos 600
            action [(Function(yn_screens_diact)), ShowMenu("main_menu")]
            
        textbutton ["Нет"]:
            style "yn_settings_header_main_menu_quit"
            text_style "yn_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [Hide("yn_quit"), Return()]

screen yn_yesno_prompt(yes_action, message, no_action):
    modal True

    add yn_gui_path + "yes_no/" + persistent.timeofday + "/yes_no.png"

    text _(message): 
        text_align 0.5 
        yalign 0.46 
        xalign 0.5

        if persistent.timeofday == "day":
            color "#64483c"

        elif persistent.timeofday == "night":
            color "#161d3d"

        elif persistent.timeofday == "sepia":
            color "#000000"

        elif persistent.timeofday == "sunset":
            color "#5a3525"

        font yn_header_font 
        size 30

    textbutton ["Да"]: 
        text_size 60 
        style "yn_log_button" 
        text_style "yn_settings_link" 
        yalign 0.65 
        xalign 0.3 
        action yes_action

    textbutton ["Нет"]: 
        text_size 60 
        style "yn_log_button" 
        text_style "yn_settings_link" 
        yalign 0.65 
        xalign 0.7 
        action no_action

screen yn_text_history():
    tag menu

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "small":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "large":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(yn_gui_path + "choice/" + persistent.timeofday + "/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "yn_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size

                        if "color" in h.who_args:
                            color h.who_args["color"]
                            
                textbutton h.what:
                    text_size history_text_size
                    style "yn_log_button" 
                    text_style "yn_text_history" 
                    xpos 100                    
                    xmaximum xmax
                    text_color "#ffdd7d"

                    if persistent.timeofday == "day":
                        text_hover_color "#40e138"

                    elif persistent.timeofday == "night":
                        text_hover_color "#008193"

                    elif persistent.timeofday == "sepia":
                        text_hover_color "#b7a492"

                    elif persistent.timeofday == "sunset":
                        text_hover_color "#636840"
                    
                    action RollbackToIdentifier(h.rollback_identifier)
        
        vbar value YScrollValue("yn_text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb yn_gui_path + "preferences/" + persistent.timeofday + "/yn_vthumb.png" xoffset 1700  

screen yn_choice(items):
    modal True
    
    $ yn_choice_colors_hover = {                        
        "day": "#9dcd55",
        "night": "#3ccfa2",
        "sunset": "#dcd168"
    }

    $ yn_choice_colors = {
        "day": "#466123",
        "night": "#145644",
        "sunset": "#69652f"
    }

    $ yn_choice_colors_selected = {                        
        "day": "#2a3b15",
        "night": "#0b3027",
        "sunset": "#42401e"
    }

    window background Frame(get_image("gui/choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:

                button background None:
                    xalign 0.5
                    action action

                    if persistent.licensed:
                        if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right" and caption != "Ir a la izquierda" and caption != "Ir a la derecha":
                            text caption font header_font size 37 hover_size 37 color yn_choice_colors_selected[persistent.timeofday] hover_color yn_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5
                            
                        else:
                            text caption font header_font size 37 hover_size 37 color yn_choice_colors[persistent.timeofday] hover_color yn_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                    else:
                        text caption font header_font size 37 hover_size 37 color yn_choice_colors[persistent.timeofday] hover_color yn_choice_colors_hover[persistent.timeofday] xalign 0.5
            else:
                if persistent.licensed:
                    text caption font header_font size 60 color yn_choice_colors[persistent.timeofday] text_align 0.5 xcenter 0.5

                else:
                    text caption font header_font size 40 color yn_choice_colors[persistent.timeofday] xalign 0.5 text_align 0.5 xcenter 0.5

screen yn_help():
    tag menu
    modal True

    add yn_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
    
    text "Информация":
        size 70
        xalign 0.5
        ypos 33
        font yn_link_font
        antialias True
        kerning 2
            
    textbutton ["Группа VK"]:
        style "yn_log_button" 
        text_style "yn_settings_header_main_menu_quit"
        xalign 0.5
        ypos 350
        action OpenURL("https://vk.com/public176281709")
            
    textbutton ["Бессонница"]:
        style "yn_log_button" 
        text_style "yn_settings_header_main_menu_quit"
        xalign 0.5
        ypos 500
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2343598706")

    textbutton ["Дни нигде"]:
        style "yn_log_button" 
        text_style "yn_settings_header_main_menu_quit"
        xalign 0.5
        ypos 500

    textbutton ["Один украденный день"]:
        style "yn_log_button" 
        text_style "yn_settings_header_main_menu_quit"
        xalign 0.5
        ypos 500
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=1746278653")

    textbutton ["Всех не спасти"]:
        style "yn_log_button" 
        text_style "yn_settings_header_main_menu_quit"
        xalign 0.5
        ypos 500
            
    textbutton ["Петля времени"]:
        style "yn_log_button" 
        text_style "yn_settings_header_main_menu_quit"
        xalign 0.5
        ypos 650
        action OpenURL("https://youtu.be/x2KBAuBKWL8")        
            
    imagebutton:
        idle yn_gui_path + "logowhite_hover.png"
        hover yn_gui_path + "logowhite_hover.png"
        xpos 1520
        ypos 890
        action NullAction()

    textbutton ["Назад"]: 
        style "yn_log_button" 
        text_style "yn_settings_link" 
        xalign 0.015 
        yalign 0.92 
        action Return()

screen yn_interface_info():
    tag menu
    modal True

    add yn_gui_path + "misc/yn_interface_tip.png"

    textbutton ["продолжить..."]:
        style "yn_dw_info_text_style"
        text_style "yn_dw_info_text_style"
        xalign 0.5
        ypos 855
        action [Hide("yn_interface_info", Dissolve(0.5)), Return()]
