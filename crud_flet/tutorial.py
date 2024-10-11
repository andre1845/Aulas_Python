import flet as ft

def main(page: ft.Page):
    page.title = "Teste"
    page.scroll = "adaptive"
    
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
        page.update()

    page.add(
        ft.Row(ft.ElevatedButton(text="Click me", on_click=button_clicked))
        )

    page.update()

ft.app(main)