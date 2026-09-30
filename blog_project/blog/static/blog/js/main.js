document.addEventListener('DOMContentLoaded', () => {

    // 1) Dark / Light theme toggle (saved in localStorage)
    const themeBtn = document.getElementById('theme-toggle');
    const root = document.documentElement;

    const applyTheme = (theme) => {
        root.dataset.theme = theme;
        localStorage.setItem('theme', theme);
        if (themeBtn) themeBtn.textContent = theme === 'dark' ? '🌙' : '☀️';
    };

    applyTheme(root.dataset.theme || 'dark');

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
        });
    }

    // 2) Mobile menu
    const menuBtn = document.getElementById('menu-toggle');
    const navLinks = document.getElementById('nav-links');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => navLinks.classList.toggle('open'));
    }

    // 3) Live search on the home page cards
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        const cards = document.querySelectorAll('.posts-grid .card');
        searchInput.addEventListener('input', () => {
            const q = searchInput.value.trim().toLowerCase();
            cards.forEach(card => {
                const match = card.textContent.toLowerCase().includes(q);
                card.style.display = match ? '' : 'none';
            });
        });
    }

    // 4) Character counter for any textarea with maxlength
    document.querySelectorAll('textarea[maxlength]').forEach(area => {
        const counter = document.createElement('small');
        counter.className = 'char-counter';
        area.insertAdjacentElement('afterend', counter);

        const update = () => {
            const left = area.maxLength - area.value.length;
            counter.textContent = `${area.value.length} / ${area.maxLength}`;
            counter.classList.toggle('warn', left < 20);
        };
        area.addEventListener('input', update);
        update();
    });

    // 5) Auto-hide alert messages after 4 seconds
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 400);
        }, 4000);
    });

    // 6) Confirm before submitting any form with data-confirm
    document.querySelectorAll('form[data-confirm]').forEach(form => {
        form.addEventListener('submit', e => {
            if (!confirm(form.dataset.confirm)) e.preventDefault();
        });
    });
});