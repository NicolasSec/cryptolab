"""Testes unitários e de integração do RSA Lab didático."""

import pytest

from cryptolab.rsa import (
    ehprimo,
    fatorar_fermat,
    calcular_totiente,
    calcular_chave_privada,
    texto_para_numero,
    numero_para_texto,
    criptografar,
    descriptografar,
    executar_criptografia,
    executar_descriptografia,
    executar_criptoanalise,
    main,
)


@pytest.mark.parametrize(
    "numero, esperado",
    [(2, True), (53, True), (61, True), (15, False), (1, False), (0, False)],
)
def test_primalidade(numero, esperado):
    assert ehprimo(numero) is esperado


@pytest.mark.parametrize(
    "n, fatores",
    [(3233, (53, 61)), (5959, (59, 101)), (40000014400001287, (200000033, 200000039))],
)
def test_fatoracao_fermat(n, fatores):
    p, q = fatorar_fermat(n)
    assert (p, q) == fatores
    assert p * q == n


@pytest.mark.parametrize("n", [0, 2, 3, 100, 101])
def test_fatoracao_rejeita_modulos_invalidos(n):
    with pytest.raises(ValueError):
        fatorar_fermat(n)


def test_totiente():
    assert calcular_totiente(53, 61) == 3120


def test_chave_privada():
    assert calcular_chave_privada(17, 3120) == 2753


@pytest.mark.parametrize("e", [1, 10, 3120])
def test_expoente_invalido(e):
    with pytest.raises(ValueError):
        calcular_chave_privada(e, 3120)


def test_criptografia():
    assert criptografar(65, 17, 3233) == 2790


def test_descriptografia():
    assert descriptografar(2790, 2753, 3233) == 65


def test_conversao_utf8():
    mensagem_bytes, numero = texto_para_numero("Linux")
    assert mensagem_bytes == b"Linux"
    assert numero == 328186361208
    assert numero_para_texto(numero, len(mensagem_bytes)) == "Linux"


def test_conversao_unicode():
    mensagem_bytes, numero = texto_para_numero("Olá")
    assert numero_para_texto(numero, len(mensagem_bytes)) == "Olá"


def test_mensagem_grande_rejeitada():
    with pytest.raises(ValueError):
        criptografar(5000, 17, 3233)


def test_ciclo_completo():
    n, e = 3233, 17
    p, q = fatorar_fermat(n)
    d = calcular_chave_privada(e, calcular_totiente(p, q))
    mensagem_bytes, mensagem_num = texto_para_numero("A")
    cifrado = criptografar(mensagem_num, e, n)
    decifrado = descriptografar(cifrado, d, n)
    assert decifrado == mensagem_num
    assert numero_para_texto(decifrado, len(mensagem_bytes)) == "A"


def test_cifra_conhecida_ctf():
    n, e, cifrado = 40000014400001287, 65537, 33923388484858950
    p, q = fatorar_fermat(n)
    assert (p, q) == (200000033, 200000039)
    d = calcular_chave_privada(e, calcular_totiente(p, q))
    assert d == 13733926103239809
    assert descriptografar(cifrado, d, n) == 27980592901091891


def test_opcao_criptografar(monkeypatch, capsys):
    entradas = iter(["3233", "17", "A"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(entradas))
    executar_criptografia()
    saida = capsys.readouterr().out
    assert "Mensagem cifrada: 2790" in saida


def test_opcao_descriptografar(monkeypatch, capsys):
    entradas = iter(["3233", "2753", "2790"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(entradas))
    executar_descriptografia()
    saida = capsys.readouterr().out
    assert "Número recuperado: 65" in saida
    assert "Texto recuperado: A" in saida


def test_opcao_criptoanalise(monkeypatch, capsys):
    entradas = iter(["3233", "17", "2790"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(entradas))
    executar_criptoanalise()
    saida = capsys.readouterr().out
    assert "Expoente privado (d): 2753" in saida
    assert "Texto recuperado: A" in saida


def test_menu_invalido(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _prompt: "9")
    main()
    assert "Opção inválida." in capsys.readouterr().out
