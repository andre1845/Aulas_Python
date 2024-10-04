import flet as ft
import time

def main(page: ft.Page):
    page.title = "Maioridade"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def calcular_maioridade(e):
        if idade.value.isdigit():
            idade_val = int(idade.value)
            if idade_val >= 18:
                result.value = f"{nome.value} é maior de idade."
                result.color = "blue"
            else:
                result.value = f"{nome.value} é menor de idade."
                result.color = "red"
                piscar_texto(result, 5)
        else:
            result.value = "Por favor, insira uma idade válida."
        page.update()
        
    def limpar_formulario(e):
        nome.value = ""
        idade.value = ""
        result.value = ""
        page.update()
        
    def piscar_texto(text_element, vezes):
        for _ in range(vezes):
            text_element.opacity = 0
            page.update()
            time.sleep(0.2)  # Intervalo para piscar (invisível)
            text_element.opacity = 1
            page.update()
            time.sleep(0.2)  # Intervalo para piscar (visível)
    
    nome = ft.TextField(label="Nome")
    idade = ft.TextField(label="Idade", suffix_text=" anos", on_submit=calcular_maioridade)
    result = ft.Text(size=30, weight="bold")
    
    page.add(
        ft.Row(
            [ft.Text("Maioridade", size=40, weight="bold")],
            alignment=ft.MainAxisAlignment.CENTER
            
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [idade],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Calcular maioridade", on_click=calcular_maioridade)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Limpar formulario", on_click=limpar_formulario)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)