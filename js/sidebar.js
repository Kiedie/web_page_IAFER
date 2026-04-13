/**
 * SIDEBAR.JS - Gestor del árbol de navegación
 * Maneja expand/collapse, navegación activa, etc.
 */

class SidebarNavigator {
    constructor(sidebarId = 'page-sidebar') {
        this.sidebar = document.getElementById(sidebarId);
        if (!this.sidebar) return;

        this.treeItems = this.sidebar.querySelectorAll('.tree-item');
        this.observeCurrentPage();
        this.setupEventListeners();
        this.setupSmoothScroll();
    }

    /**
     * Configura listeners para expand/collapse
     */
    setupEventListeners() {
        this.treeItems.forEach(item => {
            const toggle = item.querySelector('.tree-toggle');
            const children = item.querySelector('.tree-children');

            if (toggle && children && item.dataset.expandable !== 'false') {
                item.addEventListener('click', (e) => {
                    // Solo si hacer click en el toggle o el item mismo
                    if (e.target === toggle || e.target.closest('.tree-toggle')) {
                        this.toggleItem(item);
                        e.stopPropagation();
                    }
                });

                // Click en el label navega, no expande
                const label = item.querySelector('.tree-label');
                if (label && label.closest('a')) {
                    label.addEventListener('click', (e) => {
                        e.stopPropagation();
                    });
                }
            }
        });
    }

    /**
     * Toggle expand/collapse de un item
     */
    toggleItem(item) {
        const isCollapsed = item.dataset.collapsed === 'true';
        item.dataset.collapsed = !isCollapsed;
    }

    /**
     * Expande todos los parents hasta una url específica
     */
    expandToUrl(url) {
        // Encontrar el item activo
        const activeItem = Array.from(this.treeItems).find(item => {
            const link = item.querySelector('a');
            if (!link) return false;
            return this.urlMatches(link.href, url);
        });

        if (activeItem) {
            // Expandir todos los parents
            let parent = activeItem.closest('.tree-children');
            while (parent) {
                const parentItem = parent.closest('.tree-item');
                if (parentItem) {
                    parentItem.dataset.collapsed = 'false';
                    parent = parentItem.closest('.tree-children');
                } else {
                    break;
                }
            }

            // Marcar como activo
            this.setActive(activeItem);

            // Scroll en la sidebar
            this.scrollToItem(activeItem);
        }
    }

    /**
     * Establece un item como activo
     */
    setActive(item) {
        // Remover clase activa de otros
        this.treeItems.forEach(i => i.classList.remove('active'));
        // Agregar a este
        item.classList.add('active');
    }

    /**
     * Scroll para que el item sea visible en la sidebar
     */
    scrollToItem(item) {
        setTimeout(() => {
            const rect = item.getBoundingClientRect();
            const sidebarRect = this.sidebar.getBoundingClientRect();

            // Si está fuera de vista
            if (rect.top < sidebarRect.top || rect.bottom > sidebarRect.bottom) {
                // Calcular posición de scroll
                const scrollTop = this.sidebar.scrollTop;
                const offset = rect.top - sidebarRect.top;
                this.sidebar.scrollTop = scrollTop + offset - 100; // Offset para mejor visibilidad
            }
        }, 100);
    }

    /**
     * Compara URLs ignorando parámetros
     */
    urlMatches(href, currentUrl) {
        try {
            const url1 = new URL(href, window.location.origin);
            const url2 = new URL(currentUrl, window.location.origin);
            return url1.pathname === url2.pathname;
        } catch {
            return false;
        }
    }

    /**
     * Detecta la página actual y actualiza el estado
     */
    observeCurrentPage() {
        const currentUrl = window.location.pathname;
        this.expandToUrl(currentUrl);

        // Escuchar cambios de URL (para SPA)
        window.addEventListener('popstate', () => {
            this.observeCurrentPage();
        });
    }

    /**
     * Scroll suave para links internos
     */
    setupSmoothScroll() {
        this.sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                if (href && href.startsWith('#')) {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth' });
                        this.setActive(link.closest('.tree-item'));
                    }
                }
            });
        });
    }
}

/**
 * Toggle del sidebar en móviles
 */
class SidebarToggle {
    constructor() {
        this.sidebar = document.getElementById('page-sidebar');
        this.body = document.body;
        this.toggle = document.querySelector('.sidebar-toggle');

        if (this.toggle) {
            this.toggle.addEventListener('click', () => this.toggleSidebar());
            this.setupResponsive();
        }

        // Cerrar sidebar al hacer click en un link
        if (this.sidebar) {
            this.sidebar.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth < 1024) {
                        this.closeSidebar();
                    }
                });
            });
        }
    }

    toggleSidebar() {
        this.body.classList.toggle('sidebar-open');
    }

    closeSidebar() {
        this.body.classList.remove('sidebar-open');
    }

    openSidebar() {
        this.body.classList.add('sidebar-open');
    }

    setupResponsive() {
        // Cerrar sidebar al cambiar a desktop
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 1024) {
                this.closeSidebar();
            }
        });
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new SidebarNavigator();
    new SidebarToggle();

    console.log('✅ Sidebar Navigator inicializado');
});
