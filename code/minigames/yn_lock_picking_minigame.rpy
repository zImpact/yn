init python:
    yn_lockpicking_minigame_images = ["yn/images/mini_games/lockpicking/lock_plate.png", "yn/images/mini_games/lockpicking/lock_cylinder.png", "yn/images/mini_games/lockpicking/lock_tension.png", "yn/images/mini_games/lockpicking/lock_pick.png"]

    renpy.music.register_channel("yn_lock_move", mixer = "sfx", loop = True)
    renpy.music.register_channel("yn_lock_click", mixer = "sfx", loop = False, tight = True)

    class YnLockpickingMinigame(renpy.Displayable):
        def __init__(self, difficulty, resize = 1920, **kwargs):
            super(YnLockpickingMinigame, self).__init__(**kwargs)
            
            self.width = resize
            self.lock_plate_image = im.Scale(yn_lockpicking_minigame_images[0], resize, resize)
            self.lock_cylinder_image = im.Scale(yn_lockpicking_minigame_images[1], resize, resize)
            self.lock_tension_image = im.Scale(yn_lockpicking_minigame_images[2], resize, resize)
            self.lock_pick_image = im.Scale(yn_lockpicking_minigame_images[3], resize, resize)
            self.offset = (resize * 2 ** 0.5 - resize) / 2
            
            self.cylinder_min = 0
            self.cylinder_max = 90
            self.cylinder_pos = 0
            self.cylinder_try_rotate = False
            self.cylinder_can_rotate = False
            self.cylinder_released = False
            self.pick_min = 0
            self.pick_max = 180
            self.pick_pos = 90
            self.pick_can_rotate = True
            self.pick_broke = False
            self.sweet_spot = renpy.random.randint(0, 180)
            self.difficulty = difficulty
            self.breakage = (difficulty / 7 + 0.75)
        
        def event(self, ev, x, y, st):
            import pygame
            LEFT = 1
            RIGHT = 3
            
            remaining = 0 + st
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT:
                self.cylinder_try_rotate = True
                self.cylinder_released = False
            
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == LEFT:
                renpy.sound.stop(channel = "yn_lock_move")
                self.cylinder_try_rotate = False
                self.cylinder_released = True
                self.pick_can_rotate = True
                self.pick_broke = False
            
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == RIGHT:
                global current_chest
                current_chest = None
                renpy.hide_screen("lockpicking")
        
        def render(self, width, height, st, at):
            import pygame
            
            if self.difficulty > 29:
                self.difficulty = 29
            
            elif self.difficulty < 1:
                self.difficulty = 1
            
            if self.pick_can_rotate == True:
                x, y = renpy.get_mouse_pos()
                self.pick_pos = x / 5.3333333333 - 90
                
                if self.pick_pos > 180:
                    self.pick_pos = 180
                
                elif self.pick_pos < 0:
                    self.pick_pos = 0
                
                if self.pick_pos > self.sweet_spot:
                    if (self.pick_pos - self.sweet_spot) < self.difficulty:
                        self.cylinder_can_rotate = True
                        self.cylinder_max = 90
                    
                    else:
                        self.cylinder_can_rotate = True
                        self.cylinder_max = 90 - (self.pick_pos - self.sweet_spot) * (30 / self.difficulty)
                        
                        if self.cylinder_max < 0:
                            self.cylinder_max = 0
                
                elif self.pick_pos < self.sweet_spot:
                    if (self.sweet_spot - self.pick_pos) < self.difficulty:
                        self.cylinder_can_rotate = True
                        self.cylinder_max = 90
                    
                    else:
                        self.cylinder_can_rotate = True
                        self.cylinder_max = 90 - (self.sweet_spot - self.pick_pos) * (30 / self.difficulty)
                        
                        if self.cylinder_max < 0:
                            self.cylinder_max = 0
                
                else:
                    self.cylinder_can_rotate = True
                    self.cylinder_max = 90
            
            if self.pick_broke == True:
                pick = Transform(child = None)
            
            else:
                pick = Transform(child = self.lock_pick_image, rotate = self.pick_pos, subpixel = True)
            
            global display_pos
            display_pos = self.pick_pos
            
            global display_spot
            display_spot = self.sweet_spot
            
            if self.cylinder_try_rotate == True:
                if self.cylinder_can_rotate:
                    
                    self.cylinder_pos += (2 * st) / (at + 1)
                    
                    cylinder = Transform(child = self.lock_cylinder_image, rotate = self.cylinder_pos, subpixel = True)
                    tension = Transform(child = self.lock_tension_image, rotate = self.cylinder_pos, subpixel = True)
                    
                    if self.cylinder_pos > self.cylinder_max:
                        self.cylinder_pos = self.cylinder_max
                        
                        if self.cylinder_pos == 90:
                            renpy.sound.stop(channel = "yn_lock_move")
                            renpy.sound.play("yn/sounds/sfx/lock_unlock.mp3", channel = "yn_lock_click")
                            self.cylinder_max = 90
                            self.cylinder_pos = 90
                            global set_timers
                            global timers
                            timers = 0
                            set_timers = False
                            pygame.time.wait(150)
                            self.cylinder_can_rotate = False
                            renpy.jump("opened_chest")
                        
                        else:
                            if renpy.sound.is_playing != True:
                                renpy.sound.play("yn/sounds/sfx/lock_moving.mp3", channel = "yn_lock_move")
                            
                            angle1 = self.cylinder_pos + renpy.random.randint(-2, 2)
                            angle2 = self.cylinder_pos + renpy.random.randint(-4, 4)
                            cylinder = Transform(child = self.lock_cylinder_image, subpixel = True, rotate = angle1)
                            tension = Transform(child = self.lock_tension_image, subpixel = True, rotate = angle2)
                            
                            self.pick_can_rotate = False
                            
                            global lockpicks
                            global set_timers
                            global timers
                            
                            if set_timers == False:
                                timers = at
                                set_timers = True
                            
                            if set_timers == True:
                                if at > timers + self.breakage:
                                    renpy.sound.stop(channel = "yn_lock_move")
                                    renpy.sound.play("yn/sounds/sfx/lock_pick_break.mp3", channel = "yn_lock_click")
                                    renpy.notify("Broke a lock pick!")
                                    mispick = renpy.random.randint(-30, 30)
                                    pick = Transform(child = self.lock_pick_image, rotate = self.pick_pos + (2 * mispick), subpixel = True)
                                    self.pick_can_rotate = False
                                    pygame.time.wait(200)
                                    self.pick_broke = True
                                    self.cylinder_try_rotate = False
                                    lockpicks -= 1
                                    timers = 0
                                    set_timers = False
                                    pygame.mouse.set_pos([self.width / 2, self.width / 4])
                                    pygame.time.wait(100)
                
                else:
                    if renpy.sound.is_playing != True:
                        renpy.sound.play("yn/sounds/sfx/lock_moving.mp3", loop = True, channel = "yn_lock_move")
                    
                    angle1 = self.cylinder_pos + renpy.random.randint(-2, 2)
                    angle2 = self.cylinder_pos + renpy.random.randint(-4, 4)
                    cylinder = Transform(child = self.lock_cylinder_image, subpixel = True, rotate = angle1)
                    tension = Transform(child = self.lock_tension_image, subpixel = True, rotate = angle2)
                    
                    self.pick_can_rotate = False
                    
                    global lockpicks
                    global set_timers
                    global timers
                    
                    if set_timers == False:
                        timers = at
                        set_timers = True
                    
                    if set_timers == True:
                        if at > timers + self.breakage:
                            renpy.sound.stop(channel = "yn_lock_move")
                            renpy.sound.play("yn/sounds/sfx/lock_pick_break.mp3", channel = "yn_lock_click")
                            renpy.notify("Broke a lock pick!")
                            mispick = renpy.random.randint(-30, 30)
                            pick = Transform(child = self.lock_pick_image, rotate = self.pick_pos + (2 * mispick), subpixel = True)
                            self.pick_can_rotate = False
                            pygame.time.wait(200)
                            self.pick_broke = True
                            self.cylinder_try_rotate = False
                            lockpicks -= 1
                            timers = 0
                            set_timers = False
                            pygame.mouse.set_pos([self.width / 2, self.width / 4])
                            pygame.time.wait(100)
            
            else:
                if self.cylinder_released == True:
                    if self.cylinder_pos > 15:
                        renpy.sound.play("yn/sounds/sfx/lock_moving_back.mp3", channel = "yn_lock_click")
                    
                    self.pick_can_rotate = True
                    self.cylinder_pos -= (5 * st) / (at + 1)
                    
                    if self.cylinder_pos < self.cylinder_min:
                        self.cylinder_pos = self.cylinder_min
                        self.cylinder_released = False
                        renpy.sound.stop(channel = "yn_lock_click")
                
                cylinder = Transform(child = self.lock_cylinder_image, rotate = self.cylinder_pos, subpixel = True)
                tension = Transform(child = self.lock_tension_image, rotate = self.cylinder_pos, subpixel = True)
            
            lock_plate_render = renpy.render(self.lock_plate_image, width, height, st, at)
            lock_cylinder_render = renpy.render(cylinder, width, height, st, at)
            lock_tension_render = renpy.render(tension, width, height, st, at)
            lock_pick_render = renpy.render(pick, width, height, st, at)
            
            render = renpy.Render(self.width, self.width)
            
            render.blit(lock_plate_render, (0, 0))
            render.blit(lock_cylinder_render, (-self.offset, -self.offset))
            render.blit(lock_tension_render, (-self.offset, -self.offset))
            render.blit(lock_pick_render, (-self.offset, -self.offset))
            
            renpy.redraw(self, 0)
            
            return render
        
        def reset(self):
            self.cylinder_min = 0
            self.cylinder_max = 90
            self.cylinder_pos = 0
            self.cylinder_try_rotate = False
            self.cylinder_can_rotate = False 
            self.pick_min = 0
            self.pick_max = 180
            self.pick_pos = 90
            self.sweet_spot = renpy.random.randint(0, 180)

    def str_to_class(str):
        return getattr(sys.modules[__name__], str)

