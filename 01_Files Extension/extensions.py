def main():
    # Solicitar nome do ficheiro ao utilizador [não esquecer de utilizar a técnica case insensitive: input().strip().lower()]
    file_name = input("File name: ").strip().lower()

    # Classificação do tipo de ficheiro e resposta correspondente
    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
