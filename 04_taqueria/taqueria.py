def main():
    # Dicionário que associa cada item do menu ao respectivo preço
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    # Variável para armazenar o valor total do pedido
    total = 0.0

    # Loop contínuo para permitir que o utilizador insira múltiplos itens,
    # adicionando cada um ao total. O loop só termina quando o utilizador
    # pressiona Control-D (indicando que não quer inserir mais itens).
    while True:
        try:
            # Solicita um item do usuário (ignorando diferenciação de maiúsculas/minúsculas e removendo os espaços em branco)
            item = input("Item: ").strip().title()

            # Verificação se o item está no menu
            if item in menu:
                total += menu[item]

                # Mostra o total atualizado com duas casas decimais
                print(f"Total: ${total:.2f}")

            # Caso contrário, o item não está no menu e ignoramos a entrada
            else:
                # Se o item não estiver no menu, simplesmente ignora e continua o loop
                continue

        # Trata a saída do loop quando o usuário insere Control-D
        except EOFError:
            print()
            # Sai do loop e termina o programa
            break

# Executa main() apenas se o ficheiro for executado diretamente, não quando importado.
if __name__ == "__main__":
    main()
