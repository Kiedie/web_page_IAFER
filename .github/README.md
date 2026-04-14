# Customizaciones de Copilot - IAFER Web Project

Este directorio contiene configuraciones personalizadas de GitHub Copilot para el proyecto IAFER.

## 📁 Estructura

```
.github/
├── agents/
│   └── webdev-expert.agent.md       # Agente experto en desarrollo web
├── prompts/
│   ├── launch-server.prompt.md       # Prompt rápido: Levanta servidor
│   └── diagnose-issues.prompt.md     # Prompt rápido: Diagnostica problemas
└── copilot-instructions.md           # Instrucciones workspace generales
```

## 🚀 Cómo Usar

### 1. Activar el Agente WebDev Expert

El agente se activa automáticamente cuando mencionas palabras clave como:
- "levanta el servidor"
- "diagnostica el error"
- "revisa el HTML"
- "arregla los estilos"
- "localhost"
- "express"

También puedes invocarlo explícitamente mencionando `webdev-expert`.

### 2. Usar los Prompts Rápidos

Accede via slash commands (`/`) en el chat de Copilot:
- `/launch-server` → Levanta Express en localhost:3000
- `/diagnose-issues` → Ejecuta diagnóstico completo

### 3. Instrucciones Workspace

Las instrucciones en `copilot-instructions.md` se aplican automáticamente a archivos:
- `**/*.js` (JavaScript)
- `**/*.html` (HTML)
- `**/*.css` (CSS)
- `**/*.json` (JSON)

## 🎯 Capacidades del WebDev Expert

✅ Levantar/detener servidor Express  
✅ Diagnosticar errores frontend y backend  
✅ Revisar y reparar HTML, CSS, JavaScript  
✅ Ejecutar comandos npm  
✅ Validar rutas y endpoints API  
✅ Verificar dependencias  

## 📊 Tech Stack del Proyecto

- **Backend**: Node.js + Express.js (puerto 3000)
- **Frontend**: HTML5 + CSS3 + Vanilla JavaScript
- **Data**: JSON dinámico
- **Estructura**: Sitio estático con secciones (GPAIS, Trustworthy AI)

## 🔧 Verificación Rápida

```bash
# Ver que todo está configurado
node --version  # Node.js debe estar instalado
npm --version   # npm debe estar disponible
npm install     # Instalar dependencias
npm start       # Levanta servidor en localhost:3000
```

## 📝 Notas

- El agente webdev-expert tiene acceso a herramientas de terminal, lectura de archivos y edición
- Los prompts son atajos convenientes para tareas comunes
- Las instrucciones workspace se aplican implícitamente a ciertos tipos de archivos

---

**Última actualización**: 14 de abril de 2026
