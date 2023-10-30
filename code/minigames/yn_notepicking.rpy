init python:   
    yn_note_picking_minigame_parts_count = 0
    yn_note_picking_visible = True

    def yn_note_picking_piece_dragged(drags, drop):
        global yn_note_picking_minigame_parts_count
        global note_picking_visible

        if not drop:
            for part in ["null", "first", "second", "third", "fourth", "fifth"]:
                if drags[0].drag_name == part:
                    win_xpos = yn_note_picking_win_positions[part][0]
                    win_ypos = yn_note_picking_win_positions[part][1]

                    if abs(drags[0].x - win_xpos) <= 70 and abs(drags[0].y - win_ypos) <= 70:
                        yn_note_picking_minigame_parts_count += 1
                        drags[0].snap(win_xpos, win_ypos, 0.3)
                        drags[0].draggable = False

                        if yn_note_picking_minigame_parts_count == 6:
                            yn_note_picking_visible = False

                        renpy.restart_interaction()
            return
        
        return True

init:
    $ yn_note_picking_start_positions = [
        (500, 300),
        (700, 500),
        (900, 400),
        (1300, 400),
        (1700, 200),
        (0, 500)
    ]

    $ yn_note_picking_win_positions = {
        "null": (539, 81),
        "first": (549, 267),
        "second": (960, 81),
        "third": (702, 405),
        "fourth": (930, 316),
        "fifth": (571, 692)
    }

    image yn_note_full = "yana/images/mini_games/note_picking/yn_note_full.png"

screen yn_note_picking_minigame():
    timer 0.5 repeat True action If(not yn_note_picking_visible, true=[Hide('yn_note_picking_minigame', Dissolve(1.5)), Return()])

    draggroup:
        drag:
            drag_name "null"
            child "yana/images/mini_games/note_picking/yn_note_part0.png"
            droppable False
            dragged yn_note_picking_piece_dragged
            pos yn_note_picking_start_positions[0]
            
        drag:
            drag_name "first"
            child "yana/images/mini_games/note_picking/yn_note_part1.png"
            droppable False
            dragged yn_note_picking_piece_dragged
            pos yn_note_picking_start_positions[1]
            
        drag:
            drag_name "second"
            child "yana/images/mini_games/note_picking/yn_note_part2.png"
            droppable False
            dragged yn_note_picking_piece_dragged
            pos yn_note_picking_start_positions[2]
            
        drag:
            drag_name "third"
            child "yana/images/mini_games/note_picking/yn_note_part3.png"
            droppable False
            dragged yn_note_picking_piece_dragged
            pos yn_note_picking_start_positions[3]

        drag:
            drag_name "fourth"
            child "yana/images/mini_games/note_picking/yn_note_part4.png"
            droppable False
            dragged yn_note_picking_piece_dragged
            pos yn_note_picking_start_positions[4]

        drag:
            drag_name "fifth"
            child "yana/images/mini_games/note_picking/yn_note_part5.png"
            droppable False
            dragged yn_note_picking_piece_dragged
            pos yn_note_picking_start_positions[5]