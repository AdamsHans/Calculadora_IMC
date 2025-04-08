# ⚖️ Calculadora de IMC com Flet

Uma aplicação interativa construída com [Flet](https://flet.dev) que calcula o Índice de Massa Corporal (IMC) com base nos dados do usuário: altura, peso e gênero. A interface é responsiva, amigável e exibe o resultado com texto e imagens ilustrativas.

---

## 🧮 Como Funciona

1. O usuário informa sua **altura**, **peso** e **gênero**.
2. Clica em **"Calcular IMC"**.
3. O sistema calcula o IMC e exibe:
   - Valor numérico do IMC
   - Classificação do resultado (ex: "Peso saudável", "Obeso", etc.)
   - Imagem correspondente ao resultado
4. Se algum campo estiver vazio, um **banner de aviso** será exibido.

---

## ✨ Funcionalidades

- ✅ Cálculo automático do IMC
- ✅ Classificação personalizada por gênero
- ✅ Interface visual com imagens e texto
- ✅ Feedback em tempo real com banner de alerta
- ✅ Layout responsivo com `ResponsiveRow` e `Container`

---

## 🛠️ Tecnologias Utilizadas

- [Flet](https://flet.dev) – framework para interfaces Python com frontend Flutter
- Python – lógica de programação
- Imagens personalizadas para representar os níveis de IMC

---

## 📂 Estrutura Esperada
projeto/ ├── main.py ├── logo.png ├── 2.png ← Severamente obeso ├── 3.png ├── 4.png ├── 5.png ├── 6.png ├── 7.png ├── 8.png ├── 9.png ← Abaixo do peso (masculino) ├── 10.png ← Abaixo do peso (feminino)


---

## 🧪 Classificações de IMC

As faixas de IMC são interpretadas de forma ligeiramente diferente para **masculino** e **feminino**, exibindo uma imagem específica para cada resultado.

---

## 🚀 Como Executar

1. Instale o Flet:


pip install flet

---

## Execute a aplicação:

python main.py

---

📌 Requisitos
Python 3.7+

Conexão com internet (para baixar pacotes do Flet, se necessário)








