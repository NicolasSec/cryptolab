
import base64
import urllib.parse
import re
import binascii


# BASE64

def convertEmBase64(texto):
    bytes_texto = texto.encode("utf-8")
    bytes_base64 = base64.b64encode(bytes_texto)

    return bytes_base64.decode("utf-8")


def convertBase64emTexto(texto):
    bytes_decodificados = base64.b64decode(
        texto.encode("utf-8"), validate=True
    )

    return bytes_decodificados.decode("utf-8")


# HEXADECIMAL

def hexadecimalTotexto(hexa):
    valorConvertido = bytes.fromhex(hexa).decode("UTF-8")
    return valorConvertido


def textoTohexadecimal(texto):
    valorConvertido = texto.encode("UTF-8").hex()
    return valorConvertido


# BINÁRIO

def textoToBinario(texto):
    bytes_texto = texto.encode("UTF-8")
    binario = "".join(format(byte, "08b") for byte in bytes_texto)

    return binario


def binarioToTexto(binario):

    binario = "".join(binario.split())

    if len(binario) % 8 != 0:
        raise ValueError(
            "O binário precisa ter um tamanho múltiplo de 8."
        )

    if any(bit not in "01" for bit in binario):
        raise ValueError(
            "O binário deve conter apenas 0 e 1."
        )

    bytes_binario = [
        binario[i:i+8]
        for i in range(0, len(binario), 8)
    ]

    valores = bytes(int(byte, 2) for byte in bytes_binario)

    texto = valores.decode("utf-8")

    return texto


# ROT13

def aplicarROT13(texto):

    resultado = ""

    for letra in texto:

        if "A" <= letra <= "Z":

            posicao = ord(letra) - ord("A")

            nova_posicao = (posicao + 13) % 26

            nova_letra = chr(nova_posicao + ord("A"))

            resultado += nova_letra

        elif "a" <= letra <= "z":

            posicao = ord(letra) - ord("a")

            nova_posicao = (posicao + 13) % 26

            nova_letra = chr(nova_posicao + ord("a"))

            resultado += nova_letra

        else:
            resultado += letra

    return resultado


# URL ENCODING

def textoToURL(texto):
    textoURL = urllib.parse.quote(texto, safe="/")
    return textoURL


def urlToTexto(url):
    urlTexto = urllib.parse.unquote(url)
    return urlTexto



# IDENTIFICAÇÃO AUTOMÁTICA

def pareceBinario(texto):
    texto = "".join(texto.split())

    if not texto or len(texto) % 8 != 0:
        return False

    if any(bit not in "01" for bit in texto):
        return False

    try:
        binarioToTexto(texto)
        return True
    except (ValueError, UnicodeError):
        return False


def pareceHexadecimal(texto):
    if not texto.strip():
        return False

    try:
        hexadecimalTotexto(texto)
        return True
    except (ValueError, UnicodeError):
        return False


def pareceBase64(texto):
    if not texto or len(texto) % 4 != 0:
        return False

    try:
        dados = base64.b64decode(texto, validate=True)

        if base64.b64encode(dados).decode("ascii") != texto:
            return False

        dados.decode("utf-8")

        return len(dados) > 0

    except (ValueError, UnicodeError, binascii.Error):
        return False


#Faz um regex que verifica se existe % seguido de dois dígitos hexadecimais
def pareceURL(texto):
    return bool(re.search(r"%[0-9A-Fa-f]{2}", texto))


## Retorna uma lista de possiveis codificacoes do texto para ser utilizado no Decodificador de camadas
def identificarCodificacao(texto):
    formatos = []

    if pareceBinario(texto):
        formatos.append("Binário")

    if pareceHexadecimal(texto):
        formatos.append("Hexadecimal")

    if pareceBase64(texto):
        formatos.append("Base64")

    if pareceURL(texto):
        formatos.append("URL")

    return formatos


##  DECODIFICADOR EM CAMADAS


