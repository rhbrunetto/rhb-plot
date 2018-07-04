# Remover comentário da linha abaixo para compilar no Windows
SHELL=cmd.exe
EXEC=main
CFLAGS=-w
LFLAGS=-o
SOURCES=*.c

# Para compilar no Windows: trocar execute por execute_W
# Caso não deseje executar: trocar execute por clear (ou clear_W para Windows)
all: execute_W
	@echo "Sucesso!"

compile:
	@gcc $(CFLAGS) $(SOURCES) $(LFLAGS) $(EXEC) -lm

clear: compile
	-@rm -f *.o
	-@rm -f */*.o

clear_W: compile
	-@del *.o 2>NUL
	-@del */*.o 2>NUL

execute_W: clear_W
	@start "" $(EXEC).exe

execute: clear
	./$(EXEC)
