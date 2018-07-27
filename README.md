# rhb-plot

Este trabalho foi desenvolvido para a disciplina de Computação Gráfica (Ciência da Computação - UEM) em Julho/2018 por Ricardo Henrique Brunetto (ra94182@uem.br).

## Descrição

Este trabalho visa a construir um editor gráfico 2D com operações e objetos básicos. Dessa forma, fora construído um sistema de visualização de objetos bidimensionais que implementa:
  
- Transformações geométricas básicas
  - Translação
  - Rotação
  - Escala
- Objetos gráficos básicos
  - Reta
  - Círculo
  - Triângulo
  - Quadrado
  - Retângulo
- Zoom estendido (Janela-Viewport)
- Zoom
- Seleção
- Clear

Além disso, funções extras foram inseridas para aprimorar a experiência do usuário.

Além da interação básica com o usuário por cliques na área de desenho, o **rhb-plot** conta com uma interface por linha de comando, onde as funcionalidades podem ser acessadas:

> create line <x,y> <x,y>
> create rectangle <x,y> <x,y>
> create square <x,y> r
> create circle <x.y> r
> create triangle <x,y> <x,y> <x,y>
> select <x,y> <x,y>
> select all
> unselect <x,y> <x,y>
> unselect all
> zoom <x,y> <x,y>
> zoom-ext
> load filepath

<!-- TODO: change link -->
<!-- Detalhes de uso podem ser encontrados no [Manual de Uso](main.py). -->

## Especificações Tecnológicas

Todo o programa foi escrito em `python` na versão 2.7, fazendo uso das bibliotecas:

- Tkinter (nativo);
- numpy (`sudo pip install numpy`).

Os conceitos de orientação a objetos foram amplamente utilizados, a fim de prover modularização do código.

## Utilização

Então, basta executar o script `main.py` através do seguinte:

`python main.py`

<!-- Alguns detalhes de implementação constam no documento de apresentação, disponível [aqui](slides.pdf). -->

### Limitações e Sugestões

Não foi possível cumprir todos os itens inicialmente propostos. Contudo, uma nova versão está em desenvolvimento, por tempo

- Ficaram pendentes as seguintes funcionalidades:
  <!-- - Separar autor e título
  - Identificar o problema do artigo
  - Identificar o objetivo do artigo
  - Identificar a solução proposta no artigo
  - Interface gráfica -->
<!-- - Sugere-se aperfeiçoar a forma como os dados estão sendo salvos e refinar as referências bibliográficas. -->

## Licença

Este projeto segue a licença [Creative Commons Attribution-ShareAlike (BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/), que está detalhada no arquivo [`LICENSE.md`](LICENSE.md).
<p align="center">
  <img src="https://licensebuttons.net/l/by-sa/3.0/88x31.png">
</p>
