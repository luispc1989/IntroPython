# Importa o módulo 'sys' para aceder aos argumentos da linha de comandos e manipular a saída do programa
import sys

# Importa o módulo 'os' para verificar a existência de ficheiros no sistema de ficheiros
import os

def main():
    # Verifica se o número de argumentos fornecido pelo utilizador está correto (deve ser exatamente 2)
    if len(sys.argv) != 2:
        # Sai do programa com uma mensagem de instrução de uso, caso o número de argumentos esteja errado
        sys.exit("Usage: python lines.py FILENAME")

    # Obtém o nome do ficheiro passado como argumento
    filename = sys.argv[1]

    # Verifica se o ficheiro fornecido tem a extensão .py (para garantir que é um ficheiro Python)
    if not filename.endswith(".py"):
        # Sai do programa com uma mensagem de erro se o ficheiro não for um ficheiro Python
        sys.exit("Not a Python file")

    # Verifica se o ficheiro existe no sistema
    if not os.path.isfile(filename):
        # Sai do programa com uma mensagem de erro se o ficheiro não existir
        sys.exit("File does not exist")

    # Tenta abrir o ficheiro e contar as linhas de código
    try:
        with open(filename, "r") as file:
            # Chama a função para contar as linhas de código válidas no ficheiro
            loc = count_lines_of_code(file)
            # Imprime o número de linhas de código contadas
            print(loc)
    # Caso ocorra um erro de ficheiro não encontrado, executa esta parte
    except FileNotFoundError:
        # Sai do programa com uma mensagem de erro se o ficheiro não for encontrado
        sys.exit("File does not exist")

def count_lines_of_code(file):
    # Inicializa o contador de linhas de código
    lines_of_code = 0

    # Percorre cada linha do ficheiro
    for line in file:
        # Remove espaços em branco iniciais para tratar corretamente os comentários e linhas em branco
        stripped_line = line.lstrip()

        # Ignora as linhas em branco e as que começam por "#" (comentários)
        if stripped_line == "" or stripped_line.startswith("#"):
            continue

        # Caso a linha não seja em branco nem um comentário, incrementa o contador de linhas de código
        lines_of_code += 1

    # Devolve o total de linhas de código contadas
    return lines_of_code

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
