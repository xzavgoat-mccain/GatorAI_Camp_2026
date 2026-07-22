import pygame
import os


class SansFight:
    """A lightweight Undertale-style Sans battle encounter triggered by interacting with Sans."""

    def __init__(self, surface):
        self.surface = surface
        self.active = False
        self.state = "idle"
        self.timer = 0.0
        self.font = None
        self.sans_color = (255, 255, 255)
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.message = "* You feel a terrible chill..."
        self.bones = []
        self.player_y = 360
        self.player_speed = 220
        self.phase = 0
        self._init_font()

    def _init_font(self):
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            font_path = os.path.join(base_path, "font", "LycheeSoda.ttf")
            self.font = pygame.font.Font(font_path, 28)
        except Exception:
            self.font = pygame.font.SysFont(None, 28)

    def start(self):
        self.active = True
        self.state = "intro"
        self.timer = 0.0
        self.bones = []
        self.player_y = 360
        self.phase = 0
        self.message = "* You feel a terrible chill..."

    def update(self, dt, events=None):
        if not self.active:
            return

        if events is None:
            events = []

        if self.state == "intro":
            self.timer += dt
            if self.timer > 1.2:
                self.state = "fight"
                self.message = "* SANS is preparing a bad time."
        elif self.state == "fight":
            self.timer += dt
            if self.timer > 0.35:
                self.timer = 0.0
                self._spawn_bone()
            self._move_player(dt)
            if self.phase >= 5:
                self.state = "outro"
                self.message = "* The battle ends."
        elif self.state == "outro":
            self.timer += dt
            if self.timer > 1.0:
                self.active = False

    def _spawn_bone(self):
        self.bones.append({"x": 640, "y": 180 + (self.phase % 3) * 80, "speed": 260 + self.phase * 20})
        self.phase += 1

    def _move_player(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player_y = max(120, self.player_y - self.player_speed * dt)
        if keys[pygame.K_DOWN]:
            self.player_y = min(420, self.player_y + self.player_speed * dt)

    def draw(self):
        if not self.active:
            return

        self.surface.fill(self.bg_color)
        sans_text = self.font.render("SANS", True, self.sans_color)
        self.surface.blit(sans_text, (260, 120))

        pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(220, self.player_y, 24, 24))

        for bone in list(self.bones):
            bone["x"] -= bone["speed"] * 0.016
            pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(int(bone["x"]), int(bone["y"]), 24, 12))
            if bone["x"] < -40:
                self.bones.remove(bone)

        text_surface = self.font.render(self.message, True, self.text_color)
        self.surface.blit(text_surface, (40, 420))

    def handle_event(self, event):
        if not self.active:
            return
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.active = False
