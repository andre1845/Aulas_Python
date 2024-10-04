import flet as ft
import time
import math

def main(page: ft.Page):
    page.title = "Travel Planner"
    page.scroll = "Adaptive"
    page.theme_mode = ft.ThemeMode.DARK
    
    def limpar_formulario(e):
        origem.value = ""
        destino.value = ""
        distancia.value = ""
        drive_dia.value = ""
        consumo.value = ""
        combustivel_valor.value = ""
        velocidade.value = ""
        result.value = ""
        page.update()
        
    def calcular_viagem(e):
        try:
            distancia_val = float(distancia.value)
            velocidade_val = float(velocidade.value)
            consumo_val = float(consumo.value)
            drive_dia_val = float(drive_dia.value)
            combustivel_valor_val = float(combustivel_valor.value)
           
            drive_total = (distancia_val/velocidade_val)
            litros = (distancia_val/consumo_val)
            custo = (litros * combustivel_valor_val)
            horas = (drive_total%drive_dia_val)
            dias = math.floor(drive_total/drive_dia_val)
            
            result.value = (
                f"\nViagem de {origem.value} a {destino.value}. "
                f"Tempo total de viagem: {drive_total:.2f} horas. \n"
                f"Isso corresponde a {dias} dias e {horas:.2f} horas dirigindo "
                f"{drive_dia_val} horas por dia.\n"
                f"Consumo de combustível: {litros:.2f} litros.\n"
                f"Custo total do combustível: R$ {custo:.2f}.\n")
        except:
            result.value = f"Valores inválidos!"
        page.update()
    
# Elementos da interface
    titulo = ft.Text("Travel Planner", size=40, weight="bold", color="blue")
    origem = ft.TextField(label="Origem", width="400", content_padding=10,text_size=20,border_color="white")
    destino = ft.TextField(label="Destino", width="400", content_padding=10,text_size=20,border_color="white")
    distancia = ft.TextField(label="Distância (em km)", width="400", content_padding=10,text_size=20,border_color="white")
    drive_dia = ft.TextField(label="Tempo total de direção por dia (em horas)", width="400", content_padding=10,text_size=20,border_color="white")
    
    
    combustivel_valor = ft.TextField(label="Valor do litro de combustivel (em reais)", width="400", content_padding=10,text_size=20,border_color="white")
    consumo = ft.TextField(label="Consumo médio do veículo (em km/l)", width="400", content_padding=10,text_size=20,border_color="white")
    velocidade = ft.TextField(label="Velocidade média (em km/h)", width="400", content_padding=10,text_size=20,border_color="white", on_submit=calcular_viagem)
    result = ft.Text(size=25)
        
  
    page.add(
        ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([origem], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([destino], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([distancia], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([drive_dia], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([combustivel_valor], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([consumo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([velocidade], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([result], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [ft.ElevatedButton("Calcular viagem", on_click=calcular_viagem)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Limpar formulário", on_click=limpar_formulario)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        
        
    )
    page.update()
    
ft.app(main)