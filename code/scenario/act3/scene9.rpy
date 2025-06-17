label yn_act3_scene9:
    $ yn_onload("lock")
    $ renpy.block_rollback()
    $ persistent.timeofday = "day"
    $ persistent.sprite_time = "day"
    $ renpy.pause(3, hard=True)
    $ yn_chapter_intro(
        "Действие девятое.",
        "bg yn_ext_camp_entrance_day_blurred",
        "camp_entrance_day",
        "yn_yana smile2",
        "yn_play_nineth_intro_text"
    )
    scene bg black with Dissolve(2)
    jump yn_act3_scene10
