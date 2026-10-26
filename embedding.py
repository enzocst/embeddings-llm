import ollama

MODELO = "nomic-embed-text"

texto = input("Digite o texto: ").strip()

resposta = ollama.embed(model=MODELO, input=texto)
embedding = resposta["embeddings"][0]

print(f"\nEmbedding ({len(embedding)} dimensões):")
print(embedding)
