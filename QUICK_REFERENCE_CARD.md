# IAFER - QUICK REFERENCE CARD

## 1-PAGE CHEAT SHEET

### Los 3 Pilares IAFER en 30 segundos

```
GPAIS (13 papers)          XAI (6 papers)           GOVERNANCE (14+ papers)
Algoritmos Avanzados       Explicabilidad           Confiabilidad & Equidad
├─ AutoML ⭐              ├─ Atribucion 🎯          ├─ Privacy & FL 🔒
├─ Zero-Shot            ├─ Conceptos 📚           ├─ Fairness 📊
├─ Transformers ✨        ├─ Ejemplos ➡️           ├─ Robustez 🛡️
├─ EvolutionaryComp ♻️   ├─ Locales 🔍            └─ Audit 📋
└─ TimeSeries 📈        ├─ Globales 🌍
                        └─ Mixtas ☯️
```

---

### XAI Explicado Visualmente (El triangulo)

```
                    INTERPRETABILIDAD PERFECTA
                          (Imposible)
                           /\
                          /  \
         REGLAS LOGICAS  /    \  MODELOS LINEALES
         (Transparentes) /      \  (Interpretables)
                        /        \
                       /          \
                      /   XAI ZONE \
                     /  (Where we    \
                    /    work)        \
                   /____________________\
                REDES PROFUNDAS (Black Box)
                 (CUBOS = Explicables)
```

**XAI = Hacemos legible lo que no lo es**

---

### La Matriz 2x2: Scope + Metodo

```
                LOCAL                  GLOBAL
ATRIBUCION    Per-instance          All-feature
(Features)    LIME, SHAP            Permutation
              ◉ ◉ ◉                importance
              
CONCEPTOS     Concept vectors       World knowledge
(Symbolic)    CUBIC-local           CUBIC-global
              Rule explanations     Knowledge graphs
              
EJEMPLOS      Nearest neighbors     Prototypes
(Instance)    Counterfactuals       Exemplars
              ◯ → ◯ → ◉             Gallery

MIXTAS        Hierarchical          System dashboard
(Hybrid)      Context + local       Context + global
              ◯ ← ◉ → ◯             ◯ → [◉] ← ◯
```

---

### Papers Imprescindibles (READ FIRST)

| Paper | Why | Time | Link |
|-------|-----|------|------|
| **Reflections on XAI** | Survey overview | 30m | Herrera 2025 |
| **CUBIC** | Bias detection breakthrough | 45m | Mendez 2025 |
| **STOOD-X** | Robustness + explain | 45m | Sevillano 2026 |
| **AutoEnergy** | GPAIS en accion | 30m | Alkhulaifi 2025 |
| **WinStat** | Transformers avanzados | 40m | Moya-Mota 2025 |

**Total: ~2.5 hours para entender IAFER**

---

### Aplicacion Practica (Choose Your Adventure)

```
Quiero aprender sobre...

┌─ EXPLICABILIDAD
│  ├─ ¿Bias en AI? → CUBIC + Mendez papers
│  ├─ ¿OOD Detection? → STOOD-X + Sevillano
│  ├─ ¿General? → Herrera survey
│  └─ ¿Frameworks? → MM4XAI + THREE-LEVEL
│
├─ ALGORITMOS
│  ├─ ¿Feature engineering? → AutoEnergy + decision-focused
│  ├─ ¿Series temporales? → WinStat + time series survey
│  ├─ ¿Zero-shot? → Herrera-Aranda papers
│  └─ ¿Evolutivos? → Molina et al.
│
├─ APLICACIONES
│  ├─ ¿Salud? → Lung biopsy + MALDI-TOF + CLL
│  ├─ ¿Energía? → AutoEnergy + decision-focused
│  ├─ ¿Agricultura? → Wildfire mapping + vegetation
│  └─ ¿SMEs? → Sanchez + adoption framework
│
└─ GOBERNANZA
   ├─ ¿Privacy? → Rodriguez-Barroso FL papers
   ├─ ¿Fairness? → CUBIC + bias detection
   ├─ ¿Auditoria? → MM4XAI + reproducibility
   └─ ¿Critica? → Mentxaka governance
```

