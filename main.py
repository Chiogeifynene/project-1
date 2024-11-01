from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from random import randint, uniform
from kivy.core.audio import SoundLoader
from pydub import AudioSegment

Window.size = (800, 600)


class Player(Widget):
    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    speed = NumericProperty(10)
    frame_width = NumericProperty(128)
    frame_height = NumericProperty(128)
    frame_index = NumericProperty(0)
    frame_index2 = NumericProperty(8)
    frame_index3 = NumericProperty(4)
    frame_num = NumericProperty(0)
    frame_num1 = NumericProperty(7)
    frame_num2 = NumericProperty(4)
    frame_num3 = NumericProperty(4)
    frame_num4 = NumericProperty(8)
    frame_num5 = NumericProperty(8)
    frame_num6 = NumericProperty(13)
    frame_num7 = NumericProperty(4)
    frame_source = StringProperty("")
    frame_state = StringProperty("")
    s1 = StringProperty("images/Idle.png")
    s2 = StringProperty("images/Dead.png")
    s3 = StringProperty("images/Shot_2.png")
    s4 = StringProperty("images/Run_5.png")
    s5 = StringProperty("images/Run_25.png")
    s6 = StringProperty("images/Recharge.png")
    s7 = StringProperty("images/Shot_25.png")

    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (self.frame_width, self.frame_height)
        self.pos = (self.pos[0], self.pos[1])
        Clock.schedule_interval(self.update_state, 0.1)
        with self.canvas:
            Color(1, 1, 1)
            self.player = Rectangle(source=self.frame_source, pos=self.pos, size=self.size, frame_num=self.frame_num)
        self.frame_state = "idle"

    def update_state(self, dt):
        if self.frame_state == "idle":
            self.frame_index += 1
            if self.frame_index >= self.frame_num1:
                self.frame_index = 0
            self.player.pos = self.pos
            self.player.source = self.s1
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region((self.frame_index%self.frame_num1)*self.frame_width, 0, self.frame_width, self.frame_height)
        if self.frame_state == "dead":
            self.frame_index += 1
            if self.frame_index >= self.frame_num2:
                self.frame_index = 0
            self.player.pos = self.pos
            self.player.source = self.s2
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region(
                (self.frame_index % self.frame_num2) * self.frame_width, 0, self.frame_width, self.frame_height)
        if self.frame_state == "shooting":
            self.frame_index += 1
            if self.frame_index >= self.frame_num3:
                self.frame_index = 0
            self.player.pos = self.pos
            self.player.source = self.s3
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region(
                (self.frame_index % self.frame_num3) * self.frame_width, 0, self.frame_width, self.frame_height)
        if self.frame_state == "shooting_2":
            self.frame_index3 -= 1
            if self.frame_index3 <= 0:
                self.frame_index3 = self.frame_num7
            self.player.pos = self.pos
            self.player.source = self.s7
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region(
                (self.frame_index3 % self.frame_num7) * self.frame_width, 0, self.frame_width, self.frame_height)
        if self.frame_state == "run_right":
            self.frame_index += 1
            if self.frame_index >= self.frame_num4:
                self.frame_index = 0
            self.player.pos = self.pos
            self.player.source = self.s4
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region(
                (self.frame_index % self.frame_num4) * self.frame_width, 0, self.frame_width, self.frame_height)
        if self.frame_state == "run_left":
            self.frame_index2 -= 1
            if self.frame_index2 <= 0:
                self.frame_index2 = self.frame_num5
            self.player.source = self.s5
            self.player.pos = self.pos
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region((self.frame_index2 % self.frame_num5) * self.frame_width, 0, self.frame_width, self.frame_height)
        if self.frame_state == "reload":
            self.frame_index += 1
            if self.frame_index >= self.frame_num6:
                self.frame_index = 0
            self.player.pos = self.pos
            self.player.source = self.s6
            self.player.size = self.size
            self.player.texture = self.player.texture.get_region(
                (self.frame_index % self.frame_num6) * self.frame_width, 0, self.frame_width, self.frame_height)

    def move_player(self):
        self.x += self.vel_x
        self.y += self.vel_y


