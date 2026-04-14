#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import csv
import os
import re
from collections import defaultdict

# Leer datos JSON
json_files = [f for f in os.listdir("data/papers") if f.endswith(".json")]
papers_data = []

for json_file in json_files:
    try:
        with open(f"data/papers/{json_file}", "r", encoding="utf-8") as f:
            paper = json.load(f)
            papers_data.append(paper)
    except:
        pass

# Leer CSV para obtener información de repositorios y enlaces
papers_csv_data = {}
with open("papers/Publicaciones IAFER.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Extraer autores y título para matching
        ref = row["Referencia (Autores, titulo, revista/congreso, numero volumen)"]
        papers_csv_data[ref] = {
            "Enlace": row["Enlace"],
            "Responsable": row["Responsable"],
            "Notas": row.get("Notas", ""),
        }

# ============= ESTRUCTURA DE CONOCIMIENTO DETALLADA =============
knowledge_structure = {
    "IAFER (IA Fiable, Explicable y Responsable)": {
        "description": "Marco de investigación integral sobre Inteligencia Artificial confiable, explicable y responsable",
        "areas": {
            "GPAIS (Algoritmos de IA de Propósito General)": {
                "description": "Desarrollo de algoritmos generales de IA y computación evolutiva",
                "lines": {
                    "Algoritmos de IAPG": {
                        "description": "Diseño y optimización de algoritmos generales",
                        "methods": [
                            "Computación Evolutiva",
                            "Optimización Multiobjetivo",
                            "Ingeniería de Características",
                        ],
                        "papers": [],
                    },
                    "AutoML y Few-shot Learning": {
                        "description": "Aprendizaje automático automatizado y con pocos ejemplos",
                        "methods": [
                            "Feature Engineering Automática",
                            "Meta-aprendizaje",
                            "Adaptación de dominio",
                        ],
                        "papers": [],
                    },
                    "Zero-Shot Learning": {
                        "description": "Aprendizaje sin ejemplos previos de la clase objetivo",
                        "methods": [
                            "Espacios Semánticos",
                            "Selección de Atributos",
                            "Optimización de Espacios (Atributos semánticos)",
                        ],
                        "papers": [],
                    },
                    "Deep Learning y Series Temporales": {
                        "description": "Redes profundas para análisis temporal",
                        "methods": [
                            "Transformers",
                            "Codificaciones Posicionales",
                            "Clasificación de Series Temporales",
                        ],
                        "papers": [],
                    },
                    "Contrastive Learning": {
                        "description": "Aprendizaje mediante comparación de ejemplos",
                        "methods": [
                            "Self-supervised Learning",
                            "Representaciones contrastivas",
                        ],
                        "papers": [],
                    },
                },
            },
            "XAI (Explicabilidad)": {
                "description": "Inteligencia Artificial Explicable - Métodos y enfoques",
                "categories": {
                    "Métodos de Explicabilidad": {
                        "Atribución de Importancias (Feature-level)": {
                            "description": "Determina qué características son importantes para la predicción",
                            "subtypes": [
                                "LIME (Local Interpretable Model-agnostic Explanations)",
                                "SHAP (SHapley Additive exPlanations)",
                                "Gradient-based methods (Saliency maps)",
                                "Attention mechanisms",
                            ],
                            "scope": "Local",
                            "papers": [],
                        },
                        "Métodos Basados en Reglas y Conceptos": {
                            "description": "Usa reglas lógicas o conceptos para explicar decisiones",
                            "subtypes": [
                                "Concept-based explanations",
                                "Rule extraction",
                                "Symbolic AI",
                                "Knowledge graphs",
                            ],
                            "scope": "Global",
                            "papers": [
                                "CUBIC: Unsupervised Detection of Conceptual Biases"
                            ],
                        },
                        "Métodos Basados en Ejemplos": {
                            "description": "Proporciona ejemplos similares o prototípicos",
                            "subtypes": [
                                "Case-based explanations",
                                "Example-based methods",
                                "Prototype selection",
                                "Instance-based learning",
                            ],
                            "scope": "Local",
                            "papers": [],
                        },
                    },
                    "Scopes de Explicabilidad": {
                        "Explicaciones Locales": {
                            "description": "Explica decisiones individuales o predicciones específicas",
                            "characteristics": [
                                "Enfoque en instancias individuales",
                                "Perturbaciones locales",
                                "Justificaciones específicas del caso",
                            ],
                            "papers": [],
                        },
                        "Explicaciones Globales": {
                            "description": "Explica el comportamiento general del modelo",
                            "characteristics": [
                                "Patrones a nivel de modelo",
                                "Reglas generales",
                                "Importancia de características global",
                            ],
                            "papers": [],
                        },
                        "Explicaciones Mixtas": {
                            "description": "Combina perspectivas locales y globales",
                            "characteristics": [
                                "Híbridos local-global",
                                "Explicaciones jerárquicas",
                                "Framework integrados",
                            ],
                            "papers": [],
                        },
                    },
                },
            },
            "Gobernanza y Confiabilidad de IA": {
                "description": "Aspectos de auditoría, reproducibilidad, certificación y gobernan za",
                "lines": {
                    "Reproducibilidad y Auditoría": {
                        "description": "Asegurar reproducibilidad de resultados y auditoría de sistemas IA",
                        "papers": [],
                    },
                    "Privacidad y Seguridad": {
                        "description": "Aprendizaje federado, diferencial privacy y trazabilidad",
                        "papers": [],
                    },
                    "Equidad y Mitigación de Sesgos": {
                        "description": "Detección y mitigación de bias en modelos de IA",
                        "papers": [],
                    },
                    "Robustez y Detección de Anomalías": {
                        "description": "Out-of-distribution detection, adversarial robustness",
                        "papers": [],
                    },
                },
            },
        },
    }
}

# Clasificar papers
for paper in papers_data:
    title = paper.get("title", "")
    area = paper.get("research_area", "")
    line = paper.get("research_line", "")

    # Asignar a la estructura
    if area == "gpais":
        if "AutoML" in line or "Few-shot" in line:
            knowledge_structure["IAFER (IA Fiable, Explicable y Responsable)"]["areas"][
                "GPAIS (Algoritmos de IA de Propósito General)"
            ]["lines"]["AutoML y Few-shot Learning"]["papers"].append(title)
        elif "Zero-Shot" in line:
            knowledge_structure["IAFER (IA Fiable, Explicable y Responsable)"]["areas"][
                "GPAIS (Algoritmos de IA de Propósito General)"
            ]["lines"]["Zero-Shot Learning"]["papers"].append(title)
        elif "Series Temporales" in line:
            knowledge_structure["IAFER (IA Fiable, Explicable y Responsable)"]["areas"][
                "GPAIS (Algoritmos de IA de Propósito General)"
            ]["lines"]["Deep Learning y Series Temporales"]["papers"].append(title)
        elif "Contrastive" in line:
            knowledge_structure["IAFER (IA Fiable, Explicable y Responsable)"]["areas"][
                "GPAIS (Algoritmos de IA de Propósito General)"
            ]["lines"]["Contrastive Learning"]["papers"].append(title)
        else:
            knowledge_structure["IAFER (IA Fiable, Explicable y Responsable)"]["areas"][
                "GPAIS (Algoritmos de IA de Propósito General)"
            ]["lines"]["Algoritmos de IAPG"]["papers"].append(title)

# Imprimir en formato markdown
import sys

sys.stdout.reconfigure(encoding="utf-8")

print(
    """
# ESTRUCTURA DEL CONOCIMIENTO - IAFER

## Vision General

El grupo IAFER (Inteligencia Artificial Fiable, Explicable y Responsable) se organiza alrededor de tres pilares principales:

1. **GPAIS**: Algoritmos de propósito general y aprendizaje automático avanzado
2. **XAI**: Explicabilidad y transparencia en IA
3. **Gobernanza**: Confiabilidad, equidad y responsabilidad

---

## 1. GPAIS (Algoritmos de IA de Propósito General)

### 1.1 Computación Evolutiva y Optimización
- **Propósito**: Desarrollar algoritmos generales basados en evolución para resolver problemas complejos
- **Métodos clave**:
  - Algoritmos genéticos
  - Estrategias evolutivas
  - Optimización multiobjetivo
  - Ingeniería automática de características

### 1.2 AutoML y Few-shot Learning
- **Propósito**: Automatizar el proceso de construcción de modelos ML con recursos limitados
- **Métodos clave**:
  - Feature engineering automática
  - Meta-aprendizaje
  - Transfer learning
  - Adaptación de dominio

### 1.3 Zero-Shot Learning (ZSL)
- **Propósito**: Clasificar objetos de clases nunca vistas mediante espacios semánticos
- **Métodos clave**:
  - Atributos semánticos
  - Selección de atributos (feature selection)
  - Refinamiento de espacios semánticos
  - Preprocesamiento de características

### 1.4 Deep Learning y Series Temporales
- **Propósito**: Análisis de datos secuenciales complejos
- **Métodos clave**:
  - Transformers
  - Codificaciones posicionales entrenables
  - Atención local
  - Clasificación de series temporales

### 1.5 Contrastive Learning
- **Propósito**: Aprendizaje autodirigido mediante comparación de ejemplos
- **Métodos clave**:
  - Contrastive loss functions
  - Self-supervised learning
  - Representaciones robustas

---

## 2. XAI (Inteligencia Artificial Explicable)

### 2.1 Métodos de Explicabilidad por Tipo

#### A. Métodos Basados en Atribución de Importancias
**Concepto**: Determinan qué características (features) son más importantes para la decisión del modelo

- **Métodos Locales**:
  - LIME: Crea modelos lineales locales alrededor de predicciones
  - SHAP: Valores de Shapley para atribución justa
  - Gradient-based Saliency: Basados en gradientes de activación

- **Métodos Globales**:
  - Feature importance global
  - Permutation importance
  - Partial dependence plots

- **Aplicaciones en IAFER**: OOD Detection (STOOD-X)

#### B. Métodos Basados en Reglas y Conceptos
**Concepto**: Usan conceptos semánticos o reglas lógicas para explicar decisiones

- **Enfoques**:
  - Concept-based explanations (CVEC, ACE)
  - Extracción de reglas
  - Conocimiento simbólico
  - Grafos de conocimiento
  - Embeddings visión-lenguaje (CUBIC)

- **Aplicaciones en IAFER**: 
  - CUBIC: Detección de sesgos conceptuales
  - Modelos generativos explicables

#### C. Métodos Basados en Ejemplos
**Concepto**: Proporciona ejemplos representativos o casos similares

- **Enfoques**:
  - Explicaciones basadas en casos
  - Selección de prototipos
  - Ejemplos contradictorios (counterfactuals)
  - Instancias influenciales

### 2.2 Métodos de Explicabilidad por Alcance

#### Explicaciones Locales
- Explican predicciones individuales
- Perturbaciones alrededor de la instancia
- Justificaciones específicas del caso
- **Ejemplo**: "Este paciente tiene esta enfermedad porque..."

#### Explicaciones Globales
- Explican el comportamiento general del modelo
- Patrones a nivel de modelo completo
- Reglas y patrones generales
- **Ejemplo**: "Todas las imágenes con esta característica tienden a..."

#### Explicaciones Mixtas (Local + Global)
- Combina perspectivas locales y globales
- Frameworks jerárquicos
- Vistas multi-nivel
- **Ejemplo**: "Este paciente tiene esta enfermedad POR ESTAS razones LOCALES, que son casos especiales de este patrón GLOBAL"

---

## 3. Gobernanza, Confiabilidad y Responsabilidad

### 3.1 Reproducibilidad y Auditoría
- Asegurar resultados reproducibles
- Certificación de modelos
- Trazabilidad de decisiones
- Evaluación de madurez XAI

### 3.2 Privacidad y Seguridad
- Aprendizaje federado
- Privacidad diferencial
- Blockchain para trazabilidad
- Análisis de huella de privacidad

### 3.3 Equidad y Mitigación de Sesgos
- Detección de bias conceptual (CUBIC)
- Mitigación de discriminación
- Equidad en aplicaciones críticas
- Auditoría de sesgo

### 3.4 Robustez y Confiabilidad
- Detección Out-of-Distribution (STOOD-X)
- Robustez adversarial
- Detección de anomalías
- Validación de distribución

---

## 4. Intersecciones Clave

### XAI + GPAIS
- Explicabilidad de modelos evolutivos
- Algoritmos que aprenden a explicar
- Meta-learning para explicabilidad
- Few-shot learning con interpretabilidad

### XAI + Gobernanza
- Frameworks de evaluación XAI
- Auditoría explicable
- Certificación de sistemas
- Responsabilidad y transparencia

### GPAIS + Gobernanza
- AutoML equitativo
- Selección automática de modelos justos
- Feature engineering ético
- Optimización con restricciones de confiabilidad

---

## 5. Aplicaciones Verticales

### Salud y Medicina
- Diagnóstico explicable
- Predicción de complicaciones
- Análisis genómico interpretable
- Out-of-distribution detection para nuevas enfermedades

### Energía y Sostenibilidad
- Predicción de consumo energético
- Optimización de almacenamiento
- Forecasting explicable
- Feature engineering automática

### Agricultura
- Detección de daño post-incendio
- Clasificación de plantas
- Mapeo predictivo
- Imágenes UAV interpretables

### Educación
- Predicción de desempeño estudiantil
- Análisis de minería de datos educativos
- Evaluación interpretable

---

## 6. Dimensiones de Evaluación de XAI (según IAFER)

1. **Dimensión Técnica**: Precisión y calidad de explicaciones
2. **Dimensión de Auditoría**: Trazabilidad y reproducibilidad
3. **Dimensión de Gobernanza**: Conformidad y certificabilidad
4. **Dimensión Humana**: Comprensibilidad y usabilidad

"""
)

print("\n\n" + "=" * 100)
print("PAPERS CLASIFICADOS POR ÁREA")
print("=" * 100)

# Mostrar papers por área
for paper in sorted(papers_data, key=lambda p: p.get("research_area", "")):
    area = paper.get("research_area", "unknown")
    line = paper.get("research_line", "unknown")
    title = paper.get("title", "Unknown")
    print(f"\n[{area.upper()}] {line}")
    print(f"  └─ {title[:85]}")
