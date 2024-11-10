# Importa o módulo 'sys' para aceder aos argumentos da linha de comandos e terminar o programa, se necessário.
import sys

# Importa o módulo 'requests' para fazer pedidos HTTP à API do CoinDesk.
import requests

def main():
    # Verifica se o utilizador forneceu um argumento (número de Bitcoins).
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Tenta converter o argumento para um número decimal (float) para validar a entrada.
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Faz um pedido à API da CoinDesk para obter o preço atual do Bitcoin.
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Assegura que o pedido foi bem-sucedido.
        data = response.json()  # Converte a resposta para um dicionário Python.
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]  # Extrai o preço do Bitcoin em dólares.
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    # Calcula o custo total em dólares com base na quantidade de Bitcoins.
    cost = bitcoins * price_per_bitcoin

    # Imprime o custo total formatado com 4 casas decimais e separadores de milhar.
    print(f"${cost:,.4f}")

# Garante que a função main() só é executada se o script for executado diretamente.
if __name__ == "__main__":
    main()

