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

// ============================================
// NAVBAR.JS - Navbar functionality
// ============================================
(function() {
    const toggle = document.getElementById('navbar-toggle');
    const menu = document.getElementById('navbar-menu');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', function() {
        this.classList.toggle('active');
        menu.classList.toggle('open');
    });

    // Mobile dropdown handling
    if ('ontouchstart' in window || window.innerWidth <= 768) {
        document.querySelectorAll('.navbar__item--dropdown > .navbar__link').forEach(function(link) {
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    this.parentElement.classList.toggle('open');
                }
            });
        });
    }

    // Close menu when clicking dropdown link
    document.querySelectorAll('.navbar__dropdown a').forEach(function(link) {
        link.addEventListener('click', function() {
            menu.classList.remove('open');
            toggle.classList.remove('active');
        });
    });

    // Reset on resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            menu.classList.remove('open');
            toggle.classList.remove('active');
            document.querySelectorAll('.navbar__item--dropdown').forEach(function(item) {
                item.classList.remove('open');
            });
        }
    });

    log('Navbar initialized');
})();
