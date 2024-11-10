def main():
    # Módulo 1: Solicitar a matrícula ao utilizador
    plate = input("Plate: ")

    # Módulo 2: Verificar se a matrícula é válida através da função is_valid()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Módulo 3: Verificar as condições básicas da matrícula
    # - O comprimento deve ser entre 2 e 6 caracteres
    # - Deve começar com duas letras
    # - Deve conter apenas letras e números
    if 1 < len(s) <= 6 and s[:2].isalpha() and s.isalnum():

        # Módulo 4: Dividir a string em duas partes, ou seja dividimos a matrícula na primeira e segunda metade.
        # Usar esta divisão para verificar se a segunda parte começa com '0'.
        divide = [s[:len(s)//2], s[len(s)//2:]]

        # Módulo 5: Verificar se a segunda parte da matrícula começa com '0'
        # Se a segunda parte começar com '0', a matrícula é inválida.
        if divide[1][0] == '0':
            return False

        # Módulo 6: Se todas as condições forem cumpridas, a matrícula é válida.
        else:
            return True


# Módulo 7: função principal para iniciar o programa
main()
