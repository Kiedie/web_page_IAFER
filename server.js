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
          title_es: paper.title_es || '',
          year: paper.year || 0,
          authors: authors,
          research_area: paper.research_area || 'other',
          research_line: paper.research_line || '',
          image: paper.image || '',
          paper_url: paper.paper_url || paper.arxiv_url || '',
          venue: paper.publication?.venue || '',
          tags: (paper.keywords || []).slice(0, 5)
        };

        papers.push(paperEntry);
        if (paperEntry.research_area) researehAreas.add(paperEntry.research_area);
        if (paperEntry.research_line) researchLines.add(paperEntry.research_line);
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