class Zombies(Widget):
    source = StringProperty("")
    s1 = StringProperty("images/Walk_2.png")
    s2 = StringProperty("images/Run_3.png")
    s3 = StringProperty("images/Walk_4.png")
    s4 = StringProperty("images/Run_2.png")
    s5 = StringProperty("images/Run_3.png")
    s6 = StringProperty("images/Run_4.png")
    s7 = StringProperty("images/Hurt_2.png")
    s8 = StringProperty("images/Hurt_3.png")
    s9 = StringProperty("images/Hurt_4.png")
    s10 = StringProperty("images/Dead_2.png")
    s11 = StringProperty("images/Dead_3.png")
    s12 = StringProperty("images/Dead_4.png")
    s13 = StringProperty("images/Attack_12.png")
    s14 = StringProperty("images/Attack_23.png")
    s15 = StringProperty("images/Attack_4.png")
    # zombie 1
    frame_width1 = NumericProperty(96)
    frame_height1 = NumericProperty(96)
    frame_index1 = NumericProperty(8)
    frame_num1 = NumericProperty(8)
    frame_index2 = NumericProperty(7)
    frame_num2 = NumericProperty(7)
    frame_index3 = NumericProperty(3)
    frame_num3 = NumericProperty(3)
    frame_index4 = NumericProperty(5)
    frame_num4 = NumericProperty(5)
    frame_index5 = NumericProperty(5)
    frame_num5 = NumericProperty(5)
    # zombie 2
    frame_index6 = NumericProperty(8)
    frame_num6 = NumericProperty(8)
    frame_index7 = NumericProperty(8)
    frame_num7 = NumericProperty(8)
    frame_index8 = NumericProperty(5)
    frame_num8 = NumericProperty(5)
    frame_index9 = NumericProperty(5)
    frame_num9 = NumericProperty(5)
    frame_index10 = NumericProperty(4)
    frame_num10 = NumericProperty(4)
    # zombie 3
    frame_index11 = NumericProperty(7)
    frame_num11 = NumericProperty(7)
    frame_index12 = NumericProperty(7)
    frame_num12 = NumericProperty(7)
    frame_index13 = NumericProperty(3)
    frame_num13 = NumericProperty(3)
    frame_index14 = NumericProperty(5)
    frame_num14 = NumericProperty(5)
    frame_index15 = NumericProperty(4)
    frame_num15 = NumericProperty(4)
    state = StringProperty("")
    species = StringProperty("")
    zombie_health = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Zombies, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (self.frame_width1, self.frame_height1)
        self.pos = (self.pos[0], self.pos[1])
        self.type = type
        self.speed = self.get_speed()
        self.health = self.get_health()
        self.damage = self.get_damage()
        with self.canvas:
            Color(1, 1, 1)
            self.zombie = Rectangle(source=self.source, size=self.size, pos=self.pos)

        Clock.schedule_interval(self.update_state, 0.1)

        self.state = "walk_1"

    def zombie_type1(self):
        self.species = "man"
        self.zombie.pos = self.pos
        self.zombie.size = self.size
#
    def zombie_type2(self):
        self.species = "woman"
        self.zombie.pos = self.pos
        self.zombie.size = self.size

    def zombie_type3(self):
        self.species = "crawler"
        self.zombie.pos = self.pos
        self.zombie.size = self.size


    def get_speed(self):
        if self.type == "man":
            speed = 0.2
            return speed
        elif self.type == "woman":
            speed = 0.5
            return speed
        elif self.type == "crawler":
            speed = 0.8
            return speed

    def get_health(self):
        if self.type == "man":
            return 10
        elif self.type == "woman":
            return 20
        elif self.type == "crawler":
            return 30

    def get_damage(self):
        if self.type == "man":
            return 5
        elif self.type == "woman":
            return 10
        elif self.type == "crawler":
            return 15

    def kill_zombie(self, damage):
        self.zombie_health -= damage
        if self.zombie_health <= 0:
            return True
        return False

    def update_state(self, dt):
        if self.state == "dead_1":
            self.frame_index4 -= 1
            if self.frame_index4 <= 0:
                self.frame_index4 = self.frame_num4
            self.zombie.source = self.s10
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index4 % self.frame_num4) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "dead_2":
            self.frame_index9 -= 1
            if self.frame_index9 <= 0:
                self.frame_index9 = self.frame_num9
            self.zombie.source = self.s11
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index9 % self.frame_num9) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "dead_3":
            self.frame_index14 -= 1
            if self.frame_index14 <= 0:
                self.frame_index14 = self.frame_num14
            self.zombie.source = self.s12
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index14 % self.frame_num14) * self.frame_width1, 0, self.frame_width1, self.frame_height1)

        # zombie 1
        if self.state == "walk_1":
            self.frame_index1 -= 1
            if self.frame_index1 <= 0:
                self.frame_index1 = self.frame_num1
            self.zombie.source = self.s1
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region((self.frame_index1%self.frame_num1) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "run_1":
            self.frame_index2 -= 1
            if self.frame_index2 <= 0:
                self.frame_index2 = self.frame_num2
            self.zombie.source = self.s4
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index2 % self.frame_num2) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "hurt_1":
            self.frame_index3 -= 1
            if self.frame_index3 <= 0:
                self.frame_index3 = self.frame_num3
            self.zombie.source = self.s7
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index3 % self.frame_num3) * self.frame_width1, 0, self.frame_width1, self.frame_height1)

        if self.state == "attack_1":
            self.frame_index5 -= 1
            if self.frame_index5 <= 0:
                self.frame_index5 = self.frame_num5
            self.zombie.source = self.s13
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index5 % self.frame_num5) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
            # zombie 2
        if self.state == "walk_2":
            self.frame_index6 -= 1
            if self.frame_index6 <= 0:
                self.frame_index6 = self.frame_num6
            self.zombie.source = self.s2
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index6 % self.frame_num6) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "run_2":
            self.frame_index7 -= 1
            if self.frame_index7 <= 0:
                self.frame_index7 = self.frame_num7
            self.zombie.source = self.s5
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index7 % self.frame_num7) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "hurt_2":
            self.frame_index8 -= 1
            if self.frame_index8 <= 0:
                self.frame_index8 = self.frame_num8
            self.zombie.source = self.s8
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index8 % self.frame_num8) * self.frame_width1, 0, self.frame_width1, self.frame_height1)

        if self.state == "attack_2":
            self.frame_index10 -= 1
            if self.frame_index10 <= 0:
                self.frame_index10 = self.frame_num10
            self.zombie.source = self.s14
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index10 % self.frame_num10) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
            # zombie 3
        if self.state == "walk_3":
            self.frame_index11 -= 1
            if self.frame_index11 <= 0:
                self.frame_index11 = self.frame_num11
            self.zombie.source = self.s3
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index11 % self.frame_num11) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "run_3":
            self.frame_index12 -= 1
            if self.frame_index12 <= 0:
                self.frame_index12 = self.frame_num12
            self.zombie.source = self.s6
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index12 % self.frame_num12) * self.frame_width1, 0, self.frame_width1, self.frame_height1)
        if self.state == "hurt_3":
            self.frame_index13 -= 1
            if self.frame_index13 <= 0:
                self.frame_index13 = self.frame_num13
            self.zombie.source = self.s9
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index13 % self.frame_num13) * self.frame_width1, 0, self.frame_width1, self.frame_height1)

        if self.state == "attack_3":
            self.frame_index15 -= 1
            if self.frame_index15 <= 0:
                self.frame_index15 = self.frame_num15
            self.zombie.source = self.s15
            self.zombie.pos = self.pos
            self.zombie.size = self.size
            self.zombie.texture = self.zombie.texture.get_region(
                (self.frame_index15 % self.frame_num15) * self.frame_width1, 0, self.frame_width1, self.frame_height1)


