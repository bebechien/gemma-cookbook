import os, re
import nbformat
from pathlib import Path

def preprocess_notebook(file_path):
    print(f"process {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    modified = False
    new_cells = []
    for cell in nb.cells:
        source_text = "".join(cell.get("source", []))

        is_copyright = bool(re.search(r"Copyright \d{4} Google LLC", source_text))
        is_license = "Licensed under the Apache License" in source_text

        if is_copyright or is_license:
            modified = True
            continue

        if "metadata" in cell and "id" in cell["metadata"]:
            del cell["metadata"]["id"]
            modified = True

        new_cells.append(cell)
            
    nb.cells = new_cells

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)

# Crawl through your docs directory to find all notebooks
docs_dir = Path('docs').resolve()
for root, dirs, files in docs_dir.walk():
    if "_build" in root.parts:
        continue

    for file in files:
        if file.endswith('.ipynb'):
            preprocess_notebook(os.path.join(root, file))
