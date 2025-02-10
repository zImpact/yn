init python:
    yn_gui_path = 'yn/images/gui/'
    yn_link_font = yn_gui_path + 'fonts/gothic.ttf'
    yn_header_font = yn_gui_path + 'fonts/corbel.ttf'
    yn_main_font = 'fonts/calibri.ttf'
    yn_main_menu_font = yn_gui_path + 'fonts/BADSCRIPT_REGULAR.ttf'
    yn_flow_ext = yn_gui_path + 'fonts/yn_flow_ext.otf'

    style.yn_button_none = Style(style.button)
    style.yn_button_none.background = None
    style.yn_button_none.hover_background = None
    style.yn_button_none.selected_background = None
    style.yn_button_none.selected_hover_background = None
    style.yn_button_none.selected_idle_background = None

    style.yn_text_style = Style(style.default)
    style.yn_text_style.color = '#ffdd7d'
    style.yn_text_style.drop_shadow = (2, 2)
    style.yn_text_style.drop_shadow_color = '#000'

    style.yn_titles_style = Style(style.default)
    style.yn_titles_style.font = yn_link_font
    style.yn_titles_style.color = '#fff'
    style.yn_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.yn_titles_style.drop_shadow_color = '#000'
    style.yn_titles_style.italic = False
    style.yn_titles_style.bold = False
    style.yn_titles_style.text_align = 0.5
    style.yn_titles_style.xmaximum = 0.8
    style.yn_titles_style.line_spacing = 15

    style.yn_log_button = Style(style.button)
    style.yn_log_button.child = None
    style.yn_log_button.focus_mask = None
    style.yn_log_button.background = None

    style.yn_save_load_button_main_menu = Style(style.button)
    style.yn_save_load_button_main_menu.background = yn_gui_path + 'save_load/main_menu/thumbnail_idle.png'
    style.yn_save_load_button_main_menu.hover_background = yn_gui_path + 'save_load/main_menu/thumbnail_hover.png'
    style.yn_save_load_button_main_menu.selected_background = yn_gui_path + 'save_load/main_menu/thumbnail_selected.png'
    style.yn_save_load_button_main_menu.selected_hover_background = yn_gui_path + 'save_load/main_menu/thumbnail_selected.png'
    style.yn_save_load_button_main_menu.selected_idle_background = yn_gui_path + 'save_load/main_menu/thumbnail_selected.png'

    style.yn_save_load_button_day = Style(style.button)
    style.yn_save_load_button_day.background = yn_gui_path + 'save_load/day/thumbnail_idle.png'
    style.yn_save_load_button_day.hover_background = yn_gui_path + 'save_load/day/thumbnail_hover.png'
    style.yn_save_load_button_day.selected_background = yn_gui_path + 'save_load/day/thumbnail_selected.png'
    style.yn_save_load_button_day.selected_hover_background = yn_gui_path + 'save_load/day/thumbnail_selected.png'
    style.yn_save_load_button_day.selected_idle_background = yn_gui_path + 'save_load/day/thumbnail_selected.png'

    style.yn_save_load_button_night = Style(style.button)
    style.yn_save_load_button_night.background = yn_gui_path + 'save_load/night/thumbnail_idle.png'
    style.yn_save_load_button_night.hover_background = yn_gui_path + 'save_load/night/thumbnail_hover.png'
    style.yn_save_load_button_night.selected_background = yn_gui_path + 'save_load/night/thumbnail_selected.png'
    style.yn_save_load_button_night.selected_hover_background = yn_gui_path + 'save_load/night/thumbnail_selected.png'
    style.yn_save_load_button_night.selected_idle_background = yn_gui_path + 'save_load/night/thumbnail_selected.png'

    style.yn_save_load_button_sepia = Style(style.button)
    style.yn_save_load_button_sepia.background = yn_gui_path + 'save_load/sepia/thumbnail_idle.png'
    style.yn_save_load_button_sepia.hover_background = yn_gui_path + 'save_load/sepia/thumbnail_hover.png'
    style.yn_save_load_button_sepia.selected_background = yn_gui_path + 'save_load/sepia/thumbnail_selected.png'
    style.yn_save_load_button_sepia.selected_hover_background = yn_gui_path + 'save_load/sepia/thumbnail_selected.png'
    style.yn_save_load_button_sepia.selected_idle_background = yn_gui_path + 'save_load/sepia/thumbnail_selected.png'

    style.yn_save_load_button_sunset = Style(style.button)
    style.yn_save_load_button_sunset.background = yn_gui_path + 'save_load/sunset/thumbnail_idle.png'
    style.yn_save_load_button_sunset.hover_background = yn_gui_path + 'save_load/sunset/thumbnail_hover.png'
    style.yn_save_load_button_sunset.selected_background = yn_gui_path + 'save_load/sunset/thumbnail_selected.png'
    style.yn_save_load_button_sunset.selected_hover_background = yn_gui_path + 'save_load/sunset/thumbnail_selected.png'
    style.yn_save_load_button_sunset.selected_idle_background = yn_gui_path + 'save_load/sunset/thumbnail_selected.png'

    style.yn_base_font = Style(style.default)
    style.yn_base_font.font = yn_main_font
    style.yn_base_font.size = 28
    style.yn_base_font.line_spacing = 2

    style.yn_settings_header_main_menu_quit = Style(style.yn_base_font)
    style.yn_settings_header_main_menu_quit.font = yn_header_font
    style.yn_settings_header_main_menu_quit.size = 60
    style.yn_settings_header_main_menu_quit.color = '#d1d1d1'
    style.yn_settings_header_main_menu_quit.hover_color = '#ffffff'

    style.yn_settings_link = Style(style.yn_base_font)
    style.yn_settings_link.font = yn_link_font
    style.yn_settings_link.size = 60
    style.yn_settings_link.kerning = 3
    style.yn_settings_link.color = '#909ca3'
    style.yn_settings_link.hover_color = '#ffffff'
    style.yn_settings_link.selected_color = '#909ca3'
    style.yn_settings_link.selected_idle_color = '#909ca3'
    style.yn_settings_link.selected_hover_color = '#ffffff'
    style.yn_settings_link.insensitive_color = '#909ca3'

    style.yn_settings_link_main_menu = Style(style.yn_base_font)
    style.yn_settings_link_main_menu.font = yn_link_font
    style.yn_settings_link_main_menu.size = 60
    style.yn_settings_link_main_menu.kerning = 3
    style.yn_settings_link_main_menu.color = '#ffffff'
    style.yn_settings_link_main_menu.hover_color = '#ffffff'
    style.yn_settings_link_main_menu.selected_color = '#ffffff'
    style.yn_settings_link_main_menu.selected_idle_color = '#ffffff'
    style.yn_settings_link_main_menu.selected_hover_color = '#ffffff'
    style.yn_settings_link_main_menu.insensitive_color = '#ffffff'

    style.yn_settings_link_main_menu_preferences = Style(style.yn_base_font)
    style.yn_settings_link_main_menu_preferences.font = yn_link_font
    style.yn_settings_link_main_menu_preferences.size = 60
    style.yn_settings_link_main_menu_preferences.kerning = 3
    style.yn_settings_link_main_menu_preferences.color = '#d1d1d1'
    style.yn_settings_link_main_menu_preferences.hover_color = '#ffffff'
    style.yn_settings_link_main_menu_preferences.selected_color = '#d1d1d1'
    style.yn_settings_link_main_menu_preferences.selected_idle_color = '#d1d1d1'
    style.yn_settings_link_main_menu_preferences.selected_hover_color = '#ffffff'
    style.yn_settings_link_main_menu_preferences.insensitive_color = '#d1d1d1'

    style.yn_settings_header_main_menu_preferences = Style(style.yn_base_font)
    style.yn_settings_header_main_menu_preferences.font = yn_main_menu_font
    style.yn_settings_header_main_menu_preferences.size = 50
    style.yn_settings_header_main_menu_preferences.color = '#55544d'
    style.yn_settings_header_main_menu_preferences.hover_color = '#000000'
    style.yn_settings_header_main_menu_preferences.selected_color = '#000000'

    style.yn_settings_header_main_menu_preferences_locked = Style(style.yn_base_font)
    style.yn_settings_header_main_menu_preferences_locked.font = yn_main_menu_font
    style.yn_settings_header_main_menu_preferences_locked.size = 50
    style.yn_settings_header_main_menu_preferences_locked.color = '#55544d'
    style.yn_settings_header_main_menu_preferences_locked.hover_color = '#55544d'
    style.yn_settings_header_main_menu_preferences_locked.selected_color = '#55544d'

    style.yn_settings_header_main_menu_preferences_inverse = Style(style.yn_base_font)
    style.yn_settings_header_main_menu_preferences_inverse.font = yn_main_menu_font
    style.yn_settings_header_main_menu_preferences_inverse.size = 50
    style.yn_settings_header_main_menu_preferences_inverse.color = '#000000'
    style.yn_settings_header_main_menu_preferences_inverse.hover_color = '#000000'
    style.yn_settings_header_main_menu_preferences_inverse.selected_color = '#000000'

    style.yn_settings_header_day = Style(style.yn_base_font)
    style.yn_settings_header_day.font = yn_header_font
    style.yn_settings_header_day.size = 50
    style.yn_settings_header_day.color = '#4d2e19'
    style.yn_settings_header_day.hover_color = '#a27146'
    
    style.yn_settings_header_night = Style(style.yn_base_font)
    style.yn_settings_header_night.font = yn_header_font
    style.yn_settings_header_night.size = 50
    style.yn_settings_header_night.color = '#161d3d'
    style.yn_settings_header_night.hover_color = '#008193'

    style.yn_settings_header_sepia = Style(style.yn_base_font)
    style.yn_settings_header_sepia.font = yn_header_font
    style.yn_settings_header_sepia.size = 50
    style.yn_settings_header_sepia.color = '#9b6f31'
    style.yn_settings_header_sepia.hover_color = '#9b6f31'

    style.yn_settings_header_sunset = Style(style.yn_base_font)
    style.yn_settings_header_sunset.font = yn_header_font
    style.yn_settings_header_sunset.size = 50
    style.yn_settings_header_sunset.color = '#5a3525'
    style.yn_settings_header_sunset.hover_color = '#636840'

    style.yn_settings_text_day = Style(style.yn_settings_header_day)
    style.yn_settings_text_day.size = 36
    style.yn_settings_text_day.selected_color = '#4d2e19'
    style.yn_settings_text_day.hover_color = '#a27146'

    style.yn_settings_text_night = Style(style.yn_settings_header_night)
    style.yn_settings_text_night.size = 36
    style.yn_settings_text_night.selected_color = '#161d3d'
    style.yn_settings_text_night.hover_color = '#008193'

    style.yn_settings_text_sepia = Style(style.yn_settings_header_sepia)
    style.yn_settings_text_sepia.size = 36
    style.yn_settings_text_sepia.selected_color = '#9b6f31'
    style.yn_settings_text_sepia.hover_color = '#9b6f31'

    style.yn_settings_text_sunset = Style(style.yn_settings_header_sunset)
    style.yn_settings_text_sunset.size = 36
    style.yn_settings_text_sunset.selected_color = '#5a3525'
    style.yn_settings_text_sunset.hover_color = '#636840'

    style.yn_text_history = Style(style.yn_base_font)
    style.yn_text_history.color = '#ffffff'
    style.yn_text_history.drop_shadow = (2, 2)
    style.yn_text_history.drop_shadow_color = '#000'

    style.yn_dw_answers_text_style = Style(style.default)
    style.yn_dw_answers_text_style.size = 35
    style.yn_dw_answers_text_style.color = '#ffdd7d'
    style.yn_dw_answers_text_style.drop_shadow = (2, 2)
    style.yn_dw_answers_text_style.drop_shadow_color = '#000'

    style.yn_dw_info_text_style = Style(style.default)
    style.yn_dw_info_text_style.size = 35
    style.yn_dw_info_text_style.color = '#8b7843'
    style.yn_dw_info_text_style.hover_color = '#ffdd7d'
    style.yn_dw_info_text_style.drop_shadow = (2, 2)
    style.yn_dw_info_text_style.drop_shadow_color = '#000'