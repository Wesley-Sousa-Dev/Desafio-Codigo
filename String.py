texto = input("Insira um texto: ")

texto_minusculo = texto.lower()

counter = texto_minusculo.count("a")

if(counter > 0):
    print(f"Existe(m) {counter} letra(s) A no texto")
else:
    print("Não existe letra A no texto fornecido")