# Visualizador de Imagens

Este projeto implementa um visualizador de imagens em Python, que permite ao usuário carregar uma imagem, aplicar filtros e transformações, visualizar os resultados ao lado da imagem original e, finalmente, salvar a imagem modificada em um novo arquivo.

## Funcionalidades

- **Carregar Imagem**: Permite ao usuário carregar uma imagem para edição.
- **Aplicar Filtros**: O visualizador oferece vários filtros e transformações, como:
  - Escala de cinza
  - Inversão de cores
  - Aumento de contraste
  - Desfoque (blur)
  - Nitidez (sharpen)
  - Detecção de bordas
- **Exibição Lado a Lado**: A imagem original e a imagem modificada são exibidas lado a lado para fácil comparação.
- **Salvar Imagem**: O usuário pode salvar a imagem modificada em um novo arquivo, sem alterar a imagem original.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem utilizada para o desenvolvimento do visualizador.
- **Tkinter**: Biblioteca para criação da interface gráfica.
- **Pillow (PIL)**: Biblioteca para manipulação e processamento de imagens.

## Como Usar

### Passo 1: Instalar Dependências

Certifique-se de ter o Python 3.x instalado e, em seguida, instale a biblioteca Pillow:

```bash
pip install pillow
````

### Passo 2: Rodar o Script

Execute o script Python para iniciar o visualizador:

```bash
python app.py
```

### Passo 3: Carregar e Modificar Imagens

1. Clique em **"Carregar Imagem"** para selecionar uma imagem do seu computador.
2. A imagem será exibida à esquerda. A imagem modificada será exibida à direita.
3. Aplique os filtros desejados clicando nos botões correspondentes.
4. As alterações feitas na imagem serão mostradas em tempo real, lado a lado com a imagem original.

### Passo 4: Salvar a Imagem Modificada

1. Após aplicar os filtros, clique em **"Salvar Imagem"**.
2. Escolha o local onde deseja salvar a imagem modificada e o formato (PNG ou JPEG).

## Exemplo de Interface

A interface gráfica do programa exibe duas imagens lado a lado: à esquerda, a imagem original e à direita, a imagem com os filtros aplicados. Abaixo, há botões para carregar a imagem, aplicar filtros e salvar a versão modificada.

## Observações

* **Imagens Modificadas**: A imagem original não é alterada. As alterações são feitas em uma cópia da imagem original, garantindo que você sempre tenha a versão original intacta.
* **Redimensionamento**: As imagens são redimensionadas automaticamente para se ajustar ao tamanho do visualizador, mantendo a proporção original da imagem.