init python:
    def counter(st, at):
        f = 0.0
        
        if hasattr(store, "display_pos"):
            f = store.display_pos
        
        return Text("%.1f" % f, color="#09c", size=30), .1

    def counter2(st, at):
        f = 0.0
        
        if hasattr(store, "display_spot"):
            f = store.display_spot
        
        return Text("%.1f" % f, color = "#09c", size = 30), .1

image counter = DynamicDisplayable(counter)
image counter2 = DynamicDisplayable(counter2)

default display_pos = 0
default display_spot = 0
default timers = 0
default set_timers = 0
default current_chest = None

image lock_dark = Solid("#000c")
image lock_plate = "yn/images/mini_games/lockpicking/lock_plate.png"
image lock_cylinder = "yn/images/mini_games/lockpicking/lock_cylinder.png"
image lock_tension = "yn/images/mini_games/lockpicking/lock_tension.png"
image lock_pick = "yn/images/mini_games/lockpicking/lock_pick.png"

image lock_chest1_closed = "yn/images/mini_games/lockpicking/lock_chest1_closed.png"
image lock_chest1_hover = "yn/images/mini_games/lockpicking/lock_chest1_hover.png"
image lock_chest1_open = "yn/images/mini_games/lockpicking/lock_chest1_open.png"
image lock_chest1_open_hover = "yn/images/mini_games/lockpicking/lock_chest1_open_hover.png"

