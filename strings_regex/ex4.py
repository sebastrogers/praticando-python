url = input("Digite uma URL: ")
if url.startswith("http://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")  