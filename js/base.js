// ============================================
// BASE.JS - Funciones compartidas (opcional)
// ============================================

// Función de utilidad para logging
function log(message) {
    console.log(`[IAFER] ${message}`);
}

// Smooth scroll para enlaces internos
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});

// Función para mostrar/ocultar elementos
function toggle(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = element.style.display === 'none' ? 'block' : 'none';
    }
}

log('Base JS loaded');
