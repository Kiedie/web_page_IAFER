#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re

# Leer datos JSON
json_files = {}
import os

for fname in os.listdir("data/papers"):
    if fname.endswith(".json"):
        with open(f"data/papers/{fname}", "r", encoding="utf-8") as f:
            paper = json.load(f)
            json_files[paper.get("id", fname)] = paper

# Crear doc de repositorios
output = """# 🔗 BÚSQUEDA DE REPOSITORIOS DE PAPERS IAFER

## Guía de Búsqueda

Los repositorios pueden encontrarse en:
- GitHub (github.com)
- GitLab (gitlab.com)  
- Zenodo (zenodo.org)
- OSF (osf.io)
- Dentro de suplementarios del paper en arXiv o revistas

### Palabras clave útiles para búsqueda:
- Nombres de autores
- Nombre del paper (completo o acrónimo)
- Año de publicación
- Nombre de la revista/congreso

---

## Papers Clasificados por Tipo y Area

"""

# Clasificar por area y research line
by_area_line = {}
for paper in json_files.values():
    area = paper.get("research_area", "unknown")
    line = paper.get("research_line", "unknown")
    if area not in by_area_line:
        by_area_line[area] = {}
    if line not in by_area_line[area]:
        by_area_line[area][line] = []
    by_area_line[area][line].append(paper)

# Generar listado
for area in sorted(by_area_line.keys()):
    output += f"\n## AREA: {area.upper()}\n"
    for line in sorted(by_area_line[area].keys()):
        output += f"\n### {line}\n"
        for paper in by_area_line[area][line]:
            title = paper.get("title", "Unknown")
            authors = ", ".join([a.get("name", "") for a in paper.get("authors", [])])
            year = paper.get("year", "")
            venue = paper.get("publication", {}).get("venue", "")
            paper_url = paper.get("paper_url", "")
            arxiv_url = paper.get("arxiv_url", "")

            output += f"\n#### {title}\n"
            output += f"- **Autores**: {authors}\n"
            output += f"- **Año**: {year}\n"
            output += f"- **Venue**: {venue}\n"

            if paper_url:
                output += f"- **Paper URL**: [{paper_url}]({paper_url})\n"
            if arxiv_url:
                output += f"- **arXiv**: [{arxiv_url}]({arxiv_url})\n"

            # Sugerir búsquedas
            search_terms = []

            # Buscar acrónimos en el título
            acronyms = re.findall(r"[A-Z]{2,}(?:[A-Z0-9]*)", title)
            if acronyms:
                search_terms.append(f"`{acronyms[0]}`")

            # Agregar primer autor si existe
            if authors:
                first_author = authors.split(",")[0].strip()
                search_terms.append(f"`{first_author}`")

            # Agregar año
            if year:
                search_terms.append(f"`{year}`")

            output += f"- **Buscar repositorio**: GitHub con términos: {', '.join(search_terms)}\n"
            output += f"  - Comando: `site:github.com {' OR '.join(search_terms)} repository`\n"

with open("repositorios_busqueda.md", "w", encoding="utf-8") as f:
    f.write(output)

print("✓ Archivo generado: repositorios_busqueda.md")
print(f"✓ Total de papers procesados: {len(json_files)}")
