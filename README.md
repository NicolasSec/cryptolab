<div align="center">

# CryptoLab

**Cryptographic Analysis & Security Toolkit**

Laboratório pessoal de criptografia em Python para explorar algoritmos, compreender seus fundamentos matemáticos e estudar a segurança da informação na prática.

[Sobre](#sobre-o-projeto) · [Áreas de estudo](#áreas-de-estudo) · [Abordagem](#abordagem) · [Autor](#autor)

</div>

---

## Sobre o projeto

O **CryptoLab** é um projeto de estudo e experimentação dedicado à criptografia e à análise criptográfica. Sua proposta é reunir, em um laboratório organizado, conhecimentos sobre representação de dados, criptografia simétrica e assimétrica, funções de hash e assinaturas digitais.

Desenvolvido em **Python**, o projeto conecta teoria e prática por meio da construção de implementações didáticas e da análise das operações envolvidas na proteção de informações. O foco é compreender como cada técnica funciona, quais problemas resolve e como suas escolhas matemáticas e de implementação influenciam a segurança.

O laboratório também propõe investigar as limitações dos algoritmos e os efeitos de configurações inadequadas, desenvolvendo uma visão crítica sobre confidencialidade, integridade e autenticidade.

## Áreas de estudo

O escopo do CryptoLab está organizado em seis áreas complementares:

| Área | Foco |
| --- | --- |
| **Decoder** | Representação e transformação de dados com hexadecimal, Base64 e ROT13, distinguindo codificação de criptografia. |
| **XOR Analyzer** | Operações bit a bit, aplicação de chaves e análise de padrões para compreender o papel do XOR em transformações criptográficas. |
| **RSA Lab** | Criptografia de chave pública, números primos, aritmética modular, totiente de Euler, inverso modular e fatoração pelo método de Fermat. |
| **AES Lab** | Criptografia simétrica, uso de chaves, modos de operação e influência de parâmetros como vetores de inicialização e padding. |
| **File Integrity** | Funções de hash, resumos criptográficos e comparação de arquivos para estudar a detecção de alterações. |
| **Signatures** | Fundamentos de assinaturas digitais e a relação entre hashes, chaves públicas e privadas, autenticidade e integridade. |

Essas áreas definem a proposta de estudo do projeto e orientam a construção do laboratório.

## Parte 3 — RSA Lab

A terceira parte do CryptoLab implementa um laboratório interativo de criptografia assimétrica baseado nos fundamentos matemáticos do RSA. O módulo apresenta três operações independentes:

| Operação | Entrada | Funcionalidade |
| --- | --- | --- |
| **Criptografia** | Módulo público `N`, expoente público `e` e texto | Converte a mensagem UTF-8 em um inteiro e aplica a exponenciação modular RSA. |
| **Descriptografia** | Módulo `N`, expoente privado `d` e cifra numérica | Recupera o inteiro original e tenta interpretá-lo como texto UTF-8. |
| **Criptoanálise (Fermat)** | Módulo público `N`, expoente `e` e cifra numérica | Fatora módulos vulneráveis com primos próximos, valida os fatores, calcula o totiente de Euler, reconstrói `d` e tenta recuperar a mensagem. |

A implementação utiliza a aritmética de inteiros do Python, o cálculo de raízes quadradas inteiras, a verificação de primalidade e o inverso modular. Seu desenvolvimento prioriza a compreensão de cada etapa e a observação das limitações matemáticas e operacionais dos algoritmos.

O módulo inclui testes automatizados com **pytest**, abrangendo resultados conhecidos, casos inválidos, conversões UTF-8 e as três operações disponíveis no terminal.

**Uso didático:** esta implementação demonstra RSA sem padding e fatoração de Fermat; não se destina à proteção de dados reais. A fatoração depende das características dos fatores de `N`, e dados recuperados não representam necessariamente texto UTF-8. Para aplicações reais, devem ser usados esquemas padronizados, como RSA-OAEP, com bibliotecas confiáveis.

```bash
python -m cryptolab.rsa
python -m pytest -q
```

## Objetivos

- **Compreender os fundamentos:** relacionar conceitos matemáticos ao comportamento dos algoritmos.
- **Experimentar com clareza:** observar como mensagens, chaves e parâmetros afetam os resultados.
- **Analisar a segurança:** estudar limitações, escolhas inadequadas e diferenças entre demonstrações didáticas e aplicações reais.
- **Consolidar conhecimento:** transformar os estudos em código legível e explicações técnicas.
- **Conectar criptografia e cibersegurança:** compreender o papel dessas técnicas na proteção e na verificação de informações.

## Abordagem

O CryptoLab adota uma abordagem modular, com separação entre os conceitos estudados e as operações de cada algoritmo. A prioridade é tornar o raciocínio acessível, permitindo acompanhar as transformações dos dados e compreender o motivo de cada etapa.

**Python** é a linguagem central do laboratório por permitir expressar operações matemáticas e manipular dados de forma direta. A experimentação é acompanhada por documentação e validação com resultados conhecidos, favorecendo a reprodução e a análise dos estudos.

O propósito do projeto é educacional: desenvolver compreensão técnica sobre os mecanismos criptográficos e seus limites de aplicação.

## Autor

**Nicolas Moreira Silva**  
Estudante de Cibersegurança e desenvolvedor do CryptoLab.

[Perfil no GitHub](https://github.com/NicolasSec)