class Bullet(Widget):
    bullet_width = NumericProperty(100)
    bullet_height = NumericProperty(50)
    bulet = ObjectProperty(None)
    source = StringProperty("")
    bullet_speed = NumericProperty(5)

    def __init__(self, **kwargs):
        super(Bullet, self).__init__(**kwargs)
        self.size = (self.bullet_width, self.bullet_height)
        self.pos = (self.pos[0], self.pos[1])
        self.type = type
        self.vel = 10
        with self.canvas:
            self.rect = Rectangle(source="images/Light_Shell2.png", size=self.size, pos=self.pos)

    def fire_bullet(self):
        if self.type == "right":
            self.pos[0] += self.vel
        elif self.type == "left":
            self.pos[0] -= self.vel
        self.rect.pos = self.pos


class Items(Widget):
    source = StringProperty("")
    item = StringProperty("")
    life = ObjectProperty(None)
    Building_life = ObjectProperty(None)
    item_top = NumericProperty(80)
    item_bottom = NumericProperty(80)
    vel_x = NumericProperty(1.5)

    def __init__(self, **kwargs):
        super(Items, self).__init__(**kwargs)
        self.size = (self.item_top, self.item_bottom)
        self.pos = self.pos
        with self.canvas:
            Color(1, 1, 1)
            self.rect = Rectangle(source=self.source, pos=self.pos, size=self.size)

    def coin(self):
        self.item = "coin"
        self.rect.source = "images/Coin_A.png"
        self.rect.pos = self.pos
        self.rect.size = self.size

    def health(self):
        self.item = "health"
        self.rect.source = "images/HP_icon.png"
        self.rect.pos = self.pos
        self.rect.size = self.size

    def bomb(self):
        self.item = "bomb"
        self.rect.source = "images/Bomb_A.png"
        self.rect.pos = self.pos
        self.rect.size = self.size

    def move(self):
        self.pos[0] -= self.vel_x
        self.rect.pos = self.pos


