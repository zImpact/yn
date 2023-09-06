init python:
    def yn_diary_say(text, page):
        global yn_diary_page
        global yn_diary_page_one

        yn_diary_page = page
        renpy.say(yn_narrator_diary, text)

        if yn_diary_page == 1:
            yn_diary_page_one = text

    yn_narrator_diary = Character(None, screen = "yn_diary_mode", what_color = "#000000")

screen yn_diary_mode(what, who):
    add "yn_diary_" + persistent.timeofday

    if yn_diary_page == 1:
        text what:
            id "what"
            font yn_flow_ext
            xpos 377
            ypos 122 
            xmaximum 500
            size 34
            line_spacing 9

    elif yn_diary_page == 2:
        text "{color=#000000}[yn_diary_page_one]{/color}":
            font yn_flow_ext
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