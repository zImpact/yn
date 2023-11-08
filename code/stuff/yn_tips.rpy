init python:
    def yn_tip_handler(text):
        renpy.show_screen('yn_tip_screen', text=text)
        renpy.restart_interaction()

    def yn_tip_tag_func(tag, argument, contents):
        size = 29 if persistent.font_size == 'large' else 24
        text = argument
        return [(renpy.TEXT_TAG, u'size={}'.format(size))] + [(renpy.TEXT_TAG, u'a=yn_tip_h:{}'.format(text))] + contents + [(renpy.TEXT_TAG, u'/a')] + [(renpy.TEXT_TAG, u'/size')]

    yn_tip_phrases = {
        'geterohrom': '{b}Гетерохромия{/b} - редкое явление, предполагающее разный цвет глаз у человека. Эта патология проявляется не только в расцветке органов зрения, но и в окрасе радужки.',
        'fraulein': '{b}Фройляйн{/b} - форма вежливого упоминания по отношению к незамужней женщине или к девушке в Германии и в некоторых других странах, обычно присоединяемое к фамилии или имени.',
        'mitskatta': '{b}Митскатта{/b} - в переводе с японского означает «нашла».',
        'dekfaul': '{b}Нецензурно ругается на немецком.{/b}',
        'aisawu': '{b}Айсацу{/b} - японское приветствие.',
        'totemo': '{b}Очень красиво.{/b}',
        'sayonara': '«Сайонара!» по-японски значит {b}«До свидания!».{/b}',
        'dubina': '{b}Болван, дурак и т. п.{/b}',
        'suita': 'Одна из основных разновидностей циклической формы в инструментальной музыке.'
    }

screen yn_tip_screen(text):
    modal False
    zorder 100

    python:
        blocked_action = [Hide('yn_tip_screen'), Return()]

    key 'dismiss':
        action blocked_action

    key 'toggle_skip':
        action blocked_action

    key 'skip':
        action blocked_action

    if not config.skipping:
        frame background Frame('images/gui/choice/' + persistent.timeofday + '/choice_box.png', 0, 0) xalign 0.98 yalign 0.01 left_padding 75 right_padding 75 bottom_padding 75 top_padding 75 at notify_appear:
            text yn_tip_phrases[text]:
                font header_font 
                size 37 
                color '#ffdd7d' 
                xmaximum 0.35
                
    else:
        timer 0.01 action Hide('yn_tip_screen')