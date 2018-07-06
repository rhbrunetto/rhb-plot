#include <stdio.h>
#include <math.h>

typedef struct{
  int linhas, colunas;
  int ** matriz;
}Matriz;

#define SINGULAR_QTD_FUNCOES 3
#define DOUBLE_QTD_FUNCOES 1

#define SINGULAR_MAKEIDENTIDADE 0
#define SINGULAR_MAKENUL 1
#define SINGULAR_PRINT 2

#define DOUBLE_MULTIPLICAR 0

typedef void (*S_FUNCTION)(Matriz * mat, int i, int j);
typedef void (*D_FUNCTION)(Matriz * matA, Matriz * matB, Matriz * matC, int i, int j, int a, int b);
static D_FUNCTION * d_functions;
static S_FUNCTION * s_functions;


// FUNÇÕES DE PARÂMETRO SINGULAR

void * s_makeidentidade(Matriz *mat, int i, int j){
  if(i==j)
    mat->matriz[i][j] = 1;
  else
    mat->matriz[i][j] = 0;
}

void * s_makenul(Matriz *mat, int i, int j){
    mat->matriz[i][j] = 0;
}

void * s_print(Matriz *mat, int i, int j){
  printf("%i\t", mat->matriz[i][j]);
  if(j == mat->colunas -1) printf("\n");
}

// FUNÇÕES DE APLICAÇÃO SINGULAR

void percorrer_matriz_singular_aplicar(Matriz *mat, S_FUNCTION f){
  for(int i=0; i<mat->linhas; i++){
    for(int j=0; j<mat->colunas; j++){
      f(mat, i, j);
    }
  }
}


// FUNÇÕES DE PARÂMETRO DUPLO

void d_multiplicar(Matriz * matA, Matriz * matB, Matriz * matC, int i, int j, int a, int b){

}

// FUNÇÕES DE APLICAÇÃO DUPLA
void percorrer_matriz_double_aplicar()
// FUNÇÕES ADMINISTRATIVAS

void matriz_inicializar(Matriz * mat, int linhas, int colunas){
  mat->linhas = linhas;
  mat->colunas = colunas;
  mat->matriz = (int**) malloc(sizeof(int*) * linhas);
  for(int i=0; i<mat->linhas; i++)
    mat->matriz[i] = (int *)malloc(sizeof(int) * colunas);
}

void matriz_makenul(Matriz * mat){
  percorrer_matriz_singular_aplicar(mat, s_functions[SINGULAR_MAKENUL]);
}

void matriz_makeidentidade(Matriz * mat){
  if(mat->linhas != mat->colunas){ printf("Matriz nao quadrada!\n"); return; }
  percorrer_matriz_singular_aplicar(mat, s_functions[SINGULAR_MAKEIDENTIDADE]);
}

void matriz_multiplicar(Matriz * A, Matriz * B, Matriz * C){

}

void matriz_print(Matriz * mat){
  percorrer_matriz_singular_aplicar(mat, s_functions[SINGULAR_PRINT]);
}


void setup_lib(){
  s_functions = (S_FUNCTION *)malloc(sizeof(S_FUNCTION) * SINGULAR_QTD_FUNCOES);
  d_functions = (D_FUNCTION *)malloc(sizeof(D_FUNCTION) * DOUBLE_QTD_FUNCOES);

  s_functions[SINGULAR_MAKEIDENTIDADE] = (S_FUNCTION)&s_makeidentidade;
  s_functions[SINGULAR_MAKENUL] = (S_FUNCTION)&s_makenul;
  s_functions[SINGULAR_PRINT] = (S_FUNCTION)&s_print;

  d_functions[DOUBLE_MULTIPLICAR] = (D_FUNCTION)&d_multiplicar;
}
