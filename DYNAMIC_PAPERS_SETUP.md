# 📚 Carga Dinámica de Papers - Setup

## ¿Cómo funciona?

Ahora tienes un sistema completamente dinámico:

### 1. **Servidor Node.js** (`server.js`)
Lee automáticamente **todos** los JSONs en `data/papers/` sin necesidad de mantener un índice manual.

### 2. **API REST**
- `GET /api/papers` → Lista dinámicade todos los papers
- `GET /api/papers/:id` → Detalle completo de un paper

### 3. **Fallback automático**
- Si el servidor está corriendo → Usa la API
- Si está offline → Carga desde `data/papers.json` (si existe)

## 🚀 Instalación y uso

### 1. Instalar dependencias
```bash
npm install
```

### 2. Ejecutar el servidor
```bash
npm start
# O npm run dev
```

El servidor estará disponible en: **http://localhost:3000**

### 3. ✨ ¡Listo!
Simplemente agrega nuevos archivos JSON a `data/papers/` y automáticamente aparecerán en la web sin necesidad de actualizar nada.

## 📝 Estructura de un paper JSON

```json
{
  "id": "unique-id",
  "title": "Paper Title",
  "title_es": "Título en Español",
  "year": 2025,
  "authors": [
    {"name": "Autor 1", "affiliation": "Universidad X"},
    {"name": "Autor 2", "affiliation": "Universidad Y"}
  ],
  "research_area": "gpais",
  "research_line": "Zero-Shot Learning",
  "paper_url": "https://...",
  "arxiv_url": "https://arxiv.org/...",
  "image": "images/...",
  "keywords": ["keyword1", "keyword2"],
  "publication": {
    "venue": "Conference Name"
  }
}
```

## 🎯 Ventajas
✓ Cargas dinámicas - no necesitas actualizar config manual
✓ Escalable - agrega papers sin cambiar código
✓ Fallback automático - funciona con o sin servidor
✓ API REST - fácil de extender

¡Disfruta! 🎉
