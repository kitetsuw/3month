import flet as ft

def main(page: ft.Page):
    page.title = "Flet app"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    user_label = ft.Text("info")
    user_text = ft.TextField( value=0, width=100, text_align= ft.TextAlign.CENTER)


    def get_info(e):
        user_label.value = user_text.value
        page.update()

    page.add(
        ft.Row(
            [
                user_label,
                user_text,

                ft.IconButton(ft.icons.HOME, on_click= get_info),
                ft.Icon(ft.icons.BACK_HAND),
                ft.ElevatedButton(text='click me', on_click= get_info)

            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )  

ft.app(target=main)