default lock_chest1_lock = YnLockpickingMinigame(20)
default lock_chest1_have_key = False
default lock_chest1_opened = False

default lockpicks = 5

screen click_chest(chest1_name, chest2_name=None, chest3_name=None, chest4_name=None, chest5_name=None):
    if str_to_class("{}_opened".format(chest1_name)) != True:
        imagebutton:
            idle "yn/images/mini_games/lockpicking/{}_closed.png".format(chest1_name)
            hover "yn/images/mini_games/lockpicking/{}_hover.png".format(chest1_name)
            focus_mask True
            action Show("pick_choose", dissolve, chest1_name)

    else:
        imagebutton:
            idle "yn/images/mini_games/lockpicking/{}_open.png".format(chest1_name)
            hover "yn/images/mini_games/lockpicking/{}_open_hover.png".format(chest1_name)
            focus_mask True
            action Show("pick_choose", dissolve, chest1_name)

screen pick_choose(chest_name):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 300

        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 50

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 60

            textbutton "Отмычки: [lockpicks]":
                xalign 0.8
                action [Function(str_to_class('{}_lock'.format(chest_name)).reset), SetVariable("current_chest", chest_name), Hide("pick_choose"), Show("lockpicking", dissolve, str_to_class('{}_lock'.format(chest_name)), chest_name)]

screen lockpicking(lock, chest_name):
    modal True

    add "lock_dark"

    add lock:
        xalign 0.5
        yalign 0.5

    vbox:
        hbox:
            label "Отмычки: [lockpicks]"












screen temp_screen(chest_name):
    on "show":
        action [SetVariable('{}_opened'.format(chest_name), True), Hide("temp_screen")]



label opened_chest:
    show screen temp_screen(current_chest)
    hide screen lockpicking
    with dissolve
    "You opened the chest!"
    window hide
    pause(1.0)
    $ current_chest = None

    jump start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
