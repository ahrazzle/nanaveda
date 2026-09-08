/**
 * Nanaveda — Clickable Terms System
 * 
 * Clicking on highlighted terms opens a modal with:
 * - Definition from verified sources
 * - Cultural/historical context
 * - Link to learn more
 * 
 * Data source: terms_complete.json (encyclopedic definitions)
 * Fallback: Wikipedia API for terms not in local database
 */

// Terms database (populated from terms_complete.json)
let termsDB = {};

// Load terms database
async function loadTermsDB() {
    try {
        const response = await fetch('terms_complete.json');
        termsDB = await response.json();
    } catch (e) {
        console.warn('Could not load terms database, using fallback');
    }
}

// Open term popup
function openTermPopup(termKey, event) {
    event.preventDefault();
    event.stopPropagation();
    
    const popup = document.getElementById('term-popup');
    const popupContent = document.getElementById('term-popup-content');
    
    // Normalize term key
    const key = termKey.replace(/\s+/g, '_').replace(/[()]/g, '');
    const termData = termsDB[key] || termsDB[termKey] || null;
    
    let html = '';
    
    if (termData) {
        html = `
            <h3 id="term-popup-title">${termData.title || termKey}</h3>
            <p class="term-popup-description">${termData.description || ''}</p>
            ${termData.extract ? `<p class="term-popup-extract">${termData.extract}</p>` : ''}
            ${termData.url ? `<a href="${termData.url}" target="_blank" rel="noopener" class="term-popup-link">Learn more →</a>` : ''}
            <p class="term-popup-source">Source: Wikipedia / Grokipedia</p>
        `;
    } else {
        html = `
            <h3 id="term-popup-title">${termKey}</h3>
            <p class="term-popup-description">Loading definition...</p>
            <p class="term-popup-source">Information being researched.</p>
        `;
        // Attempt Wikipedia fetch as fallback
        fetchWikipediaTerm(termKey).then(data => {
            if (data) {
                document.getElementById('term-popup-title').textContent = data.title || termKey;
                const descEl = document.querySelector('.term-popup-description');
                if (descEl) descEl.textContent = data.description || data.extract || 'No definition available.';
            }
        });
    }
    
    popupContent.innerHTML = html;
    popup.classList.add('active');
    document.body.style.overflow = 'hidden';
    
    // Focus management for accessibility
    setTimeout(() => {
        const closeBtn = popup.querySelector('.term-popup-close');
        if (closeBtn) closeBtn.focus();
    }, 100);
}

// Close term popup
function closeTermPopup() {
    const popup = document.getElementById('term-popup');
    popup.classList.remove('active');
    document.body.style.overflow = '';
    
    // Return focus to trigger element
    if (lastFocusedElement) {
        lastFocusedElement.focus();
        lastFocusedElement = null;
    }
}

let lastFocusedElement = null;

// Fetch from Wikipedia as fallback
async function fetchWikipediaTerm(term) {
    try {
        const response = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(term)}`);
        if (response.ok) {
            return await response.json();
        }
    } catch (e) {
        console.warn('Wikipedia fetch failed:', e);
    }
    return null;
}

// Initialize term clickability
function initClickableTerms() {
    // Add click handlers to all term elements
    document.querySelectorAll('.term').forEach(el => {
        el.addEventListener('click', function(e) {
            lastFocusedElement = this;
            const termKey = this.getAttribute('data-term') || this.textContent;
            openTermPopup(termKey, e);
        });
        
        // Keyboard accessibility
        el.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                lastFocusedElement = this;
                const termKey = this.getAttribute('data-term') || this.textContent;
                openTermPopup(termKey, e);
            }
        });
        
        // Make focusable
        el.setAttribute('tabindex', '0');
        el.setAttribute('role', 'button');
        el.setAttribute('aria-label', `Learn more about ${el.textContent}`);
    });
    
    // Close popup on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeTermPopup();
        }
    });
    
    // Close popup on backdrop click
    const popup = document.getElementById('term-popup');
    if (popup) {
        popup.addEventListener('click', function(e) {
            if (e.target === this) {
                closeTermPopup();
            }
        });
    }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    loadTermsDB().then(() => {
        initClickableTerms();
    });
});
