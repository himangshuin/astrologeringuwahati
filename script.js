// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Mobile menu toggle (optional enhancement)
const navToggle = () => {
    const navLinks = document.querySelector('.nav-links');
    if (window.innerWidth <= 768) {
        // Add mobile menu button if needed
        if (!document.querySelector('.mobile-menu-btn')) {
            const btn = document.createElement('button');
            btn.innerHTML = '☰';
            btn.className = 'mobile-menu-btn';
            btn.style.cssText = 'font-size: 2rem; background: none; border: none; cursor: pointer;';
            document.querySelector('.navbar .container').prepend(btn);
            
            btn.addEventListener('click', () => {
                navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            });
        }
    }
};

// Add active class to current page navigation
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.getAttribute('href') === currentPage) {
        link.classList.add('active');
    }
});

// Track WhatsApp clicks for analytics
const whatsappButtons = document.querySelectorAll('a[href*="wa.me"]');
whatsappButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        console.log('WhatsApp click tracked - Tarot With Himu');
        // You can add Google Analytics or Facebook Pixel tracking here
    });
});

// Add structured data dynamically
const addStructuredData = () => {
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.textContent = JSON.stringify({
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Tarot With Himu",
        "description": "Best Tarot Reader in India and Guwahati. Certified Astrologer, Numerologist, Vastu Consultant.",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Anandapur Rd, Krishnanagar",
            "addressLocality": "Guwahati",
            "addressRegion": "Assam",
            "postalCode": "781005"
        },
        "telephone": "+916901529861",
        "email": "support@tarotwithhimu.com",
        "url": "https://tarotwithhimu.com"
    });
    document.head.appendChild(script);
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    navToggle();
    addStructuredData();
    console.log('Tarot With Himu — Best Astrologer in Guwahati website loaded');
});
