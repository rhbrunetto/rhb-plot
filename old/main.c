#include <stdio.h>
#include <math.h>
#include "entidades/ponto.c"

int main(){
  Matriz m, n;
  setup_lib();
  matriz_inicializar(&m, 1, 2);
  matriz_makenul(&m);
  matriz_print(&m);
  matriz_inicializar(&m, 5, 5);
  matriz_makeidentidade(&m);
  matriz_print(&m);

  matriz_inicializar(&n, 2, 2);

  // matriz_multiplicar(NULL, NULL, &n);

  system("pause");
  return 0;
}
