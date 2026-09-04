#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re

ROOT = "/home/claude/build"
DATA = json.load(open("/home/claude/cities_data.json", encoding="utf-8"))

WA_BASE = "https://wa.me/916901529861"
PHONE = "+916901529861"
PHONE_DISPLAY = "+91 6901529861"
EMAIL = "support@tarotwithhimu.com"
SITE = "https://himangshuin.github.io/astrologeringuwahati"

# Keyword-forward brand: lead with the primary SEO phrase everywhere,
# keep "Himu" as the named practitioner for trust/E-E-A-T.
BRAND = "Himu Astrology"
BRAND_TAG = "Best Astrologer in Guwahati"
PERSON = "Himu"

FONTS_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500;1,9..144,600&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
)

LOGO_MARK = (
    '<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true">'
    '<path d="M20.5 4.5c-6 1.2-10 6.4-10 12.2 0 6.9 5.6 12.5 12.5 12.5 2 0 3.9-.5 5.5-1.3-2.6 3.5-6.8 5.6-11.4 5.6C9.6 33.5 3 26.9 3 18.9S9.6 4.3 17.1 4.3c1.2 0 2.3.1 3.4.2z" fill="currentColor" transform="translate(0,-2.3) scale(0.86)"/>'
    '<circle cx="24.5" cy="7.5" r="1.4" fill="currentColor"/><circle cx="27.5" cy="12.5" r="0.9" fill="currentColor"/><circle cx="21" cy="11" r="0.7" fill="currentColor"/>'
    '</svg>'
)

WHATSAPP_ICON = (
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3C7 3 3 6.8 3 11.5c0 2 .8 3.9 2.1 5.3L4 21l4.4-1.3c1.1.5 2.3.8 3.6.8 5 0 9-3.8 9-8.5S17 3 12 3z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>'
    '<path d="M8.7 10.4c.4 2.3 2.3 4.1 4.6 4.5.6.1 1-.5.7-1l-.7-1.1c-.2-.3-.6-.4-.9-.2l-.5.3c-.7-.4-1.4-1.1-1.8-1.8l.3-.5c.2-.3.1-.7-.2-.9l-1.1-.7c-.5-.3-1.1.1-1 .7z" fill="currentColor"/></svg>'
)

# Top dropdown cities (kept consistent across all pages, mirrors original curated list)
DROPDOWN_CITIES = [
    ("best-astrologer-in-barpeta.html", "Best Astrologer in Barpeta"),
    ("best-astrologer-in-biswanath-chariali.html", "Best Astrologer in Biswanath Chariali"),
    ("best-astrologer-in-bongaigaon.html", "Best Astrologer in Bongaigaon"),
    ("best-astrologer-in-dhemaji.html", "Best Astrologer in Dhemaji"),
    ("best-astrologer-in-dhubri.html", "Best Astrologer in Dhubri"),
    ("best-astrologer-in-dibrugarh.html", "Best Astrologer in Dibrugarh"),
    ("best-astrologer-in-diphu.html", "Best Astrologer in Diphu"),
    ("best-astrologer-in-goalpara.html", "Best Astrologer in Goalpara"),
    ("best-astrologer-in-golaghat.html", "Best Astrologer in Golaghat"),
    ("best-astrologer-in-haflong.html", "Best Astrologer in Haflong"),
]

def wa_link(text):
    from urllib.parse import quote
    return f"{WA_BASE}?text={quote(text)}"

def nav(active=""):
    dd_items = "\n".join(
        f'                        <a href="{href}">{label}</a>' for href, label in DROPDOWN_CITIES
    )
    def cls(name):
        return ' class="active"' if active == name else ''
    dd_active = ' active' if active == "locations" else ''
    return f'''<nav class="navbar">
    <div class="container nav-container">
        <div class="logo">
            <a href="index.html" style="text-decoration:none;">
                <p class="logo-title">{LOGO_MARK}Best Astrologer in Guwahati</p>
            </a>
            <p>Himu — Top Astrologer in Assam | Tarot • Vedic Astrology • Numerology • Vastu</p>
        </div>
        <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M2 5h16M2 10h16M2 15h16" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        </button>
        <ul class="nav-links">
            <li><a href="index.html"{cls("home")}>Home</a></li>
            <li><a href="index.html#why"{cls("why")}>Why Us</a></li>
            <li class="has-dropdown">
                <a href="locations.html" class="dropdown-toggle{dd_active}">Areas We Serve ▾</a>
                <div class="dropdown-menu">
{dd_items}
                    <a class="view-all" href="locations.html">View All 35 Districts →</a>
                </div>
            </li>
            <li><a href="blog.html"{cls("blog")}>Blog</a></li>
            <li><a href="index.html#services">Services</a></li>
            <li><a href="index.html#pricing">Pricing</a></li>
            <li><a href="index.html#contact">Contact</a></li>
            <li><a href="{wa_link("Hello Himu, I want to book a tarot/astrology reading session")}" class="btn-consult" target="_blank" rel="noopener">Book Session</a></li>
        </ul>
    </div>
</nav>'''

def whatsapp_float():
    return f'''<div class="whatsapp-float">
    <a href="{wa_link("Hello Himu, I want to book a tarot/astrology reading session")}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WHATSAPP_ICON}</a>
</div>'''

def sticky_cta_href(wa_href):
    return f'''<div class="sticky-cta">
    <a class="sc-wa" href="{wa_href}" target="_blank" rel="noopener">WhatsApp</a>
    <a class="sc-call" href="tel:{PHONE}">Call Now</a>
</div>'''

def footer():
    return f'''<footer>
    <div class="container">
        <div class="footer-grid">
            <div>
                <h4>Best Astrologer in Guwahati</h4>
                <p class="footer-blurb">Himu — Top Astrologer in Assam, offering Vedic Astrology, Tarot, Numerology &amp; Vastu.</p>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="locations.html">Areas We Serve</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="index.html#services">Services</a></li>
                    <li><a href="index.html#pricing">Pricing</a></li>
                </ul>
            </div>
            <div>
                <h4>Popular Locations</h4>
                <ul>
                    <li><a href="best-astrologer-in-barpeta.html">Barpeta</a></li>
                    <li><a href="best-astrologer-in-biswanath-chariali.html">Biswanath Chariali</a></li>
                    <li><a href="best-astrologer-in-bongaigaon.html">Bongaigaon</a></li>
                    <li><a href="best-astrologer-in-dhemaji.html">Dhemaji</a></li>
                </ul>
            </div>
            <div>
                <h4>More Locations</h4>
                <ul>
                    <li><a href="best-astrologer-in-dhubri.html">Dhubri</a></li>
                    <li><a href="best-astrologer-in-dibrugarh.html">Dibrugarh</a></li>
                    <li><a href="best-astrologer-in-diphu.html">Diphu</a></li>
                    <li><a href="best-astrologer-in-goalpara.html">Goalpara</a></li>
                </ul>
            </div>
            <div>
                <h4>Contact</h4>
                <ul>
                    <li><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li>
                    <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                    <li><a href="https://www.facebook.com/tarotwithhimu" target="_blank" rel="noopener">Facebook</a></li>
                    <li><a href="https://www.instagram.com/tarotwithhimu" target="_blank" rel="noopener">Instagram</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2026 Himu — Best Astrologer in Guwahati &amp; Top Astrologer in Assam | Certified Vedic Astrologer &amp; Tarot Reader</p>
            <p class="footer-small">Serving Guwahati and all 35 districts of Assam, plus clients worldwide online | Numerology | Vastu Consultant</p>
        </div>
    </div>
</footer>'''

