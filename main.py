import flet as ft


def main(page: ft.Page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    def calcular(e):
        # Verificar se os campos de peso, altura e gênero estão preenchidos
        if peso.value == "" or altura.value == "" or genero.value == "":
            page.banner.open = True
            page.update()
        else:
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)

            # Calcular o IMC
            imc = valor_peso / (valor_altura * valor_altura)
            imc = float(f"{imc:.2f}")

            # Exibir o valor do IMC
            IMC.value = f"Seu IMC é {imc}"

            # Atualizar imagem e detalhes com base no IMC e gênero
            if genero.value == "Feminino":
                if imc < 18.5:
                    img_resultado.src = "10.png"
                    detalhes.value = "Abaixo do peso"
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = "8.png"
                    detalhes.value = "Peso Saudável"
                elif 25 <= imc < 29.9:
                    img_resultado.src = "6.png"
                    detalhes.value = "Sobrepeso ou Pré-Obeso"
                elif 30 <= imc < 34.9:
                    img_resultado.src = "4.png"
                    detalhes.value = "Obeso"
                else:
                    img_resultado.src = "2.png"
                    detalhes.value = "Severamente Obeso"
            else:
                if imc < 18.5:
                    img_resultado.src = "9.png"
                    detalhes.value = "Abaixo do peso"
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = "7.png"
                    detalhes.value = "Peso Saudável"
                elif 25 <= imc < 29.9:
                    img_resultado.src = "5.png"
                    detalhes.value = "Sobrepeso ou Pré-Obeso"
                elif 30 <= imc < 34.9:
                    img_resultado.src = "3.png"
                    detalhes.value = "Obeso"
                else:
                    img_resultado.src = "2.png"
                    detalhes.value = "Severamente Obeso"

            # Limpar Campos
            peso.value = ""
            altura.value = ""
            genero.value = ""

            # Atualizar a página
            page.update()

    # Configuração da Página
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text("Calculadora IMC"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT
    )

    page.window_width = 400
    page.window_height = 550

    # Configuração do Banner de Notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,
                        color=ft.colors.AMBER, size=40),
        content=ft.Text("Ops, preencha todos os campos"),
        actions=[
            ft.TextButton("OK", on_click=close_banner),
        ],
    )

    # Entrada de altura, peso e gênero
    altura = ft.TextField(
        label="Altura", hint_text="Por favor insira sua altura")
    peso = ft.TextField(label="Peso", hint_text="Por favor insira seu peso")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero?",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ],
    )

    # Botão para calcular o IMC
    b_calcular = ft.ElevatedButton(text="Calcular IMC", on_click=calcular)

    # Exibição do IMC e resultados
    IMC = ft.Text("Seu IMC é ...", size=30)
    detalhes = ft.Text("Insira seus dados", size=20)

    img_capa = ft.Image(
        src="logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info_app_resultado = ft.Column(
        controls=[
            IMC,
            detalhes,
        ]
    )

    img_resultado = ft.Image(
        src="logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info = ft.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ]
    )

    # Layout da página
    layout = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=info,   # Adicionando o campo de Informação
                padding=5,
                col={"sm": 4, "md": 4, "xl": 4},
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=altura,  # Adicionando o campo de Altura
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                content=peso,  # Adicionando o campo de Peso
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                content=genero,  # Adicionando o campo de Gênero
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                content=b_calcular,  # Adicionando o campo de Calcular
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
        ]
    )

    # Adicionar o layout à página
    page.add(layout)


ft.app(target=main)
