import nbformat
import glob

notebooks = glob.glob('notebooks/**/*.ipynb', recursive=True)

for nb_path in notebooks:
    nb = nbformat.read(nb_path, as_version=nbformat.NO_CONVERT)
    if 'widgets' in nb['metadata']:
        del nb['metadata']['widgets']
        nbformat.write(nb, nb_path)
        print(f'Widgets removidos de {nb_path}')