DEFAULT_WA = wa_link("Hello Himu, I want to book a tarot/astrology reading session")

def page_shell(head_extra, body, wa_sticky_href=DEFAULT_WA):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="Y7HAcD4-tik6Ed_JMMSuXnI6-qL1G9U10HX8z_CHCy0" />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <meta name="theme-color" content="#0e0a1c">
{head_extra}
    {FONTS_LINK}
    <link rel="stylesheet" href="style.css">
</head>
<body>
{whatsapp_float()}
{body}
<button id="backToTop" class="back-to-top" aria-label="Back to top" type="button">
    <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M10 15V5M10 5l-5 5M10 5l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>
<script src="script.js"></script>
{sticky_cta_href(wa_sticky_href)}
</body>
</html>
'''

SERVICE_CARDS = [
    ("icon-tarot", '<rect x="10" y="6" width="14" height="22" rx="2" transform="rotate(-8 17 17)" fill="none" stroke="currentColor" stroke-width="1.6"/><rect x="16" y="10" width="14" height="22" rx="2" transform="rotate(8 23 21)" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="23" cy="21" r="2.4" fill="currentColor"/>',
     "Tarot Reading", "In-depth past, present &amp; future insights for clarity in relationships, career &amp; decisions.",
     ["Love &amp; relationship tarot", "Career &amp; decision-making spreads", "Yes/No &amp; timing questions"]),
    ("icon-moon", '<path d="M25 8c-7 1-12 7-12 14s5 13 12 14c-2.6 1.3-5.6 2-8.7 2C7 38 1 30.8 1 22S7 6 16.3 6c3.1 0 6.1.7 8.7 2z" transform="translate(6,-2)" fill="currentColor"/><circle cx="30" cy="10" r="1.3" fill="currentColor"/><circle cx="33" cy="15" r="0.9" fill="currentColor"/>',
     "Vedic Astrology", "Vedic birth chart (Kundli) analysis, planetary remedies, and life predictions.",
     ["Birth chart &amp; Dasha analysis", "Marriage &amp; Kundli matching", "Planetary remedies"]),
    ("icon-number", '<circle cx="20" cy="20" r="13" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M17 14v12M14 14h6M14 26h6M23 26l4-12h-4.5M23 26h5" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
     "Numerology", "Decode your date of birth, name numbers, and unlock your soul's blueprint.",
     ["Life path number reading", "Name correction guidance", "Lucky number &amp; date selection"]),
    ("icon-home", '<path d="M8 19 20 9l12 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M11 17v13h18V17" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M17 30v-7h6v7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
     "Vastu Consultation", "Harmonize home &amp; office energies for prosperity and peace.",
     ["Home &amp; office Vastu audit", "Simple, low-cost remedies", "New construction guidance"]),
]

BLOG_POSTS = [
    dict(icon="icon-tarot", svg=SERVICE_CARDS[0][1], title="5 Signs You Need a Tarot Reading Immediately",
         href="post1.html", meta="5 min read", desc="Discover the unmistakable signs that the universe is calling you for guidance through tarot...",
         cta="Read More →", live=True),
    dict(icon="icon-number", svg=SERVICE_CARDS[2][1], title="How Numerology Can Transform Your Career Path",
         href=wa_link("Hello Himu, I'd like to read the Numerology & Career article"), meta="Coming soon",
         desc="Learn how your birth date numbers reveal your professional destiny and success path...",
         cta="Ask Himu →", live=False),
    dict(icon="icon-home", svg=SERVICE_CARDS[3][1], title="Vastu Tips for a Harmonious Home",
         href=wa_link("Hello Himu, I'd like to read the Vastu Tips article"), meta="Coming soon",
         desc="Simple yet powerful Vastu corrections to bring positive energy into your living space...",
         cta="Ask Himu →", live=False),
    dict(icon="icon-moon", svg=SERVICE_CARDS[1][1], title="Understanding Your Birth Chart: A Beginner's Guide",
         href=wa_link("Hello Himu, I'd like to read the Birth Chart Guide article"), meta="Coming soon",
         desc="Demystify astrology with this comprehensive guide to reading your natal chart...",
         cta="Ask Himu →", live=False),
]

def services_section():
    cards = []
    for icon_cls, svg, title, desc, items in SERVICE_CARDS:
        li = "\n".join(f"                    <li>{i}</li>" for i in items)
        cards.append(f'''            <div class="service-card">
                <div class="icon {icon_cls}"><svg viewBox="0 0 40 40" aria-hidden="true">{svg}</svg></div>
                <h3>{title}</h3>
                <p>{desc}</p>
                <ul>
{li}
                </ul>
            </div>''')
    return f'''<section id="services" class="services">
    <div class="container">
        <h2 class="section-title">Astrology, Tarot, Numerology &amp; Vastu Services</h2>
        <p class="section-subtitle">The complete offering that makes Himu the best astrologer in Guwahati and a top astrologer in Assam</p>
        <div class="services-grid">
{chr(10).join(cards)}
        </div>
    </div>
