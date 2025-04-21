import flet as ft 

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world!")

    HISTORY_FILE = "history.txt"

    greeting_history = []

    def load_history():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    name = line.strip()
                    if name:
                        greeting_history.append(name)
                history_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
                page.updata()

        except FileNotFoundError:
            pass

        def save_history():
            with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
                for name in greeting_history:
                    file.write(name + "\n")



    history_text = ft.Text("История приветствий:", size="bodyMedium")



    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            greet_button.text = "Поздороваться снова"
            name_input.value = ""

            greeting_history.append(name)
            history_text.value = "История приветсвий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = 'Пожалуйста, введите имя ❌'
            
        page.update()


    name_input = ft.TextField(label="Введите имя", autofocus=True,
                                on_submit=on_button_click)

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

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, 
                                 tooltip='Сменить тему',
                                 on_click=toggle_theme)

    greet_button = ft.ElevatedButton('Поздороваться', 
                                    on_click=on_button_click,
                                    icon=ft.icons.HANDSHAKE)
    
    clear_button = ft.TextButton("Очистить исорию", on_click=clear_history)

    clear_button_2 = ft.IconButton(icon=ft.icons.DELETE,
                                    tooltip='Очистить историю',
                                    on_click=clear_history)

    load_history()
    # page.add(theme_button, greeting_text, name_input, greet_button, history_text, clear_button)
    page.add(ft.Row([theme_button, clear_button, clear_button_2],  alignment=ft.MainAxisAlignment.CENTER),
                    greeting_text,
                    name_input,
                    greet_button,
                    history_text)

ft.app(main, view= ft.AppView.WEB_BROWSER)