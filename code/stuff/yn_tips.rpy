init python:
    def yn_tip_handler(text):
        renpy.show_screen("yn_tip_screen", text = text)
        renpy.restart_interaction()

    def yn_tip_tag_func(tag, argument, contents):
        size = 29 if persistent.font_size == "large" else 24
        text = argument
        return [(renpy.TEXT_TAG, u"size={}".format(size))] + [(renpy.TEXT_TAG, u"a=yn_tip_h:{}".format(text))] + contents + [(renpy.TEXT_TAG, u"/a")] + [(renpy.TEXT_TAG, u"/size")]

    yn_tip_phrases = {
        "fraulein": "{b}Фройляйн{/b} - форма вежливого упоминания по отношению к незамужней женщине или к девушке в Германии и в некоторых других странах, обычно присоединяемое к фамилии или имени.",
        "mitskatta": "{b}Митскатта{/b} - в переводе с японского означает «нашла».",
    }

screen yn_tip_screen(text):
    modal False
    zorder 100

    key "dismiss":
        action [Hide("yn_tip_screen"), Return()]

    key "toggle_skip":
        action [Hide("yn_tip_screen"), Return()]

    key "skip":
        action [Hide("yn_tip_screen"), Return()]

    if not config.skipping:
        frame background Frame("images/gui/choice/" + persistent.timeofday + "/choice_box.png", 0, 0) xalign 0.98 yalign 0.01 left_padding 75 right_padding 75 bottom_padding 75 top_padding 75 at notify_appear:
            text yn_tip_phrases[text]:
                font header_font 
                size 37 
                color "#ffdd7d" 
                xmaximum 0.35

    else:
        timer 0.01 action Hide("yn_tip_screen")