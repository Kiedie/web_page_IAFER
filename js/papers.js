/**
 * Sistema de gestión modular de papers
 * Carga papers desde JSON y los renderiza dinámicamente
 * Soporta visualización embebida de PDFs
 */

console.log('📚 Sistema de Papers v1.0 - Cargado correctamente');

class PapersManager {
  constructor(basePath = './') {
    this.basePath = basePath;
    this.papers = [];
    this.loaded = false;
  }

  /**
   * Carga la lista de papers dinámicamente desde la API o datos embebidos
   */
  async loadPapers() {
    try {
      // Primero intenta usar datos embebidos (para uso local sin servidor)
      if (window.__EMBEDDED_PAPERS_DATA__) {
        console.log('📦 Usando datos embebidos (sin fetch)');
        const data = window.__EMBEDDED_PAPERS_DATA__;
        this.papers = data.papers || [];
        this.loaded = true;
        console.log('Papers cargados:', this.papers.length);
        return this.papers;
      }

      // Intenta cargar desde API (si hay servidor ejecutándose)
      try {
        const url = '/api/papers';
        console.log('🌐 Cargando papers desde API:', url);
        const response = await fetch(url);
        if (response.ok) {
          const data = await response.json();
          this.papers = data.papers || [];
          this.loaded = true;
          console.log('✓ Papers cargados desde API:', this.papers.length);
          return this.papers;
        }
      } catch (apiError) {
        console.warn('API no disponible, intentando fallback a JSON estático...');
      }

      // Si no hay API, intenta cargar desde JSON estático
      const url = `${this.basePath}data/papers.json`;
      console.log('📄 Cargando papers desde:', url);
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
      
      const data = await response.json();
      this.papers = data.papers || [];
      this.loaded = true;
      console.log('✓ Papers cargados:', this.papers.length);
      return this.papers;
    } catch (error) {
      console.error('❌ Error loading papers:', error);
      return [];
    }
  }

  /**
   * Carga un paper específico desde su archivo JSON
   */
  async loadPaper(paperId) {
    const paperMeta = this.papers.find(p => p.id === paperId);
    if (!paperMeta) return null;

    try {
      const response = await fetch(`${this.basePath}data/papers/${paperMeta.file}`);
      if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
      return await response.json();
    } catch (error) {
      console.error(`Error loading paper ${paperId}:`, error);
      return null;
    }
  }

  /**
   * Filtra papers por área de investigación
   */
  filterByResearchArea(area) {
    return this.papers.filter(p => p.research_area === area);
  }

  /**
   * Ordena papers por año (descendente)
   */
  sortByYear() {
    return [...this.papers].sort((a, b) => b.year - a.year);
  }

  /**
   * Genera HTML para una tarjeta de paper
   */
  generatePaperCard(paper) {
    const year = paper.year || 'N/A';
    const authors = paper.authors || 'Autores no disponibles';
    const paperUrl = paper.paper_url || '#';
    const title = paper.title_es || paper.title || 'Sin título';
    const imagePath = paper.image || '';
    const gradient = this.getGradientForPaper(paper.id);
    const backgroundStyle = imagePath 
      ? 'background-image: url(' + imagePath + '); background-size: cover; background-position: center;' 
      : 'background: ' + gradient + ';';
    
    return `
      <article class="paper-card" data-paper-id="${paper.id}">
        <div class="paper-card__image-wrapper" style="${backgroundStyle}">
          <div class="paper-card__preview">
            <a href="${paperUrl}" target="_blank" rel="noopener noreferrer" class="paper-card__title-link" title="Abrir artículo en nueva pestaña">
              ${title}
            </a>
          </div>
          <span class="paper-badge">${year}</span>
        </div>
        <div class="paper-card__content">
          <h3 class="paper-card__title">${paper.title}</h3>
          <p class="paper-card__authors">${authors}</p>
          <div class="paper-card__actions">
            <a href="${paperUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-small btn-primary">
              Ver Paper
            </a>
            <button class="btn btn-small btn-secondary" data-action="show-citation" data-paper-id="${paper.id}">
              Cita
            </button>
          </div>
        </div>
      </article>
    `;
  }

  /**
   * Genera un degradado único para cada paper basado en su ID
   */
  getGradientForPaper(paperId) {
    const gradients = [
      'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
      'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
      'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
      'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
    ];
    const index = paperId.charCodeAt(0) % gradients.length;
    return gradients[index];
  }

  /**
   * Renderiza un carrusel de papers
   */
  renderCarousel(containerId, papers = null) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const papersToRender = papers || this.papers;
    const html = papersToRender.map(p => this.generatePaperCard(p)).join('');
    
    container.innerHTML = `
      <div class="carousel-wrapper">
        <div class="carousel-container" id="carousel-content">
          ${html}
        </div>
        <button class="carousel-nav carousel-nav--prev" aria-label="Anterior">←</button>
        <button class="carousel-nav carousel-nav--next" aria-label="Siguiente">→</button>
      </div>
    `;

