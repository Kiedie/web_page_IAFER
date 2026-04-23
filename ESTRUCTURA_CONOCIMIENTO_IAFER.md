# ESTRUCTURA DEL CONOCIMIENTO - IAFER

## Vision General

El grupo IAFER (Inteligencia Artificial Fiable, Explicable y Responsable) se organiza alrededor de tres pilares principales:

1. **GPAIS**: Algoritmos de propósito general y aprendizaje automático avanzado
2. **XAI**: Explicabilidad y transparencia en IA
3. **Gobernanza**: Confiabilidad, equidad y responsabilidad

---

## 1. GPAIS (Algoritmos de IA de Propósito General)

### 1.1 Computacion Evolutiva y Optimizacion
- **Proposito**: Desarrollar algoritmos generales basados en evolucion para resolver problemas complejos
- **Metodos clave**:
  - Algoritmos geneticos
  - Estrategias evolutivas multiobjetivo
  - Ingenieria automatica de caracteristicas (AutoFE)
  - Seleccion de caracteristicas adaptativa

**Papers clave**:
- Molina et al.: Evolutionary computation for design and enrichment of general-purpose AI systems
- Adaptive Feature Selection with Evolutionary Strategies

### 1.2 AutoML y Few-shot Learning
- **Proposito**: Automatizar la construccion de modelos ML con recursos limitados
- **Metodos clave**:
  - Feature engineering automatica (AutoEnergy)
  - Meta-aprendizaje
  - Transfer learning
  - Adaptacion de dominio

**Aplicaciones**:
- AutoEnergy: Feature engineering para prediccion de consumo energetico
- Decision-focused learning con AutoML
- Stock detection con minimal data (Few-shot)

### 1.3 Zero-Shot Learning (ZSL)
- **Proposito**: Clasificar objetos de clases nunca vistas mediante espacios semanticos
- **Metodos clave**:
  - Optimizacion de espacios semanticos
  - Seleccion de atributos semanticos
  - Refinamiento de caracteristicas
  - Preprocesamiento de espacios

**Research line**: 
- A preliminary study on preprocessing the semantic space in zero-shot learning
- A first approach to refine semantic spaces in zero-shot learning with GA
- Semantic-Inductive Attribute Selection for Zero-Shot Learning

### 1.4 Deep Learning y Series Temporales
- **Proposito**: Analisis de datos secuenciales complejos
- **Metodos clave**:
  - Transformers con codificaciones posicionales entrenables
  - Mecanismos de atencion local
  - Clasificacion de series temporales
  - Forecasting de series

**Papers**:
- WinStat: A family of trainable positional encodings for transformers
- Local attention mechanism for long-sequence time series
- Machine Learning for Time Series Classification: Comprehensive review

### 1.5 Contrastive Learning
- **Proposito**: Aprendizaje autodirigido mediante comparacion de ejemplos
- **Metodos clave**:
  - Contrastive loss functions
  - Self-supervised learning
  - Frequency-aware contrastive learning
  - Representaciones robustas

---

## 2. XAI (Inteligencia Artificial Explicable)

### 2.1 Clasificacion de Metodos XAI

#### A. Metodos Basados en Atribucion de Importancias
**Concepto**: Determinan que caracteristicas son mas importantes para la decision del modelo

**Metodos Locales**:
- LIME: Modelos lineales locales alrededor de predicciones
- SHAP: Valores de Shapley para atribucion justa
- Gradient-based: Mapas de saliency basados en gradientes
- Attention mechanisms: Mecanismos de atencion en redes

**Metodos Globales**:
- Feature importance global
- Permutation importance
- Partial dependence plots

**Aplicacion en IAFER**: 
- STOOD-X: Deteccion explicable de muestras Out-of-Distribution usando pruebas estadisticas

#### B. Metodos Basados en Reglas y Conceptos
**Concepto**: Usan conceptos semanticos o reglas logicas para explicar decisiones

