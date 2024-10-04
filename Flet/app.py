import flet as ft

def main(page: ft.Page):
    
    def acao(e):
        result.value = texto.value
        page.update()
    
    page.title = "Meu Flet app"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    texto = ft.TextField(label="Digite o texto aqui", on_change=acao)
    result = ft.Text(size=35)
    
    page.add(texto,
             result)
    
    page.update()
    
ft.app(main)