init:
    $ yn_dw_buttons_count = 6

    $ yn_dw_buttons_positions = {
        0: (960, 716),
        1: (1005, 746),
        2: (960, 790),
        3: (794, 790),
        4: (776, 746),
        5: (815, 716)
    }

    $ yn_dw_text_positions = {
        0: (1125, 687),
        1: (1154, 754),
        2: (1135, 828),
        3: (735, 828),
        4: (715, 755),
        5: (800, 690)
    }

    image yn_peacocks_check_logo = yn_gui_path + 'dialogue_wheel/yn_peacocks_check_logo.png'
    image yn_pigeons_check_logo = yn_gui_path + 'dialogue_wheel/yn_pigeons_check_logo.png'
    image yn_sparrows_check_logo = yn_gui_path + 'dialogue_wheel/yn_sparrows_check_logo.png'
    image yn_tomtits_check_logo = yn_gui_path + 'dialogue_wheel/yn_tomtits_check_logo.png'

    transform yn_dw_picloc():
        xalign 0.5
        yalign 0.5

init python:
    class YnDialogueWheel():
        def __init__(self, questions_dict):
            self.questions_dict = questions_dict

        def yn_dw_call(self):
            renpy.call_screen('yn_dialogue_wheel', questions_dict=self.questions_dict)

        @staticmethod
        def yn_dw_remove_choice(dw, choice):
            del dw[choice]

    Yn_dw_choice = renpy.curry(YnDialogueWheel.yn_dw_remove_choice)

screen yn_dw_iconscreen(icon):
    add icon:
        xalign 0.5 
        ypos 750

screen yn_dialogue_wheel(questions_dict):
    add yn_gui_path + 'dialogue_wheel/yn_dialogue_wheel_bg.png'

    for number in range(yn_dw_buttons_count):
        if number in questions_dict:
            text questions_dict[number][0]:
                style 'yn_dw_answers_text_style'

                if number >= 3:
                    xpos questions_dict[number][3]                 

                else:
                    xpos yn_dw_text_positions[number][0]
                
                ypos yn_dw_text_positions[number][1]

            imagebutton:
                auto yn_gui_path + 'dialogue_wheel/' + persistent.timeofday + '/{}_%s.png'.format(number)
                pos yn_dw_buttons_positions[number]
                
                if questions_dict[number][2]:
                    hovered [Show('yn_dw_iconscreen', Dissolve(0.2), icon=questions_dict[number][2])]
                    unhovered [Hide('yn_dw_iconscreen', Dissolve(0.2))]

                action [Hide('yn_dw_iconscreen', Dissolve(0.2)), Yn_dw_choice(questions_dict, number), Jump(questions_dict[number][1])]

        else:
            add yn_gui_path + 'dialogue_wheel/' + persistent.timeofday + '/{}_noactive.png'.format(number) pos yn_dw_buttons_positions[number]