</section>'''

FAQ_HOME = [
    ("Who is the best astrologer in Guwahati?",
     "Himu is a certified Vedic astrologer and tarot reader based in Guwahati, widely regarded as one of the best and most trusted astrologers in the city — offering birth chart readings, tarot sessions, numerology and Vastu consultation, both online (WhatsApp/video call) and in person at the Krishnanagar studio."),
    ("Who is the top astrologer in Assam?",
     "Himu is recognised as a top astrologer in Assam, serving clients across Guwahati and all 35 districts of the state through accurate Vedic astrology, tarot reading, numerology and Vastu guidance — available online to clients anywhere in Assam."),
    ("What is the difference between tarot reading and Vedic astrology?",
     "Vedic astrology uses your exact date, time and place of birth to map planetary positions and predict long-term life patterns, while tarot reading uses card spreads to give intuitive guidance on a specific question or current situation. Many clients combine both."),
    ("How do I book an online astrology or tarot consultation?",
     "Message Himu on WhatsApp with your name, date of birth (and time/place for astrology), and the area you're calling from. Available slots and consultation fees will be shared, and sessions are conducted over WhatsApp voice/video call."),
    ("Does the best astrologer in Guwahati serve areas outside the city?",
     "Yes — clients from all 35 districts of Assam are served online, from Silchar and Karimganj in the Barak Valley to Dibrugarh and Tinsukia in Upper Assam. See the full list on the Areas We Serve page."),
    ("What can astrology and tarot help with?",
     "Common areas include love and relationships, marriage compatibility (Kundli matching), career and job changes, financial decisions, family matters, and identifying planetary remedies for ongoing difficulties."),
    ("How much does a session with the best astrologer in Guwahati cost?",
     "Fees vary by session type (tarot, Vedic astrology, numerology or Vastu) and duration. Message Himu on WhatsApp with what you need and the exact price and available slots will be shared before you book."),
]

STATS = [
    ("8+", "Years of Practice"),
    ("3,500+", "Readings Delivered"),
    ("35", "Districts Served in Assam"),
    ("4.9★", "Average Client Rating"),
]

def stats_bar():
    items = "\n".join(
        f'''            <div class="stat-item">
                <span class="stat-num">{num}</span>
                <span class="stat-label">{label}</span>
            </div>''' for num, label in STATS
    )
    return f'''<section class="stats-bar">
    <div class="container stats-grid">
{items}
    </div>
</section>'''

WHY_US = [
    ("icon-tarot", "Certified &amp; Experienced", "8+ years reading for clients across Guwahati and Assam, trained in Vedic astrology, tarot and numerology."),
    ("icon-moon", "Accurate, Practical Guidance", "Predictions paired with clear, doable remedies — not vague generalities."),
    ("icon-number", "100% Confidential", "Every session is private and judgement-free, whether on WhatsApp or in person."),
    ("icon-home", "Available Across Assam", "Online consultations for all 35 districts, plus in-person sessions in Guwahati."),
]

def why_choose_section():
    cards = "\n".join(
        f'''            <div class="why-card">
                <div class="icon {icon_cls}"><svg viewBox="0 0 40 40" aria-hidden="true">{[svg for c,svg,*_ in SERVICE_CARDS if c==icon_cls][0]}</svg></div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>''' for icon_cls, title, desc in WHY_US
    )
    return f'''<section id="why" class="why-choose">
    <div class="container">
        <h2 class="section-title">Why Clients Call Himu the Best Astrologer in Guwahati</h2>
        <p class="section-subtitle">What sets a top astrologer in Assam apart — trust, accuracy and genuine care</p>
        <div class="why-grid">
{cards}
        </div>
    </div>
</section>'''

PROCESS_STEPS = [
    ("01", "Message on WhatsApp", "Reach out with your name and what you'd like guidance on — love, career, marriage, finance or general life direction."),
    ("02", "Share Your Details", "For astrology, share your date, time &amp; place of birth. For tarot, just come with an open question or situation in mind."),
    ("03", "Get Your Reading", "Himu prepares your chart or draws your spread and walks you through it on a WhatsApp voice/video call."),
    ("04", "Follow-Up Guidance", "Leave with clear remedies and next steps — with follow-up support if you need clarity later."),
]

def process_section():
    steps = "\n".join(
        f'''            <div class="step-card">
                <span class="step-num">{n}</span>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>''' for n, title, desc in PROCESS_STEPS
    )
    return f'''<section class="process-section">
    <div class="container">
        <h2 class="section-title">How a Session Works</h2>
        <p class="section-subtitle">Booking the best astrologer in Guwahati is simple — here's what to expect</p>
        <div class="process-grid">
{steps}
        </div>
    </div>
</section>'''

ZODIAC_SIGNS = [
    ("Aries", "Mar 21 – Apr 19"), ("Taurus", "Apr 20 – May 20"), ("Gemini", "May 21 – Jun 20"),
    ("Cancer", "Jun 21 – Jul 22"), ("Leo", "Jul 23 – Aug 22"), ("Virgo", "Aug 23 – Sep 22"),
    ("Libra", "Sep 23 – Oct 22"), ("Scorpio", "Oct 23 – Nov 21"), ("Sagittarius", "Nov 22 – Dec 21"),
    ("Capricorn", "Dec 22 – Jan 19"), ("Aquarius", "Jan 20 – Feb 18"), ("Pisces", "Feb 19 – Mar 20"),
]

def zodiac_section():
    cards = "\n".join(
        f'''            <a class="zodiac-card" href="{wa_link(f"Hello Himu, I would like a reading for my zodiac sign: {name}")}" target="_blank" rel="noopener">
                <span class="z-name">{name}</span>
                <span class="z-dates">{dates}</span>
            </a>''' for name, dates in ZODIAC_SIGNS
    )
    return f'''<section class="zodiac-section">
    <div class="container">
        <h2 class="section-title">Rashi &amp; Zodiac Guidance</h2>
        <p class="section-subtitle">Tap your sign to ask Himu, the best astrologer in Guwahati, for a quick reading</p>
        <div class="zodiac-grid">
{cards}
        </div>
    </div>
</section>'''

PRICING_PLANS = [
    ("Quick Clarity", "Tarot Reading", "₹499", "Focused on one question or situation — love, career or a decision you're facing.", ["30-minute WhatsApp/video session", "3–5 card focused spread", "Voice-note summary to keep"], False),
    ("Full Birth Chart", "Vedic Astrology", "₹999", "Complete Kundli analysis with Dasha timing and remedies — the most popular session.", ["60-minute detailed reading", "Birth chart &amp; Dasha analysis", "Personalised planetary remedies", "Follow-up questions included"], True),
    ("Life Guidance", "Astrology + Numerology + Vastu", "₹1,999", "A combined session for major life decisions — marriage, career shift, or new home.", ["90-minute combined session", "Kundli, numbers &amp; Vastu review", "Written action plan", "Priority WhatsApp support"], False),
]

def pricing_section():
    cards = []
    for name, sub, price, desc, feats, popular in PRICING_PLANS:
        li = "\n".join(f"                    <li>{f}</li>" for f in feats)
        badge = '<span class="popular-badge">Most Booked</span>' if popular else ""
        cls = " popular" if popular else ""
        cards.append(f'''            <div class="price-card{cls}">
                {badge}
                <h3>{name}</h3>
                <span class="price-sub">{sub}</span>
                <div class="price-amount">{price}<span>starting</span></div>
                <p>{desc}</p>
                <ul>
{li}
                </ul>
                <a href="{wa_link(f"Hello Himu, I want to book the {name} session")}" class="btn-secondary" target="_blank" rel="noopener">Book on WhatsApp →</a>
            </div>''')
    return f'''<section id="pricing" class="pricing-section">
    <div class="container">
        <h2 class="section-title">Consultation Packages</h2>
        <p class="section-subtitle">Transparent starting prices from the best astrologer in Guwahati — final fee confirmed on WhatsApp based on your exact requirement</p>
        <div class="pricing-grid">
{chr(10).join(cards)}
        </div>
    </div>
