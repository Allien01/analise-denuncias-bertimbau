import nbformat
import glob

# Caminhos exatos das suas pastas
paths = [
    'notebooks/k-fold/*.ipynb',
    'notebooks/treino_teste_validacao/*.ipynb'
]

total = 0
alterados = 0

for pattern in paths:
    for nb_path in glob.glob(pattern):
        total += 1
        try:
            nb = nbformat.read(nb_path, as_version=nbformat.NO_CONVERT)
            if 'widgets' in nb.get('metadata', {}):
                del nb['metadata']['widgets']
                nbformat.write(nb, nb_path)
                alterados += 1
                print(f"[OK] Widgets removidos de {nb_path}")
        except Exception as e:
            print(f"[ERRO] Falha ao processar {nb_path}: {e}")

print(f"\nResumo: {alterados}/{total} notebooks ajustados.")
