import flet as ft

def main(page: ft.Page):
    page.title = 'Oh Chat!'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def enviar(e):
        chat.controls.append(ft.Text(nova_msg.value))
        nova_msg.value = ""
        page.update()

    chat = ft.Column()
    nova_msg = ft.TextField(label='Digite sua mensagem', on_submit=enviar)


    page.add(
        ft.Row([ft.Text('Oh, chat!', size=60, weight='bold', color=ft.colors.INDIGO_400)],
               alignment=ft.MainAxisAlignment.CENTER
               ),
        chat,
        ft.Row(
            controls=[nova_msg, ft.ElevatedButton('Enviar', on_click=enviar)],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
    )

    page.update()

ft.app(main)