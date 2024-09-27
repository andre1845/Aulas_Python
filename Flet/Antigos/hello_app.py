import flet as ft

def main(page: ft.Page):
    page.title = "Ola mundo"
    page.scroll = "adaptive"
    
    nome = ft.TextField(label="Nome")
    
    page.add(
        ft.Text("Ola mundo", size=50, color="red"),
        nome,
        ft.Text("TESTE", size=40, color="yellow"),
        ft.TextField(label="teste", text_size=35),
        ft.TextButton("Clique Aqui")
    )
    page.update()
    
ft.app(main)