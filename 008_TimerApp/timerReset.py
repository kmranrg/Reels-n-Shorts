import flet as ft
from time import sleep

class TimerApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.seconds = ft.TextField(hint_text="seconds...", border_radius=30, width=120, text_align="center")
        self.time = ft.Text(style="displayLarge", color="white")
        self.timer_running = False
        self.remaining_time = 0

    def build(self):
        def start_timer(e):
            if not self.timer_running:
                self.remaining_time = int(self.seconds.value)
                self.timer_running = True
                self.update_timer()
                self.update()


        def reset_timer(e):
            self.timer_running = False
            self.remaining_time = 0
            self.seconds.value = "0"
            self.update_timer_display()
            self.update()

        start_button = ft.ElevatedButton("Start", on_click=start_timer, color="green")
        reset_button = ft.ElevatedButton("Reset", on_click=reset_timer, color="red")

        return ft.Column([
            ft.Container(padding=20),
            self.seconds,
            ft.Row([start_button, reset_button], alignment="center"),
            ft.Container(padding=20),
            self.time,
        ], horizontal_alignment='center')

    def update_timer(self):
        while self.timer_running and self.remaining_time > 0:
            self.update_timer_display()
            self.remaining_time -= 1
            sleep(1)
            self.update()
        self.timer_running = False
        self.update()

    def update_timer_display(self):
        mins, secs = divmod(self.remaining_time, 60)
        self.time.value = f"{mins:02d}:{secs:02d}"
        self.update()

def main(page: ft.Page):
    page.title = "Timer App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"
    page.padding = 40
    page.window_frameless = False
    page.window_height = 500
    page.window_width = 300

    page.add(TimerApp())

ft.app(target=main)