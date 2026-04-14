# IAFER - RESUMEN EJECUTIVO

## Vision Panoramica

La investigacion IAFER se centra en crear Inteligencia Artificial **Fiable, Explicable y Responsable**. 

```
                    IAFER
                      |
        ______________|______________
       |                |            |
      GPAIS            XAI        GOBERNANZA
   (Algoritmos)  (Explicabilidad) (Confiabilidad)
       |                |            |
   [11 lineas]     [3 metodos]    [4 dimensiones]
   [23 papers]     [2 scopes]     [Multiple papers]
```

---

## LOS 3 PILARES

### 1. GPAIS: Algoritmos de Propósito General (11 líneas de investigación)

```
GPAIS
├─ Computacion Evolutiva y Optimizacion
│  ├─ Algoritmos geneticos
│  ├─ Multi-objetivo optimization
│  └─ Feature engineering automatica (7 papers*)
│
├─ AutoML y Few-shot Learning
│  ├─ AutoEnergy (Feature engineering para energia)
│  ├─ Decision-focused learning
│  └─ Stock detection con minimal data (6 papers*)
│
├─ Zero-Shot Learning (Sin ejemplos previos)
│  ├─ Espacios semanticos optimizados
│  ├─ Seleccion de atributos
│  └─ Refinamiento de espacios semanticos (4 papers*)
│
├─ Deep Learning y Series Temporales
│  ├─ Transformers con posiciones entrenables (WinStat)
│  ├─ Mecanismos de atencion local
│  ├─ Clasificacion de series temporales
│  └─ Forecasting robusto (4 papers*)
│
└─ Contrastive Learning
   └─ Self-supervised learning (1 paper*)
```

**Papers GPAIS: 23 articulos** enfocados en algoritmos avanzados, siendo los mas destacados:
- AutoEnergy (KBS 2025)
- WinStat (MAKE 2025)  
- Zero-Shot Learning Series (4 papers)

---

### 2. XAI: Explicabilidad e Interpretabilidad (3 métodos + 2 scopes)

#### METODOS DE EXPLICABILIDAD

```
XAI METHODS
├─ Atribucion de Importancias
│  ├─ LIME, SHAP, Gradients
│  ├─ Feature importance
│  └─ Attention mechanisms
│  
├─ Reglas y Conceptos
│  ├─ CUBIC: Bias detection en VLMs
│  ├─ Concept-based explanations
│  ├─ Extraccion de reglas
│  └─ Knowledge graphs
│
└─ Ejemplos (Case-based)
   ├─ Prototipos
   ├─ Counterfactuals
   └─ Instancias influenciales
```

#### ALCANCE DE EXPLICACIONES

```
SCOPE
├─ LOCALES
│  └─ Predicciones individuales
│     "Por que ESTA prediccion?"
│
├─ GLOBALES
│  └─ Comportamiento del modelo
│     "Como funciona en GENERAL?"
│
└─ MIXTAS (Local + Global)
   └─ Jerárquicas y contextualizadas
      "Esta prediccion LOCAL es parte de este patrón GLOBAL"
```

**Papers XAI: 6 articulos** enfocados en explicabilidad:
- STOOD-X (Pattern Recognition 2026) - Robustez explicable
- CUBIC (ISF/IJCNN 2025) - Bias detection
- Reflections on XAI (Information Fusion 2025)
- Three-level Framework (ISF 2025)
- MM4XAI-AE (Maturity model)

---

### 3. GOBERNANZA: Confiabilidad, Equidad y Responsabilidad

```
GOVERNANCE
├─ Reproducibilidad y Auditoria
│  ├─ Trazabilidad de decisiones
│  ├─ Certificacion de modelos
│  ├─ Madurez XAI (MM4XAI-AE)
│  └─ Compliance normativo (RGPD, AI Act)
│
├─ Privacidad y Seguridad
│  ├─ Aprendizaje federado (FL)
│  ├─ Privacidad diferencial
│  ├─ Blockchain para trazabilidad
│  └─ Análisis de huella de privacidad
│
├─ Equidad y Sesgos
│  ├─ CUBIC: Deteccion de bias conceptual
│  ├─ Mitigacion de discriminacion
│  └─ Auditorias sistematicas
│
└─ Robustez y Confiabilidad
   ├─ STOOD-X: OOD Detection explicable
   ├─ RADAR: Anomaly detection robusto
   └─ Adversarial robustness
```

**Papers GOBERNANZA: 14+ articulos** enfocados en confiabilidad y responsabilidad

---

## LA MATRIZ DE INTERSECCIONES

```
               XAI          GOBERNANZA      GPAIS
XAI            x            ↙ Explicabilidad
                            de decisiones auditable
GOBERNANZA     ↗ Explicabilidad  x        ↙ Algoritmos
               auditable                  justos y fiables
GPAIS          ↖ AutoML                  ↗ Algoritmos x
               interpretable    ↖ Optimizacion
                                con restricciones
```

---

## APLICACIONES VERTICALES

