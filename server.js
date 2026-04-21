const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 8000;

// Servir archivos estáticos con más especificidad
app.use(express.static('.', {
  etag: false,
  setHeaders: (res, path) => {
    // No cachear JSON y HTML para ver cambios en desarrollo
    if (path.includes('.json') || path.includes('.html')) {
      res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
    }
  }
}));

console.log('Server starting...');
console.log('Serving static files from:', process.cwd());

/**
 * Generar data/papers.json dinámicamente desde data/papers/
 */
function generatePapersJson() {
  const papersDir = path.join(__dirname, 'data', 'papers');
  const outputFile = path.join(__dirname, 'data', 'papers.json');

  try {
    const files = fs.readdirSync(papersDir).filter(f => f.startsWith('paper_') && f.endsWith('.json'));
    const papers = [];
    const researchAreas = new Set();
    const researchLines = new Set();

    files.forEach(file => {
      const filePath = path.join(papersDir, file);
      const content = fs.readFileSync(filePath, 'utf-8');
      const paper = JSON.parse(content);

      let authors = 'Autores no disponibles';
      if (paper.authors && Array.isArray(paper.authors)) {
        authors = paper.authors
          .map(a => typeof a === 'string' ? a : a.name || '')
          .filter(a => a)
          .join(', ');
      }

      const paperEntry = {
        id: paper.id,
        file: file,
        title: paper.title || '',
        year: paper.year || 0,
        authors: authors,
        research_area: paper.research_area || 'other',
        image: paper.image || '',
        paper_url: paper.paper_url || paper.arxiv_url || '',
        venue: paper.publication?.venue || '',
        tags: paper.tags || [],
        github_url: paper.github_url || ''
      };

      papers.push(paperEntry);
      if (paperEntry.research_area) researchAreas.add(paperEntry.research_area);
      (paper.tags || []).forEach(tag => researchLines.add(tag));
    });

    // Ordenar por año descendente
    papers.sort((a, b) => (-a.year || 0) - (-b.year || 0));

    const output = {
      papers,
      metadata: {
        total: papers.length,
        last_updated: new Date().toISOString().split('T')[0],
        research_areas: Array.from(researchAreas).sort(),
        research_lines: Array.from(researchLines).sort()
      }
    };

    fs.writeFileSync(outputFile, JSON.stringify(output, null, 2), 'utf-8');
    console.log(`✓ Generated data/papers.json with ${papers.length} papers`);
    return papers.length;
  } catch (error) {
    console.error('✗ Error generating papers.json:', error.message);
    return 0;
  }
}

// Generar papers.json al iniciar el servidor
generatePapersJson();

/**
 * API: GET /api/papers
 * Lee dinámicamente todos los JSON de data/papers/ y devuelve su índice
 */
app.get('/api/papers', (req, res) => {
  try {
    const papersDir = path.join(__dirname, 'data', 'papers');
    const files = fs.readdirSync(papersDir).filter(f => f.startsWith('paper_') && f.endsWith('.json'));
    
    const papers = [];
    const researehAreas = new Set();
    const researchLines = new Set();

    files.forEach(file => {
      try {
        const filePath = path.join(papersDir, file);
        const content = fs.readFileSync(filePath, 'utf-8');
        const paper = JSON.parse(content);

        // Extraer info básica
        let authors = 'Autores no disponibles';
        if (paper.authors && Array.isArray(paper.authors)) {
          authors = paper.authors
            .map(a => typeof a === 'string' ? a : a.name || '')
            .filter(a => a)
            .join(', ');
        }

        const paperEntry = {
          id: paper.id,
          file: file,
          title: paper.title || '',
          year: paper.year || 0,
          authors: authors,
          research_area: paper.research_area || 'other',
          image: paper.image || '',
          paper_url: paper.paper_url || paper.arxiv_url || '',
          venue: paper.publication?.venue || '',
          tags: paper.tags || [],
          github_url: paper.github_url || ''
        };

        papers.push(paperEntry);
        if (paperEntry.research_area) researehAreas.add(paperEntry.research_area);
        // Añadir tags a researchLines para compatibilidad
        (paper.tags || []).forEach(tag => researchLines.add(tag));
      } catch (e) {
        console.error(`Error leyendo ${file}:`, e.message);
      }
    });

    // Ordenar por año descendente
    papers.sort((a, b) => (-a.year || 0) - (-b.year || 0));

    res.json({
      papers,
      metadata: {
        total: papers.length,
        research_areas: Array.from(researehAreas).sort(),
        research_lines: Array.from(researchLines).sort()
      }
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: error.message });
  }
});

/**
 * API: GET /api/papers/:id
 * Devuelve el contenido completo de un paper específico
 */
app.get('/api/papers/:id', (req, res) => {
  try {
    const papersDir = path.join(__dirname, 'data', 'papers');
    const files = fs.readdirSync(papersDir);
    
    // Buscar el archivo que contiene ese ID
    let found = false;
    for (const file of files) {
      if (file.startsWith('paper_') && file.endsWith('.json')) {
        const filePath = path.join(papersDir, file);
        const content = fs.readFileSync(filePath, 'utf-8');
        const paper = JSON.parse(content);
        
        if (paper.id === req.params.id) {
          res.json(paper);
          found = true;
          break;
        }
      }
    }

    if (!found) {
      res.status(404).json({ error: 'Paper no encontrado' });
    }
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log('');
  console.log('IAFER Website Server');
  console.log('====================');
  console.log('');
  console.log('Web:  http://localhost:' + PORT);
  console.log('API:  http://localhost:' + PORT + '/api/papers');
  console.log('Docs: http://localhost:' + PORT + '/papers/');
  console.log('');
  console.log('Press Ctrl+C to stop');
  console.log('');
});
