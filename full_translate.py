#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full translation of HTML files from Spanish to English
"""

import os
import sys

# Dictionary with all translations
translation_dict = {
    # Navigation and common
    "Navegacion principal": "Main navigation",
    "Abrir menu": "Open menu",
    "Explorar contenido": "Explore content",
    "Volver a GPAIS": "Back to GPAIS",
    "Volver a Trustworthy": "Back to Trustworthy",
    "Volver a inicio": "Back to home",
    "Resultados": "Results",
    "Inicio": "Home",
    "Líneas Investigación": "Research Lines",
    "Equipo": "Team",
    # Titles and sections
    "¿Qué es Contrastive Learning?": "What is Contrastive Learning?",
    "¿Qué es Self-Supervised Learning?": "What is Self-Supervised Learning?",
    "¿Qué es Zero-Shot Learning?": "What is Zero-Shot Learning?",
    "¿Qué es la IA Agéntica?": "What is Agentic AI?",
    "¿Qué es?": "What is it?",
    "¿Por qué importa la gobernanza?": "Why does governance matter?",
    "¿Qué es Explainability?": "What is Explainability?",
    "¿Qué es Fairness en IA?": "What is Fairness in AI?",
    "¿Qué es Robustez en IA?": "What is Robustness in AI?",
    "¿Qué es Federated Learning con Privacidad?": "What is Federated Learning with Privacy?",
    "¿Por qué son críticos estos dominios?": "Why are these domains critical?",
    # Main section titles
    "¿Qué son los pares contrastivos?": "What are Contrastive Pairs?",
    "Métodos principales": "Main Methods",
    "Desafíos Actuales": "Current Challenges",
    "Nuestra Investigación": "Our Research",
    "Aplicaciones Prácticas": "Practical Applications",
    "Tipos de métodos": "Types of methods",
    "Nuestras líneas de investigación": "Our research lines",
    "Cómo funciona el Contrastive Learning": "How Contrastive Learning works",
    "Retos Actuales": "Current Challenges",
    "Tipos de espacio semántico": "Types of semantic space",
    "Workflow No Agéntico": "Non-Agentic Workflow",
    "Workflow Agéntico": "Agentic Workflow",
    "Grados de autonomía": "Degrees of autonomy",
    "¿Por qué fallan los LLMs?": "Why do LLMs fail?",
    "Aplicaciones en Instalaciones Críticas": "Applications in Critical Facilities",
    "Trustworthy Artificial Intelligence": "Trustworthy Artificial Intelligence",
    "Pilares de Confianza": "Pillars of Trust",
    "Enfoques de Interpretabilidad": "Approaches to Interpretability",
    "Aplicaciones Clave": "Key Applications",
    "Dimensiones de Equidad": "Dimensions of Fairness",
    "Estrategias de Mitigación": "Mitigation Strategies",
    "Fuentes de Vulnerabilidad": "Sources of Vulnerability",
    "Estrategias de Defensa": "Defense Strategies",
    "Componentes Clave": "Key Components",
    "Casos de Uso": "Use Cases",
    "Marcos Regulatorios": "Regulatory Frameworks",
    "Pilares de Gobernanza Efectiva": "Pillars of Effective Governance",
    "Desafíos Regulatorios": "Regulatory Challenges",
    "Fases de AutoML": "AutoML Phases",
    "Mecanismos de Trustworthiness en AutoML": "Trustworthiness Mechanisms in AutoML",
    "Sectores de Impacto": "Impact Sectors",
    "Requisitos de Trustworthiness": "Trustworthiness Requirements",
    "Desafíos en Despliegue": "Deployment Challenges",
    "Aplicaciones en Dominios Críticos": "Applications in Critical Domains",
    "Algoritmos de referencia": "Reference Algorithms",
    # Other common phrases
    "NAVBAR PRINCIPAL": "MAIN NAVBAR",
    "Líneas de Investigación Activas": "Active Research Lines",
    "Publicaciones": "Publications",
    "ARIA": "ARIA",
    "Introducción": "Introduction",
    "Abstract": "Abstract",
    "Autores": "Authors",
}


def translate_file(filepath):
    """Translate all Spanish text in a file to English"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply all translations
        for spanish, english in translation_dict.items():
            content = content.replace(spanish, english)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"Error in {filepath}: {e}")
        return False


# Files to translate
files = [
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

# Change to working directory
os.chdir("c:\\Users\\isega\\Documents\\web_page_IAFER")

# Translate files
success = 0
for f in files:
    if os.path.exists(f):
        if translate_file(f):
            print(f"✓ {f}")
            success += 1
        else:
            print(f"✗ {f}")
    else:
        print(f"? {f} (not found)")

print(f"\n{success}/{len(files)} files translated successfully")
