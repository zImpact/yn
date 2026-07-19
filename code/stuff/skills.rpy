default yn_dialogue_skill_pending_icon = None
default yn_dialogue_skill_icon = None
default yn_dialogue_skill_history_icon = None
default yn_dialogue_skill_icon_locked = False

init python:
    yn_skill_order = [
        YN_EMPATHY_SKILL,
        YN_PERCEPTION_SKILL,
        YN_DRAMA_SKILL,
        YN_CHARISMA_SKILL,
        YN_ECNYCLOPEDIA_SKILL
    ]

    yn_skill_sound_paths = {
        "empathy": "yn/sounds/skills/empathy.mp3",
        "perception": "yn/sounds/skills/perception.mp3",
        "drama": "yn/sounds/skills/drama.mp3",
        "charisma": "yn/sounds/skills/charisma.mp3",
        "encyclopedia": "yn/sounds/skills/encyclopedia.mp3"
    }

    renpy.music.register_channel("yn_skills", mixer="yn_skills", loop=False)

    if "yn_skills" not in _preferences.volumes:
        _preferences.set_volume("yn_skills", 1.0)

    yn_skill_data = {
        YN_EMPATHY_SKILL: {
            "title": u"Эмпатия",
            "short": u"Яна чувствует и понимает эмоции других людей.",
            "effect": u"Позволяет снизить недоверие окружающих.",
            "mechanic": u"-1 балл к изначальному порогу проверки очков лояльности.",
            "full": u"""Несмотря на выпадение из социума на длительный срок Яна всё ещё хорошо разбирается в людях. Это настоящее искусство, улавливать мимолётные сигналы, которые подающий их человек и сам может не заметить. Лёгкая улыбка, скрытая грусть, брезгливый взгляд.

Яна может действительно представлять, каково это оказаться в чужой шкуре, и с лёгкостью улавливает уровень реакции своего собеседника."""
        },
        YN_PERCEPTION_SKILL: {
            "title": u"Восприятие",
            "short": u"Яна видит и слышит гораздо больше, чем другие.",
            "effect": u"Позволяет в некоторых диалогах предугадывать реакцию собеседника.",
            "mechanic": u"Подсвечивает положительные и отрицательные последствия выбора.",
            "full": u"""Визуальный анализ - конёк Яны. Видеть, слышать и чувствовать то, на что любой другой не обратит ни малейшего внимания.

Ещё ни разу не было такого, чтобы Яна не находила потерянную вещь. Кто-то клянётся, что говорит только правду и ничего, кроме правды, но глаза его бегают в разные стороны. Другая уверяет, что у неё всё в порядке, но голос её срывается на истеричные ноты.

Найти иголку в стоге сена? Раз плюнуть! Она даже любую ноту сможет угадать всего с двух букв!"""
        },
        YN_DRAMA_SKILL: {
            "title": u"Драматизм",
            "short": u"Яна любит драматизировать настолько, что порой доходит до фантасмагории.",
            "effect": u"Некоторые реплики и мысли Яны становятся абсурдными и гиперболизированными. Не любит слишком серьёзных.",
            "mechanic": u"Не рекомендуется брать при первом прохождении, чтобы не портить атмосферу.",
            "full": u"""Почто? Доколе мы и дальше будем притворяться, что весь мир не сцена театра? Яна уверена, что софиты направлены прямо на неё.

Низкопробное кривлянье и гримасничество плохих актёров в постановке под названием жизнь видны ей с первого взгляда. «Не верю!», - громко заявляет она, когда видит плохой отыгрыш дешёвой лжи.

Пусть она немного несносна и порой окружающих сбивают с толку некоторые её высказывания. Она прима этой постановки. Реплики выучены, занавес медленно поднимается... Время блистать!"""
        },
        YN_CHARISMA_SKILL: {
            "title": u"Харизма",
            "short": u"Стильные солнцезащитные очки, уверенность в себе и куча обаяния.",
            "effect": u"Окружающие становятся более лояльными и лучше идут на контакт.",
            "mechanic": u"+0.5 к каждому прибавлению очков и -0.5 к каждому убыванию очков.",
            "full": u"""Гремучая смесь из выдающихся внешних данных и природного обаяния. Вот как можно охарактеризовать Яночку.

Влиять на других с помощью слов и лёгкой улыбки - легко. Убеждать других, что они хотят того же, что и она, - задача, которую эта рыжеволосая симпатяжка решает, как дважды два.

Уж поверьте, Яна умеет вкладывать нужные ей мысли в головы собеседников. Спросите её, каково это, нравится всем, и она вам расскажет."""
        },
        YN_ECNYCLOPEDIA_SKILL: {
            "title": u"Энциклопедия",
            "short": u"Яна располагает множеством всесторонних знаний. Высокий уровень эрудииции.",
            "effect": u"Мозг Яны становится практически универсальным справочником. Позволяет узнать мир чуть-чуть лучше.",
            "mechanic": u"Появляются кликабельные информационные справки о мире.",
            "full": u"""Если очень много читать, то в какой-то момент сама станешь ходячим справочником. Яна порой сама удивляется, откуда она знает значение слова престидижитатор и тот факт, что первым видеомагнитофоном в СССР стал Рижский «Малахит» 1967 года выпуска.

Порой её мысли настолько забиваются таким необъятным количеством фактов и определений, что Яне становится от этого не по себе. Конечно, нельзя знать всё на свете, но лелеять мечту о такой возможности никто не запрещает."""
        }
    }

    yn_history_hover_colors = {
        "day": "#40e138",
        "night": "#008193",
        "sepia": "#b7a492",
        "sunset": "#636840"
    }

    yn_skill_header_icon_yoffsets = {
        YN_EMPATHY_SKILL: -1,
        YN_CHARISMA_SKILL: -3,
        YN_ECNYCLOPEDIA_SKILL: -1
    }

    def yn_has_skill(skill_id):
        return skill_id in store.yn_selected_skills

    def yn_clear_dialogue_skill_state():
        store.yn_dialogue_skill_pending_icon = None
        store.yn_dialogue_skill_icon = None
        store.yn_dialogue_skill_history_icon = None
        store.yn_dialogue_skill_icon_locked = False

    def yn_play_skill_sound(skill_id):
        sound_path = yn_skill_sound_paths.get(skill_id)

        if sound_path and renpy.loadable(sound_path):
            renpy.music.play(sound_path, channel="yn_skills")

    def yn_set_dialogue_skill_icon(skill_id, locked=False):
        if skill_id not in yn_skill_data or not yn_has_skill(skill_id):
            yn_clear_dialogue_skill_state()
            return False

        store.yn_dialogue_skill_pending_icon = None if locked else skill_id
        store.yn_dialogue_skill_icon = skill_id if locked else None
        store.yn_dialogue_skill_history_icon = None
        store.yn_dialogue_skill_icon_locked = locked
        yn_play_skill_sound(skill_id)
        return True

    def yn_start_skill_dialogue(skill_id):
        return yn_set_dialogue_skill_icon(skill_id, True)

    def yn_stop_skill_dialogue():
        yn_clear_dialogue_skill_state()

    def yn_get_dialogue_skill_icon():
        return store.yn_dialogue_skill_icon

    def yn_skill_icon_image(skill_id, color="#ffdd7d"):
        return im.MatrixColor(
            yn_gui_path + "skills/" + skill_id + "_icon.png",
            im.matrix.colorize("#000000", color)
        )

    def yn_skill_dialogue_callback(event, interact=True, **kwargs):
        if store.yn_dialogue_skill_icon_locked:
            return

        if event == "begin":
            store.yn_dialogue_skill_history_icon = None
            store.yn_dialogue_skill_icon = store.yn_dialogue_skill_pending_icon
            store.yn_dialogue_skill_pending_icon = None

        elif event == "end":
            if config.history_length is not None and store._history:
                store.yn_dialogue_skill_history_icon = store.yn_dialogue_skill_icon

            else:
                store.yn_dialogue_skill_history_icon = None

            store.yn_dialogue_skill_icon = None
            store.yn_dialogue_skill_pending_icon = None

    def yn_skill_fast_skipping_callback():
        if store.yn_dialogue_skill_icon_locked:
            return

        if config.history_length is not None and store._history:
            store.yn_dialogue_skill_history_icon = (
                store.yn_dialogue_skill_icon
                or store.yn_dialogue_skill_pending_icon
            )

        else:
            store.yn_dialogue_skill_history_icon = None

        store.yn_dialogue_skill_icon = None
        store.yn_dialogue_skill_pending_icon = None

    def yn_skill_history_callback(history_entry):
        history_entry.yn_skill_icon = (
            store.yn_dialogue_skill_history_icon
            or store.yn_dialogue_skill_icon
            or store.yn_dialogue_skill_pending_icon
        )

        if not store.yn_dialogue_skill_icon_locked:
            yn_clear_dialogue_skill_state()

    def yn_normalize_selected_skills(selected_skills, max_skills):
        normalized_skills = []
        skill_limit = max(0, max_skills)

        if not skill_limit:
            return normalized_skills

        for skill_id in selected_skills or []:
            if skill_id in yn_skill_data and skill_id not in normalized_skills:
                normalized_skills.append(skill_id)

                if len(normalized_skills) == skill_limit:
                    break

        return normalized_skills

    def yn_toggle_skill(selected_skills, skill_id, max_skills):
        if skill_id in selected_skills:
            selected_skills.remove(skill_id)

        elif skill_id in yn_skill_data and len(selected_skills) < max(0, int(max_skills)):
            selected_skills.append(skill_id)

    if yn_skill_history_callback not in config.history_callbacks:
        config.history_callbacks.append(yn_skill_history_callback)

    if yn_skill_fast_skipping_callback not in config.fast_skipping_callbacks:
        config.fast_skipping_callbacks.append(yn_skill_fast_skipping_callback)