</section>'''

TESTIMONIALS = [
    ("Ritu Sharma", "Guwahati", "Himu's tarot reading was incredibly accurate. He guided me through a major career shift with clarity and compassion. Truly the best astrologer in Guwahati I've consulted."),
    ("Ankur Deka", "Dibrugarh", "I was skeptical about online astrology sessions, but the Kundli reading was spot on about my career timing. Booked entirely over WhatsApp from Dibrugarh — smooth and professional."),
    ("Priyanka Baruah", "Silchar", "Consulted for marriage matching before my wedding. Himu explained the Kundli Milan report in simple terms and gave practical remedies. Highly recommend to anyone in Assam."),
    ("Rajib Gogoi", "Jorhat", "Numerology session helped me pick the right name for my new business. Detailed, honest and easy to book online from Jorhat."),
    ("Mridul Bora", "Tezpur", "Booked a Vastu consultation for our new house over a video call from Tezpur. Simple, low-cost corrections and very clear explanations — highly recommend."),
    ("Nabanita Das", "Nagaon", "Struggled with career confusion for months. One tarot session with Himu gave me the clarity to finally make a decision. Worth every rupee."),
    ("Junmoni Kalita", "Barpeta", "Genuine and accurate — not the vague, generic answers you get elsewhere. Himu's astrology reading matched exactly what I was going through."),
    ("Debojit Saikia", "Golaghat", "Easy WhatsApp booking, on-time session, and remedies that actually made sense for my situation. Recommended to my whole family in Golaghat."),
]

def testimonials_section(highlight_city=None, subtitle=None):
    items = list(TESTIMONIALS)
    if highlight_city:
        offset = sum(ord(c) for c in highlight_city) % len(items)
        items = items[offset:] + items[:offset]
        matches = [t for t in items if t[1].lower() == highlight_city.lower()]
        if matches:
            items.remove(matches[0])
            items.insert(0, matches[0])
    items = items[:4]
    sub = subtitle or "Real feedback from clients who booked the best astrologer in Guwahati"
    cards = "\n".join(
        f'''            <div class="testimonial-card">
                <div class="stars">★★★★★</div>
                <p>&quot;{quote}&quot;</p>
                <p class="client">— {name}, {city}</p>
            </div>''' for name, city, quote in items
    )
    return f'''<section class="testimonial">
    <div class="container">
        <h2 class="section-title">What Clients Across Assam Say</h2>
        <p class="section-subtitle">{sub}</p>
        <div class="testimonial-grid">
{cards}
        </div>
    </div>
</section>'''

def blog_teaser_section():
    posts = BLOG_POSTS[:3]
    cards = []
    for p in posts:
        target = "" if p["live"] else ' target="_blank" rel="noopener"'
        cards.append(f'''            <a class="blog-teaser-card" href="{p['href']}"{target}>
                <div class="icon {p['icon']}"><svg viewBox="0 0 40 40" aria-hidden="true">{p['svg']}</svg></div>
                <span class="tag">{p['meta']}</span>
                <h3>{p['title']}</h3>
                <p>{p['desc']}</p>
            </a>''')
    return f'''<section class="blog-teaser-section">
    <div class="container">
        <h2 class="section-title">From the Blog</h2>
        <p class="section-subtitle">Astrology &amp; tarot insights from the best astrologer in Guwahati</p>
        <div class="blog-teaser-grid">
{chr(10).join(cards)}
        </div>
        <div class="view-all-wrap">
            <a href="blog.html" class="btn-secondary">Read All Articles →</a>
        </div>
    </div>
</section>'''

def faq_section(title, faqs):
    items = []
    for q, a in faqs:
        items.append(f'''            <details class="faq-item">
                <summary>{q}</summary>
                <p>{a}</p>
            </details>''')
    return f'''<section class="faq-section">
    <div class="container">
        <h2 class="section-title">{title}</h2>
        <div class="faq-list">
{chr(10).join(items)}
        </div>
    </div>
</section>'''

FEATURED_LOCATIONS = [
    ("best-astrologer-in-barpeta.html", "Barpeta", "Barpeta District"),
    ("best-astrologer-in-biswanath-chariali.html", "Biswanath Chariali", "Biswanath District"),
    ("best-astrologer-in-bongaigaon.html", "Bongaigaon", "Bongaigaon District"),
    ("best-astrologer-in-dhemaji.html", "Dhemaji", "Dhemaji District"),
    ("best-astrologer-in-dhubri.html", "Dhubri", "Dhubri District"),
    ("best-astrologer-in-dibrugarh.html", "Dibrugarh", "Dibrugarh District"),
    ("best-astrologer-in-diphu.html", "Diphu", "Karbi Anglong District"),
    ("best-astrologer-in-goalpara.html", "Goalpara", "Goalpara District"),
    ("best-astrologer-in-golaghat.html", "Golaghat", "Golaghat District"),
    ("best-astrologer-in-haflong.html", "Haflong", "Dima Hasao District"),
    ("best-astrologer-in-hailakandi.html", "Hailakandi", "Hailakandi District"),
    ("best-astrologer-in-hamren.html", "Hamren", "West Karbi Anglong District"),
]

def locations_teaser():
    cards = "\n".join(
        f'''            <a class="location-card" href="{href}">
                <div class="lc-title">{name}</div>
                <div class="lc-sub">{sub}</div>
            </a>''' for href, name, sub in FEATURED_LOCATIONS
    )
    return f'''<section class="locations-section">
    <div class="container">
        <div class="locations-intro">
            <h2 class="section-title">Serving All of Assam</h2>
            <p class="section-subtitle">Online consultations available across all 35 districts — here are some of the areas we serve most</p>
        </div>
        <div class="locations-grid">
{cards}
        </div>
        <div class="view-all-wrap">
            <a href="locations.html" class="btn-secondary">View All 35 Districts of Assam →</a>
        </div>
    </div>