**Enfoques**:
- Concept-based explanations (usando incrustaciones)
- Extraccion de reglas logicas
- Conocimiento simbolico y grafos de conocimiento
- Embeddings vision-lenguaje multimodales
- Deteccion de sesgos conceptuales

**Aplicacion en IAFER**:
- CUBIC: Unsupervised Detection of Conceptual Biases via Vision-Language Embeddings
  - Detecta sesgos en modelos vision-lenguaje
  - Usa incrustaciones multimodales para explicabilidad
  - Frameworks para modelos generativos explicables

#### C. Metodos Basados en Ejemplos
**Concepto**: Proporciona ejemplos representativos o casos similares

**Enfoques**:
- Explicaciones basadas en casos (Case-based)
- Seleccion de prototipos
- Ejemplos contradictorios (Counterfactuals)
- Instancias influenciales

### 2.2 Alcance de las Explicaciones: Local vs Global

#### Explicaciones Locales
**Caracteristicas**:
- Explican predicciones individuales o especificas
- Perturbaciones alrededor de la instancia
- Justificaciones particulares del caso
- Responden: "Por que esta prediccion?"

**Metodos**: LIME, Perturbation-based, Instance-specific

#### Explicaciones Globales
**Caracteristicas**:
- Explican el comportamiento general del modelo
- Patrones a nivel de modelo completo
- Reglas y comportamientos generales
- Responden: "Como funciona el modelo en general?"

**Metodos**: Feature importance global, Rule extraction, Concept-based

#### Explicaciones Mixtas (Local + Global)
**Caracteristicas**:
- Combinan perspectivas locales y globales
- Frameworks jerarquicos
- Vistas multi-nivel
- Contextualizan explicaciones locales en patrones globales

**Ejemplo practico**:
"Este paciente tiene esa enfermedad POR ESTAS razones LOCALES (estos sintomas especificos), que son casos especiales de ESTE patrón GLOBAL (pacientes con este perfil tienden a tenerla)"

**Aplicacion en IAFER**:
- Hybrid Evolutionary Assessment based on Logic Programming (local + global scope)
- Framework MM4XAI (Maturity Model for Explainability)

---

## 3. Gobernanza, Confiabilidad y Responsabilidad de IA

### 3.1 Reproducibilidad y Auditoria
- Asegurar resultados reproducibles y verificables
- Certificacion de modelos
- Trazabilidad de decisiones y decisiones
- Marcos de evaluacion de madurez XAI
- Compliance y regulacion (RGPD, AI Act)

**Paper clave**:
- MM4XAI-AE: A maturity model for practical explainability

### 3.2 Privacidad y Seguridad
- Aprendizaje federado descentralizado
- Privacidad diferencial
- Tecnologia blockchain para trazabilidad
- Analisis de huella de privacidad en pesos

**Research line**: IA responsable y gobernable con FL y Blockchain

### 3.3 Equidad y Mitigacion de Sesgos
- Deteccion de bias conceptual en VLMs
- Mitigacion de discriminacion
- Equidad en aplicaciones criticas (salud, justicia)
- Auditorias de sesgo sistematico

**Papers**:
- CUBIC: Deteccion de sesgos conceptuales
- Padial-Fuillerat et al.: Robust ML para identificacion de microorganismos

### 3.4 Robustez y Confiabilidad
- Deteccion Out-of-Distribution (OOD)
- Robustez adversarial
- Deteccion de anomalias
- Validacion de distribucion segura

**Papers**:
- STOOD-X: Explainable OOD Detection via Nonparametric Statistical Testing
- RADAR: Robust Anomaly Detection and Recognition

---

## 4. Intersecciones Clave Entre Areas

### XAI + GPAIS
- Algoritmos evolutivos explicables
- Meta-learning para generacion de explicaciones
- Optimizacion de espacios semanticos interpretables
- Few-shot learning con features entendibles

