# Gerador de Embedding com Ollama

Este projeto tem como objetivo principal realizar a leitura de um texto e fazer a geração do embedding a partir dele.

O modelo utilizado pelo arquivo `embedding.py` é o
[`nomic-embed-text`](https://ollama.com/library/nomic-embed-text).

## Requisitos

- Python 3.8 ou superior;
- Ollama instalado e em execução;
- biblioteca Python `ollama`;
- modelo `nomic-embed-text` baixado.

## Instalação do Ollama

### Windows

1. Acesse a página oficial de download do
   [Ollama](https://ollama.com/download).
2. Clique em **Download for Windows**.
3. Execute o instalador baixado e siga as instruções na tela.
4. Após a instalação, abra o **PowerShell** ou o **Prompt de Comando**.
5. Verifique se o Ollama foi instalado corretamente:

   ```powershell
   ollama --version
   ```

6. Baixe o modelo usado pelo projeto:

   ```powershell
   ollama pull nomic-embed-text
   ```

O Ollama normalmente permanece disponível em segundo plano após a instalação.
Se for necessário iniciá-lo manualmente, execute:

```powershell
ollama serve
```

## Instalação da dependência Python

Instale a biblioteca Python:

```bash
pip install ollama
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
