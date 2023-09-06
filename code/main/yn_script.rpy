init python:
    class yn_FunctionCallback(Action):
        def __init__(self,function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)
    
    def yn_on_load_callback(slot):
        try:
            if persistent.yn_on_save_timeofday[slot]:
                persistent.timeofday = persistent.yn_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.yn_on_save_timeofday[slot][1]
                persistent.font_size = persistent.yn_on_save_timeofday[slot][2]
                persistent.yn_protagonist_mood = persistent.yn_on_save_timeofday[slot][3]
                persistent.yn_protagonist = persistent.yn_on_save_timeofday[slot][4]
                _preferences.volumes["music"] = persistent.yn_on_save_timeofday[slot][5]
                _preferences.volumes["sfx"] = persistent.yn_on_save_timeofday[slot][6]
                _preferences.volumes["voice"] = persistent.yn_on_save_timeofday[slot][7]
        
        except:
            pass
    
    def yn_on_save_callback(slot):
        if not persistent.yn_on_save_timeofday:
            persistent.yn_on_save_timeofday = {}

        persistent.yn_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, persistent.yn_protagonist_mood, persistent.yn_protagonist, _preferences.volumes["music"], _preferences.volumes["sfx"], _preferences.volumes["voice"])
        
    def yn_screen_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("yn_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
        
    def yn_screen_act():
        config.window_title = u"Яна"
        config.name = "Yana_mod"
        config.version = "1.0"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("yn_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненые данные?"

        renpy.free_memory()
            
        config.overlay_functions.append(yn_set_timeofday_cursor)
        config.main_menu_music = yn_i_am_waiting_for_you_last_summer_new_noise
        config.hyperlink_handlers["yn_tip_h"] = yn_tip_handler
        config.custom_text_tags["yn_tip_tag"] = yn_tip_tag_func 
        config.linear_saves_page_size = None
        persistent._file_page = "yn_FilePage_1"

        style.hyperlink_text = Style(style.default)
        style.hyperlink_text.color = "#a18c4f"
        style.hyperlink_text.hover_color = "#ffdd7d"
        style.hyperlink_text.drop_shadow = (2, 2)
        style.hyperlink_text.underline = True
        style.hyperlink_text.drop_shadow_color = "#000"

    def yn_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("yn_old_" + screen_name, None)]
          
        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            
        renpy.free_memory()
        yn_stop_predict_screens()
        yn_stop_predict_resources()

        config.overlay_functions.remove(yn_set_timeofday_cursor)
        config.mouse_displayable = MouseDisplayable("images/misc/mouse/1.png", 0, 0)
        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
        del config.hyperlink_handlers["yn_tip_h"]
        del config.custom_text_tags["yn_tip_tag"]
        renpy.block_rollback()

        style.hyperlink_text = Style(style.settings_link)
        style.hyperlink_text.underline = True
        style.hyperlink_text.hover_color = "#0ff"
        style.hyperlink_text.idle_color = "#08f"

        persistent._file_page = 1
        renpy.music.stop("ambience")
        renpy.music.stop("music")
        renpy.music.stop("sound")
        renpy.music.stop("sound_loop")
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def yn_screens_save_act():
        yn_screen_save()
        yn_screen_act()