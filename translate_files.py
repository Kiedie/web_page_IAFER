#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to translate HTML files from Spanish to English
"""

import os
import glob

# Translation dictionary
translations = {
    'lang="es"': 'lang="en"',
    "Navegacion principal": "Main navigation",
    "Abrir menu": "Open menu",
    "¿Qué es Contrastive Learning?": "What is Contrastive Learning?",
    "Aprende sobre": "Learn about",
    "Explorar contenido": "Explore content",
    "Volver a GPAIS": "Back to GPAIS",
    "Volver a Trustworthy": "Back to Trustworthy",
    "¿Qué son los pares contrastivos?": "What are Contrastive Pairs?",
    "Par Positivo": "Positive Pair",
    "Par Negativo": "Negative Pair",
    "Pérdida Contrastiva": "Contrastive Loss",
    "Métodos principales": "Main Methods",
    "Desafíos Actuales": "Current Challenges",
    "Nuestra Investigación": "Our Research",
    "Aplicaciones Prácticas": "Practical Applications",
    "Publicaciones": "Publications",
    "Sección": "Section",
    "sección": "section",
    "Navegación del sitio": "Site Navigation",
    "Inicio": "Home",
    "Líneas de Investigación": "Research Lines",
    "Equipo": "Team",
}


def translate_file(filepath):
    """Translate a single HTML file from Spanish to English"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply translations
        for spanish, english in translations.items():
            content = content.replace(spanish, english)

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return True, None
    except Exception as e:
        return False, str(e)


# Files to translate
files_to_translate = [
    "gpais/contrastive-learning.html",
    "gpais/self-supervised.html",
    "gpais/zero-shot.html",
    "gpais/agentic-ai.html",
    "trustworthy/index.html",
    "trustworthy/explainability/index.html",
    "trustworthy/fairness/index.html",
    "trustworthy/robustness/index.html",
    "trustworthy/privacy/index.html",
    "trustworthy/governance/index.html",
    "trustworthy/automl/index.html",
    "trustworthy/critical-applications/index.html",
]

# Run translations
results = {}
for filepath in files_to_translate:
    full_path = os.path.join(os.getcwd(), filepath)
    if os.path.exists(full_path):
        success, error = translate_file(full_path)
        results[filepath] = {"success": success, "error": error}
        print(f"{'✓' if success else '✗'} {filepath}")
    else:
        print(f"✗ {filepath} (not found)")
        results[filepath] = {"success": False, "error": "File not found"}

print(
    f"\n\nTotal: {sum(1 for r in results.values() if r['success'])}/{len(results)} files translated"
)
