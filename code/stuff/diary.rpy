init python:
    def yn_diary_say(text):
        if not hasattr(yn_diary_say, "page"):
            yn_diary_say.page = 1

        else:
            yn_diary_say.page = 1 if yn_diary_say.page == 2 else 2
        
        renpy.say(yn_narrator_diary, text)

        if yn_diary_say.page == 1:
            yn_diary_say.page_one_text = text

    yn_narrator_diary = Character(None, screen="yn_diary_mode", what_color="#000000")

screen yn_diary_mode(what, who):
    add "yn_diary_" + persistent.timeofday

    if yn_diary_say.page == 1:
        text what:
            id "what"
            font yn_flow_ext
            xpos 377
            ypos 122 
            xmaximum 500
            size 34
            line_spacing 9

    elif yn_diary_say.page == 2:
        text "[yn_diary_say.page_one_text]":
            font yn_flow_ext
            color "#000000"
            xpos 377
            ypos 122 
            xmaximum 500
            size 34
            line_spacing 9

        text what:
            id "what"
            font yn_flow_ext
            xpos 1030
            ypos 122 
            xmaximum 495
            size 34
            line_spacing 9