class GameOverScreen(Widget):

    def __init__(self, **kwargs):
        super(GameOverScreen, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        super().on_touch_down(touch)


class LoadingScreen(Widget):

    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        super().on_touch_down(touch)

    def update_progress(self, dt):
        if self.ids._loading_screen_progressbar.value < 100:
            self.ids._loading_screen_progressbar.value += 10 * dt
        else:
            self.ids._button_start.disabled = False


class DefenderGame(Widget):
    bullet1 = ObjectProperty(None)
    bullet2 = ObjectProperty(None)
    zombie1 = ObjectProperty(None)
    zombie2 = ObjectProperty(None)
    zombie3 = ObjectProperty(None)
    item1 = ObjectProperty(None)
    item2 = ObjectProperty(None)
    item3 = ObjectProperty(None)
    actor = ObjectProperty(None)
    bg_text = ObjectProperty(None)
    st_text = ObjectProperty(None)
    green_text = ObjectProperty(None)
    blue_text = ObjectProperty(None)
    brown_text = ObjectProperty(None)
    white_text = ObjectProperty(None)
    bone_text = ObjectProperty(None)
    water_text = ObjectProperty(None)
    sand_text = ObjectProperty(None)
    hurt_text = ObjectProperty(None)
    barrow_text = ObjectProperty(None)
    tree_text = ObjectProperty(None)
    stone_text = ObjectProperty(None)
    adding_zombie = NumericProperty(0)
    difficulty = NumericProperty(0)
    zombie = []
    items = []
    bullets = []
    zombie_rage = NumericProperty(0)
    zombie_rage_text = StringProperty("")
    player_house_life = NumericProperty(100)
    house_revive = StringProperty("")
    player_life = NumericProperty(100)
    player_timing = NumericProperty(0)
    player_score = NumericProperty(0)
    player_coin = NumericProperty(0)
    player_kills = NumericProperty(0)
    player_kills_status = StringProperty("PLAYER KILLS")
    coin_status = StringProperty("TOWN HEALTH")
    state_game_over = False
    state_game_has_started = False
    game_pause_state = False
    sound = True
    loading_screen = ObjectProperty(None)
    game_over_screen = ObjectProperty(None)
    sounds = []

    def __init__(self, **kwargs):
        super(DefenderGame, self).__init__(**kwargs)
        self.fence_text = Image(source="").texture
        self.st_text = Image(source="images/decor_1.png").texture
        self.bg_text = Image(source="images/bg.png").texture
        self.blue_text = Image(source="images/Blue-gray_ruins1.png").texture
        self.barrow_text = Image(source="images/decor_8.png").texture
        self.tree_text = Image(source="images/tree_9.png").texture
        self.stone_text = Image(source="images/stones_9.png").texture
        self.hurt_text = Image(source="images/decor_2.png").texture
        self.brown_text = Image(source="images/Brown-gray_ruins1.png").texture
        self.green_text = Image(source="images/greenery_6.png").texture
        self.water_text = Image(source="images/Puddle_02.png").texture
        self.bone_text = Image(source="images/Monster_fish_bones_shadow1.png").texture
        self.colliding = False
        self.is_colliding = False
        self.item_collide = False
        self.item_collide_zombie = False
        self.is_paused = False
        self.is_playing = False
        self.adding_zombie = 0
        self.difficulty = 0
        self.zombie_death_delay = 0
        self.shooting_bullet = 0
        self.disappear = 0
        self.appear = 0
        self.zombie_life = 100
        self.sound_timer1 = 0
        self.is_alive = False
        self.is_loading = False
        self.is_not_sounding = False
        self.is_dead = False

        Clock.schedule_interval(self.update_progress, 0.1)

        self.play_sound("sounds/defeat-background-39613.wav")
        # sounds for the game
        # background sound
        self.back_sound = SoundLoader.load("sounds/relaxing-guitar-loop-v5-245859.wav")
        self.back_sound.loop = True
        self.sounds.append(self.back_sound)
        # shooting sound
        self.shooting_sound = SoundLoader.load("sounds/shoot-2-81137.wav")
        self.sounds.append(self.shooting_sound)
        # man hurt sound
        self.hurt_sound = SoundLoader.load("sounds/ough-47202.wav")
        self.sounds.append(self.hurt_sound)
        # man running
        self.running_sound = SoundLoader.load("sounds/running-soundscape-200116.wav")
        self.sounds.append(self.running_sound)
        # game loading sound
        self.game_loading_sound = SoundLoader.load("sounds/defeat-background-39613.wav")
        self.sounds.append(self.game_loading_sound)
        # coin, bomb, life, house repair items sound
        self.life_sound = SoundLoader.load("sounds/8-bit-video-game-points-version-1-145826.wav")
        self.sounds.append(self.life_sound)
        self.coin_sound = SoundLoader.load("sounds/coins27-36030.wav")
        self.sounds.append(self.coin_sound)
        self.bomb_sound = SoundLoader.load("sounds/explosion-42132.wav")
        self.sounds.append(self.bomb_sound)
        self.house_repair_sound = SoundLoader.load("sounds/hammer-or-mace-melee-weapon-impact-236208.wav")
        self.sounds.append(self.house_repair_sound)

        # zombie live and dead sounds
        self.zombie1_sound = SoundLoader.load("sounds/scary-monster-growl-roar-2-199380.wav")
        self.sounds.append(self.zombie1_sound)
        self.zombie2_sound = SoundLoader.load("sounds/scary-scream-193752.wav")
        self.sounds.append(self.zombie2_sound)
        self.zombie1_death_sound = SoundLoader.load("sounds/zombie-pain-1-95166.wav")
        self.sounds.append(self.zombie1_death_sound)
        self.zombie2_death_sound = SoundLoader.load("sounds/goblin-death-6729.wav")
        self.sounds.append(self.zombie2_death_sound)
        self.zombie3_death_sound = SoundLoader.load("sounds/zombie-screaming-207590.wav")
        self.sounds.append(self.zombie3_death_sound)
        self.zombie_rage_sound = SoundLoader.load("sounds/alert-in-war-rpg-italian-83264.wav")
        self.sounds.append(self.zombie3_death_sound)
        # game over sound
        self.game_over_sound = SoundLoader.load("sounds/dun-dun-dun-252946.wav")
        self.sounds.append(self.game_over_sound)

        self.actor = Player()
        self.actor.size_hint = (None, None)
        self.actor.size = (self.x + 150, self.x + 170)
        self.actor.pos = (self.x + 200, self.y + 300)
        self.add_widget(self.actor)
        self.actor.opacity = 0

        self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self.keyboard.bind(on_key_down=self.on_keyboard_down)
        self.keyboard.bind(on_key_up=self.on_keyboard_up)

    def update_progress(self, dt):
        if self.ids._loading_screen_progressbar.value < 100:
            self.ids._loading_screen_progressbar.value += 10 * dt
        else:
            self.ids._button_start.disabled = False
            self.ids._loading_screen_label3.text = "GO PROTECT HUMANITY"

    def load_game(self):
        self.state_game_has_started = True
        self.state_game_over = False
        self.actor.opacity = 1
        self.loading_screen.opacity = 0
        self.game_over_screen.opacity = 0
        self.zombie_rage = 0
        self.adding_zombie = 0
        self.zombie_rage_text = ""
        self.player_house_life = 100
        self.house_revive = ""
        self.player_life = 100
        self.player_timing = 0
        self.player_score = 0
        self.player_coin = 0
        self.player_kills = 0
        self.back_sound.play()
        self.stop_loop("sounds/defeat-background-39613.wav")

        Clock.unschedule(self.update_progress, 0)

    def restart_game(self):
        self.game_over_screen.opacity = 0
        self.loading_screen.opacity = 1
        Clock.schedule_interval(self.update_progress, 0.1)
        self.ids._button_start.disabled = True
        self.ids._loading_screen_label3.text = "Game Loading..."
        self.play_sound("sounds/defeat-background-39613.wav")

    def paused_state(self):
        if not self.game_pause_state:
            self.game_pause_state = True
        elif self.game_pause_state:
            self.game_pause_state = False

    def convert_mp3_to_wav(self, mp3_file, wav_file):
        sound = AudioSegment.from_mp3(mp3_file)
        sound.export(wav_file, format="wav")

    def _keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard = None

    def on_keyboard_up(self, text, modifiers):
        if not self.state_game_over and self.state_game_has_started:
            self.actor.frame_state = "idle"
            self.running_sound.stop()
            self.coin_status = "TOWN HEALTH"

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            if keycode[1] == "left":
                self.actor.frame_state = "run_left"
                self.actor.pos[0] -= 3
                self.running_sound.play()
            if keycode[1] == "right":
                self.actor.frame_state = "run_right"
                self.actor.pos[0] += 3
                self.running_sound.play()
            if keycode[1] == "up":
                self.actor.frame_state = "run_right"
                self.actor.pos[1] += 3
                self.running_sound.play()
            if keycode[1] == "down":
                self.actor.pos[1] -= 3
                self.actor.frame_state = "run_right"
                self.running_sound.play()
            if keycode[1] == "a":
                self.actor.frame_state = "shooting"
                if self.shooting_bullet < 1:
                    self.create_bullets()
                    self.add_widget(self.bullet1)
                    self.shooting_sound.play()
            if keycode[1] == "x":
                if self.player_kills >= 50:
                    for zombie in self.zombie:
                        if zombie.pos[0] <= Window.width - 50:
                            if zombie in self.zombie:
                                self.zombie.remove(zombie)
                                self.remove_widget(zombie)
                                self.player_kills = 0
                                self.bomb_sound.play()
                                self.player_kills_status = "PLAYER KILLS"
                                self.ids._main_label5.color = (1, 1, 1, 1)
                elif self.player_kills <= 50:
                    self.player_kills_status = "NOT ENOUGH"
            if keycode[1] == "d":
                if self.player_coin >= 200:
                    self.player_house_life = 100
                    self.player_coin -= 200
                    self.coin_status = "REVIVE SUCCESSFUL"
                    self.house_repair_sound.play()
                elif self.player_coin < 200:
                    self.coin_status = "NOT ENOUGH COINS"

    def play_sound(self, file):
        if self.sound:
            sound = SoundLoader.load(file)
            sound.play()

    def loop_sounds(self, file):
        if self.sound:
            sound = SoundLoader.load(file)
            sound.loop = True
            sound.play()

    def stop_loop(self, file):
        if self.sound:
            sound = SoundLoader.load(file)
            sound.loop = False
            sound.stop()

    def create_bullets(self):
        self.bullet1 = Bullet(pos=(self.actor.center_x + 15, self.actor.center_y - 42))
        self.bullet1.type = "right"
        self.bullets.append(self.bullet1)

        self.bullet2 = Bullet(pos=(self.actor.center_x - 115, self.actor.center_y - 42))
        self.bullet2.type = "left"
        self.bullets.append(self.bullet2)

    def create_zombies(self):
        self.zombie1 = Zombies(pos=(Window.width, randint(self.y + 150, Window.height - 100)))
        self.zombie1.size_hint = (0.2, 0.2)
        self.zombie1.state = "walk_1"
        self.zombie1.type = "man"
        self.zombie1.zombie_type1()
        self.zombie.append(self.zombie1)
#

        self.zombie2 = Zombies(pos=(Window.width, randint(self.y + 150, Window.height - 100)))
        self.zombie2.size_hint = (0.2, 0.2)
        self.zombie2.state = "walk_2"
        self.zombie2.type = "crawler"
        self.zombie2.zombie_type2()
        self.zombie.append(self.zombie2)
#

        self.zombie3 = Zombies(pos=(Window.width, randint(self.y + 150, Window.height - 100)))
        self.zombie3.size_hint = (0.2, 0.2)
        self.zombie3.state = "walk_3"
        self.zombie3.type = "woman"
        self.zombie3.zombie_type3()
        self.zombie.append(self.zombie3)
#

    def create_item1(self):
        self.item1 = Items(pos=(Window.width, randint(self.y + 100, Window.height - 100)))
        self.item1.size_hint = (None, None)
        self.item1.size = (self.x + 70, self.x + 70)
        self.item1.coin()
        self.items.append(self.item1)
        self.add_widget(self.item1)

    def create_item2(self):
        self.item2 = Items(pos=(Window.width, randint(self.y + 100, Window.height - 100)))
        self.item2.size_hint = (None, None)
        self.item2.size = (self.x + 50, self.x + 50)
        self.item2.health()
        self.items.append(self.item2)
        self.add_widget(self.item2)

    def create_item3(self):
        self.item3 = Items(pos=(Window.width, randint(self.y + 100, Window.height - 100)))
        self.item3.size_hint = (None, None)
        self.item3.size = (self.x + 50, self.x + 50)
        self.item3.bomb()
        self.items.append(self.item3)
        self.add_widget(self.item3)

    def add_zombies(self):
        if self.player_timing >= 60 and self.player_timing < 10800:
            self.adding_zombie += 2
        if self.player_timing >= 10800 and self.player_timing < 21600:
            self.adding_zombie += 3
        elif self.player_timing >= 21600 and self.player_timing < 32400:
            self.adding_zombie += 4
        elif self.player_timing >= 32400 and self.player_timing < 43200:
            self.adding_zombie += 5
        elif self.player_timing >= 43200 and self.player_timing < 54000:
            self.adding_zombie += 6
        elif self.player_timing >= 54000:
            self.adding_zombie += 7

        r = randint(1, 4)
        if self.adding_zombie >= 420:
            if r == 1:
                self.zombie1 = Zombies(pos=(self.width, uniform(self.y + 150, self.height - 100)))
                self.zombie1.size_hint = (None, None)
                self.zombie1.size = (self.x + 96, self.y + 96)
                self.zombie1.state = "walk_1"
                self.zombie1.type = "man"
                self.zombie.append(self.zombie1)
                self.add_widget(self.zombie1)
                self.adding_zombie = 0
            elif r == 2:
                self.zombie2 = Zombies(pos=(self.width, uniform(self.y + 150, self.height - 100)))
                self.zombie2.size_hint = (None, None)
                self.zombie2.size = (self.x + 96, self.y + 96)
                self.zombie2.state = "walk_2"
                self.zombie2.type = "crawler"
                self.zombie.append(self.zombie2)
                self.add_widget(self.zombie2)
                self.adding_zombie = 0
            elif r == 3:
                self.zombie3 = Zombies(pos=(self.width, uniform(self.y + 150, self.height - 100)))
                self.zombie3.size_hint = (None, None)
                self.zombie3.size = (self.x + 96, self.y + 96)
                self.zombie3.state = "walk_3"
                self.zombie3.type = "woman"
                self.zombie.append(self.zombie3)
                self.add_widget(self.zombie3)
                self.adding_zombie = 0

    def add_bullets(self):
        self.shooting_bullet += 1
        if self.shooting_bullet >= 30:
            self.shooting_bullet = 0
        if self.actor.frame_state == "shooting":
            if self.shooting_bullet < 1:
                self.create_bullets()
                self.add_widget(self.bullet1)
                self.shooting_sound.play()
        for bullet in self.bullets:
            bullet.fire_bullet()
            if bullet.pos[0] >= self.width:
                if bullet in self.bullets:
                    self.bullets.remove(bullet)
                    self.remove_widget(bullet)

    def add_items(self):
        self.appear += 1
        i = randint(1, 8)
        if self.appear == 300 and i == 1:
            self.create_item1()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 2:
            self.create_item1()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 3:
            self.create_item1()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 4:
            self.create_item1()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 5:
            self.create_item1()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 6:
            self.create_item2()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 7:
            self.create_item3()
            if self.appear >= 300:
                self.appear = 0
        elif self.appear == 300 and i == 8:
            self.create_item3()
            if self.appear >= 300:
                self.appear = 0

    def shoot_enemies_right(self):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            self.actor.frame_state = "shooting"

    def on_touch_down(self, touch):
        #if not self.state_game_over and self.state_game_has_started:
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            if touch.x < self.width - 300:
                if touch.dx > 0:
                    self.actor.frame_state = "run_right"
                    self.actor.pos[0] += 1
                    self.running_sound.play()
                if touch.dx < 0:
                    self.actor.frame_state = "run_left"
                    self.actor.pos[0] -= 1
                    self.running_sound.play()
                if touch.dy > 0:
                    self.actor.frame_state = "run_right"
                    self.actor.pos[1] += 1
                    self.running_sound.play()
                if touch.dy < 0:
                    self.actor.frame_state = "run_right"
                    self.actor.pos[1] -= 1
                    self.running_sound.play()
            if touch.x > self.width - 300:
                self.running_sound.stop()
            super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            self.actor.frame_state = "idle"
            self.running_sound.stop()
        super().on_touch_up(touch)

    def revive_house_strength(self):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            if self.player_coin >= 200:
                self.player_house_life = 100
                self.player_coin -= 200
                self.coin_status = "REVIVE SUCCESSFUL"
                self.house_repair_sound.play()
            elif self.player_coin < 200:
                self.coin_status = "NOT ENOUGH COINS"

    def button_released(self):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            self.coin_status = "TOWN HEALTH"

    def bomb_clear(self):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            if self.player_kills >= 50:
                for zombie in self.zombie:
                    if zombie.pos[0] <= Window.width - 50:
                        if zombie in self.zombie:
                            self.zombie.remove(zombie)
                            self.remove_widget(zombie)
                            self.player_kills = 0
                            self.bomb_sound.play()
                            self.player_kills_status = "PLAYER KILLS"
                            self.ids._main_label5.color = (1, 1, 1, 1)
            elif self.player_kills < 50:
                self.player_kills_status = "NOT ENOUGH"

    def zombie_sounds(self):
        self.sound_timer1 += 1
        z = randint(1, 2)
        if self.sound_timer1 == 3600:
            if z == 1:
                self.zombie1_sound.play()
            elif z == 2:
                self.zombie2_sound.play()
            if self.sound_timer1 >= 3600:
                self.sound_timer1 = 0

    def clear_objects(self):
        for zombie in self.zombie:
            self.remove_widget(zombie)
        for item in self.items:
            self.remove_widget(item)
        self.zombie = []
        self.items = []
        self.bullets = []

    def update(self, dt):
        if not self.state_game_over and self.state_game_has_started and not self.game_pause_state:
            self.player_timing += 1
            self.zombie_rage += 0.5
            if self.zombie_rage >= 3600:
                for zombie in self.zombie:
                    self.zombie_rage_text = "ZOMBIE RAGE"
                    zombie.pos[0] -= 40 * dt
                    self.zombie_rage_sound.play()
                if self.zombie_rage >= 5000:
                    self.zombie_rage = 0
                    self.zombie_rage_text = ""
                    self.zombie_rage_sound.stop()
            if self.player_score >= 0:
                self.ids._main_label3.text = "SURVIVOR"
                self.ids._main_label3.color = (1, 1, 1, 1)
            if self.player_score >= 1500:
                self.ids._main_label3.text = "UNDEAD EXECUTIONER"
                self.ids._main_label3.color = (0, 0, 1, 1)
            if self.player_score >= 5500:
                self.ids._main_label3.text = "SURVIVAL SPECIALIST"
                self.ids._main_label3.color = (0, 1, 0, 1)
            if self.player_score >= 15000:
                self.ids._main_label3.text = "LEGEND SLAYER"
                self.ids._main_label3.color = (0.5, 0, 0.5, 1)
            if self.player_score >= 25000:
                self.ids._main_label3.text = "MASTER OF UNDEAD"
                self.ids._main_label3.color = (1, 0, 0, 1)
            if self.player_score >= 50000:
                self.ids._main_label3.text = "CHAMPION OF HUMANITY"
                self.ids._main_label3.color = (1, 0.8, 0, 1)

            self.zombie_sounds()
            self.add_zombies()
            self.add_bullets()
            self.add_items()
            # check boundary of Player
            if self.actor.x <= self.x + 220:
                self.actor.x = self.x + 220
            elif self.actor.x >= self.width - 100:
                self.actor.x = self.width - 100
            if self.actor.y <= self.y + 110:
                self.actor.y = self.y + 110
            elif self.actor.y >= self.height - 90:
                self.actor.y = self.height - 90

        # checking zombies, items and bullets and moving them
        bul_pad = 30
        zom_pad = 28
        zom_pad_bottom = 15
        act_pad = 60
        act_top = 90
        act_bottom = 10
        item_pad = 20
        if not self.game_pause_state:
            for zombie in self.zombie:
                zombie.pos[0] -= zombie.get_speed()
                if zombie.pos[0] <= self.x + 150:
                    self.player_house_life -= 25
                    if self.player_house_life <= 0 and not self.state_game_over and self.state_game_has_started:
                        self.game_over_sound.play()
                        self.state_game_over = True
                        self.game_over_screen.opacity = 1
                        self.clear_objects()
                        self.actor.opacity = 0
                        self.back_sound.stop()
                        self.ids._loading_screen_progressbar.value = 0
                        self.actor.pos = (self.x + 200, self.y + 300)
                    if zombie in self.zombie:
                        self.zombie.remove(zombie)
                        self.remove_widget(zombie)

                if self.actor.collide_widget(zombie):
                    if not self.is_colliding:
                        if (zombie.pos[0] + zom_pad <= self.actor.pos[0] + self.actor.size[0] - act_pad and
                            zombie.pos[0] + zombie.size[0] - zom_pad >= self.actor.pos[0] + act_pad) and \
                                (zombie.pos[1] <= self.actor.pos[1] + self.actor.size[1] - act_top and zombie.pos[1] +
                                    zombie.size[1] - zom_pad >= self.actor.pos[1] + act_bottom):
                            self.hurt_sound.play()
                            self.player_life -= 10
                            if self.player_life <= 0 and not self.state_game_over and self.state_game_has_started:
                                self.game_over_sound.play()
                                self.state_game_over = True
                                self.game_over_screen.opacity = 1
                                self.clear_objects()
                                self.actor.opacity = 0
                                self.back_sound.stop()
                                self.ids._loading_screen_progressbar.value = 0
                                self.actor.pos = (self.x + 200, self.y + 300)
                            if zombie in self.zombie:
                                self.zombie.remove(zombie)
                                self.remove_widget(zombie)
                            self.is_colliding = True
                else:
                    if self.is_colliding:
                        self.is_colliding = False

                for bullet in self.bullets:
                    if bullet.collide_widget(zombie):
                        if not self.colliding:
                            if (zombie.pos[0] + zom_pad <= bullet.pos[0] + bullet.size[0] - bul_pad and
                                zombie.pos[0] + zombie.size[0] - zom_pad >= bullet.pos[0] + bul_pad) and \
                                    (zombie.pos[1] <= bullet.pos[1] + bullet.size[1] - bul_pad and zombie.pos[1] + zombie.size[
                                        1] - zom_pad >= bullet.pos[1] + bul_pad):
                                if zombie.state == "walk_1":
                                    self.zombie1_death_sound.play()
                                if zombie.state == "walk_2":
                                    self.zombie2_death_sound.play()
                                if zombie.state == "walk_3":
                                    self.zombie3_death_sound.play()
                                if zombie in self.zombie:
                                    self.zombie.remove(zombie)
                                    self.remove_widget(zombie)
                                    self.player_score += 10
                                    self.player_kills += 1
                                    self.player_kills_status = "PLAYER KILLS"
                                    if self.player_kills >= 50:
                                        self.player_kills_status = "GRENADE"
                                        self.ids._main_label5.color = (1, 0, 0, 1)
                                        if self.player_kills >= 60:
                                            self.player_kills = 0
                                            self.ids._main_label5.color = (1, 1, 1, 1)

                                if bullet in self.bullets:
                                    self.bullets.remove(bullet)
                                    self.remove_widget(bullet)
                                self.colliding = True
                    else:
                        if self.colliding:
                            self.colliding = False

            for item in self.items:
                item.move()
                if item.pos[0] <= self.x + 150:
                    if item in self.items:
                        self.items.remove(item)
                        self.remove_widget(item)
                if item.collide_widget(self.actor):
                    if not self.item_collide:
                        if (item.pos[0] + item_pad <= self.actor.pos[0] + self.actor.size[0] - act_pad and
                            item.pos[0] + item.size[0] - item_pad >= self.actor.pos[0] + act_pad) and \
                                (item.pos[1] <= self.actor.pos[1] + self.actor.size[1] - act_top and item.pos[1] +
                                 item.size[1] - item_pad >= self.actor.pos[1] + act_bottom):
                            if item.item == "coin":
                                self.coin_sound.play()
                                self.player_coin += 20
                                if item in self.items:
                                    self.items.remove(item)
                                    self.remove_widget(item)
                            elif item.item == "health":
                                if self.player_life < 100:
                                    self.life_sound.play()
                                    self.player_life += 10
                                    if item in self.items:
                                        self.items.remove(item)
                                        self.remove_widget(item)
                            elif item.item == "bomb":
                                self.hurt_sound.play()
                                self.player_life -= 1
                                item.rect.source = "images/Explosion_A_03.png"
                                if self.player_life <= 0 and not self.state_game_over and self.state_game_has_started:
                                    self.game_over_sound.play()
                                    self.state_game_over = True
                                    self.game_over_screen.opacity = 1
                                    self.clear_objects()
                                    self.actor.opacity = 0
                                    self.ids._loading_screen_progressbar.value = 0
                                    self.back_sound.stop()
                                    self.actor.pos = (self.x + 200, self.y + 300)
                            self.item_collide = True
                else:
                    if self.item_collide:
                        self.actor.frame_state = "idle"
                        if item.rect.source == "images/Explosion_A_03.png":
                            if item in self.items:
                                self.items.remove(item)
                                self.remove_widget(item)
                        self.item_collide = False

                for zombie in self.zombie:
                    if item.collide_widget(zombie):
                        if not self.item_collide_zombie:
                            if (item.pos[0] + item_pad <= zombie.pos[0] + zombie.size[0] - zom_pad and
                                item.pos[0] + item.size[0] - item_pad >= zombie.pos[0] + zom_pad) and \
                                    (item.pos[1] <= zombie.pos[1] + zombie.size[1] - zom_pad and item.pos[1] +
                                     item.size[1] - item_pad >= zombie.pos[1] + zom_pad_bottom):
                                if item.item == "bomb":
                                    if zombie.state == "walk_1":
                                        self.zombie1_death_sound.play()
                                    elif zombie.state == "walk_2":
                                        self.zombie2_death_sound.play()
                                    elif zombie.state == "walk_3":
                                        self.zombie3_death_sound.play()
                                    item.rect.source = "images/Explosion_A_03.png"
                                    if item in self.items:
                                        self.items.remove(item)
                                        self.remove_widget(item)
                                    if zombie in self.zombie:
                                        self.zombie.remove(zombie)
                                        self.remove_widget(zombie)
                                self.item_collide_zombie = True
                    else:
                        if self.item_collide_zombie:
                            self.item_collide_zombie = False


class MainApp(App):
    def build(self):
        game = DefenderGame()
        Clock.schedule_interval(game.update, 1/60)
        return game

    def exit_game(self):
        self.stop()


if __name__ == "__main__":
    MainApp().run()
