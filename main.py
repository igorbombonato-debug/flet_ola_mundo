import flet as ft

def main(page: ft.Page):
    page.title ="Meu primeiro APP flet"
    page.bgcolor = "yellow"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Iguin!!!"),
        ft.ElevatedButton('Clique Aqui')
    )

ft.run(main)
