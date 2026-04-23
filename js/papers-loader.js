/**
 * Research Line Paper Loader
 * Carga dinámicamente los papers filtrados por research line tag
 * Uso: <div id="research-line-papers" data-research-line="Explainability (XAI)"></div>
 */

(function() {
  'use strict';

  class ResearchLinePaperLoader {
    constructor(containerId, researchLine) {
      this.container = document.getElementById(containerId);
      this.researchLine = researchLine;
      this.papers = [];
    }

    getBasePath() {
      // Detectar si estamos en GitHub Pages (subdirectorio) o en local (raíz)
      const path = window.location.pathname;
      const parts = path.split('/').filter(p => p.length > 0);

      // Buscar el índice de 'gpais' o 'trustworthy' para encontrar la raíz del proyecto
      let rootIndex = -1;
      for (let i = 0; i < parts.length; i++) {
        if (parts[i] === 'gpais' || parts[i] === 'trustworthy' || parts[i] === 'data' || parts[i] === 'papers') {
          rootIndex = i;
          break;
        }
      }

      if (rootIndex > 0) {
        // Estamos en un subdirectorio (ej: /web_page_IAFER/gpais/...)
        return '../'.repeat(parts.length - rootIndex);
      } else if (rootIndex === 0) {
        // Estamos en la raíz (ej: /gpais/...)
        return '../'.repeat(parts.length - 1);
      }

      return '../'.repeat(parts.length - 1);
    }

    async loadPapers() {
      try {
        console.log('Loading papers for research line:', this.researchLine);
        const basePath = this.getBasePath();
        const papersPath = basePath + 'data/papers.json?v=2';
        console.log('Fetching papers from:', papersPath);

        const response = await fetch(papersPath);
        console.log('Response status:', response.status);
        if (!response.ok) throw new Error('Could not load papers.json');

        const data = await response.json();
        this.papers = data.papers || [];
        console.log('Total papers loaded:', this.papers.length);

        // Para Critical Applications, incluir tanto Healthcare como Environment
        // Para Agentic AI, mapear a Generative AI
        let filteredPapers;
        if (this.researchLine === 'Critical Applications') {
          filteredPapers = this.papers.filter(p =>
            (p.tags || []).includes('Critical Applications (Healthcare)') ||
            (p.tags || []).includes('Critical Applications (Environment)')
          );
        } else if (this.researchLine === 'Agentic AI') {
          filteredPapers = this.papers.filter(p =>
            (p.tags || []).includes('Generative AI')
          );
        } else {
          // Filtrar papers que tienen el tag de esta research line
          filteredPapers = this.papers.filter(p =>
            (p.tags || []).includes(this.researchLine)
          );
        }
        console.log('Filtered papers for', this.researchLine, ':', filteredPapers.length);

        this.renderPapers(filteredPapers);
      } catch (error) {
        console.error('Error loading papers:', error);
        this.container.innerHTML = '<p class="error-message">Unable to load publications.</p>';
      }
    }

    renderPapers(papers) {
      if (papers.length === 0) {
        this.container.innerHTML = `
          <div class="empty-state">
            <p>No publications available for this research line yet.</p>
          </div>
        `;
        return;
      }

      const html = papers.map(paper => this.generatePaperCard(paper)).join('');
      this.container.innerHTML = html;
    }

    generatePaperCard(paper) {
      const year = paper.year || 'N/A';
      const venue = paper.venue || '';
      const paperUrl = paper.paper_url || '#';
      const title = paper.title || 'Untitled';
      const imagePath = paper.image || '';
      const githubUrl = paper.github_url || paper.metadata?.github_url;
      const hasGithub = githubUrl && githubUrl.trim() !== '';
      const basePath = this.getBasePath();
      const imagePrefix = basePath + '../';

      return `
        <article class="publication-card">
          <div class="publication-image-wrapper">
            <img src="${imagePrefix}${imagePath}"
                 alt="${title}"
                 class="publication-image"
                 onerror="this.src='${imagePrefix}images/placeholder.png'">
            <span class="publication-badge">${year}</span>
          </div>
          <div class="publication-content">
            <h4 class="publication-title">${title}</h4>
            <p class="publication-venue-info">
              ${venue ? `<span class="venue">${venue}</span>` : ''}
              ${year ? `<span class="year">${year}</span>` : ''}
            </p>
            <div class="publication-actions">
              ${paperUrl && paperUrl !== '#' ? `
                <a href="${paperUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-small btn-primary">
                  View Paper
                </a>
              ` : ''}
              ${hasGithub ? `
                <a href="${githubUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-small btn-secondary github-btn" style="background-color: #f5f5f5; color: #333; border-color: #ddd;">
                  <img src="${imagePrefix}images/github-logo.svg" alt="GitHub" class="github-icon" style="width:16px;height:16px;vertical-align:middle;margin-right:4px;">GitHub
                </a>
              ` : ''}
            </div>
          </div>
        </article>
      `;
    }
  }

  // Auto-initialize when DOM is ready
  function init() {
    const containers = document.querySelectorAll('[data-research-line]');
    containers.forEach(container => {
      const researchLine = container.getAttribute('data-research-line');
      const loader = new ResearchLinePaperLoader(container.id, researchLine);
      loader.loadPapers();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose class globally for manual initialization
  window.ResearchLinePaperLoader = ResearchLinePaperLoader;
})();
