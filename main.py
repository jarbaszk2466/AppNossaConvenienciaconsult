import flet as ft
import requests

def main(page: ft.Page):
    page.title = "NossaConsulT"
    page.padding = 0
    page.bgcolor = "black"
    
    URL_BASE = "http://192.168.1.86:5000/consulta/"

    txt_barras = ft.TextField(
        label="BIPE O PRODUTO", 
        autofocus=True,
        on_submit=lambda e: consultar(e),
        width=280,
        bgcolor="white",
        color="black"
    )
    
    res_nome = ft.Text(value="", size=26, weight="bold", color="blue", text_align="center")
    res_preco = ft.Text(value="", size=60, color="green", weight="bold")
    status = ft.Text(value="Sistema Pronto", size=14, color="white")

    def consultar(e):
        if not txt_barras.value: return
        status.value = "Buscando..."
        page.update()
        try:
            r = requests.get(f"{URL_BASE}{txt_barras.value}", timeout=4)
            if r.status_code == 200:
                d = r.json()
                res_nome.value = str(d['nome']).upper()
                res_preco.value = f"R$ {float(d['preco']):.2f}"
                status.value = "Conectado"
            else:
                res_nome.value = "NÃO CADASTRADO"
                res_preco.value = ""
        except:
            status.value = "Erro de Rede"
        
        txt_barras.value = ""
        txt_barras.focus() 
        page.update()

    # Se as imagens não existirem, o Container branco segura o layout
    content_box = ft.Container(
        content=ft.Column([res_nome, res_preco], horizontal_alignment="center"),
        padding=20, bgcolor="#CCFFFFFF", border_radius=20, width=380
    )

    page.add(
        ft.Stack([
            ft.Container(bgcolor="black", width=1080, height=2400), # Fundo reserva
            ft.Column([
                ft.Container(height=60),
                ft.Row([txt_barras], alignment="center"),
                ft.Container(height=40),
                content_box,
                status
            ], horizontal_alignment="center", width=450)
        ])
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")