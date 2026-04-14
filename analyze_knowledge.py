#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import csv
import os
from collections import defaultdict
import re

# Leer CSV de publicaciones
papers_metadata = {}
with open("papers/Publicaciones IAFER.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ref = row["Referencia (Autores, titulo, revista/congreso, numero volumen)"]
        papers_metadata[ref] = {
            "Actividad": row["Actividad"],
            "Enlace": row["Enlace"],
            "Responsable": row["Responsable"],
            "Estado": row["Publicado/Enviado"],
        }

# Leer datos JSON
json_files = [f for f in os.listdir("data/papers") if f.endswith(".json")]
papers_data = []

for json_file in json_files:
    try:
        with open(f"data/papers/{json_file}", "r", encoding="utf-8") as f:
            paper = json.load(f)
            papers_data.append(paper)
    except Exception as e:
        print(f"Error leyendo {json_file}: {e}")

# Organizar por research_area y research_line
by_area = defaultdict(lambda: defaultdict(list))
for paper in papers_data:
    area = paper.get("research_area", "unknown")
    line = paper.get("research_line", "unknown")
    by_area[area][line].append(paper)

print("=" * 100)
print("ESTRUCTURA DEL CONOCIMIENTO - IAFER")
print("=" * 100)
print()

for area in sorted(by_area.keys()):
    print(f"\n🔬 ÁREA DE INVESTIGACIÓN: {area.upper()}")
    print("-" * 100)
    for line in sorted(by_area[area].keys()):
        print(f"  └─ {line}")
        for paper in by_area[area][line]:
            tags = ", ".join(paper.get("tags", [])[:3])
            title = paper.get("title", "Unknown")[:70]
            print(f"     • {title}")
            if tags:
                print(f"       Keywords: {tags}")

# Análisis de temas en XAI y métodos de explicabilidad
print("\n" + "=" * 100)
print("CLASIFICACIÓN DE MÉTODOS DE EXPLICABILIDAD EN XAI")
print("=" * 100)

# Categorías de XAI
xai_categories = {
    "Métodos Basados en Atribución de Importancias": [],
    "Métodos Basados en Reglas y Conceptos": [],
    "Métodos Basados en Ejemplos": [],
    "Explicaciones Locales": [],
    "Explicaciones Globales": [],
    "Explicaciones Mixtas (Local + Global)": [],
    "Evaluación y Gobernanza de XAI": [],
}

# Palabras clave por categoría
attribution_keywords = [
    "attribution",
    "importance",
    "feature attribution",
    "saliency",
    "shap",
    "lime",
]
rule_keywords = ["rule", "concept", "regla", "conceptual", "rule-based", "symbolic"]
example_keywords = ["example", "exemplar", "case-based", "prototype", "instance"]
local_keywords = ["local", "localized", "local explanation"]
global_keywords = ["global", "global explanation", "model-level"]
mixed_keywords = ["hybrid", "framework", "mixed", "both local"]
governance_keywords = [
    "governance",
    "audit",
    "reproducibility",
    "maturity",
    "evaluation",
    "fairness",
]


def categorize_paper(paper):
    title = paper.get("title", "").lower()
    keywords = [k.lower() for k in paper.get("keywords", [])]
    tags = [t.lower() for t in paper.get("tags", [])]
    all_text = " ".join(keywords + tags + [title])

    categories = []

    if any(word in all_text for word in attribution_keywords):
        categories.append("Métodos Basados en Atribución de Importancias")
    if any(word in all_text for word in rule_keywords):
        categories.append("Métodos Basados en Reglas y Conceptos")
    if any(word in all_text for word in example_keywords):
        categories.append("Métodos Basados en Ejemplos")
    if any(word in all_text for word in local_keywords):
        categories.append("Explicaciones Locales")
    if any(word in all_text for word in global_keywords):
        categories.append("Explicaciones Globales")
    if any(word in all_text for word in mixed_keywords):
        categories.append("Explicaciones Mixtas (Local + Global)")
    if any(word in all_text for word in governance_keywords):
        categories.append("Evaluación y Gobernanza de XAI")

    return categories if categories else None


# Clasificar papers
for paper in papers_data:
    cats = categorize_paper(paper)
    if cats:
        for cat in cats:
            if cat in xai_categories:
                xai_categories[cat].append(paper)

# Imprimir resultados
for category, papers in xai_categories.items():
    if papers:
        print(f"\n{category} ({len(papers)} papers)")
        print("-" * 100)
        for paper in papers:
            print(f"  • {paper.get('title', 'Unknown')[:80]}")
            print(f"    Línea: {paper.get('research_line', 'N/A')}")

print("\n" + "=" * 100)
print(f"Total de papers analizados: {len(papers_data)}")
print(f"Áreas de investigación: {len(by_area)}")
print("=" * 100)
