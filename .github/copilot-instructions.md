---
name: iafer-web-workspace
description: "IAFER Project workspace instructions for Node.js + Express web development."
applyTo: "**/*.{js,html,css,json}"
---

# IAFER Web Project Instructions

## Project Context

- **Type**: Static website with dynamic Express backend
- **Server**: Node.js + Express on port 3000
- **Frontend**: HTML5 + CSS3 + Vanilla JavaScript
- **Data**: JSON files in `data/papers/`

## Quick Start

```bash
npm install     # Install dependencies
npm start       # Launch localhost:3000
```

## Key Files

- `server.js` - Express configuration and API routes
- `index.html` - Home page
- `gpais/` - GPAIS section
- `trustworthy/` - Trustworthy AI section
- `data/papers/` - Research papers metadata
- `css/` - Stylesheets for different sections
- `js/` - Frontend JavaScript

## Common Tasks

- **Debug server**: Check `npm start` output and browser DevTools
- **Fix styles**: Look in `css/base.css` (global) or section-specific CSS
- **Check links**: Verify relative paths in HTML files
- **API issues**: Debug server.js route handlers