### XAI + Gobernanza
- Frameworks de evaluacion de madurez XAI
- Auditoria transparente de decisiones
- Trazabilidad y reproducibilidad
- Certificacion de sistemas explicables

### GPAIS + Gobernanza
- AutoML equitativo (sin discrimination)
- Seleccion automatica de caracteristicas justas
- Ingenieria de features etica
- Optimizacion con restricciones de confiabilidad

### Las Tres Areas
- Modelos generativos confiables (LLMs)
- Sistemas criticos con IA (salud, energia, agricultura)
- Gobernanza de sistemas generales (AGI readiness)

---

## 5. Aplicaciones Verticales

### Salud y Medicina
**Casos de uso**:
- Diagnostico con explicaciones clinicas
- Prediccion de complicaciones en biopsias pulmonares
- Identificacion de microorganismos resistentes
- Prediccion de variaciones genomicas en canales de calcio

**Requirenimientos**: 
- Robustez garantizada (OOD detection)
- Explainabilidad para validacion clinica
- Fairness y equidad entre poblaciones

### Energia y Sostenibilidad
**Casos de uso**:
- Prediccion de consumo energetico
- Optimizacion de almacenamiento
- Forecasting de demanda
- Feature engineering automatica para eficiencia

**Requirenimientos**: 
- AutoML bajo recursos
- Interpretabilidad de predicciones
- Credibilidad de modelos

### Agricultura y Medio Ambiente
**Casos de uso**:
- Deteccion de dano post-incendio con UAV
- Clasificacion inteligente de plantas
- Mapeo predictivo de viñedos
- Procesamiento de imagenes ultra-alta resolucion

**Requirenimientos**: 
- Interpretabilidad visual
- Robustez a cambios de distribucion
- Few-shot learning (datos limitados)

### Educacion
**Casos de uso**:
- Prediccion de desempeño academico
- Identificacion de estudiantes en riesgo
- Minerai de datos educativos
- Recomendaciones de aprendizaje personalizadas

**Requirenimientos**:
- Transparencia en mecanismos de prediccion
- Evitar discriminacion por origen
- Interpretabilidad para educadores

### Sistemas a gran escala (AGI-ready)
- Algoritmos generales para multiples dominios
- Composicion modular de metodos explicables
- Gobernanza escalable
- Confianza en sistemas autonomos

---

## 6. Marco de Evaluacion de XAI

### Cuatro Dimensiones (segun IAFER):

1. **Dimension Tecnica**
   - Precision de explicaciones
   - Fidelidad (explicacion genuina vs. artefacto)
   - Completitud
   - Estabilidad

2. **Dimension de Auditoria**
   - Trazabilidad de decisiones
   - Reproducibilidad
   - Verificabilidad
   - Documentacion

3. **Dimension de Gobernanza**
   - Conformidad normativa
   - Certificabilidad
   - Responsabilidad
   - Escalabilidad

4. **Dimension Humana**
   - Comprensibilidad para usuarios finales
   - Usabilidad de explicaciones
   - Trust en el sistema
   - Aceptabilidad

---

## 7. Listado Completo de Papers por Categoria

### PAPERS GPAIS
**Algoritmos de IAPG**:
- Hybrid Evolutionary Assessment based on Logic Programming
- Adaptive Feature Selection with Evolutionary Strategies

**AutoML y Few-shot**:
- AutoEnergy: Automated feature engineering for energy consumption
- Decision-focused learning with automated feature engineering
- Exploring TabPFNv2 for ADMET Prediction (Few-shot baseline)

**Zero-Shot Learning**:
- Semantic-Inductive Attribute Selection for ZSL
- A first approach to refine semantic spaces with GA
- A preliminary study on preprocessing semantic spaces

**Series Temporales**:
- Machine Learning for Time Series Classification (survey)
- WinStat: Trainable positional encodings for transformers
- Local attention mechanism for long-sequence forecasting

### PAPERS XAI

