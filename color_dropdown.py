import flet as ft
def main(Page: ft.Page):
    def Button_click(e):
        output_text.value = f"dropdown value is{color_dropdown}"
        Page.update()
        output_text = ft.Text()
        submit_btn = ft.ElevatedButton(text="submit",on_click=Button_click)
        color_dropdown = ft.dropdown(width = 100,option=[ft.dropdown.Option("blue"),ft.dropdown.Option("green"),ft.dropdown.Option("Yelow"),ft.dropdown.Option("red")])
        Page.add(output_text,submit_btn,color_dropdown)
    ft.app(target=main)