import math


# Verificação de primalidade
def ehprimo(numero):
    if numero < 2:
        return False

    for divisor in range(2, math.isqrt(numero) + 1):
        if numero % divisor == 0:
            return False

    return True


# Método de Fermat (descobrir os valores de p e q)
def fatorar_fermat(n):
    if n <= 3 or n % 2 == 0:
        raise ValueError("N deve ser um inteiro ímpar maior que 3")

    a = math.isqrt(n)

    if a * a < n:
        a += 1

    limite = 100000

    for tentativa in range(limite):
        b2 = a ** 2 - n
        b = math.isqrt(b2)

        if b ** 2 == b2:
            p = a - b
            q = a + b
            break

        a += 1
    else:
        raise ValueError("Fatores não encontrados no limite definido.")

    if p == q or not ehprimo(p) or not ehprimo(q):
        raise ValueError("Os fatores devem ser primos distintos.")

    return p, q


# Calcular o totiente de Euler
def calcular_totiente(p, q):
    totiEu = (p - 1) * (q - 1)
    return totiEu


# Reconstrução da chave privada RSA
def calcular_chave_privada(e, totiEu):
    if not (1 < e < totiEu) or math.gcd(e, totiEu) != 1:
        raise ValueError("Expoente público inválido.")

    d = pow(e, -1, totiEu)
    return d


# Converter texto em número inteiro
def texto_para_numero(mensagem):
    mensagemBytes = mensagem.encode("utf-8")
    mensagemNum = int.from_bytes(mensagemBytes, byteorder="big")

    return mensagemBytes, mensagemNum


# Criptografia RSA
def criptografar(mensagemNum, e, n):
    if not (0 <= mensagemNum < n):
        raise ValueError(
            "A mensagem é grande demais para este módulo RSA."
        )

    cifrado = pow(mensagemNum, e, n)
    return cifrado


# Descriptografia RSA
def descriptografar(cifrado, d, n):
    decifrado = pow(cifrado, d, n)
    return decifrado


# Converter número inteiro novamente em texto
def numero_para_texto(decifrado, tamanho):
    bytesRecuperados = decifrado.to_bytes(
        tamanho, byteorder="big"
    )

    textoRecuperado = bytesRecuperados.decode("utf-8")
    return textoRecuperado

def preparar_chaves():
    n = int(input("Digite o valor de N: "))

    p, q = fatorar_fermat(n)

    print("\nFatores encontrados:")
    print("P:", p)
    print("Q:", q)

    totiEu = calcular_totiente(p, q)
    print("\nTotiente de Euler:", totiEu)

    e = int(input("Digite o valor de e: "))

    d = calcular_chave_privada(e, totiEu)
    print("\nExpoente privado (d):", d)

    return n, e, d


# Converter o inteiro recuperado em texto, quando possível
def exibir_resultado(decifrado):
    print("Número recuperado:", decifrado)

    tamanho = max(1, (decifrado.bit_length() + 7) // 8)

    try:
        textoRecuperado = numero_para_texto(decifrado, tamanho)
        print("Texto recuperado:", textoRecuperado)

    except UnicodeDecodeError:
        print("O resultado não representa texto UTF-8 válido.")


# OPÇÃO 1 - Criptografar utilizando a chave pública
def executar_criptografia():
    n = int(input("Digite o valor de N: "))
    e = int(input("Digite o valor de e: "))
    mensagem = input("Digite sua mensagem: ")

    mensagemBytes, mensagemNum = texto_para_numero(mensagem)

    cifrado = criptografar(mensagemNum, e, n)

    print("\n--- RESULTADOS ---")
    print("Mensagem original:", mensagem)
    print("Mensagem em bytes:", mensagemBytes)
    print("Mensagem como número:", mensagemNum)
    print("Mensagem cifrada:", cifrado)


# OPÇÃO 2 - Descriptografar com a chave privada conhecida
def executar_descriptografia():
    n = int(input("Digite o valor de N: "))
    d = int(input("Digite o valor de d: "))
    cifrado = int(input("Digite o número cifrado: "))

    if not (0 <= cifrado < n):
        raise ValueError("O número cifrado deve estar entre 0 e N-1.")

    decifrado = descriptografar(cifrado, d, n)

    print("\n--- RESULTADOS ---")
    print("Mensagem cifrada:", cifrado)
    exibir_resultado(decifrado)


# OPÇÃO 3 - Criptoanálise utilizando a fatoração de Fermat
def executar_criptoanalise():
    n = int(input("Digite o valor de N: "))
    e = int(input("Digite o valor de e: "))
    cifrado = int(input("Digite o número cifrado: "))

    if not (0 <= cifrado < n):
        raise ValueError("O número cifrado deve estar entre 0 e N-1.")

    p, q = fatorar_fermat(n)

    print("\nFatores encontrados:")
    print("P:", p)
    print("Q:", q)

    totiEu = calcular_totiente(p, q)
    print("Totiente de Euler:", totiEu)

    d = calcular_chave_privada(e, totiEu)
    print("Expoente privado (d):", d)

    decifrado = descriptografar(cifrado, d, n)

    print("\n--- RESULTADOS ---")
    print("Mensagem cifrada:", cifrado)
    exibir_resultado(decifrado)

def main():

    print("\n--- CRYPTOLAB RSA ---")
    print("1 - Criptografar mensagem")
    print("2 - Descriptografar com chave privada")
    print("3 - Criptoanálise RSA (Fermat)")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        executar_criptografia()

    elif opcao == "2":
        executar_descriptografia()

    elif opcao == "3":
        executar_criptoanalise()

    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