</section>'''

def hero_visual_svg():
    return '''<div class="hero-visual" aria-hidden="true">
                <svg viewBox="0 0 320 320">
                    <circle class="hv-ring" cx="160" cy="160" r="128"/>
                    <path class="hv-moon" d="M196 76c-46 8-78 46-78 92 0 50 38 90 87 94-18 12-40 18-63 18-58 0-105-52-105-116S144 48 202 48c22 0 43 6 61 15-24 3-46 7-67 13z"/>
                    <g class="hv-stars">
                        <circle cx="238" cy="70" r="3.4"/>
                        <circle cx="256" cy="98" r="2.1"/>
                        <circle cx="90" cy="238" r="2.6"/>
                        <circle cx="66" cy="90" r="2"/>
                    </g>
                    <g class="hv-card">
                        <rect x="120" y="118" width="92" height="132" rx="10"/>
                        <path d="M166 150v68M140 184h52" />
                        <circle cx="166" cy="150" r="5"/>
                    </g>
                </svg>
            </div>'''

def build_index():
    head_extra = f'''    <title>Best Astrologer in Guwahati | Top Astrologer in Assam – Himu</title>
    <meta name="description" content="Best Astrologer in Guwahati — Himu is a top-rated, certified Vedic astrologer &amp; tarot reader serving Guwahati and all of Assam. Astrology, Numerology &amp; Vastu for love, career, marriage &amp; finance. Book on WhatsApp today.">
    <meta name="keywords" content="best astrologer in Guwahati, top astrologer in Guwahati, top astrologer in Assam, astrologer in Guwahati, best tarot reader in Guwahati, best numerologist Assam, vastu consultant Guwahati, astrology reading Assam">
    <meta name="author" content="Himu">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="IN-AS">
    <meta name="geo.placename" content="Guwahati">
    <link rel="canonical" href="{SITE}/">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Best Astrologer in Guwahati | Top Astrologer in Assam – Himu">
    <meta property="og:description" content="Vedic astrology, tarot reading, numerology &amp; Vastu consultation from the best astrologer in Guwahati — serving all of Assam.">
    <meta property="og:image" content="{SITE}/og-image.jpg">
    <meta property="og:url" content="{SITE}/">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"ProfessionalService","name":"Himu Astrology — Best Astrologer in Guwahati","description":"Best Astrologer in Guwahati and Top Astrologer in Assam. Certified Vedic Astrologer, Tarot Reader, Numerologist and Vastu Consultant, Himu, serving all of Assam.","image":f"{SITE}/og-image.jpg","address":{"@type":"PostalAddress","streetAddress":"Anandapur Rd, Krishnanagar","addressLocality":"Guwahati","addressRegion":"Assam","postalCode":"781005","addressCountry":"IN"},"areaServed":{"@type":"State","name":"Assam"},"geo":{"@type":"GeoCoordinates","latitude":26.1445,"longitude":91.7362},"telephone":"+916901529861","email":EMAIL,"url":f"{SITE}/","priceRange":"₹","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"186"},"sameAs":["https://www.facebook.com/tarotwithhimu","https://www.instagram.com/tarotwithhimu"]}, ensure_ascii=False)}</script>
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ_HOME]}, ensure_ascii=False)}</script>'''

    body = f'''{nav("home")}

<header class="hero">
    <div class="container hero-container">
        <div class="hero-content">
            <div class="hero-badge">Assam's Top-Rated | Guwahati's Best</div>
            <h1>Best Astrologer in <span class="highlight">Guwahati</span><br>&amp; Top Astrologer in Assam</h1>
            <p>Himu — certified Vedic astrologer &amp; tarot reader based in Guwahati, trusted by clients across every district of Assam. Accurate predictions for love, career, marriage, finance and life purpose.</p>
            <div class="hero-buttons">
                <a href="{wa_link("Hello Himu, I want to book a tarot reading session")}" class="btn-primary" target="_blank" rel="noopener">Book a Reading</a>
                <a href="#services" class="btn-outline">Explore Services</a>
            </div>
            <div class="keywords">
                <span>Best Astrologer in Guwahati</span>
                <span>Top Astrologer in Assam</span>
                <span>Best Numerologist Assam</span>
                <span>Vastu Consultant Guwahati</span>
            </div>
        </div>
        <div class="hero-image">
            {hero_visual_svg()}
            <p class="hero-tagline">"Accurate. Empathetic. Life-changing insights."</p>
        </div>
    </div>
</header>

<div class="badges-strip">
    <div class="container">
        <span class="rating-chip">★★★★★ 4.9/5 — 186+ Readings</span>
        <span>Vedic &amp; Tarot Certified</span>
        <span>Online Sessions via WhatsApp</span>
        <span>Serving All 35 Districts of Assam</span>
        <span>Same-Day Slots Available</span>
    </div>
</div>

{stats_bar()}

{services_section()}

{why_choose_section()}

{process_section()}

<section id="about" class="about">
    <div class="container about-container">
        <div class="about-text">
            <h2>Meet Himu — Best Astrologer in Guwahati</h2>
            <p><strong>Himu</strong> is widely regarded as the best astrologer in Guwahati and a top astrologer in Assam, offering accurate and intuitive guidance through Vedic Astrology, Tarot Reading, Numerology, and Vastu Consultation. Based in <strong>Guwahati, Assam</strong>, Himu provides personalized readings that help clients gain clarity in love, career, health, finance, and life purpose.</p>
            <p>Whether you're searching for the best numerologist in Assam to decode your date of birth or a Vastu consultant in Guwahati to harmonize your home energy, Himu's readings combine ancient wisdom with modern insights. Online and offline sessions are available through WhatsApp and video calls — to clients in Guwahati and across every district of Assam.</p>
            <div class="about-tags">
                <span>Best Astrologer in Guwahati</span>
                <span>Top Astrologer in Assam</span>
                <span>Astrology Reading Assam</span>
                <span>Certified Tarot Reader</span>
            </div>
        </div>
        <div class="contact-info" id="contact">
            <h3>Visit or Connect</h3>
            <p><strong>Address:</strong> Anandapur Rd, Krishnanagar, Guwahati, Assam 781005</p>
            <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
            <p><strong>Phone / WhatsApp:</strong> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></p>
            <div class="social-links">
                <a href="https://www.facebook.com/tarotwithhimu" target="_blank" rel="noopener">Facebook</a>
                <a href="https://www.instagram.com/tarotwithhimu" target="_blank" rel="noopener">Instagram</a>
                <a href="{SITE}" target="_blank" rel="noopener">Website</a>
            </div>
        </div>
    </div>
</section>

{zodiac_section()}

{pricing_section()}

{locations_teaser()}

{testimonials_section()}

{blog_teaser_section()}

{faq_section("Frequently Asked Questions", FAQ_HOME)}

<section class="cta">
    <div class="container">
        <h2>Ready to transform your life?</h2>
        <p>Get clarity, healing, and direction with the best astrologer in Guwahati and a top astrologer in Assam. Sessions available in-person (Guwahati) or online across Assam and worldwide.</p>
        <div class="cta-buttons">
            <a href="{wa_link("Hello Himu, I want to book a tarot reading session")}" class="btn-wa" target="_blank" rel="noopener">WhatsApp Now</a>
            <a href="tel:{PHONE}" class="btn-call">Call for Appointment</a>
        </div>
        <p class="cta-note">Same-day online readings available | Evening slots for working professionals</p>
    </div>
</section>

<div class="map-container">
    <div class="container">
        <iframe src="https://maps.google.com/maps?q=Anandapur%20Rd%2C%20Krishnanagar%2C%20Guwahati%2C%20Assam%20781005&t=&z=15&output=embed" width="100%" height="300" style="border:0; border-radius: 24px;" allowfullscreen="" loading="lazy" title="Best Astrologer in Guwahati — studio location map"></iframe>
    </div>
