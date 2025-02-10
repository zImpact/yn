init python:
    mods['yn_start'] = u'{font=yn/images/gui/fonts/ljk_streamster.otf}{size=70} Яна{/font}{/size}'

    try:
        modsImages['yn_start'] = ('yn/images/gui/misc/yn_tabular_list_preview.png', False)

    except:
        pass 

label yn_start:
    $ persistent.timeofday = 'day'
    $ persistent.sprite_time = 'day'
    $ persistent.yn_protagonist = 'yana'
    $ persistent.yn_protagonist_mood = 'normal'
    $ yn_set_main_menu_cursor()
    $ yn_onload('lock')
    $ yn_screens_save_act()
    $ renpy.pause(3, hard = True)
    scene yn_main_menu_intro
    show expression renpy.display.behavior.ImageButton(yn_gui_path + '/main_menu/yn_skip_idle.png', yn_gui_path + '/main_menu/yn_skip_hover.png', clicked=[Jump('yn_after_intro')]) at yn_skip_pos
    with Dissolve(3)
    play sound yn_konami
    $ renpy.pause(2.5, hard = True)
    scene bg black with Dissolve(2)
    $ renpy.pause(3, hard = True)
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard = True)
    $ renpy.movie_cutscene('yn/images/gui/main_menu/yn_main_menu_intro_start_background.ogv')
    scene yn_main_menu_background_full
    $ renpy.pause(0.5, hard = True)
    scene yn_main_menu_background_full:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 1.5 zoom 1.63 xalign 0.845 yalign 0.65
    $ renpy.pause(1.6, hard = True)
    scene bg black with dissolve
    $ renpy.pause(0.5, hard = True)
    play sound yn_insert_cassette
    $ renpy.pause(1, hard = True)
    $ yn_set_main_menu_cursor()
    $ yn_onload('unlock')

    label yn_after_intro:
        $ renpy.transition(dissolve)