---

### Keyword Cloud (Las palabras mas importantes)

```
        EXPLICABILIDAD
              ⭐
    Interpretability ⭐ XAI
        ⭐     ⭐     
   LIME  SHAP  Feature-Attribution
   ⭐             ⭐
        Concepts  CUBIC
        ⭐    ⭐
    OOD ⭐ Examples
  Detection  ⭐ LOCAL vs GLOBAL
    ⭐   ⭐      ⭐
    Privacy Federated  Robustness
    Learning ⭐     ⭐
        ⭐  TRUSTWORTHY
        ⭐ AutoML ⭐
    Zero-Shot ⭐ Transformers
        ⭐  Evolution  ⭐
        TimeSeries|Fairness
```

---

### Busqueda Rapida de Repos (30 sec method)

1. **Copiar nombre del paper**
   - Ej: "CUBIC", "STOOD-X", "AutoEnergy"

2. **Buscar 3 lugares (en orden)**
   ```
   github.com/search?q=CUBIC
   zenodo.org (search)
   gitlab.com/search?q=CUBIC
   ```

3. **Si no hay resultado → Contactar autor**
   - Email: firstname.lastname@ugr.es
   - Twitter: @authorname
   - LinkedIn: Buscar "Universidad de Granada"

---

### Status de Papers (Junio 2026)

```
PUBLICADOS (16): ✅
├─ Journals: 9
├─ Conferences: 7

ENVIADOS (7): 🕐
├─ Under Review: 5
├─ Aceptados sin publicar: 2

ESTADISTICAS:
├─ 2024: 3 papers
├─ 2025: 10 papers ⬆️ Peak
├─ 2026: 10 papers (proyectado)
└─ Tasa: 1.43 papers/mes
```

---

### Los 10 Conceptos Fundamentales

1. **GPAIS** = Algoritmos generales para IA
2. **XAI** = Hacer IA legible para humanos
3. **ATRIBUCION** = Qué features importan
4. **CONCEPTOS** = Explicar con significado
5. **LOCAL** = Prediccion individual
6. **GLOBAL** = Comportamiento del modelo
7. **OOD** = Detectar datos anormales
8. **FL** = Aprendizaje federado (privado)
9. **FAIRNESS** = Equidad, sin discrimination
10. **AUDITORIA** = Verificable y reproducible

---

### Niveles de Profundidad

```
LEVEL 0: Beginner
├─ Lee: Resumen ejecutivo (30 min)
├─ Watch: Video intro XAI (10 min)
└─ Know: 3 pilares IAFER

LEVEL 1: Intermediate  
├─ Lee: 2-3 papers survey
├─ Mira: Code en GitHub
└─ Entiende: Diferencia local/global

LEVEL 2: Advanced
├─ Lee: Todos los 23 papers
├─ Implementa: Reproduce 1 paper
└─ Contribuye: Mejoras a repos

LEVEL 3: Expert (PhD level)
├─ Todos los anteriores +
├─ Tesis doctoral original
└─ Funding/nuevas lineas
```

---

### Conexiones Entre Conceptos

```
           ATRIBUCION
                |
            (explica)
                |
          Modelos IA ←→ Confianza Humana
         (black box)     (necesidad)
                |
                ├─ (requiere)
                |
        CONCEPTOS + EJEMPLOS
                |
            (proporciona)
                |
         Explicabilidad ←→ FAIRNESS
                |
            (necesita)
                |
         AUDITORIA
                |
         (verifica)
                |
           PRIVACIDAD (FL)
                |
         (protege a)
                |
        Datos Personales
```

---

### Proximos Events & Deadlines

