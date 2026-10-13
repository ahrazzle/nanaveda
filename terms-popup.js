/** Clickable glossary definitions from the local terms database. */
let termsDB = {};
let lastFocusedElement = null;
let popupRequest = 0;
let pendingLookup = null;

async function loadTermsDB() {
    try {
        const response = await fetch('terms_complete.json', { signal: AbortSignal.timeout(8000) });
        if (!response.ok) throw new Error('Glossary unavailable');
        termsDB = await response.json();
    } catch {
        console.warn('Could not load the local glossary.');
    }
}

function paragraph(className, text) {
    const node = document.createElement('p');
    node.className = className;
    node.textContent = text;
    return node;
}

async function openTermPopup(termKey, event) {
    event.preventDefault();
    event.stopPropagation();
    pendingLookup?.abort();
    const request = ++popupRequest;
    const popup = document.getElementById('term-popup');
    const content = document.getElementById('term-popup-content');
    const key = termKey.replace(/\s+/g, '_').replace(/[()]/g, '');
    const data = termsDB[key] || termsDB[termKey];
    const title = document.createElement('h3');
    title.id = 'term-popup-title';
    title.textContent = data?.title || termKey;
    const description = paragraph('term-popup-description', data?.description || 'Loading definition…');
    content.replaceChildren(title, description);
    if (data?.extract) content.appendChild(paragraph('term-popup-extract', data.extract));
    if (data?.url && /^https?:\/\//i.test(data.url)) {
        const link = document.createElement('a');
        link.href = data.url;
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        link.className = 'term-popup-link';
        link.textContent = 'Learn more →';
        content.appendChild(link);
    }
    if (data) content.appendChild(paragraph('term-popup-source', 'Source: Wikipedia / Grokipedia'));
    popup.classList.add('active');
    popup.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    popup.querySelector('.term-popup-close').focus();
    if (!data) {
        pendingLookup = new AbortController();
        const result = await fetchWikipediaTerm(termKey, pendingLookup.signal);
        if (request !== popupRequest) return;
        title.textContent = result?.title || termKey;
        description.textContent = result?.description || result?.extract || 'Definition unavailable. Please try again when you are connected.';
    }
}

function closeTermPopup() {
    const popup = document.getElementById('term-popup');
    if (!popup.classList.contains('active')) return;
    ++popupRequest;
    pendingLookup?.abort();
    popup.classList.remove('active');
    popup.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    lastFocusedElement?.focus();
    lastFocusedElement = null;
}

async function fetchWikipediaTerm(term, signal) {
    try {
        const response = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(term)}`, {
            signal: AbortSignal.any([signal, AbortSignal.timeout(8000)]),
        });
        return response.ok ? await response.json() : null;
    } catch { return null; }
}

function initClickableTerms() {
    document.querySelectorAll('.term').forEach(el => {
        const open = e => {
            lastFocusedElement = el;
            void openTermPopup(el.getAttribute('data-term') || el.textContent, e);
        };
        el.addEventListener('click', open);
        el.addEventListener('keydown', e => {
            if (e.key === 'Enter' || e.key === ' ') open(e);
        });
        el.setAttribute('tabindex', '0');
        el.setAttribute('role', 'button');
        el.setAttribute('aria-label', `Learn more about ${el.textContent}`);
    });
    const popup = document.getElementById('term-popup');
    popup.querySelector('.term-popup-close').addEventListener('click', closeTermPopup);
    popup.addEventListener('click', e => { if (e.target === popup) closeTermPopup(); });
    document.addEventListener('keydown', e => {
        if (!popup.classList.contains('active')) return;
        if (e.key === 'Escape') { e.preventDefault(); closeTermPopup(); }
        if (e.key === 'Tab') {
            const focusable = Array.from(popup.querySelectorAll('a[href], button'));
            const first = focusable[0], last = focusable[focusable.length - 1];
            if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
            else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    // Make terms usable immediately, including if the database fails to load.
    initClickableTerms();
    void loadTermsDB();
});
