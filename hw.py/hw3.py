import flet as ft
from datetime import datetime
def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world!")
    greeting_history = []
    history_text = ft.Text("История приветствий:", size="bodyMedium")

    def on_button_click(_):
        time =  datetime.now().hour
        name = name_input.value.strip()
        if name:
            if 6 <= time < 12:
                greeting_text.value = f"Доброе утро, {name}!"
            elif 6 <= time < 18:
                greeting_text.value = f"Добрый день, {name}!"
            elif 6 <= time < 24:
                greeting_text.value = f"Добрый вечер, {name}!"
            else:
                greeting_text.value = f"Доброй ночи, {name}!"
            
            greet_button.text = "Поздороваться снова"
            name_input.value = ""
            greeting_history.append(f"{datetime.now().replace(microsecond=0)}: {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите имя"
        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    name_input = ft.TextField(
        label="Введите имя",
        autofocus=True,
        on_submit=on_button_click
    )

    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)
    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)
    clear_button_2 = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить историю", on_click=clear_history)
    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)

    page.add(
        ft.Row(
            [theme_button, clear_button, clear_button_2],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        greeting_text,
        name_input,
        greet_button,
        history_text
    )

ft.app(main)