**Explicabilidad y Gobernanza**:
- Reflections on eXplainable AI (XAI): Journey from criticisms to human-AI collaboration
- MM4XAI-AE: Maturity model for practical explainability
- A Three-level Framework for LLM-enhanced XAI

**Explicabilidad y Robustez**:
- STOOD-X: Explainable OOD Detection via Statistical Testing

**Explicabilidad y Modelos Generativos**:
- CUBIC: Unsupervised Detection of Conceptual Biases via VLM
- Hybrid interpretable-deep learning for wildfire mapping

### PAPERS GOBERNANZA

**Reproducibilidad y Confiabilidad**:
- RADAR: Robust Anomaly Detection and Recognition framework
- Robust ML for MALDI-TOF MS analysis
- In silico prediction of genomic impact on ion channel function

**Privacidad y Federada Learning**:
- From Privacy to Trust in Agentic Era (FL taxonomy)
- Do Deep Learning Models Keep a Privacy Signature?

**Equidad y Responsabilidad**:
- AI Adoption in SMEs: Framework analysis
- Transformative AI in Critical Infrastructures

**Aplicaciones Criticas**:
- Prediction of complications in lung biopsies with AI
- ExG-Supervised U-Net for vineyard fire mapping
- Generalizing stock detection with minimal data

---

## Estrategia de Busqueda de Repositorios

Los repositorios de los papers pueden encontrarse en:

### Lugares Comunes:
1. **GitHub** (github.com) - mas probable
2. **GitLab** (gitlab.org/gitlab.com)
3. **Zenodo** (zenodo.org) - para codigo de investigacion
4. **OSF** (osf.io) - Open Science Framework
5. **Institutional repositories** - Universidad de Granada, etc.
6. **Paper supplements** - En arXiv, el sitio del journal, o suplementarios

### Terminos de Busqueda por Paper:

**CUBIC** (Conceptual Bias Detection):
- Buscar: "CUBIC" + "Mendez" OR "vision-language" + "bias" en GitHub
- Autores probables: David Mendez, Natalia Diaz-Rodriguez
- Repo likely: python package con detection de bias

**STOOD-X** (OOD Detection):
- Buscar: "STOOD-X" OR "Sevillano" + "OOD" + "statistical testing"
- Autores: Ivan Sevillano-Garcia, Julian Luengo
- Posiblemente en: github.com/julianluengo o similares

**AutoEnergy** (Feature Engineering para Energia):
- Buscar: "AutoEnergy" + "Alkhulaifi" OR "feature engineering" + "energy"
- Aplicacion clara: feature engineering para forecasting de consumo

**ZSL Papers** (Zero-Shot Learning):
- Buscar: "Herrera-Aranda" + "semantic space" OR "attribute selection"
- Key terms: "zero-shot" "genetic algorithm" "semantic"

**WinStat** (Transformers):
- Buscar: "WinStat" + "positional encoding" OR "time series" + "transformer"

### Comandos de Busqueda Efectivos:

```
site:github.com "CUBIC" "vision-language" OR "bias detection"
site:github.com "STOOD-X" OR "Sevillano"
site:github.com "AutoEnergy" OR "Alkhulaifi"
site:github.com "WinStat" OR "Moya-Mota"
site:github.com "zero-shot" + "semantic" + "Herrera"
site:zenodo.org IAFER OR "Pattern Recognition" 2026
```

### Recomendaciones:

1. **Contactar directamente con autores** - Los autores muchas veces tienen repos privados
2. **Revisar suplementarios en arXiv** - Frecuentemente linkean al codigo
3. **Buscar en universidades** - Granada, Sevilla, etc. tienen repos de investigacion
4. **GitHub personal del primer autor** - Suelen publicar ahi
5. **Pulsar a los autores en Twitter/LinkedIn** - Muchos comparten en redes

### URLs de Interes:
- Universidad de Granada: github.com/Universidad-de-Granada or similar
- Investigadores individuales: Buscar perfiles GitHub
- Papers con DOI: Revisar supplementaries en Zenodo

