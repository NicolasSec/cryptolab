def aplicar_xor(texto, chave):
    bytesTexto = texto.encode("utf-8")

    xor = bytes(byte ^ chave for byte in bytesTexto)

    return xor

def testar_chaves(byteU):

    resultados = []

    for chave in range(256):
        resultado = bytes(byte ^ chave for byte in byteU)

        resultados.append((chave, resultado))

    return resultados

def analisar_resultado(resultado):
    try:
        texto = resultado.decode("utf-8")
    except UnicodeDecodeError:
        return False

    return texto.isprintable()

def exibir_resultados(resultados):
    for chave, resultado in resultados:

        if analisar_resultado(resultado):
            texto = resultado.decode("utf-8")

            print(f"Chave {chave}: {texto}")

def main():
    mensagem = input("Digite a mensagem que deseja analisar: ")

    mensagemBytes = mensagem.encode("utf-8")

    print("\n--- ANALISE XOR ---")
    print("Mensagem original:", mensagem)
    print("Mensagem em bytes:", mensagemBytes)

    resultados = testar_chaves(mensagemBytes)

    print("\n--- RESULTADOS DAS CHAVES ---")
    exibir_resultados(resultados)

if __name__ == "__main__":
    main()
