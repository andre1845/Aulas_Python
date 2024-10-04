
import flet as ft

def main(page: ft.Page):
    page.title = "CRUD JSON"
    page.scroll = "Adaptive"
    page.theme_mode = ft.ThemeMode.DARK
    
    titulo = ft.Text("CRUD JSON", size=40, weight="bold", color="white")
    
    page.add(
    ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER)    
    )
    page.update()
ft.app(main)

