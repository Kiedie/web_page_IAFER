// ============================================
// COMPONENTS.JS - Renderizado de navbar y footer
// ============================================

(function () {
    'use strict';

    // Calcula la profundidad relativa basándose en la ruta del script actual.
    // Si el script se carga como ../../js/components.js, depth = 2.
    function getBasePath() {
        const script = document.querySelector('script[src*="components.js"]');
        if (!script) return './';
        const src = script.getAttribute('src') || '';
        const depth = (src.match(/\.\.\//g) || []).length;
        return '../'.repeat(depth) || './';
    }

    function resolveUrl(relPath) {
        return getBasePath() + relPath;
    }

    function renderNavbar() {
        const container = document.getElementById('navbar-root');
        if (!container || typeof SITE_CONFIG === 'undefined') return;

        const cfg = SITE_CONFIG;
        const base = getBasePath();

        const itemsHtml = cfg.navItems.map(item => {
            if (item.type === 'dropdown') {
                const childrenHtml = item.children.map(child =>
                    `<li><a href="${resolveUrl(child.url)}">${child.label}</a></li>`
                ).join('');
                return `
                    <li class="navbar__item navbar__item--dropdown">
                        <a href="${resolveUrl(item.url)}" class="navbar__link">${item.label}</a>
                        <ul class="navbar__dropdown">${childrenHtml}</ul>
                    </li>
                `;
            }
            return `
                <li class="navbar__item">
                    <a href="${resolveUrl(item.url)}" class="navbar__link">${item.label}</a>
                </li>
            `;
        }).join('');

        container.innerHTML = `
            <nav class="navbar" aria-label="Main navigation">
                <div class="navbar__inner">
                    <a href="${base}" class="navbar__brand">${cfg.brand}</a>
                    <ul class="navbar__menu" id="navbar-menu">${itemsHtml}</ul>
                    <button class="navbar__hamburger" id="navbar-toggle" aria-label="Open menu">
                        <span></span><span></span><span></span>
                    </button>
                </div>
            </nav>
        `;
    }

    function renderFooter() {
        const container = document.getElementById('footer-root');
        if (!container || typeof SITE_CONFIG === 'undefined') return;

        const cfg = SITE_CONFIG;
        const base = getBasePath();

        const pageTitle = document.body.dataset.pageTitle || '';
        const titleHtml = pageTitle ? `<strong>${pageTitle}</strong> <span aria-hidden="true">•</span> ` : '';

        container.innerHTML = `
            <footer class="footer">
                <div class="container">
                    <p class="footer-text">
                        ${titleHtml}
                        ${cfg.footer.copy}
                        <span aria-hidden="true">•</span>
                        <a href="${base}" class="footer-link">${cfg.footer.linkText}</a>
                    </p>
                </div>
            </footer>
        `;
    }

    function initSite() {
        renderNavbar();
        renderFooter();

        // Inicializar comportamiento de navbar móvil (del base.js)
        const toggle = document.getElementById('navbar-toggle');
        const menu = document.getElementById('navbar-menu');

        if (toggle && menu) {
            toggle.addEventListener('click', function () {
                this.classList.toggle('active');
                menu.classList.toggle('open');
            });

            // Mobile dropdown handling
            if ('ontouchstart' in window || window.innerWidth <= 768) {
                document.querySelectorAll('.navbar__item--dropdown > .navbar__link').forEach(function (link) {
                    link.addEventListener('click', function (e) {
                        if (window.innerWidth <= 768) {
                            e.preventDefault();
                            this.parentElement.classList.toggle('open');
                        }
                    });
                });
            }

            document.querySelectorAll('.navbar__dropdown a').forEach(function (link) {
                link.addEventListener('click', function () {
                    menu.classList.remove('open');
                    toggle.classList.remove('active');
                });
            });

            window.addEventListener('resize', function () {
                if (window.innerWidth > 768) {
                    menu.classList.remove('open');
                    toggle.classList.remove('active');
                    document.querySelectorAll('.navbar__item--dropdown').forEach(function (item) {
                        item.classList.remove('open');
                    });
                }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSite);
    } else {
        initSite();
    }
})();