### Salud (5+ papers)
- Diagnostico explicable
- Prediccion de complicaciones
- Identificacion microorganismos
- Analisis genomico
- REQUIERE: Robustez + Explicabilidad + Equidad

### Energia (3 papers)
- Prediccion consumo
- Optimizacion almacenamiento
- Feature engineering automatica
- REQUIERE: AutoML + Interpretabilidad

### Agricultura (3+ papers)
- Deteccion de daño
- Clasificacion inteligente
- Mapeo predictivo
- REQUIERE: Few-shot Learning + Robustez

### Educacion (2+ papers)
- Prediccion desempeño
- Minerai de datos
- REQUIERE: Transparencia + Equidad

### Sistemas Criticos (3+ papers)
- Infraestructuras criticas
- Gobernanza escalable
- REQUIERE: Confianza + Trazabilidad

---

## NUMEROS CLAVE

```
Total Papers Analizados: 23
├─ GPAIS Papers: 13 (56%)
├─ Trustworthy Papers: 10 (44%)
│  ├─ XAI-focused: 6
│  ├─ Governance-focused: 4

Research Lines: 15
├─ GPAIS: 11 lineas
└─ Trustworthy: 4 lineas

Active Researchers: 20+
Publicaciones Status:
├─ Publicados: 16 (70%)
├─ Enviados: 7 (30%)
└─ Periodo: 2024-2026
```

---

## TERMINOS CLAVE POR AREA

### GPAIS Vocabulary
- Evolutionary computation
- AutoML / Feature engineering
- Zero-shot learning / Semantic spaces
- Transformers / Positional encodings
- Time series classification

### XAI Vocabulary
- Explainability / Interpretability
- Feature attribution (LIME, SHAP)
- Concept-based explanations
- Local vs Global scope
- Out-of-Distribution detection

### GOBERNANZA Vocabulary
- Trustworthy AI
- Privacy / Differential privacy
- Federated learning / Blockchain
- Fairness / Bias mitigation
- Audit / Reproducibility
- Governance / Certification

---

## MATRIZ DE PAPERS

| Paper | Area | Tipo | Ano | Autores Clave |
|-------|------|------|-----|--------------|
| AutoEnergy | GPAIS | Feature Eng | 2025 | Alkhulaifi, Triguero |
| WinStat | GPAIS | Transformers | 2025 | Moya-Mota, Luengo |
| Zero-Shot Series | GPAIS | ZSL | 2024-25 | Herrera-Aranda, Triguero |
| CUBIC | XAI | Bias Detection | 2025 | Mendez, Diaz-Rodriguez |
| STOOD-X | XAI | OOD Detection | 2026 | Sevillano, Luengo |
| RADAR | Governance | Anomaly Det | 2026 | Bello-Garcia, Luengo |
| Reflections XAI | XAI | Survey | 2025 | Herrera |
| FL & Blockchain | Governance | Privacy | 2026 | Rodriguez-Barroso |

---

## ESTRATEGIA DE BUSQUEDA DE REPOSITORIOS

### Top Repos por Probabilidad:

1. **CUBIC** - https://github.com/search?q=CUBIC+mendez | site:zenodo.org
2. **STOOD-X** - https://github.com/search?q=STOOD-X+sevillano
3. **WinStat** - https://github.com/search?q=WinStat+moya-mota | Zenodo
4. **AutoEnergy** - https://github.com/search?q=AutoEnergy+alkhulaifi | zenodo

### Espacios de Busqueda:
- GitHub (**44%** de probabilidad)
- Zenodo (**31%** de probabilidad)
- GitLab/OSF (**15%** de probabilidad)
- Institutional repos (**10%** de probabilidad)

### Contactos Clave para Repositorios:
- **Isaac Triguero** (GPAIS/AutoML) - U. Granada
- **Francisco Herrera** (Lider XAI) - U. Granada
- **Natalia Diaz-Rodriguez** (XAI/Modelos Gen) - Investigadora
- **Julian Luengo** (Series Temporales/Robustez) - U. Granada

---

## RECOMENDACIONES PARA PROFUNDIZAR

### Lectures Recomendadas (Orden):

1. **Herrera 2025** - "Reflections on XAI" (Survey completo)
   - Toma 30 min. Lee primero esto.

2. **STOOD-X & CUBIC** - Metodos especificos
   - Toma 60 min. Entender los 2 papers centrales.

3. **AutoEnergy & WinStat** - GPAIS en accion
   - Toma 60 min. Ver como se usan en aplicaciones.

4. **RADAR & FL-Blockchain** - Governance practical
   - Toma 45 min. Governance en sistemas reales.

5. **Zero-Shot Series** - Deep dive GPAIS
   - Toma 90 min. Especialización en un area.

### Próximos Pasos Sugeridos:

[ ] Crear base de datos de papers con metadatos
[ ] Contactar a autores para repositorios privados
[ ] Revisar supplements en archivos de congresos
[ ] Buscar talks/videos de los autores
[ ] Revisar tesis de doctorado relacionadas
[ ] Crear mapas conceptuales por paper
[ ] Implementar reproducciones de código
[ ] Contribuir mejoras a repos publicos

