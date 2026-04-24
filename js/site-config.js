// ============================================
// SITE-CONFIG.JS - Fuente única de la estructura del sitio
// ============================================

const SITE_CONFIG = {
    brand: 'IAFER',
    brandUrl: 'index.html',
    navItems: [
        {
            label: 'GPAIS',
            url: 'gpais/index.html',
            type: 'dropdown',
            children: [
                { label: 'Contrastive Learning', url: 'gpais/contrastive-learning/index.html' },
                { label: 'Self-Supervised Learning', url: 'gpais/self-supervised/index.html' },
                { label: 'Zero-Shot Learning', url: 'gpais/zero-shot/index.html' },
                { label: 'AutoML & Few-Shot Learning', url: 'gpais/automl/index.html' },
                { label: 'Agentic AI', url: 'gpais/agentic-ai/index.html' },
            ]
        },
        {
            label: 'Trustworthy',
            url: 'trustworthy/index.html',
            type: 'dropdown',
            children: [
                { label: 'Explainability (XAI)', url: 'trustworthy/explainability/index.html' },
                { label: 'Fairness & Bias', url: 'trustworthy/fairness/index.html' },
                { label: 'Robustness & OOD', url: 'trustworthy/robustness/index.html' },
                { label: 'Privacy & Federated Learning', url: 'trustworthy/privacy/index.html' },
                { label: 'Governance & Regulation', url: 'trustworthy/governance/index.html' },
                { label: 'Critical Applications', url: 'trustworthy/critical-applications/index.html' },
            ]
        },
        {
            label: 'Results',
            url: 'papers/index.html',
            type: 'link'
        }
    ],
    footer: {
        copy: '© 2026 IAFER Chair – University of Granada.',
        linkText: 'ENIA IAFER Chair',
        linkUrl: 'index.html'
    }
};
