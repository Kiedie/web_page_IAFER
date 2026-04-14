import os

# Diccionario de traducciones español -> inglés
translations = {
    # Títulos meta y encabezados
    "Aplicaciones en Dominios Críticos": "Critical Applications",
    "AutoML Confiable": "Trustworthy AutoML",
    "Privacidad + Confianza en FL": "Privacy in Federated Learning",
    "Robustez y OOD": "Robustness and Out-of-Distribution Detection",
    "Explainability Útil y Evaluable": "Useful and Evaluable Explainability",
    "Gobernanza y Regulación": "Governance and Regulation",
    # Descripciones meta
    "Investigación en despliegue seguro de IA en salud, justicia, finanzas y otros sectores de alto riesgo.": "Research on safe AI deployment in healthcare, justice, finance, and other high-risk sectors.",
    "Investigación en privacidad diferencial y aprendizaje federado: protección de datos y garantías de privacidad distribuida.": "Research in differential privacy and federated learning: data protection and distributed privacy guarantees.",
    "Investigación en robustez de sistemas de IA: resiliencia ante datos fuera de distribución, ataques adversariales y cambios ambientales.": "Research in AI robustness: resilience to out-of-distribution data, adversarial attacks, and environmental changes.",
    "Machine Learning automatizado que preserva explicabilidad, equidad y robustez.": "Automated Machine Learning that preserves explainability, fairness, and robustness.",
    "Investigación en explicabilidad y interpretabilidad de sistemas de IA: métodos evaluables, auditoría y trazabilidad.": "Research in explainability and interpretability of AI systems: evaluable methods, audit, and traceability.",
    "Research in algorithmic fairness, bias detection, and preservation of human autonomy in AI systems.": "Research in algorithmic fairness, bias detection, and preservation of human autonomy in AI systems.",
    # Contenido de páginas
    "Nuestra Investigación": "Our Research",
    "Líneas de Investigación Activas": "Active Research Lines",
    "Líneas de investigación activas": "Active research lines",
    "Línea de": "Line of",
    "línea de": "line of",
    "¿Qué es": "What is",
    "Investigación": "Research",
    # Conceptos de investigación
    "Equidad": "Fairness",
    "equidad": "fairness",
    "Sesgo": "Bias",
    "sesgos": "bias",
    "Cátedra": "Chair",
    "Auditoría": "Audit",
    "auditoría": "audit",
    "IA responsable": "responsible AI",
    # Secciones específicas de Trustworthy
    "Publicaciones": "Publications",
}

html_dir = r"c:\Users\isega\Documents\web_page_IAFER"

files_to_translate = [
    "index.html",
    "gpais\\index.html",
    "gpais\\agentic-ai.html",
    "gpais\\contrastive-learning.html",
    "gpais\\zero-shot.html",
    "gpais\\self-supervised.html",
    "trustworthy\\index.html",
    "trustworthy\\explainability\\index.html",
    "trustworthy\\fairness\\index.html",
    "trustworthy\\robustness\\index.html",
    "trustworthy\\governance\\index.html",
    "trustworthy\\automl\\index.html",
    "trustworthy\\privacy\\index.html",
    "trustworthy\\critical-applications\\index.html",
]

print("INICIANDO TRADUCCIÓN DE ARCHIVOS AL INGLÉS")
print("=" * 70)

translated_count = 0
total_replaced = 0

for rel_path in files_to_translate:
    filepath = os.path.join(html_dir, rel_path)
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content
            replaced = 0

            # Realizar traducciones
            for es, en in translations.items():
                count = content.count(es)
                if count > 0:
                    content = content.replace(es, en)
                    replaced += count

            # Guardar si hubo cambios
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                translated_count += 1
                total_replaced += replaced
                print(f"✓ {rel_path:<50} ({replaced} cambios)")
            else:
                print(f"- {rel_path:<50} (sin cambios)")
        except Exception as e:
            print(f"✗ {rel_path:<50} ERROR: {str(e)[:30]}")
    else:
        print(f"✗ {rel_path:<50} NO ENCONTRADO")

print("=" * 70)
print(f"ARCHIVOS MODIFICADOS: {translated_count}/{len(files_to_translate)}")
print(f"TOTAL DE CAMBIOS: {total_replaced}")
print("✅ TRADUCCIÓN COMPLETADA")
