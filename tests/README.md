# Testes automatizados

A suíte de testes do CryptoLab utiliza **pytest** para verificar as implementações didáticas e detectar regressões.

## RSA Lab — Parte 3

O arquivo `test_rsa.py` cobre fatoração de Fermat, primalidade, totiente de Euler, reconstrução do expoente privado, criptografia, descriptografia, conversão UTF-8, entradas inválidas e as três operações da interface de terminal. Inclui um caso com valores conhecidos de estudo.

Para executar a partir da raiz do repositório:

```bash
python -m pip install pytest
python -m pytest -q
```

Os testes verificam o comportamento esperado dentro dos limites da implementação didática; não constituem uma auditoria de segurança de um sistema criptográfico de produção.