def decodificarCamadas(texto, limite=5):

    atual = texto
    historico = []
    visitados = {texto}

    funcoes = {
        "Binário": binarioToTexto,
        "Hexadecimal": hexadecimalTotexto,
        "Base64": convertBase64emTexto,
        "URL": urlToTexto
    }

    for camada in range(1, limite + 1):

        formatos = identificarCodificacao(atual)

        if not formatos:
            break

        if len(formatos) > 1:
            print("\n[AVISO] Formatos ambíguos:", formatos)
            break

        formato = formatos[0]

        try:
            resultado = funcoes[formato](atual)

        except (ValueError, UnicodeError, binascii.Error):
            break

        if resultado == atual or resultado in visitados:
            break

        historico.append({
            "camada": camada,
            "formato": formato,
            "entrada": atual,
            "resultado": resultado
        })

        atual = resultado
        visitados.add(atual)

    return atual, historico

def main():

    while True:

        print("\n========== CRYPTOLAB ==========")
        print("            DECODER           ")
        print("===============================")
        print("[1] Base64")
        print("[2] Hexadecimal")
        print("[3] Binário")
        print("[4] ROT13")
        print("[5] URL Encoding")
        print("[6] Identificação automática")
        print("[7] Decodificação em camadas")
        print("[0] Sair")
        print("===============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("\nEncerrando CryptoLab...")
            break

        if opcao not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\n[ERRO] Opção inválida!")
            continue

        try:

            # IDENTIFICAÇÃO AUTOMÁTICA

            if opcao == "6":

                texto = input("\nDigite o texto para análise: ")

                formatos = identificarCodificacao(texto)

                print("\n========== ANÁLISE ==========")

                if formatos:
                    print("Possíveis codificações encontradas:")

                    for formato in formatos:
                        print("-", formato)

                else:
                    print("Nenhuma codificação reconhecida.")

                print("=============================")
                continue

            # DECODIFICAÇÃO EM CAMADAS

            elif opcao == "7":

                texto = input("\nDigite o texto codificado: ")

                resultado, historico = decodificarCamadas(texto)

                print("\n========== CAMADAS ==========")

                if historico:

                    for etapa in historico:

                        print(f"\nCamada {etapa['camada']}")
                        print("Formato:", etapa["formato"])
                        print("Entrada:", etapa["entrada"])
                        print("Resultado:", etapa["resultado"])

                else:
                    print("Nenhuma camada decodificada.")

                print("\n========== RESULTADO ==========")
                print("Resultado final:", resultado)
                print("===============================")
                continue
            
            # OPERAÇÕES MANUAIS

            print("\n========== OPERAÇÃO ==========")
            print("[1] Codificar")
            print("[2] Decodificar")
            print("==============================")

            operacao = input("Escolha uma operação: ")

            if operacao not in ["1", "2"]:
                print("\n[ERRO] Operação inválida!")
                continue

            texto = input("\nDigite o texto: ")

            if opcao == "1":

                if operacao == "1":
                    resultado = convertEmBase64(texto)
                else:
                    resultado = convertBase64emTexto(texto)

            elif opcao == "2":

                if operacao == "1":
                    resultado = textoTohexadecimal(texto)
                else:
                    resultado = hexadecimalTotexto(texto)

            elif opcao == "3":

                if operacao == "1":
                    resultado = textoToBinario(texto)
                else:
                    resultado = binarioToTexto(texto)

            elif opcao == "4":

                resultado = aplicarROT13(texto)

            elif opcao == "5":

                if operacao == "1":
                    resultado = textoToURL(texto)
                else:
                    resultado = urlToTexto(texto)

            print("\n========== RESULTADO ==========")
            print("Entrada:", texto)
            print("Saída:", resultado)
            print("===============================")

        except (ValueError, UnicodeError) as erro:
            print(
                f"\n[ERRO] Não foi possível realizar a operação: {erro}"
            )

        except Exception as erro:
            print(
                f"\n[ERRO INESPERADO] {erro}"
            )


if __name__ == "__main__":
    main()