screen yn_skill_selection(max_skills=2, default_selected=None):
    modal True

    $ yn_skill_scroll_bar_full = Frame(im.Rotozoom(yn_gui_path + "preferences/" + persistent.timeofday + "/bar_full.png", 90, 1.0), 8, 36, 8, 36)
    $ yn_skill_scroll_bar_null = Frame(im.Rotozoom(yn_gui_path + "preferences/" + persistent.timeofday + "/bar_null.png", 90, 1.0), 8, 36, 8, 36)
    $ yn_skill_scroll_thumb = im.Composite(
        (24, 24),
        (1, 2), im.Scale(yn_gui_path + "preferences/" + persistent.timeofday + "/htumb.png", 20, 20)
    )

    default selected_skills = yn_normalize_selected_skills(default_selected, max_skills)
    default focused_skill = (selected_skills or yn_skill_order)[0]
    default hovered_skill = None
    default show_full_description = False

    key "K_F1":
        action NullAction()

    frame:
        background Frame(yn_gui_path + "choice/" + persistent.timeofday + "/choice_box.png", 50, 50)
        xalign 0.5
        ypos 25
        xsize 1640
        ysize 970
        left_padding 0
        right_padding 0
        top_padding 0
        bottom_padding 0

        fixed:
            text "Выберите характерные особенности Яны":
                font yn_header_font
                color "#ffdd7d"
                size 48
                xcenter 820
                ypos 75
                text_align 0.5
                drop_shadow (2, 2)
                drop_shadow_color "#000000"

            $ selected_skills_count = len(selected_skills)

            text "Выбрано: [selected_skills_count]/[max_skills]":
                font yn_main_font
                color "#d1d1d1"
                size 30
                xcenter 820
                ypos 135
                text_align 0.5

            fixed:
                xpos 35
                yalign 0.5
                yoffset 25
                xsize 840
                ysize 595

                for index, skill_id in enumerate(yn_skill_order):
                    $ skill = yn_skill_data[skill_id]
                    $ skill_selected = skill_id in selected_skills
                    $ skill_highlighted = skill_selected or hovered_skill == skill_id
                    $ skill_highlight_color = "#ffdd7d" if skill_highlighted else "#8b7843"
                    $ skill_card_alpha = 1.0 if skill_highlighted else 0.7
                    $ skill_xpos = index * 280 if index < 3 else 140 + (index - 3) * 280
                    $ skill_ypos = 0 if index < 3 else 300

                    button:
                        at Transform(alpha=skill_card_alpha)
                        xpos skill_xpos
                        ypos skill_ypos
                        xsize 280
                        ysize 295
                        background None
                        hover_background None
                        selected skill_selected

                        hovered [
                            SetScreenVariable("focused_skill", skill_id),
                            SetScreenVariable("hovered_skill", skill_id),
                            SetScreenVariable("show_full_description", False)]
                        unhovered SetScreenVariable("hovered_skill", None)
                        action If(
                            skill_id in selected_skills or len(selected_skills) < max_skills,
                            Function(yn_toggle_skill, selected_skills, skill_id, max_skills),
                            NullAction()
                        )

                        fixed:
                            xsize 280
                            ysize 295

                            add Frame(yn_gui_path + "dialogue_box/day/side_box.png", 36, 36):
                                xpos 50
                                xsize 180
                                ysize 210

                            add yn_gui_path + "skills/" + skill_id + ".png":
                                xcenter 140
                                ycenter 105
                                size (170, 198)

                            text skill["title"]:
                                style "yn_dw_info_text_style"
                                color skill_highlight_color
                                xalign 0.5
                                ypos 225
                                xmaximum 280
                                text_align 0.5

                            add yn_skill_icon_image(skill_id, skill_highlight_color):
                                xalign 0.5
                                ypos 269
                                size (24, 24)

            frame:
                background Frame(yn_gui_path + "dialogue_box/day/side_box.png", 36, 36)
                xpos 975
                yalign 0.5
                yoffset 25
                xsize 580
                ysize 595

                fixed:
                    $ focused = yn_skill_data[focused_skill]
                    $ focused_selected = focused_skill in selected_skills
                    $ focused_can_toggle = focused_selected or len(selected_skills) < max_skills
                    $ focused_action_text = "Убрать" if focused_selected else "Выбрать"
                    $ focused_icon_yoffset = yn_skill_header_icon_yoffsets.get(focused_skill, 0)

                    hbox:
                        xpos 35
                        ypos 28
                        spacing 14

                        add yn_skill_icon_image(focused_skill):
                            yalign 0.5
                            yoffset focused_icon_yoffset
                            size (36, 36)

                        text focused["title"]:
                            font yn_header_font
                            color "#ffdd7d"
                            size 44
                            yalign 0.5
                            xmaximum 450

                    if show_full_description:
                        viewport id "yn_skill_description_viewport":
                            xpos 40
                            ypos 100
                            xsize 490
                            ysize 355
                            mousewheel True
                            draggable True

                            text focused["full"]:
                                font yn_main_font
                                color "#ffffff"
                                size 24
                                xmaximum 470
                                line_spacing 7

                        vbar:
                            value YScrollValue("yn_skill_description_viewport")
                            xpos 541
                            ypos 100
                            xsize 24
                            ysize 355
                            top_bar yn_skill_scroll_bar_full
                            bottom_bar yn_skill_scroll_bar_null
                            thumb yn_skill_scroll_thumb
                            hover_thumb yn_skill_scroll_thumb

                        textbutton "Назад":
                            style "yn_dw_info_text_style"
                            text_style "yn_dw_info_text_style"
                            xpos 40
                            ypos 490
                            action SetScreenVariable("show_full_description", False)

                    else:
                        frame:
                            background Solid("#8b7843")
                            xpos 40
                            ypos 100
                            xsize 195
                            ysize 195

                            add yn_gui_path + "skills/" + focused_skill + ".png":
                                xalign 0.5
                                yalign 0.5
                                size (165, 193)

                        text focused["short"]:
                            font yn_main_font
                            italic True
                            color "#ffffff"
                            size 28
                            xpos 270
                            ypos 105
                            xmaximum 295
                            line_spacing 4

                        text focused["effect"]:
                            font yn_main_font
                            color "#d1d1d1"
                            size 25
                            xpos 40
                            ypos 330
                            xmaximum 520
                            line_spacing 4

                        text focused["mechanic"]:
                            font yn_main_font
                            color "#ffdd7d"
                            size 24
                            xpos 40
                            ypos 425
                            xmaximum 520
                            line_spacing 4

                        textbutton "Описание":
                            style "yn_dw_info_text_style"
                            text_style "yn_dw_info_text_style"
                            xpos 40
                            ypos 490
                            action SetScreenVariable("show_full_description", True)

                    textbutton focused_action_text:
                        style "yn_dw_info_text_style"
                        text_style "yn_dw_info_text_style"
                        xpos 260
                        ypos 490
                        sensitive focused_can_toggle
                        action Function(yn_toggle_skill, selected_skills, focused_skill, max_skills)

            $ done_button_text = "Не выбирать" if not selected_skills else "Готово"

            textbutton done_button_text:
                style "yn_dw_info_text_style"
                text_style "yn_dw_info_text_style"
                xalign 0.5
                ypos 850
                action Return(selected_skills)
