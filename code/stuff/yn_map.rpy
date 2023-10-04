init python:
    class YnCampMap:
        def __init__(self, zones_dict, continue_label, map_screen):
            self.zones_dict = zones_dict
            self.continue_label = continue_label
            self.map_screen = map_screen

        def yn_cm_count_zones(self, dict_):
            return sum(1 + yn_cm_count_zones(v) if isinstance(v, dict) else 1 for _, v in dict_.iteritems())

        def call(self):
            if self.yn_cm_count_zones(self.zones_dict) != 0:
                renpy.call_screen(self.map_screen, zones_dict=self.zones_dict)

            else:
                renpy.jump(self.continue_label)

    def yn_disable_zone(dict_, zone):
        del dict_[zone]

    Yn_disable_zone = renpy.curry(yn_disable_zone)

screen yn_act_one_play_two_bypass_map(zones_dict):
    tag map
    modal True

    add 'yn_bypass' xpos 1275 ypos 175

    for place, value in yn_act_one_play_two_bypass_places.iteritems():
        if value:
            $ sign_image_ = yn_act_one_play_two_bypass_assignment[place][0]
            $ pos_ = yn_act_one_play_two_bypass_assignment[place][1]

            add sign_image_ pos pos_

    $ yn_act_one_play_two_bypass_map_zones_pos = {
        'yn_music_club': (414, 358, 62, 54),
        'yn_dining_hall': (665, 482, 85, 92),
        'yn_clubs': (291, 516, 94, 67),
        'yn_art_club': (298, 459, 72, 49),
        'yn_theatre_club': (369, 465, 70, 60),
        'yn_library': (752, 368, 101, 57),
        'yn_medic_house': (686, 422, 62, 58)
    }

    imagemap:
        auto yn_gui_path + 'bypass/yn_map_%s.png'

        for zone_name in zones_dict.keys():
            hotspot(yn_act_one_play_two_bypass_map_zones_pos[zone_name]):
                action [Yn_disable_zone(zones_dict, zone_name), Jump(zones_dict[zone_name])]

screen yn_act_two_play_fifth_map(zones_dict):
    tag map
    modal True

    $ yn_act_two_play_fifth_map_zones_pos = {
        'yn_music_club': (620, 250, 62, 54),
        'yn_clubs': (425, 505, 120, 85),
        'yn_art_club': (442, 418, 90, 80),
        'yn_library': (1158, 268, 101, 55),
    }

    imagemap:
        auto yn_gui_path + 'map/yn_map_%s.png'

        for zone_name in zones_dict.keys():
            hotspot(yn_act_two_play_fifth_map_zones_pos[zone_name]):
                action [Yn_disable_zone(zones_dict, zone_name), Jump(zones_dict[zone_name])]