</div>

{footer()}'''
    html = page_shell(head_extra, body)
    open(f"{ROOT}/index.html", "w", encoding="utf-8").write(html)

build_index()
print("index.html built")

# ---------------------------------------------------------------
# locations.html
# ---------------------------------------------------------------
DIVISIONS = [
    ("Lower Assam", [
        ("index.html", "Guwahati", "Kamrup Metropolitan (Home)", True),
        ("best-astrologer-in-barpeta.html", "Barpeta", "Barpeta District", False),
        ("best-astrologer-in-bongaigaon.html", "Bongaigaon", "Bongaigaon District", False),
        ("best-astrologer-in-dhubri.html", "Dhubri", "Dhubri District", False),
        ("best-astrologer-in-goalpara.html", "Goalpara", "Goalpara District", False),
        ("best-astrologer-in-hatsingimari.html", "Hatsingimari", "South Salmara-Mankachar District", False),
        ("best-astrologer-in-kajalgaon.html", "Kajalgaon (Chirang)", "Chirang District", False),
        ("best-astrologer-in-kokrajhar.html", "Kokrajhar", "Kokrajhar District", False),
        ("best-astrologer-in-mushalpur.html", "Mushalpur (Baksa)", "Baksa District", False),
        ("best-astrologer-in-nalbari.html", "Nalbari", "Nalbari District", False),
        ("best-astrologer-in-pathsala.html", "Pathsala", "Bajali District", False),
        ("best-astrologer-in-rangia.html", "Rangia", "Kamrup District", False),
        ("best-astrologer-in-tamulpur.html", "Tamulpur", "Tamulpur District", False),
    ]),
    ("North Assam", [
        ("best-astrologer-in-biswanath-chariali.html", "Biswanath Chariali", "Biswanath District", False),
        ("best-astrologer-in-mangaldai.html", "Mangaldai", "Darrang District", False),
        ("best-astrologer-in-tezpur.html", "Tezpur", "Sonitpur District", False),
        ("best-astrologer-in-udalguri.html", "Udalguri", "Udalguri District", False),
    ]),
    ("Upper Assam", [
        ("best-astrologer-in-dhemaji.html", "Dhemaji", "Dhemaji District", False),
        ("best-astrologer-in-dibrugarh.html", "Dibrugarh", "Dibrugarh District", False),
        ("best-astrologer-in-golaghat.html", "Golaghat", "Golaghat District", False),
        ("best-astrologer-in-jorhat.html", "Jorhat", "Jorhat District", False),
        ("best-astrologer-in-majuli.html", "Majuli", "Majuli District", False),
        ("best-astrologer-in-north-lakhimpur.html", "North Lakhimpur", "Lakhimpur District", False),
        ("best-astrologer-in-sivasagar.html", "Sivasagar", "Sivasagar District", False),
        ("best-astrologer-in-sonari.html", "Sonari (Charaideo)", "Charaideo District", False),
        ("best-astrologer-in-tinsukia.html", "Tinsukia", "Tinsukia District", False),
    ]),
    ("Central Assam", [
        ("best-astrologer-in-diphu.html", "Diphu", "Karbi Anglong District", False),
        ("best-astrologer-in-haflong.html", "Haflong", "Dima Hasao District", False),
        ("best-astrologer-in-hamren.html", "Hamren", "West Karbi Anglong District", False),
        ("best-astrologer-in-hojai.html", "Hojai", "Hojai District", False),
        ("best-astrologer-in-morigaon.html", "Morigaon", "Morigaon District", False),
        ("best-astrologer-in-nagaon.html", "Nagaon", "Nagaon District", False),
    ]),
    ("Barak Valley", [
        ("best-astrologer-in-hailakandi.html", "Hailakandi", "Hailakandi District", False),
        ("best-astrologer-in-karimganj.html", "Karimganj (Sribhumi)", "Sribhumi District", False),
        ("best-astrologer-in-silchar.html", "Silchar", "Cachar District", False),
    ]),
]

def build_locations():
    blocks = []
    for div_name, items in DIVISIONS:
        cards = []
        for href, name, sub, home in items:
            style = ' style="border-color:#cf9f52;"' if home else ''
            cards.append(f'''            <a class="location-card" href="{href}"{style}>
                <div class="lc-title">{name}</div>
                <div class="lc-sub">{sub}</div>
            </a>''')
        blocks.append(f'''        <div class="division-block">
            <h3>{div_name}</h3>
            <div class="locations-grid">
{chr(10).join(cards)}
            </div>
        </div>''')

    head_extra = f'''    <title>Best Astrologer in Assam — Top Astrologer, All 35 Districts | Himu</title>
    <meta name="description" content="Best astrologer in Assam — Himu offers Vedic astrology, tarot reading, numerology &amp; Vastu consultation across all 35 districts, from Guwahati to Silchar, Dibrugarh, Jorhat, Tezpur and beyond. Find your area below.">
    <meta name="keywords" content="best astrologer in Assam, top astrologer in Assam, astrologer near me Assam, best astrologer in Guwahati, tarot reader Assam districts, astrology consultation Assam">
    <meta name="author" content="Himu">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="IN-AS">
    <link rel="canonical" href="{SITE}/locations.html">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Best Astrologer in Assam — All 35 Districts | Himu">
    <meta property="og:description" content="Vedic astrology, tarot, numerology &amp; Vastu consultation from the best astrologer in Assam, across all 35 districts.">
    <meta property="og:url" content="{SITE}/locations.html">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/index.html"},{"@type":"ListItem","position":2,"name":"Areas We Serve","item":f"{SITE}/locations.html"}]}, ensure_ascii=False)}</script>'''

    body = f'''{nav("locations")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="index.html">Home</a></li>
            <li aria-current="page">Areas We Serve</li>
        </ol>
    </div>
</div>

<header class="hero loc-hero">
    <div class="container">
        <div class="hero-badge">All 35 Districts of Assam</div>
        <h1>Best Astrologer in Assam — <span class="highlight">Guidance Across Every District</span></h1>
        <p>Himu, the best astrologer in Guwahati, serves clients in every district of Assam — online via WhatsApp/video call, or in person at the Guwahati studio. Find your area below.</p>
    </div>
</header>

<section class="locations-section">
    <div class="container">
        <div class="locations-intro">
            <h2 class="section-title">Areas We Serve</h2>
            <p class="section-subtitle">Grouped by Assam's five administrative divisions — tap your district to see local astrology &amp; tarot services</p>
        </div>
        <div class="location-search-wrap">
            <input type="text" id="locationSearch" class="location-search" placeholder="Search your town or district…" aria-label="Search your town or district">
        </div>
{chr(10).join(blocks)}
    </div>
</section>

<section class="cta">
    <div class="container">
        <h2>Don't see your town listed?</h2>
        <p>Online sessions are available to clients anywhere in Assam — and worldwide. Message Himu directly to book, wherever you're calling from.</p>
        <div class="cta-buttons">
            <a href="{wa_link("Hello Himu, I want to book a tarot/astrology reading session")}" class="btn-wa" target="_blank" rel="noopener">WhatsApp Now</a>
            <a href="tel:{PHONE}" class="btn-call">Call for Appointment</a>
        </div>
    </div>
</section>

{footer()}'''
    html = page_shell(head_extra, body)
    open(f"{ROOT}/locations.html", "w", encoding="utf-8").write(html)

