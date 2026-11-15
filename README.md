# CryptoLab — Projeto de Criptografia

Laboratório de estudos de criptografia em Python, desenvolvido por Nicolas Moreira Silva para praticar conceitos matemáticos, analisar desafios de CTF e documentar o aprendizado em cibersegurança.

## Objetivo

Construir o projeto gradualmente, começando pelo RSA e incorporando novas implementações conforme os estudos avançarem. Cada etapa deve incluir código compreensível, exemplos reproduzíveis e documentação do que foi aprendido.

## Estado atual

Esta versão contém a estrutura inicial e a documentação. A implementação RSA já foi desenvolvida nos estudos e será incorporada a partir do arquivo atualizado do autor. Ainda não há algoritmos executáveis nesta base.

## Organização

| Caminho | Finalidade |
| --- | --- |
| `cryptolab/` | Implementações em Python |
| `tests/` | Testes das operações implementadas |
| `docs/` | Explicações técnicas e registro de evolução |
| `ctf_writeups/` | Resoluções documentadas de desafios |

## Primeira etapa: RSA

Organizar as operações existentes em funções, preservando a lógica original:

- `ehprimo`: verificar primalidade.
- `fatorar_fermat`: procurar fatores por diferença de quadrados.
- `calcular_totiente`: calcular o totiente para dois primos distintos.
- `calcular_chave_privada`: calcular o inverso modular do expoente público.
- `texto_para_numero` e `numero_para_texto`: converter representações.
- `criptografar` e `descriptografar`: realizar operações modulares de RSA.
- `main`: organizar a interação pelo terminal.

Os nomes e as interfaces serão ajustados ao código efetivamente incorporado.

## Evolução prevista

- [x] Preparar a estrutura inicial e o README.
- [ ] Incorporar o código RSA atualizado.
- [ ] Documentar a execução, as entradas e as limitações do RSA.
- [ ] Validar o RSA com exemplos e testes.
- [ ] Desenvolver estudos de hexadecimal, Base64 e ROT13.
- [ ] Desenvolver estudos de XOR.
- [ ] Desenvolver estudos de AES.
- [ ] Avaliar módulos de integridade de arquivos e assinaturas digitais.

Os itens futuros são propostas de estudo e ainda não estão implementados.

## Preparação do ambiente

Instale Python 3.10 ou superior e, dentro da pasta do projeto, crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell, ative com:

```powershell
.venv\Scripts\Activate.ps1
```

A base inicial não possui dependências externas. Os comandos de execução serão adicionados junto com o primeiro módulo funcional.

## Documentação e histórico

O progresso está em [docs/EVOLUCAO.md](docs/EVOLUCAO.md). Cada implementação deve atualizar o README quando alterar o uso do projeto e registrar seu resultado no histórico do Git.

## Uso educacional

As implementações didáticas servem para estudos e desafios autorizados. RSA sem padding e exemplos com números pequenos não são adequados para proteger dados reais.

## Autor

[Nicolas Moreira Silva](https://github.com/NicolasSec) — estudante de Cibersegurança.
