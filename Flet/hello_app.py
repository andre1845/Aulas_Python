import flet as ft

def main(page: ft.Page):
    page.title = "Ola mundo"
    page.scroll = "adaptive"
    
    page.add(
        ft.Text("Ola mundo")
    )
    page.update()
    
ft.app(main)