build_locations()
print("locations.html built")

# ---------------------------------------------------------------
# blog.html
# ---------------------------------------------------------------
def build_blog():
    cards = []
    for p in BLOG_POSTS:
        target = "" if p["live"] else ' target="_blank" rel="noopener"'
        extra_cls = "" if p["live"] else " coming-soon"
        cards.append(f'''            <article class="blog-card{extra_cls}">
                <div class="icon {p['icon']}"><svg viewBox="0 0 40 40" aria-hidden="true">{p['svg']}</svg></div>
                <span class="tag">{p['meta']}</span>
                <h2>{'<a href="'+p['href']+'">'+p['title']+'</a>' if p['live'] else p['title']}</h2>
                <p>{p['desc']}</p>
                <a href="{p['href']}" class="read-more"{target}>{p['cta']}</a>
            </article>''')

    head_extra = f'''    <title>Astrology &amp; Tarot Blog | Best Astrologer in Guwahati – Himu</title>
    <meta name="description" content="Read the latest articles on tarot reading, Vedic astrology, numerology and Vastu tips from Guwahati's best astrologer, serving all of Assam.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE}/blog.html">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Astrology & Tarot Blog | Best Astrologer in Guwahati">
    <meta property="og:url" content="{SITE}/blog.html">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/index.html"},{"@type":"ListItem","position":2,"name":"Blog","item":f"{SITE}/blog.html"}]}, ensure_ascii=False)}</script>'''

    body = f'''{nav("blog")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="index.html">Home</a></li>
            <li aria-current="page">Blog</li>
        </ol>
    </div>
</div>

<header class="hero loc-hero">
    <div class="container">
        <div class="hero-badge">Insights &amp; Guidance</div>
        <h1>Tarot &amp; Astrology <span class="highlight">Blog</span></h1>
        <p>Insights, guidance, and wisdom from Guwahati's best astrologer — for readers across Assam.</p>
    </div>
</header>

<section>
    <div class="container">
        <div class="blog-grid">
{chr(10).join(cards)}
        </div>
    </div>
</section>

{footer()}'''
    html = page_shell(head_extra, body)
    open(f"{ROOT}/blog.html", "w", encoding="utf-8").write(html)

build_blog()
print("blog.html built")

# ---------------------------------------------------------------
# post1.html
# ---------------------------------------------------------------
def build_post1():
    head_extra = f'''    <title>5 Signs You Need a Tarot Reading | Best Astrologer in Guwahati</title>
    <meta name="description" content="Discover the 5 powerful signs that indicate you need professional tarot reading guidance from Guwahati's best astrologer.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE}/post1.html">
    <meta property="og:type" content="article">
    <meta property="og:title" content="5 Signs You Need a Tarot Reading Immediately">
    <meta property="og:url" content="{SITE}/post1.html">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/index.html"},{"@type":"ListItem","position":2,"name":"Blog","item":f"{SITE}/blog.html"},{"@type":"ListItem","position":3,"name":"5 Signs You Need a Tarot Reading","item":f"{SITE}/post1.html"}]}, ensure_ascii=False)}</script>
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Article","headline":"5 Signs You Need a Tarot Reading Immediately","author":{"@type":"Person","name":"Himu"},"publisher":{"@type":"Organization","name":"Himu Astrology - Best Astrologer in Guwahati"},"mainEntityOfPage":f"{SITE}/post1.html","description":"Discover the 5 powerful signs that indicate you need professional tarot reading guidance from Guwahati's best astrologer."}, ensure_ascii=False)}</script>'''

    body = f'''{nav("blog")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="index.html">Home</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li aria-current="page">5 Signs You Need a Tarot Reading</li>
        </ol>
    </div>
</div>

<article style="padding: 56px 0 90px;">
    <div class="container post-body">
        <h1>5 Signs You Need a Tarot Reading Immediately</h1>
        <p class="post-meta">By Himu · 5 min read</p>

        <p>Have you been feeling stuck, confused, or anxious about your life's direction? The universe often sends us subtle (and not-so-subtle) signals that it's time to seek guidance. As a <strong>tarot reader in Guwahati</strong>, I've identified 5 clear signs that indicate you need a professional tarot reading.</p>

        <h2>1. You Keep Seeing Repeating Numbers</h2>
        <p>111, 222, 333, 444 — if these numbers keep appearing on clocks, receipts, or license plates, the universe is trying to communicate. A tarot reading can decode what these angel numbers mean for your specific situation.</p>

        <h2>2. You Feel Emotionally Stuck or Depleted</h2>
        <p>When you can't move past a breakup, career setback, or family conflict, tarot cards reveal the hidden emotional blocks holding you back. Many clients come to me feeling completely drained, only to discover breakthrough solutions through the cards.</p>

        <h2>3. Major Life Decisions Are Looming</h2>
        <p>Should you change jobs? Move to a new city? Start a business? Tarot doesn't predict a fixed future — it illuminates the potential outcomes of each choice, empowering you to make confident decisions.</p>

        <h2>4. You've Lost Connection With Your Intuition</h2>
        <p>If you used to "just know" what was right but now second-guess everything, tarot reading reactivates your inner guidance system. I help clients remember their own wisdom.</p>

        <h2>5. Synchronicities Are Increasing</h2>
        <p>Running into the same person, hearing the same song, or having vivid dreams about specific symbols — these aren't coincidences. A professional reading connects these dots and reveals their meaning for your life path.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">Ready for clarity?</h2>
            <p>Book your personalized tarot session with Himu, the trusted tarot reader in Guwahati.</p>
            <div class="cta-buttons">
                <a href="{wa_link("Hello Himu, I want to book a tarot reading session")}" class="btn-wa" target="_blank" rel="noopener">Book Your Reading Now →</a>
            </div>
        </div>

        <h2>Why Choose Himu — Best Astrologer in Guwahati?</h2>
        <ul>
            <li>Certified astrologer and tarot reader</li>
            <li>Accurate predictions with practical solutions</li>
            <li>Confidential, compassionate guidance</li>
            <li>Online sessions available across Assam and worldwide</li>
        </ul>

        <p>Serving clients in Guwahati, across all districts of Assam, and globally via WhatsApp and video calls. Visit the studio at Anandapur Rd, Krishnanagar, or connect online today.</p>

        <div class="local-fact-card" style="margin-top:40px;">
            <h3>About Himu</h3>
            <p style="font-size:0.94rem;">Himu is a certified astrologer, offering tarot, Vedic astrology, numerology, and Vastu consultation from Guwahati, Assam, to clients across the state and beyond.</p>
        </div>
    </div>
</article>

{footer()}'''
    html = page_shell(head_extra, body)
    open(f"{ROOT}/post1.html", "w", encoding="utf-8").write(html)

