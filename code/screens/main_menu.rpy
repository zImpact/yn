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