    this.setupCarouselNavigation(containerId);
    this.setupPaperActions(containerId);
  }

  /**
   * Configura la navegación del carrusel
   */
  setupCarouselNavigation(containerId) {
    const container = document.getElementById(containerId);
    const carousel = container.querySelector('.carousel-container');
    const prevBtn = container.querySelector('.carousel-nav--prev');
    const nextBtn = container.querySelector('.carousel-nav--next');
    
    let scrollPos = 0;
    const cardWidth = 340; // Ancho aproximado de una tarjeta + gap
    const maxScroll = carousel.scrollWidth - carousel.clientWidth;

    prevBtn.addEventListener('click', () => {
      scrollPos = Math.max(0, scrollPos - cardWidth);
      carousel.scrollTo({ left: scrollPos, behavior: 'smooth' });
      updateNavButtons();
    });

    nextBtn.addEventListener('click', () => {
      scrollPos = Math.min(maxScroll, scrollPos + cardWidth);
      carousel.scrollTo({ left: scrollPos, behavior: 'smooth' });
      updateNavButtons();
    });

    const updateNavButtons = () => {
      prevBtn.disabled = scrollPos === 0;
      nextBtn.disabled = scrollPos >= maxScroll - 10;
    };

    updateNavButtons();
  }

  /**
   * Configura acciones de los papers
   */
  setupPaperActions(containerId) {
    const container = document.getElementById(containerId);

    container.addEventListener('click', async (e) => {
      const viewPdfBtn = e.target.closest('[data-action="view-pdf"]');
      const showCitationBtn = e.target.closest('[data-action="show-citation"]');

      if (viewPdfBtn) {
        const paperId = viewPdfBtn.dataset.paperId;
        await this.openPDF(paperId);
      }

      if (showCitationBtn) {
        const paperId = showCitationBtn.dataset.paperId;
        await this.showCitation(paperId);
      }
    });
  }

  /**
   * Abre el visor de PDF en una nueva pestaña
   */
  async openPDF(paperId) {
    const paper = await this.loadPaper(paperId);
    if (!paper || !paper.pdf_url) {
      alert('PDF no disponible para este artículo');
      return;
    }

    const pdfUrl = paper.pdf_url;
    const title = encodeURIComponent(paper.title);
    window.open(`../papers/viewer.html?pdf=${encodeURIComponent(pdfUrl)}&title=${title}`, '_blank');
  }

  /**
   * Muestra modal de citations
   */
  async showCitation(paperId) {
    const paper = await this.loadPaper(paperId);
    if (!paper) return;

    const citations = paper.citations || {};
    const citationModal = this.createCitationModal(paper, citations);
    document.body.appendChild(citationModal);
  }

  /**
   * Crea modal con diferentes formatos de cita
   */
  createCitationModal(paper, citations) {
    const modal = document.createElement('div');
    modal.className = 'citation-modal-overlay';
    
    const bibtex = citations.bibtex || 'No disponible';
    const apa = citations.apa || 'No disponible';
    const mla = citations.mla || 'No disponible';

    modal.innerHTML = `
      <div class="citation-modal">
        <div class="citation-modal__header">
          <h2>Citas - ${paper.title}</h2>
          <button class="citation-modal__close" aria-label="Cerrar">&times;</button>
        </div>
        <div class="citation-modal__tabs">
          <button class="citation-tab active" data-format="bibtex">BibTeX</button>
          <button class="citation-tab" data-format="apa">APA</button>
          <button class="citation-tab" data-format="mla">MLA</button>
        </div>
        <div class="citation-modal__content">
          <textarea class="citation-textarea" readonly id="citation-text">${bibtex}</textarea>
        </div>
        <button class="btn btn-primary" id="copy-citation">Copiar cita</button>
      </div>
    `;

    // Evento de cerrar
    modal.querySelector('.citation-modal__close').addEventListener('click', () => modal.remove());
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.remove();
    });

    // Cambiar formato
    const tabs = modal.querySelectorAll('.citation-tab');
    const textarea = modal.querySelector('.citation-textarea');
    const citationData = { bibtex, apa, mla };

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const format = tab.dataset.format;
        textarea.value = citationData[format];
      });
    });

    // Copiar cita
    modal.querySelector('#copy-citation').addEventListener('click', () => {
      textarea.select();
      document.execCommand('copy');
      alert('Cita copiada al portapapeles');
    });

    return modal;
  }
}

// Instancia global
let papersManager = null;

/**
 * Inicializa el gestor de papers cuando el DOM está listo
 */
function initPapersManager(basePath = './') {
  papersManager = new PapersManager(basePath);
  return papersManager.loadPapers();
}

// No auto-inicializar - cada página debe hacerlo con su propia basePath
// if (document.readyState !== 'loading') {
//   initPapersManager();
// } else {
//   document.addEventListener('DOMContentLoaded', () => {
//     initPapersManager();
//   });
// }
