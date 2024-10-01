import flet as ft
import time

def main(page: ft.Page):
    page.title = "IMC"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK
    
    def limpar_formulario(e):
        nome.value = ""
        peso.value = ""
        altura.value = ""
        result.value = ""
        page.update()
        
    def converter_peso(peso_field):
        valor_peso = peso_field.value.replace(",", ".")
        try:
            peso_float = float(valor_peso)
            if peso_float <= 0:
                result.value = "O valor do peso é inválido."
                return None  # Indica que houve um erro
            return peso_float
        except ValueError:
            result.value = "O valor do peso é inválido."
            return None

    def converter_altura(altura_field):
        valor_altura = altura_field.value.replace(",", ".")
        try:
            altura_float = float(valor_altura)
            if altura_float <= 0:
                result.value = "O valor da altura é inválido."
                return None  # Indica que houve um erro
            return altura_float
        except ValueError:
            result.value = "O valor da altura é inválido."
            return None
        
    def piscar_texto(text_element, vezes):
        for _ in range(vezes):
            text_element.opacity = 0
            page.update()
            time.sleep(0.2)  # Intervalo para piscar (invisível)
            text_element.opacity = 1
            page.update()
            time.sleep(0.2)  # Intervalo para piscar (visível)
    

    def calcular_IMC(e):
        peso_float = converter_peso(peso)
        altura_float = converter_altura(altura)
        
        if peso_float is not None and altura_float is not None:
            imc = peso_float / (altura_float * altura_float)
            if imc < 18.5:
                result.value = f'{nome.value}, seu peso está abaixo do normal. IMC: {imc}'
            elif imc < 25:
                result.value = f'{nome.value}: Peso normal.   IMC: {imc:.2f}'
            elif imc < 30:
                result.value = f'{nome.value}: Pré-Obesidade.   IMC: {imc:.2f}'
            elif imc < 35:
                result.value = f'{nome.value}: Obesidade Grau I.   IMC: {imc:.2f}'
                result.color = "yellow"
            elif imc < 40:
                result.value = f'{nome.value}: Obesidade Grau II.   IMC: {imc:.2f}'
                result.color = "orange"
            else:
                result.value = f'{nome.value}: Obesidade Grau III.   IMC: {imc:.2f}'
                result.color = "red"
                piscar_texto(result, 8)
        
        page.update()
    
    # Elementos da interface
    titulo = ft.Text("Calculadora IMC", size=50, weight="bold", color="blue")
    nome = ft.TextField(label="Nome", width="600", content_padding=30,text_size=30,border_color="white")
    peso = ft.TextField(label="Peso (em kg)", width="600", content_padding=30,text_size=30,border_color="white")
    altura = ft.TextField(label="Altura (em metros)", width="600", content_padding=30,text_size=30,border_color="white", on_submit=calcular_IMC)
    result = ft.Text(size=30, weight="bold")
    
    page.add(
        ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([nome], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([peso], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([altura], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([result], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [ft.ElevatedButton("Calcular IMC", on_click=calcular_IMC)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Limpar formulário", on_click=limpar_formulario)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )
    
    page.update()
    
ft.app(main)

'''
flet pack main.py --icon=myicon.ico  -> para gerar executavel

'''

