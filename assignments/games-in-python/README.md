# 📘 Assignment: Jogo da Forca em Python

## 🎯 Objective

Pratique manipulação de strings, listas, loops e condicionais ao criar um jogo da Forca. O jogador tentará descobrir uma palavra escolhida aleatoriamente antes de esgotar as tentativas.

## 📝 Tasks

### 🛠️ Preparar o Jogo e Exibir o Progresso

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher a palavra secreta e prepare as variáveis necessárias para acompanhar o jogo. Mostre o progresso da palavra com letras reveladas e espaços para as letras ainda não adivinhadas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Inicializar as letras adivinhadas, o número de palpites incorretos e o limite de tentativas incorretas.
- Exibir cada letra já adivinhada e representar cada letra ainda oculta por um espaço reservado, como `_ _ _ _`.
- Solicitar ao jogador um palpite de uma letra e convertê-lo para minúscula.

### 🛠️ Processar Palpites e Encerrar a Partida

#### Descrição
Implemente o loop principal para processar os palpites, atualizar o estado do jogo e informar o resultado. A partida deve terminar quando o jogador adivinhar a palavra ou atingir o limite de tentativas incorretas.

#### Requisitos
O programa concluído deve:

- Revelar as ocorrências de um palpite correto e informar quando o palpite não estiver na palavra.
- Aumentar o contador de palpites incorretos somente quando a letra não estiver na palavra; um palpite repetido não deve consumir uma tentativa.
- Exibir o número de tentativas incorretas restantes após cada palpite incorreto.
- Encerrar a partida quando todas as letras da palavra forem adivinhadas ou o limite de tentativas incorretas for atingido.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.
