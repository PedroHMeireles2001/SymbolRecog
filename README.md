# Reconhecimento de Símbolos Específicos usando PyTorch, Tkinter e Pillow
Este projeto tem como objetivo desenvolver um modelo de inteligência artificial que seja capaz de reconhecer símbolos específicos desenhados a mão. O modelo foi desenvolvido utilizando a biblioteca PyTorch e a interface gráfica Tkinter.

## Instalação
1. Clone o repositório do projeto:
>  git clone https://github.com/seu-username/reconhecimento-de-simbolos.git

2. Certifique-se de que possui as bibliotecas necessárias instaladas
	 - Pytorch
	 - Pytorchvision
	 - Tkinter
	 - Pillow

## Utilização
1. Executar o `modelfit.py` para gerar um modelo, se não tiver um
2. Executar o arquivo `main.py`:
3. Começe a desenhar
4. Feche o canvas que ele dirá qual símbolo você desenhos

## Treinamento
O modelo foi treinado utilizando o conjunto de dados fornecido na pasta `/SymbolDataset`. Para treinar o modelo com seus próprios dados, siga as instruções abaixo:
1. Organize as imagens em pastas, onde cada pasta corresponde a uma classe. Certifique-se de que as imagens possuam a mesma dimensão e formato.
2. Altere o arquivo `modelfit.py` de acordo com o seu conjunto de dados.
3. Execute o arquivo `modelfit.py` para gerar um modelo

Você pode utilizar o`datacollector.py` para te ajudar o obter os símbolos desenhados a mão
