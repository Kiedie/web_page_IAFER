/**
 * PDF Renderer - Convierte la primera página de un PDF a imagen
 * Usa pdf.js (Mozilla's PDF.js library)
 */

// Establecer worker de pdf.js
if (typeof pdfjsLib !== 'undefined') {
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
}

class PDFRenderer {
  /**
   * Renderiza la primera página de un PDF y devuelve como imagen
   */
  static async renderPDFToImage(pdfUrl, maxWidth = 400, maxHeight = 600) {
    try {
      if (!pdfUrl || typeof pdfjsLib === 'undefined') {
        return null;
      }

      const pdf = await pdfjsLib.getDocument(pdfUrl).promise;
      const page = await pdf.getPage(1);
      
      // Calcular escala manteniendo aspecto
      const viewport = page.getViewport({ scale: 1 });
      const scale = Math.min(maxWidth / viewport.width, maxHeight / viewport.height, 2);
      const scaledViewport = page.getViewport({ scale });
      
      // Crear canvas
      const canvas = document.createElement('canvas');
      canvas.width = scaledViewport.width;
      canvas.height = scaledViewport.height;
      
      const context = canvas.getContext('2d');
      const renderContext = {
        canvasContext: context,
        viewport: scaledViewport
      };
      
      await page.render(renderContext).promise;
      
      // Convertir a data URL
      return canvas.toDataURL('image/png');
    } catch (error) {
      console.warn('Error rendering PDF:', pdfUrl, error);
      return null;
    }
  }

  /**
   * Procesa una lista de papers y genera imágenes de PDFs faltantes
   */
  static async processPapersForPDFs(papers) {
    const processed = [];
    
    for (const paper of papers) {
      const processedPaper = { ...paper };
      
      // Si no tiene imagen pero tiene pdf_url, intentar renderizar
      if (!processedPaper.image && processedPaper.pdf_url) {
        try {
          const imageDataUrl = await this.renderPDFToImage(processedPaper.pdf_url);
          if (imageDataUrl) {
            processedPaper.image = imageDataUrl;
          }
        } catch (error) {
          console.warn('Could not render PDF for paper:', paper.id);
        }
      }
      
      processed.push(processedPaper);
    }
    
    return processed;
  }
}

// Exportar para uso como módulo
if (typeof module !== 'undefined' && module.exports) {
  module.exports = PDFRenderer;
}
