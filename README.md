# Gerador de Embedding com Ollama

Este projeto lê um texto digitado no terminal, gera seu embedding usando o
Ollama e exibe o vetor resultante.

O modelo utilizado pelo arquivo `embedding.py` é o
[`nomic-embed-text`](https://ollama.com/library/nomic-embed-text).

## Requisitos

- Python 3.8 ou superior;
- Ollama instalado e em execução;
- biblioteca Python `ollama`;
- modelo `nomic-embed-text` baixado.

## Instalação

Instale a biblioteca Python:

```bash
pip install ollama
```

Baixe o modelo usado pelo script:

```bash
ollama pull nomic-embed-text
```

Se o Ollama não estiver em execução, inicie o serviço:

```bash
ollama serve
```

## Como executar

No diretório do projeto, execute:

```bash
python embedding.py
```

Digite o texto quando solicitado e pressione **Enter**.

## Exemplo

Entrada:

```text
Digite o texto: Olá, mundo!
```

Saída:

```text
Embedding (768 dimensões):
[0.0123, -0.0456, 0.0789, ...]
```

O vetor exibido pode conter valores diferentes, dependendo da versão do modelo
utilizado.