build_post1()
print("post1.html built")

# ---------------------------------------------------------------
# City pages
# ---------------------------------------------------------------
def build_city(slug, d):
    # Computed from SITE + slug (not read from cities_data.json) so it can
    # never drift out of sync if the hosting domain changes.
    canonical_url = f"{SITE}/{slug}"

    faqs = [(q, a) for q, a in d["faqs"]]
    keyword_spans = "\n".join(f"            <span>{k}</span>" for k in d["keyword_pills"])
    lc_paras = "\n".join(f"            <p>{p}</p>" for p in d["lc_paras"])
    fact_items = "\n".join(f"                <li>{i}</li>" for i in d["fact_items"])
    nearby_links = "\n".join(f'            <a href="{href}">{label}</a>' for href, label in d["nearby"])

    ld_service = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": f"Himu — Best Astrologer in {d['city_name']}",
        "description": d["service_desc"],
        "image": f"{SITE}/og-image.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": "Anandapur Rd, Krishnanagar", "addressLocality": "Guwahati", "addressRegion": "Assam", "postalCode": "781005", "addressCountry": "IN"},
        "areaServed": {"@type": "City", "name": d["city_name"]},
        "geo": d["geo"],
        "telephone": PHONE, "email": EMAIL, "url": canonical_url, "priceRange": "₹",
        "sameAs": ["https://www.facebook.com/tarotwithhimu", "https://www.instagram.com/tarotwithhimu"],
    }
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    ld_breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/index.html"},
        {"@type": "ListItem", "position": 2, "name": "Areas We Serve", "item": f"{SITE}/locations.html"},
        {"@type": "ListItem", "position": 3, "name": d["city_name"], "item": canonical_url},
    ]}

    head_extra = f'''    <title>{d['title']}</title>
    <meta name="description" content="{d['desc']}">
    <meta name="keywords" content="{d['keywords']}">
    <meta name="author" content="Himu">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="IN-AS">
    <meta name="geo.placename" content="{d['city_name']}">
    <link rel="canonical" href="{canonical_url}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Best Astrologer in {d['city_name']} | Top Astrologer in Assam – Himu">
    <meta property="og:description" content="{d['desc']}">
    <meta property="og:image" content="{SITE}/og-image.jpg">
    <meta property="og:url" content="{canonical_url}">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">{json.dumps(ld_service, ensure_ascii=False)}</script>
    <script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>
    <script type="application/ld+json">{json.dumps(ld_breadcrumb, ensure_ascii=False)}</script>'''

    body = f'''{nav("locations")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="index.html">Home</a></li>
            <li><a href="locations.html">Areas We Serve</a></li>
            <li aria-current="page">{d['city_name']}</li>
        </ol>
    </div>
</div>

<header class="hero loc-hero">
    <div class="container">
        <div class="hero-badge">{d['hero_badge']}</div>
        <h1>Best Astrologer in <span class="highlight">{d['city_name']}</span> — Top Astrologer in Assam</h1>
        <p>{d['hero_p']}</p>
        <div class="hero-buttons">
            <a href="{d['wa_href']}" class="btn-primary" target="_blank" rel="noopener">Book a Reading in {d['city_name']}</a>
            <a href="tel:{PHONE}" class="btn-outline">Call Now</a>
        </div>
        <div class="keywords">
{keyword_spans}
        </div>
    </div>
</header>

<div class="badges-strip">
    <div class="container">
        <span class="rating-chip">★★★★★ 4.9/5 — 186+ Readings</span>
        <span>Vedic &amp; Tarot Certified</span>
        <span>Online Sessions via WhatsApp</span>
        <span>Clients Across Assam</span>
        <span>Same-Day Slots Available</span>
    </div>
</div>

{stats_bar()}

{services_section()}

<section class="local-context">
    <div class="container lc-grid">
        <div>
            <h2>{d['lc_h2']}</h2>
{lc_paras}
        </div>
        <div class="local-fact-card">
            <h3>{d['fact_title']}</h3>
            <ul>
{fact_items}
            </ul>
        </div>
    </div>
</section>

{why_choose_section()}

{process_section()}

{pricing_section()}

{testimonials_section(d['city_name'], f"Real feedback from clients across {d['city_name']} and Assam who booked the best astrologer in Guwahati")}

{faq_section(f"FAQs — Best Astrologer in {d['city_name']}", faqs)}

<section class="cta">
    <div class="container">
        <h2>{d['cta_h2']}</h2>
        <p>{d['cta_p']}</p>
        <div class="cta-buttons">
            <a href="{d['cta_wa']}" class="btn-wa" target="_blank" rel="noopener">WhatsApp Now</a>
            <a href="tel:{PHONE}" class="btn-call">Call for Appointment</a>
        </div>
        <p class="cta-note">Same-day online readings available | Evening slots for working professionals</p>
    </div>
</section>

<section class="nearby-section">
    <div class="container">
        <h2>Also Serving Nearby Areas</h2>
        <div class="nearby-links">
{nearby_links}
            <a href="locations.html">View All 35 Districts →</a>
        </div>
    </div>
</section>

{footer()}'''
    html = page_shell(head_extra, body, d["cta_wa"])
    open(f"{ROOT}/{slug}", "w", encoding="utf-8").write(html)

for slug, d in DATA.items():
    build_city(slug, d)
print(f"{len(DATA)} city pages built")

# ---------------------------------------------------------------
# sitemap.xml + robots.txt — generated from SITE so they can never
# drift out of sync with the canonical/OG domain used across pages.
# ---------------------------------------------------------------
import datetime
TODAY = datetime.date.today().isoformat()

def build_sitemap_and_robots():
    pages = [("index.html", "1.0"), ("locations.html", "0.9"), ("blog.html", "0.6"), ("post1.html", "0.6")]
    pages += [(slug, "0.8") for slug in DATA.keys()]

    entries = []
    for path, priority in pages:
        loc = f"{SITE}/" if path == "index.html" else f"{SITE}/{path}"
        entries.append(f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <priority>{priority}</priority>
  </url>''')

    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
'''
    open(f"{ROOT}/sitemap.xml", "w", encoding="utf-8").write(sitemap_xml)

    robots_txt = f'''User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
'''
    open(f"{ROOT}/robots.txt", "w", encoding="utf-8").write(robots_txt)
    print(f"sitemap.xml + robots.txt built ({len(pages)} urls, domain: {SITE})")

build_sitemap_and_robots()

