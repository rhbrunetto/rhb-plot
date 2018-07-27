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

Comando           | Descrição
------------------|-----------------
create line       | Cria uma linha entre os pontos fornecidos
create rectangle  | Cria um retângulo com diagonal nos pontos fornecidos
create square     | Cria um quadrado com o ponto superior esquerdo e lado fornecidos
create circle     | Cria um círculo com centro e raios fornecidos
create triangle   | Cria um triângulo com os pontos fornecidos
select            | Seleciona os objetos que interceptam o retângulo fornecido
unselect          | Deseleciona os objetos que interceptam o retângulo fornecido
zoom              | Amplia a visualização dos objetos no retângulo fornecido
zoom-ext          | Adapta e centraliza o conteúdo da área de desenho na área de exibição
translate         | Translada os objetos selecionados com deslocamentos fornecidos
scale             | Multiplica a escala dos eixos dos objetos selecionados por fatores fornecidos, dado um ponto de referência
rotate            | Rotaciona os objetos selecionados em um ângulo fornecido, dado um ponto de referência
load              | Carrega um arquivo de scripts no formato esperado

- O formato esperado é de um comando por linha (Ex: [teste.txt](teste.txt)).

<!-- TODO: change link -->
Detalhes de uso podem ser encontrados no Manual de Uso, que será disponibilizado em breve.
<!-- [Manual de Uso](main.py). -->

## Especificações Tecnológicas

Todo o programa foi escrito em `python` na versão 2.7, fazendo uso das bibliotecas:

- Tkinter (nativo);
- numpy (`sudo pip install numpy`).

Os conceitos de orientação a objetos foram amplamente utilizados, a fim de prover modularização do código.

## Utilização

Então, basta executar o script `main.py` através do seguinte:

`python main.py`

Alguns detalhes de implementação constam no documento de apresentação, que estará disponível em breve.
<!-- [aqui](slides.pdf). -->

### Limitações e Sugestões

Não foi possível cumprir todos os itens inicialmente propostos. Contudo, uma nova versão está em desenvolvimento
para contemplar tais pontos e corrigir falhas conhecidas, sem previsão para finalização.

- Ficaram pendentes as seguintes funcionalidades:
  - Interação com preview (seleção, rotação, mudança de escala)
  - Interação com *click and drag* (translação)
  - Deletar objetos previamente selecionados
  - Ícones para os menus / Menu em cascata
  - Aplicar transformações nos objetos por `id`
    - Mostrar `id` do objeto na tela (atributo `id` já existe)
  - Alterar cores de desenho
  - Permitir preencher objetos
- Para a versão futura já está sendo desenvolvido:
  - Manual do usuário
  - Documentação do código
  - Corrigir rotação do círculo após mudança de escala

## Licença

Este projeto segue a licença [Creative Commons Attribution-ShareAlike (BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/), que está detalhada no arquivo [`LICENSE.md`](LICENSE.md).
<p align="center">
  <img src="https://licensebuttons.net/l/by-sa/3.0/88x31.png">
</p>
