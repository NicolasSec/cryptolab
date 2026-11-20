import base64
import binascii


def aplicar_xor(dados, chave):
    xor = bytes(byte ^ chave for byte in dados)
    return xor


def testar_chaves(byteU):
    resultados = []

    for chave in range(256):
        resultado = aplicar_xor(byteU, chave)
        resultados.append((chave, resultado))

    return resultados


def converter_entrada(mensagem, formato):

    if formato == "1":
        return mensagem.encode("utf-8")

    elif formato == "2":
        return bytes.fromhex(mensagem)

    elif formato == "3":
        return base64.b64decode(mensagem, validate=True)

    else:
        raise ValueError("Formato de entrada inválido.")


def analisar_resultado(resultado):

    try:
        texto = resultado.decode("utf-8")
    except UnicodeDecodeError:
        return 0

    if not texto:
        return 0

    pontos = 0

    for caractere in texto:

        if 32 <= ord(caractere) <= 126:
            pontos += 1

        if caractere.isascii() and caractere.isalpha():
            pontos += 2

        if caractere == " ":
            pontos += 3

    pontuacao = (pontos / (len(texto) * 4)) * 100

    return round(pontuacao, 2)


def exibir_resultados(resultados):

    candidatos = []

    for chave, resultado in resultados:

        pontuacao = analisar_resultado(resultado)

        candidatos.append(
            (chave, resultado, pontuacao)
        )

    candidatos.sort(
        key=lambda candidato: candidato[2],
        reverse=True
    )

    print("\n--- TOP 5 CANDIDATOS XOR ---")

    for chave, resultado, pontuacao in candidatos[:5]:

        try:
            texto = resultado.decode("utf-8")
        except UnicodeDecodeError:
            texto = repr(resultado)

        print(f"\nChave: {chave}")
        print(f"Pontuação: {pontuacao}%")
        print(f"Resultado: {texto}")


def main():

    print("\n--- XOR ANALYZER ---")

    print("\nSelecione o formato da mensagem:")
    print("1 - Texto UTF-8")
    print("2 - Hexadecimal")
    print("3 - Base64")

    formato = input("\nEscolha uma opção: ")

    mensagem = input("Digite a mensagem que deseja analisar: ")

    try:
        mensagemBytes = converter_entrada(mensagem, formato)

    except (ValueError, binascii.Error) as erro:
        print(f"\nErro ao converter a mensagem: {erro}")
        return

    print("\n--- ANALISE XOR ---")
    print("Mensagem em bytes:", mensagemBytes)

    resultados = testar_chaves(mensagemBytes)

    exibir_resultados(resultados)


if __name__ == "__main__":
    main()