```
CONFERENCIAS ACTIVAS:
├─ IEEE CAI 2026 (Feb-Mar) - 4 papers aceptados
├─ IJCNN 2025 (Rome) - CUBIC presented
└─ SMC 2025 (Vienna) - PCG + Cerezo

JOURNALS ACTIVOS:
├─ Information Fusion - 3+ papers en revision
├─ Pattern Recognition - STOOD-X (2026)
├─ Knowledge-Based Systems - AutoEnergy (2025)
└─ IEEE TEVC - Molina survey (2025)

TENDENCIAS 2026:
├─ ↑ Uso de VLMs en explicabilidad
├─ ↑ Privacidad federada
├─ ↑ OOD detection en sistemas criticos
├─ ↓ Black box sin explicacion
└─ ↓ Papers sin reproducibilidad
```

---

### Quick Repository Stats

```
REPOSITORIOS ENCONTRADOS: 6-8 de 23 (26-35%)
├─ GitHub: 5-6 repos
├─ Zenodo: 2 datasets/code
├─ GitLab/OSF: 1-2 repos
└─ Private (contactar): 15-17 papers

PAPERS SIN REPO PUBLICO:
- Aplicaciones medicas (17% de data)
- Estudios criticos (seguridad)
- Codigo proprietario
- En transicion (del lab a GitHub)

RECOMENDACION:
- Contactar directamente a autores
- Revisar supplements en PDF
- Buscar tesis relacionadas
- Join the group!
```

---

### Los 5 Comandos Magicos

```bash
# 1. Buscar paper en Google Scholar
site:scholar.google.com "CUBIC" 2025

# 2. Buscar en GitHub
site:github.com STOOD-X OR sevillano

# 3. Buscar en Zenodo
site:zenodo.org IAFER 2025

# 4. Buscar en arXiv supplements
site:arxiv.org AutoEnergy 2025 filetype:zip

# 5. Alerta Google
Set alert: "IAFER" OR "CUBIC" OR "WinStat"
```

---

### Decision Tree: Que Paper Leer Primero?

```
      START
        |
        ├─ ¿Necesitas intro? → Herrera 2025 (XAI Survey)
        |
        ├─ ¿Quieres metodo nuevo? 
        |  ├─ XAI → CUBIC o STOOD-X
        |  ├─ GPAIS → AutoEnergy o WinStat
        |  └─ Governance → FL papers
        |
        ├─ ¿Necesitas aplicacion?
        |  ├─ Salud → Lung biopsy
        |  ├─ Energia → AutoEnergy
        |  └─ Agricultura → Wildfire
        |
        └─ ¿Quieres deep dive?
           └─ Escoge un area + lee TODO
```

---

### Recursos Externos Recomendados

```
Aprendizaje XAI:
- XAI Handbook (Google)
- Interpretable ML book (Molnar)
- LIME & SHAP papers originales

Aprendizaje GPAIS:
- Transformer tutorials (Vaswani et al.)
- AutoML papers (Feurer, Hutter)
- Zero-shot learning surveys

comunidad IAFER:
- GitHub: Herrera, Triguero, Luengo
- Twitter: #XAI, #TrustworthyAI
- Conferences: IJCNN, SMC, CAI
```

---

### 🎯 OBJETIVO FINAL

```
┌─────────────────────────────────────┐
│  Sistemas IA que son:               │
│                                     │
│  ✓ EXPLICABLES (Puedes entender)    │
│  ✓ JUSTOS (Sin discriminacion)      │
│  ✓ ROBUSTOS (Confiar en ellos)      │
│  ✓ AUDITABLES (Verificables)        │
│  ✓ RESPONSABLES (Gobernable)        │
│                                     │
│  Eso es IAFER.                      │
│  Eso es el futuro.                  │
└─────────────────────────────────────┘
```

---

**Nota**: Este documento se actualiza cada mes. Revision: Junio 2026

