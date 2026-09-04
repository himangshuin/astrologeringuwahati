// Mobile nav toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('open');
        navToggle.setAttribute('aria-expanded', navLinks.classList.contains('open'));
    });
}

// Mobile "Areas We Serve" dropdown toggle
document.querySelectorAll('.nav-links li.has-dropdown > .dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function (e) {
        if (window.innerWidth <= 768) {
            e.preventDefault();
            this.parentElement.classList.toggle('open');
        }
    });
});

// Smooth scrolling for in-page anchor links, closing mobile nav after
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        const target = document.querySelector(targetId);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
            if (navLinks) navLinks.classList.remove('open');
        }
    });
});

// Highlight current page in nav
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links > li > a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
        link.classList.add('active');
    }
});

// WhatsApp click tracking (analytics hook)
document.querySelectorAll('a[href*="wa.me"]').forEach(btn => {
    btn.addEventListener('click', () => {
        console.log('WhatsApp click - Best Astrologer in Guwahati');
    });
});

// Live search/filter on the Areas We Serve (locations.html) page
const locationSearch = document.getElementById('locationSearch');
if (locationSearch) {
    locationSearch.addEventListener('input', function () {
        const q = this.value.trim().toLowerCase();
        document.querySelectorAll('.division-block').forEach(block => {
            let anyVisible = false;
            block.querySelectorAll('.location-card').forEach(card => {
                const text = card.textContent.toLowerCase();
                const match = text.includes(q);
                card.classList.toggle('hidden', !match);
                if (match) anyVisible = true;
            });
            block.classList.toggle('hidden', !anyVisible);
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('Best Astrologer in Guwahati & Top Astrologer in Assam — Himu');
});

// Scroll-reveal animation for section content
const revealTargets = document.querySelectorAll(
    '.services-grid, .why-grid, .process-grid, .zodiac-grid, .pricing-grid, ' +
    '.testimonial-grid, .blog-teaser-grid, .stats-grid, .about-container, ' +
    '.lc-grid, .faq-list, .location-card, .locations-grid'
);
revealTargets.forEach(el => el.classList.add('reveal'));

if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
} else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in-view'));
}

// Animated count-up for the trust stats bar
const statNums = document.querySelectorAll('.stat-num');
if (statNums.length && 'IntersectionObserver' in window) {
    const animateStat = (el) => {
        const raw = el.textContent.trim();
        const match = raw.match(/^([\d,]+)(.*)$/);
        if (!match) return; // e.g. "4.9★" — leave as-is
        const target = parseInt(match[1].replace(/,/g, ''), 10);
        const suffix = match[2];
        const duration = 1200;
        const start = performance.now();
        const step = (now) => {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(target * eased);
            el.textContent = current.toLocaleString('en-IN') + suffix;
            if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
    };
    const statObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStat(entry.target);
                statObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.4 });
    statNums.forEach(el => statObserver.observe(el));
}

// Back-to-top button
const backToTop = document.getElementById('backToTop');
if (backToTop) {
    window.addEventListener('scroll', () => {
        backToTop.classList.toggle('visible', window.scrollY > 500);
    }, { passive: true });
    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}
