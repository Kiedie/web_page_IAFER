#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive translation script for HTML files
"""

import os
import re

# Comprehensive translation mappings for each file
translations_map = {
    'gpais/contrastive-learning.html': {
        'lang="es"': 'lang="en"',
        'aria-label="Navegacion principal"': 'aria-label="Main navigation"',
        'aria-label="Abrir menu"': 'aria-label="Open menu"',
        '<span>Explorar contenido</span>': '<span>Explore content</span>',
        '<span>Volver a GPAIS</span>': '<span>Back to GPAIS</span>',
        '<h2 class="section-title">¿Qué es Contrastive Learning?</h2>': '<h2 class="section-title">What is Contrastive Learning?</h2>',
        '<h2 class="section-title">¿Qué son los pares contrastivos?</h2>': '<h2 class="section-title">What are Contrastive Pairs?</h2>',
        '<h2 class="section-title">Métodos principales</h2>': '<h2 class="section-title">Main Methods</h2>',
        '<h2 class="section-title">Desafíos Actuales</h2>': '<h2 class="section-title">Current Challenges</h2>',
        '<h2 class="section-title">Nuestra Investigación</h2>': '<h2 class="section-title">Our Research</h2>',
        '<h2 class="section-title">Aplicaciones Prácticas</h2>': '<h2 class="section-title">Practical Applications</h2>',
        '<p class="footer-text">\n                <strong>Contrastive Learning</strong> - GPAIS Research Area\n                <span aria-hidden="true">•</span>\n                <a href="index.html" class="footer-link">Volver a GPAIS</a>\n                <span aria-hidden="true">•</span>\n                <a href="../index.html" class="footer-link">IAFER Project 2026</a>\n            </p>': '<p class="footer-text">\n                <strong>Contrastive Learning</strong> - GPAIS Research Area\n                <span aria-hidden="true">•</span>\n                <a href="index.html" class="footer-link">Back to GPAIS</a>\n                <span aria-hidden="true">•</span>\n                <a href="../index.html" class="footer-link">IAFER Project 2026</a>\n            </p>',
    }
}

def apply_translations(filepath, translations):
    """Apply translations to a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for spanish, english in translations.items():
            content = content.replace(spanish, english)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, None
    except Exception as e:
        return False, str(e)

# Main function
def main():
    os.chdir('c:\\Users\\isega\\Documents\\web_page_IAFER')
    
    files_to_translate = [
        'gpais/contrastive-learning.html',
        'gpais/self-supervised.html',
        'gpais/zero-shot.html',
        'gpais/agentic-ai.html',
        'trustworthy/index.html',
        'trustworthy/explainability/index.html',
        'trustworthy/fairness/index.html',
        'trustworthy/robustness/index.html',
        'trustworthy/privacy/index.html',
        'trustworthy/governance/index.html',
        'trustworthy/automl/index.html',
        'trustworthy/critical-applications/index.html',
    ]
    
    results = {}
    for filepath in files_to_translate:
        print(f"Processing {filepath}...")
        translations = translations_map.get(filepath, {'lang="es"': 'lang="en"'})
        
        if os.path.exists(filepath):
            success, error = apply_translations(filepath, translations)
            results[filepath] = success
            status = "✓" if success else "✗"
            print(f"  {status} {filepath}")
            if error:
                print(f"      Error: {error}")
        else:
            print(f"  ✗ {filepath} (not found)")
            results[filepath] = False
    
    successful = sum(1 for v in results.values() if v)
    print(f"\n\nSummary: {successful}/{len(results)} files translated successfully")

if __name__ == '__main__':
    main()
