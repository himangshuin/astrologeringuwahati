#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Site generator — reads /data/cities_data.json and writes a properly
folder-structured static site to ROOT:

  /                       index.html, locations.html, blog.html, post1.html
                          robots.txt, sitemap.xml  (must stay at site root)
  /districts/*.html       34 district landing pages
  /assets/css/style.css
  /assets/js/script.js

All internal links/asset paths are built with url()/asset() below, so
pages work correctly no matter which folder they live in.
"""
import json, os, re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
ROOT = os.path.join(BASE_DIR, "build")
DATA = json.load(open(os.path.join(BASE_DIR, "data", "cities_data.json"), encoding="utf-8"))

WA_BASE = "https://wa.me/916901529861"
PHONE = "+916901529861"
PHONE_DISPLAY = "+91 6901529861"
EMAIL = "support@tarotwithhimu.com"
SITE = "https://himangshuin.github.io/astrologeringuwahati"

DISTRICTS_DIR = "districts"
BLOG_DIR = "blog"

# Populated below (right after BLOG_POSTS_FULL is defined) so url() can route
# every blog-post filename to /blog/. Empty here — nothing calls url() with a
# post slug before that point.
BLOG_SLUGS = set()

def url(path):
    """Absolute site URL for any internal page, correct from any folder depth.
    Filenames beginning with 'best-astrologer-in-' live under /districts/.
    Filenames in BLOG_SLUGS live under /blog/."""
    if path.startswith("best-astrologer-in-"):
        return f"{SITE}/{DISTRICTS_DIR}/{path}"
    if path in BLOG_SLUGS:
        return f"{SITE}/{BLOG_DIR}/{path}"
    if path in ("", "index.html"):
        return f"{SITE}/"
    return f"{SITE}/{path}"

def asset(path):
    """Absolute URL for a static asset under /assets/."""
    return f"{SITE}/assets/{path}"

U_HOME = url("index.html")
U_LOC = url("locations.html")
U_BLOG = url("blog.html")
ASSET_CSS = asset("css/style.css")
ASSET_JS = asset("js/script.js")

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
        f'                        <a href="{url(href)}">{label}</a>' for href, label in DROPDOWN_CITIES
    )
    def cls(name):
        return ' class="active"' if active == name else ''
    dd_active = ' active' if active == "locations" else ''
    return f'''<nav class="navbar">
    <div class="container nav-container">
        <div class="logo">
            <a href="{U_HOME}" style="text-decoration:none;">
                <p class="logo-title">{LOGO_MARK}Best Astrologer in Guwahati</p>
            </a>
            <p>Himu — Top Astrologer in Assam | Tarot • Vedic Astrology • Numerology • Vastu</p>
        </div>
        <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M2 5h16M2 10h16M2 15h16" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        </button>
        <ul class="nav-links">
            <li><a href="{U_HOME}"{cls("home")}>Home</a></li>
            <li><a href="{U_HOME}#why"{cls("why")}>Why Us</a></li>
            <li class="has-dropdown">
                <a href="{U_LOC}" class="dropdown-toggle{dd_active}">Areas We Serve ▾</a>
                <div class="dropdown-menu">
{dd_items}
                    <a class="view-all" href="{U_LOC}">View All 35 Districts →</a>
                </div>
            </li>
            <li><a href="{U_BLOG}"{cls("blog")}>Blog</a></li>
            <li><a href="{U_HOME}#services">Services</a></li>
            <li><a href="{U_HOME}#pricing">Pricing</a></li>
            <li><a href="{U_HOME}#contact">Contact</a></li>
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
                    <li><a href="{U_HOME}">Home</a></li>
                    <li><a href="{U_LOC}">Areas We Serve</a></li>
                    <li><a href="{U_BLOG}">Blog</a></li>
                    <li><a href="{U_HOME}#services">Services</a></li>
                    <li><a href="{U_HOME}#pricing">Pricing</a></li>
                </ul>
            </div>
            <div>
                <h4>Popular Locations</h4>
                <ul>
                    <li><a href="{url('best-astrologer-in-barpeta.html')}">Barpeta</a></li>
                    <li><a href="{url('best-astrologer-in-biswanath-chariali.html')}">Biswanath Chariali</a></li>
                    <li><a href="{url('best-astrologer-in-bongaigaon.html')}">Bongaigaon</a></li>
                    <li><a href="{url('best-astrologer-in-dhemaji.html')}">Dhemaji</a></li>
                </ul>
            </div>
            <div>
                <h4>More Locations</h4>
                <ul>
                    <li><a href="{url('best-astrologer-in-dhubri.html')}">Dhubri</a></li>
                    <li><a href="{url('best-astrologer-in-dibrugarh.html')}">Dibrugarh</a></li>
                    <li><a href="{url('best-astrologer-in-diphu.html')}">Diphu</a></li>
                    <li><a href="{url('best-astrologer-in-goalpara.html')}">Goalpara</a></li>
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
    <link rel="stylesheet" href="{ASSET_CSS}">
</head>
<body>
{whatsapp_float()}
{body}
<button id="backToTop" class="back-to-top" aria-label="Back to top" type="button">
    <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M10 15V5M10 5l-5 5M10 5l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>
<script src="{ASSET_JS}"></script>
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

def U_POSTn(slug):
    return url(slug)

# Each post: slug (filename), title, meta (read time), desc (teaser), icon/svg (reused from
# SERVICE_CARDS), keywords (meta keywords + naturally used in body), and body_html (the full
# article body, written by hand — internal links to services/pricing/districts/other posts
# are woven in naturally for SEO + internal linking).
BLOG_POSTS_FULL = [
    dict(
        slug="post1.html", icon="icon-tarot", svg=SERVICE_CARDS[0][1],
        title="5 Signs You Need a Tarot Reading Immediately",
        meta="5 min read",
        desc="Discover the unmistakable signs that the universe is calling you for guidance through tarot...",
        keywords="tarot reader in Guwahati, tarot reading in Guwahati, best tarot reader in Guwahati, online tarot reading Assam",
        og_desc="Discover the 5 powerful signs that indicate you need professional tarot reading guidance from Guwahati's best astrologer.",
        body_html=lambda: f'''<p>Have you been feeling stuck, confused, or anxious about your life's direction? The universe often sends us subtle (and not-so-subtle) signals that it's time to seek guidance. As a <strong>tarot reader in Guwahati</strong>, I've identified 5 clear signs that indicate you need a professional tarot reading.</p>

        <h2>1. You Keep Seeing Repeating Numbers</h2>
        <p>111, 222, 333, 444 — if these numbers keep appearing on clocks, receipts, or license plates, the universe is trying to communicate. A tarot reading can decode what these angel numbers mean for your specific situation.</p>

        <h2>2. You Feel Emotionally Stuck or Depleted</h2>
        <p>When you can't move past a breakup, career setback, or family conflict, tarot cards reveal the hidden emotional blocks holding you back. Many clients come to me feeling completely drained, only to discover breakthrough solutions through the cards.</p>

        <h2>3. Major Life Decisions Are Looming</h2>
        <p>Should you change jobs? Move to a new city? Start a business? Tarot doesn't predict a fixed future — it illuminates the potential outcomes of each choice, empowering you to make confident decisions. If the decision involves a long-term commitment, pairing a tarot spread with a <a href="{U_HOME}#services">Vedic astrology consultation</a> often gives a fuller picture.</p>

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

        <p>Serving clients in Guwahati, across <a href="{U_LOC}">all districts of Assam</a>, and globally via WhatsApp and video calls. Visit the studio at Anandapur Rd, Krishnanagar, or connect online today.</p>

        <div class="local-fact-card" style="margin-top:40px;">
            <h3>About Himu</h3>
            <p style="font-size:0.94rem;">Himu is a certified astrologer, offering tarot, Vedic astrology, numerology, and Vastu consultation from Guwahati, Assam, to clients across the state and beyond.</p>
        </div>''',
    ),
    dict(
        slug="numerology-career-path.html", icon="icon-number", svg=SERVICE_CARDS[2][1],
        title="How Numerology Can Transform Your Career Path",
        meta_title="Numerology & Your Career Path",
        meta="6 min read",
        desc="Learn how your birth date numbers reveal your professional destiny and success path...",
        keywords="numerologist in Guwahati, career astrologer in Guwahati, numerology consultation Assam, life path numerology, career astrology Assam",
        og_desc="Learn how numerology and your Life Path Number can guide career choices, job changes and business decisions — explained by the best astrologer in Guwahati.",
        body_html=lambda: f'''<p>Many clients come to me confused about their career — should they stay in a stable job or take a risk, switch industries, or start a business? As a <strong>numerologist in Guwahati</strong>, I've seen how a person's core numbers can bring surprising clarity to exactly these decisions.</p>

        <h2>What Is a Life Path Number?</h2>
        <p>Your Life Path Number is calculated from your full date of birth and is considered the single most important number in numerology. It describes your natural talents, the type of work environment you thrive in, and the career direction that genuinely suits your personality — not just what looks good on paper.</p>

        <h2>How Numbers Influence Career Decisions</h2>
        <p>Each Life Path Number carries distinct professional strengths. For example, Life Path 1s tend to do well as founders and leaders, Life Path 4s excel in structured, detail-driven roles, and Life Path 7s often thrive in research, analysis or spiritual work. Understanding your number helps explain past career frustrations and points toward roles where you'll naturally excel.</p>

        <h2>Name Numerology and Business Success</h2>
        <p>Beyond your birth number, the numerological value of your name (and your business name, if you run one) is believed to influence opportunity and financial flow. This is why <a href="{U_HOME}#services">name correction guidance</a> is one of the most requested numerology services from clients across Guwahati and Assam who are launching a new business or considering a name change.</p>

        <h2>When Should You Get a Numerology Reading?</h2>
        <ul>
            <li>Before accepting a new job offer or big career pivot</li>
            <li>When choosing a name for a new business or brand</li>
            <li>Before an important interview, exam or negotiation</li>
            <li>When picking a lucky date to launch, sign, or relocate</li>
        </ul>
        <p>A numerology session pairs especially well with a full <a href="{U_HOME}#services">Vedic astrology birth chart reading</a>, since Dasha (planetary period) timing and your Life Path Number often point to the same windows of opportunity.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">Curious what your numbers reveal?</h2>
            <p>Book a numerology consultation with Himu — trusted numerologist in Guwahati, serving clients across Assam online.</p>
            <div class="cta-buttons">
                <a href="{wa_link("Hello Himu, I'd like to book a numerology consultation for my career")}" class="btn-wa" target="_blank" rel="noopener">Book on WhatsApp →</a>
            </div>
        </div>

        <p>Read next: if career confusion is tied to timing rather than direction, <a href="{{POST5}}">our guide on choosing the right astrologer in Guwahati</a> explains what to look for in a consultation, and our <a href="{{POST6}}">fees guide</a> breaks down what a session typically costs.</p>''',
    ),
    dict(
        slug="vastu-tips-harmonious-home.html", icon="icon-home", svg=SERVICE_CARDS[3][1],
        title="Vastu Tips for a Harmonious Home",
        meta="5 min read",
        desc="Simple yet powerful Vastu corrections to bring positive energy into your living space...",
        keywords="vastu consultant Guwahati, vastu tips for home, vastu consultation Assam, home vastu Guwahati",
        og_desc="Simple, low-cost Vastu corrections for the kitchen, bedroom, entrance and workspace — explained by a Vastu consultant in Guwahati.",
        body_html=lambda: f'''<p>Vastu Shastra is often misunderstood as requiring expensive renovation or demolition. In reality, most homes across Guwahati and Assam can be significantly improved with small, low-cost corrections. As a <strong>Vastu consultant in Guwahati</strong>, here are the fixes I recommend most often.</p>

        <h2>1. Fix the Main Entrance Energy</h2>
        <p>The main door is considered the primary entry point for energy into your home. Keep it well-lit, clutter-free, and opening inward smoothly. Broken doorbells, squeaky hinges, or shoes piled at the entrance are simple issues worth fixing first.</p>

        <h2>2. Kitchen Placement Matters</h2>
        <p>Ideally, the kitchen should be in the south-east corner of the home, with the cook facing east while preparing food. If relocating the kitchen isn't possible, a small correction — like placing the stove so the cook doesn't face directly south — can help.</p>

        <h2>3. Bedroom Bed Direction</h2>
        <p>Sleeping with your head towards the south or east is generally favoured in Vastu, while sleeping with your head towards the north is usually avoided. This one adjustment is one of the most requested corrections in Vastu consultations for Guwahati homes.</p>

        <h2>4. Clear the North-East Corner</h2>
        <p>The north-east (Ishan corner) is associated with clarity and positive energy and should ideally be kept light, clean and clutter-free — avoid using it for storage or heavy furniture.</p>

        <h2>5. Balance the Five Elements</h2>
        <p>Vastu is ultimately about balancing the five elements — earth, water, fire, air and space — throughout your home. Simple additions like indoor plants, a small water feature, or better cross-ventilation can noticeably shift the feel of a space without any construction.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">Want a personalised Vastu review?</h2>
            <p>Send photos or a floor plan of your home or office on WhatsApp for a practical, low-cost Vastu consultation.</p>
            <div class="cta-buttons">
                <a href="{wa_link("Hello Himu, I'd like a Vastu consultation for my home")}" class="btn-wa" target="_blank" rel="noopener">Book Vastu Consultation →</a>
            </div>
        </div>

        <p>Vastu corrections often work best alongside a look at your <a href="{U_HOME}#services">birth chart and current planetary period</a>, since timing plays a role in when changes bring visible results. See our guide to <a href="{{POST4}}">understanding your birth chart</a> to learn more.</p>''',
    ),
    dict(
        slug="understanding-your-birth-chart.html", icon="icon-moon", svg=SERVICE_CARDS[1][1],
        title="Understanding Your Birth Chart: A Beginner's Guide",
        meta_title="Understanding Your Birth Chart (Kundli)",
        meta="7 min read",
        desc="Demystify astrology with this comprehensive guide to reading your natal chart...",
        keywords="kundli analysis in Guwahati, birth chart analysis Guwahati, vedic astrology Guwahati, janam kundli reading, horoscope analysis Guwahati",
        og_desc="A beginner-friendly guide to reading your Vedic birth chart (Kundli) — houses, planets and Dasha, explained by the best astrologer in Guwahati.",
        body_html=lambda: f'''<p>If you've ever received a Kundli (birth chart) and felt overwhelmed by the grid of numbers and symbols, you're not alone. This guide breaks down the basics so you can understand what your <strong>Vedic birth chart</strong> actually says about you.</p>

        <h2>What Is a Birth Chart (Kundli)?</h2>
        <p>A Kundli is a map of where each planet was positioned in the sky at your exact date, time and place of birth. It's divided into 12 houses, each representing a different life area — career, marriage, family, health, wealth and more — and 9 planets (Grahas) whose positions within those houses shape your personality and life patterns.</p>

        <h2>The 12 Houses, Simplified</h2>
        <ul>
            <li><strong>1st House</strong> — Self, personality and physical body</li>
            <li><strong>2nd House</strong> — Wealth, family and speech</li>
            <li><strong>4th House</strong> — Home, mother and emotional foundation</li>
            <li><strong>7th House</strong> — Marriage and partnerships</li>
            <li><strong>10th House</strong> — Career and public reputation</li>
            <li><strong>11th House</strong> — Income, gains and social circle</li>
        </ul>

        <h2>What Is a "Dasha" and Why Does Timing Matter?</h2>
        <p>Vedic astrology uses a system called Vimshottari Dasha to time events in your life — essentially, each planet "rules" a specific period of your life, and its placement determines whether that period brings growth or challenges in a given area. This is why two people with a similar chart can still experience very different timing for marriage, career growth or financial gain.</p>

        <h2>Common Doshas Explained</h2>
        <p>You may have heard terms like <strong>Mangal Dosha</strong> (a placement of Mars that can affect marriage compatibility), <strong>Kaal Sarp Dosha</strong>, or <strong>Kemdrum Yoga</strong>. These aren't causes for fear — most have well-established remedies once identified correctly in your chart during a proper reading.</p>

        <h2>Why a Professional Reading Matters</h2>
        <p>Free online chart generators can calculate planetary positions, but interpreting the interaction between houses, planets and Dasha periods correctly takes years of study. This is where a consultation with a <a href="{U_HOME}#services">certified Vedic astrologer in Guwahati</a> makes the real difference between a generic report and guidance that's actually accurate for your life.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">Get your birth chart read properly</h2>
            <p>Share your date, time and place of birth for a full Kundli analysis with Dasha timing and remedies.</p>
            <div class="cta-buttons">
                <a href="{wa_link("Hello Himu, I'd like a full Kundli/birth chart analysis")}" class="btn-wa" target="_blank" rel="noopener">Book Kundli Analysis →</a>
            </div>
        </div>

        <p>If marriage timing is your main question, our <a href="{{POST7}}">guide to Assamese astrology traditions</a> also covers how Kundli Milan (matching) is traditionally done before weddings in Assam.</p>''',
    ),
    dict(
        slug="how-to-choose-best-astrologer-guwahati.html", icon="icon-tarot", svg=SERVICE_CARDS[0][1],
        title="How to Choose the Best Astrologer in Guwahati (10-Point Checklist)",
        meta_title="How to Choose the Best Astrologer in Guwahati",
        meta="6 min read",
        desc="Searching for the top astrologer in Guwahati? Here's exactly what to check before you book a session...",
        keywords="best astrologer in Guwahati, top astrologer in Guwahati, top 10 astrologer in Guwahati, which astrologer is best, famous astrologer in Guwahati, astrologer near me Guwahati",
        og_desc="A practical checklist for choosing the best astrologer in Guwahati — what to verify before booking, from credentials to consultation style.",
        body_html=lambda: f'''<p>Type "<strong>best astrologer in Guwahati</strong>" or "<strong>top 10 astrologer in Guwahati</strong>" into Google and you'll get dozens of results — which makes the real question hard to answer: which astrologer is actually best <em>for you</em>? Here's a practical checklist.</p>

        <h2>1. Check Their Area of Expertise</h2>
        <p>"Astrologer" is a broad label. Some specialise in Vedic astrology and Kundli matching, others in tarot, numerology or Vastu. A <a href="{U_HOME}#services">famous astrologer in Guwahati</a> worth consulting should be transparent about exactly which systems they practise and where their strength lies.</p>

        <h2>2. Look for Clear, Specific Answers — Not Vague Statements</h2>
        <p>A skilled astrologer gives specific, grounded observations about your chart or cards, not generic statements that could apply to anyone. If every answer sounds like a horoscope column, that's a red flag.</p>

        <h2>3. Verify How Sessions Are Conducted</h2>
        <p>Since most people today search for an "<strong>astrologer near me</strong>" or "<strong>online astrologer near me</strong>", check whether the astrologer offers proper WhatsApp or video-call consultations rather than only text-based replies — a real conversation lets you ask follow-up questions.</p>

        <h2>4. Ask About Consultation Fees Upfront</h2>
        <p>Transparent, upfront pricing is a sign of professionalism. Read our detailed <a href="{{POST6}}">astrologer fees guide</a> to understand what a fair consultation fee looks like in Guwahati and Assam before you book anywhere.</p>

        <h2>5. Read Genuine Client Feedback</h2>
        <p>Look for reviews that mention specific outcomes — a career decision, a marriage timing question, a Vastu fix — rather than only star ratings with no detail.</p>

        <h2>6. Confidentiality Should Be a Given</h2>
        <p>Your birth details and personal concerns are sensitive. A trustworthy astrologer treats every session as private and judgement-free.</p>

        <h2>7. Check Availability Across Assam, Not Just Guwahati City</h2>
        <p>If you're outside Guwahati, confirm the astrologer genuinely serves your district online. Himu, for example, serves clients across <a href="{U_LOC}">all 35 districts of Assam</a>, from Silchar to Dibrugarh, entirely online.</p>

        <h2>8. Remedies Should Be Practical</h2>
        <p>Be cautious of anyone recommending extremely expensive rituals or "guaranteed" outcomes. Ethical astrology offers guidance and practical remedies — not certainty or fear-based upselling.</p>

        <h2>9. Combined Expertise Adds Value</h2>
        <p>An astrologer who can also read tarot, numerology or Vastu (as needed) often gives a more complete picture than relying on a single system alone.</p>

        <h2>10. Trust Your Own Comfort Level</h2>
        <p>Finally, the "best" astrologer is one you feel comfortable being honest with. A short introductory chat on WhatsApp before booking a full session is a good way to judge this.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">Still deciding?</h2>
            <p>Message Himu directly with your question — no pressure, no obligation to book.</p>
            <div class="cta-buttons">
                <a href="{wa_link("Hello Himu, I have a question before booking a session")}" class="btn-wa" target="_blank" rel="noopener">Ask a Question on WhatsApp →</a>
            </div>
        </div>''',
    ),
    dict(
        slug="astrologer-consultation-fees-guwahati.html", icon="icon-number", svg=SERVICE_CARDS[2][1],
        title="Astrologer Consultation Fees in Guwahati & Assam: What to Expect",
        meta_title="Astrologer Consultation Fees in Guwahati",
        meta="5 min read",
        desc="What does an astrology or tarot session actually cost in Guwahati? A transparent, honest breakdown...",
        keywords="astrologer fees, astrologer fees in India, astrology consultation in Guwahati, astrologer consultation fees Guwahati, fees of astrologer",
        og_desc="A transparent breakdown of typical astrologer and tarot reading consultation fees in Guwahati and across Assam.",
        body_html=lambda: f'''<p>"How much does an astrologer charge?" is one of the most searched questions before booking a session — and one of the least transparently answered. Here's an honest breakdown of <strong>astrologer fees in Guwahati and Assam</strong>.</p>

        <h2>Why Astrology Fees Vary So Much</h2>
        <p>Fees depend on the type of session (tarot vs. full Vedic astrology vs. Vastu), the session length, and the astrologer's experience. A quick 3-card tarot spread naturally costs less than a 60-minute Kundli analysis with Dasha timing and written remedies.</p>

        <h2>Typical Session Types &amp; What They Involve</h2>
        <ul>
            <li><strong>Quick Tarot Reading</strong> — A focused 30-minute session on one specific question (love, career or a decision). See our <a href="{U_HOME}#pricing">current pricing</a> for exact starting rates.</li>
            <li><strong>Full Vedic Birth Chart (Kundli) Reading</strong> — A detailed 60-minute session covering your full chart, Dasha timing and personalised remedies. This is the most popular option for career, marriage and major life questions.</li>
            <li><strong>Combined Session</strong> — Astrology + Numerology + Vastu together, typically for major decisions like marriage, a career shift or moving into a new home.</li>
        </ul>

        <h2>Red Flags to Watch For</h2>
        <p>Be cautious of anyone who won't quote a fee upfront, or who pressures you into expensive "special pujas" or rituals costing thousands of rupees after an initial low-cost or free reading. Ethical astrologers are transparent about pricing from the first message.</p>

        <h2>How to Get an Exact Quote</h2>
        <p>Because the right session type depends on your actual question, the most reliable way to get an accurate fee is to message directly on WhatsApp with what you need — love, career, marriage, or a Vastu review — before booking.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">See transparent pricing</h2>
            <p>View starting prices for tarot, Vedic astrology and combined sessions — final fee confirmed on WhatsApp.</p>
            <div class="cta-buttons">
                <a href="{U_HOME}#pricing" class="btn-wa">View Pricing →</a>
                <a href="{wa_link("Hello Himu, what would a consultation for my situation cost?")}" class="btn-outline" target="_blank" rel="noopener" style="margin-left:10px;">Ask on WhatsApp</a>
            </div>
        </div>

        <p>Not sure which session type fits your situation? Read <a href="{{POST5}}">how to choose the right astrologer in Guwahati</a> for a full checklist before you book.</p>''',
    ),
    dict(
        slug="assamese-astrology-rashifal-guide.html", icon="icon-moon", svg=SERVICE_CARDS[1][1],
        title="Assamese Astrology & Rashifal Explained: Tradition Meets Modern Guidance",
        meta_title="Assamese Astrology & Rashifal Explained",
        meta="6 min read",
        desc="How astrology is practised in Assamese tradition, from Rashifal to Kundli Milan before marriage...",
        keywords="astrologer in Assamese, assamese astrology rashifal, astrologer assamese, assamese astrologer, astrology in Assamese language",
        og_desc="An introduction to Assamese astrology traditions — Rashifal, Kundli Milan and how modern consultations blend both worlds.",
        body_html=lambda: f'''<p>Astrology has deep roots across Assam, woven into local traditions long before online consultations existed. Many clients specifically look for an <strong>astrologer in Assamese</strong> who understands both the technical side of Vedic astrology and the cultural context it's asked in. Here's a look at how the two connect.</p>

        <h2>What Is Rashifal?</h2>
        <p>Rashifal (রাশিফল) refers to horoscope predictions based on your Rashi (moon sign) — a tradition widely followed across Assam through newspapers, almanacs (Panjika) and now, online. Daily and monthly Rashifal readings give a general sense of favourable and challenging periods, though a personalised birth chart reading always goes deeper than a generic sign-based prediction.</p>

        <h2>Kundli Milan Before Assamese Weddings</h2>
        <p>Matching Kundlis (birth charts) before marriage remains an important tradition in many Assamese families. This process, called Kundli Milan or Guna Milan, checks compatibility across factors like temperament, health, and long-term harmony — and also screens for doshas such as Mangal Dosha that families often want addressed with remedies before the wedding date is fixed.</p>

        <h2>Choosing an Auspicious Date (Lagna/Muhurat)</h2>
        <p>Whether it's a wedding, Griha Pravesh (housewarming), or starting a new business, choosing an auspicious date and time — based on planetary positions — is a widely followed practice in Assamese households. A proper Muhurat consultation considers your personal chart alongside the general calendar, rather than relying on the Panjika alone.</p>

        <h2>Consulting in Assamese vs. Hindi vs. English</h2>
        <p>Comfort matters when discussing personal matters like marriage or family conflict. Being able to explain your situation and receive guidance in the language you're most comfortable in — Assamese, Hindi or English — makes a real difference in how clearly a consultation lands. Himu conducts sessions in all three, based on client preference.</p>

        <h2>Bringing Tradition and Modern Consultation Together</h2>
        <p>Today, clients from Guwahati and across <a href="{U_LOC}">every district of Assam</a> — from Barpeta to Sivasagar — can access the same traditional Kundli Milan and Muhurat guidance their families have relied on for generations, now over a simple WhatsApp or video call, without needing to travel.</p>

        <div class="cta" style="margin: 40px 0; padding: 40px 28px;">
            <h2 style="font-size:1.5rem;">Need a Kundli Milan or Muhurat check?</h2>
            <p>Share both birth details on WhatsApp for a traditional matching or date-selection consultation.</p>
            <div class="cta-buttons">
                <a href="{wa_link("Hello Himu, I would like a Kundli Milan / Muhurat consultation")}" class="btn-wa" target="_blank" rel="noopener">Book on WhatsApp →</a>
            </div>
        </div>

        <p>For the fundamentals of how a Kundli itself is read, see our <a href="{{POST4}}">beginner's guide to understanding your birth chart</a>.</p>''',
    ),
]

# Blog posts live under /blog/ — register their slugs before any url() calls resolve them.
BLOG_SLUGS.update(p["slug"] for p in BLOG_POSTS_FULL)

# Resolve cross-post placeholder links ({POST4} etc.) to real URLs, keyed by 1-based order.
_slug_by_index = {i + 1: url(p["slug"]) for i, p in enumerate(BLOG_POSTS_FULL)}
for _p in BLOG_POSTS_FULL:
    _resolved = _p["body_html"]()
    for _i, _u in _slug_by_index.items():
        _resolved = _resolved.replace(f"{{POST{_i}}}", _u)
    _p["body_resolved"] = _resolved

# Legacy-shaped list still used by blog_teaser_section() on the homepage (top 3 posts).
BLOG_POSTS = [
    dict(icon=p["icon"], svg=p["svg"], title=p["title"].replace("&", "&amp;"), href=url(p["slug"]), meta=p["meta"],
         desc=p["desc"], cta="Read More →", live=True)
    for p in BLOG_POSTS_FULL
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
     "Fees vary by session type (tarot, Vedic astrology, numerology or Vastu) and duration. Message Himu on WhatsApp with what you need and the exact price and available slots will be shared before you book. See the full fees breakdown on the blog."),
    ("Is there a good astrologer near me in Guwahati offering online consultations?",
     "Yes — Himu offers online astrologer consultations over WhatsApp voice/video call to clients anywhere in Guwahati and Assam, in addition to in-person sessions at the Krishnanagar studio, so 'astrologer near me' searches from anywhere in the state can be served the same day."),
    ("Is astrology available in Assamese?",
     "Yes — consultations, Kundli explanations and Rashifal guidance are available in Assamese, Hindi or English, based on what you're most comfortable with."),
    ("Who are considered the top astrologers in Guwahati?",
     "There are several practising astrologers in Guwahati; when evaluating who is 'best' for you, look at their area of expertise, transparency on fees, and genuine client feedback. Himu is recognised as one of the top-rated, certified Vedic astrologers and tarot readers in the city — read the full checklist on the blog for what to check before booking any astrologer."),
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

# Real, verified Google reviews (screenshots supplied by the client) — name, star
# rating (out of 5), and the review text (light typo cleanup only, meaning unchanged).
TESTIMONIALS = [
    ("Anna", 5, "Himu pinpointed my exact issues and gave clear, actionable remedies that brought instant clarity. Highly recommend."),
    ("Anita Borah", 4, "Tekhete mur problem khinir solution dile dhoinyabad."),
    ("Tisha Deori", 5, "He is very calm and patiently gives suggestions and answers. He explains everything. Had a nice experience."),
    ("Hirok Deka", 5, "It was really nice talking to you. I got clear answers to all my questions, and the guidance you gave was very helpful. I got the answers I was looking for and had a really good experience... Thank you so much 😊🙏"),
    ("NABA Hz", 5, "It was awesome reading. I have taken readings from him and remedied them and got many benefits. He is a good reader."),
    ("Kuwali Lahkar", 5, "I got all the questions answered. He took so much time to answer the small questions very seriously. Everything he said agreed with me. His patience is much better and he listens to the little things very carefully. Everything he said about me fits nicely. A Facebook friend of mine recommended you and now I will tell everyone about you 😊"),
]

def _stars(n):
    return "★" * n + "☆" * (5 - n)

def testimonials_section(seed=None, subtitle=None):
    items = list(TESTIMONIALS)
    if seed:
        offset = sum(ord(c) for c in seed) % len(items)
        items = items[offset:] + items[:offset]
    items = items[:4]
    sub = subtitle or "Real, verified Google reviews from clients of the best astrologer in Guwahati"
    cards = "\n".join(
        f'''            <div class="testimonial-card">
                <div class="stars">{_stars(stars)}</div>
                <p>&quot;{quote}&quot;</p>
                <p class="client">— {name} <span class="verified">✓ Verified Google Review</span></p>
            </div>''' for name, stars, quote in items
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
            <a href="{U_BLOG}" class="btn-secondary">Read All Articles →</a>
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
        f'''            <a class="location-card" href="{url(href)}">
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
            <a href="{U_LOC}" class="btn-secondary">View All 35 Districts of Assam →</a>
        </div>
    </div>
</section>'''

def towns_section(city_name, district_label, towns, wa_href_base):
    """SEO-safe local coverage block: lists every town/area within the
    district on the existing district page (no thin doorway pages)."""
    if not towns:
        return ""
    from urllib.parse import quote
    chips = "\n".join(
        f'            <a class="town-chip" href="{WA_BASE}?text={quote(f"Hello Himu, I am from {t} and want to book an astrology/tarot session")}" target="_blank" rel="noopener">{t}</a>'
        for t in towns
    )
    town_list_text = ", ".join(towns[:-1]) + (f" and {towns[-1]}" if len(towns) > 1 else towns[0])
    return f'''<section class="towns-section">
    <div class="container">
        <h2 class="section-title">Areas &amp; Towns Covered in {district_label}</h2>
        <p class="section-subtitle">Himu, the best astrologer in {city_name}, also welcomes online &amp; in-person clients from every town and revenue circle across {district_label} — including {town_list_text}.</p>
        <div class="towns-grid">
{chips}
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

{towns_section("Guwahati", "Kamrup Metropolitan", ["North Guwahati", "Dispur", "Dharapur", "Azara", "Chandrapur"], DEFAULT_WA)}

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
{footer()}'''
    html = page_shell(head_extra, body)
    os.makedirs(ROOT, exist_ok=True)
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
            cards.append(f'''            <a class="location-card" href="{url(href)}"{style}>
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
    <link rel="canonical" href="{U_LOC}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Best Astrologer in Assam — All 35 Districts | Himu">
    <meta property="og:description" content="Vedic astrology, tarot, numerology &amp; Vastu consultation from the best astrologer in Assam, across all 35 districts.">
    <meta property="og:url" content="{SITE}/locations.html">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/index.html"},{"@type":"ListItem","position":2,"name":"Areas We Serve","item":f"{SITE}/locations.html"}]}, ensure_ascii=False)}</script>'''

    body = f'''{nav("locations")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="{U_HOME}">Home</a></li>
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

{testimonials_section(subtitle="Real, verified Google reviews from clients across every district of Assam")}

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
def related_posts_block(current_slug, count=2):
    """Internal-linking block appended to every article, pointing to other posts."""
    others = [p for p in BLOG_POSTS_FULL if p["slug"] != current_slug]
    offset = sum(ord(c) for c in current_slug) % max(len(others), 1)
    picked = (others[offset:] + others[:offset])[:count]
    if not picked:
        return ""
    items = "\n".join(f'            <a href="{url(p["slug"])}">{p["title"].replace("&", "&amp;")}</a>' for p in picked)
    return f'''<section class="nearby-section">
    <div class="container">
        <h2>Related Reading</h2>
        <div class="nearby-links">
{items}
            <a href="{U_BLOG}">View All Articles →</a>
        </div>
    </div>
</section>'''

def blog_reading_block(city_name):
    """2 relevant blog links surfaced on district pages for internal linking."""
    offset = sum(ord(c) for c in city_name) % len(BLOG_POSTS_FULL)
    picked = (BLOG_POSTS_FULL[offset:] + BLOG_POSTS_FULL[:offset])[:2]
    items = "\n".join(f'            <a href="{url(p["slug"])}">{p["title"].replace("&", "&amp;")}</a>' for p in picked)
    return f'''<section class="nearby-section">
    <div class="container">
        <h2>Astrology Guides for {city_name} Readers</h2>
        <div class="nearby-links">
{items}
            <a href="{U_BLOG}">Read More on the Blog →</a>
        </div>
    </div>
</section>'''

def build_blog():
    cards = []
    for p in BLOG_POSTS_FULL:
        title_html = p['title'].replace("&", "&amp;")
        cards.append(f'''            <article class="blog-card">
                <div class="icon {p['icon']}"><svg viewBox="0 0 40 40" aria-hidden="true">{p['svg']}</svg></div>
                <span class="tag">{p['meta']}</span>
                <h2><a href="{url(p['slug'])}">{title_html}</a></h2>
                <p>{p['desc']}</p>
                <a href="{url(p['slug'])}" class="read-more">Read More →</a>
            </article>''')

    head_extra = f'''    <title>Astrology &amp; Tarot Blog | Best Astrologer in Guwahati – Himu</title>
    <meta name="description" content="Read the latest articles on tarot reading, Vedic astrology, numerology and Vastu tips from Guwahati's best astrologer, serving all of Assam.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{U_BLOG}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Astrology & Tarot Blog | Best Astrologer in Guwahati">
    <meta property="og:url" content="{SITE}/blog.html">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/index.html"},{"@type":"ListItem","position":2,"name":"Blog","item":f"{SITE}/blog.html"}]}, ensure_ascii=False)}</script>'''

    body = f'''{nav("blog")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="{U_HOME}">Home</a></li>
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
        <div class="view-all-wrap">
            <a href="{U_LOC}" class="btn-secondary">Looking for an Astrologer Near You? View All 35 Districts →</a>
        </div>
    </div>
</section>

{testimonials_section(subtitle="Real, verified Google reviews from readers who booked a session")}

{footer()}'''
    html = page_shell(head_extra, body)
    open(f"{ROOT}/blog.html", "w", encoding="utf-8").write(html)

build_blog()
print("blog.html built")

# ---------------------------------------------------------------
# Blog post pages (generic builder — every post in BLOG_POSTS_FULL)
# ---------------------------------------------------------------
def build_post(p):
    post_url = url(p["slug"])
    plain_title = re.sub("<[^<]+?>", "", p["title"])                       # full title, for JSON-LD + <h1>
    meta_plain = re.sub("<[^<]+?>", "", p.get("meta_title", p["title"]))   # short title, for <title>/OG
    html_title = plain_title.replace("&", "&amp;")
    html_meta_title = meta_plain.replace("&", "&amp;")
    head_extra = f'''    <title>{html_meta_title} | Himu Astrology</title>
    <meta name="description" content="{p['og_desc']}">
    <meta name="keywords" content="{p['keywords']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{post_url}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html_meta_title}">
    <meta property="og:description" content="{p['og_desc']}">
    <meta property="og:url" content="{post_url}">
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/index.html"},{"@type":"ListItem","position":2,"name":"Blog","item":f"{SITE}/blog.html"},{"@type":"ListItem","position":3,"name":plain_title,"item":post_url}]}, ensure_ascii=False)}</script>
    <script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Article","headline":plain_title,"author":{"@type":"Person","name":"Himu"},"publisher":{"@type":"Organization","name":"Himu Astrology - Best Astrologer in Guwahati"},"mainEntityOfPage":post_url,"description":p['og_desc']}, ensure_ascii=False)}</script>'''

    body = f'''{nav("blog")}

<div class="breadcrumb-bar">
    <div class="container">
        <ol>
            <li><a href="{U_HOME}">Home</a></li>
            <li><a href="{U_BLOG}">Blog</a></li>
            <li aria-current="page">{html_title}</li>
        </ol>
    </div>
</div>

<article style="padding: 56px 0 90px;">
    <div class="container post-body">
        <h1>{html_title}</h1>
        <p class="post-meta">By Himu · {p['meta']}</p>

        {p['body_resolved']}
    </div>
</article>

{related_posts_block(p['slug'])}

{testimonials_section(seed=p['slug'], subtitle="Real, verified Google reviews from clients of the best astrologer in Guwahati")}

{footer()}'''
    html = page_shell(head_extra, body)
    os.makedirs(f"{ROOT}/{BLOG_DIR}", exist_ok=True)
    open(f"{ROOT}/{BLOG_DIR}/{p['slug']}", "w", encoding="utf-8").write(html)

for _p in BLOG_POSTS_FULL:
    build_post(_p)
print(f"{len(BLOG_POSTS_FULL)} blog post pages built (in /{BLOG_DIR}/)")

# ---------------------------------------------------------------
# City pages
# ---------------------------------------------------------------
def build_city(slug, d):
    # Computed from SITE + slug (not read from cities_data.json) so it can
    # never drift out of sync if the hosting domain changes.
    canonical_url = url(slug)

    faqs = [(q, a) for q, a in d["faqs"]]
    keyword_spans = "\n".join(f"            <span>{k}</span>" for k in d["keyword_pills"])
    lc_paras = "\n".join(f"            <p>{p}</p>" for p in d["lc_paras"])
    fact_items = "\n".join(f"                <li>{i}</li>" for i in d["fact_items"])
    nearby_links = "\n".join(f'            <a href="{url(href)}">{label}</a>' for href, label in d["nearby"])

    towns = d.get("towns", [])
    towns_label = d.get("towns_district_label", f"{d['city_name']} District")
    towns_keywords = ", ".join(f"astrologer in {t}" for t in towns[:6])
    full_keywords = d["keywords"] + (f", {towns_keywords}" if towns_keywords else "")

    ld_service = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": f"Himu — Best Astrologer in {d['city_name']}",
        "description": d["service_desc"],
        "image": f"{SITE}/og-image.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": "Anandapur Rd, Krishnanagar", "addressLocality": "Guwahati", "addressRegion": "Assam", "postalCode": "781005", "addressCountry": "IN"},
        "areaServed": [{"@type": "City", "name": d["city_name"]}] + [{"@type": "Place", "name": t} for t in towns],
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
    <meta name="keywords" content="{full_keywords}">
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
            <li><a href="{U_HOME}">Home</a></li>
            <li><a href="{U_LOC}">Areas We Serve</a></li>
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

{towns_section(d['city_name'], towns_label, towns, d['wa_href'])}

{why_choose_section()}

{process_section()}

{pricing_section()}

{testimonials_section(d['city_name'], f"Real feedback from clients across {d['city_name']} and Assam who booked the best astrologer in Guwahati")}

{faq_section(f"FAQs — Best Astrologer in {d['city_name']}", faqs)}

{blog_reading_block(d['city_name'])}

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
            <a href="{U_LOC}">View All 35 Districts →</a>
        </div>
    </div>
</section>

{footer()}'''
    html = page_shell(head_extra, body, d["cta_wa"])
    os.makedirs(f"{ROOT}/{DISTRICTS_DIR}", exist_ok=True)
    open(f"{ROOT}/{DISTRICTS_DIR}/{slug}", "w", encoding="utf-8").write(html)

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
    pages = [("index.html", "1.0"), ("locations.html", "0.9"), ("blog.html", "0.7")]
    pages += [(p["slug"], "0.6") for p in BLOG_POSTS_FULL]
    pages += [(slug, "0.8") for slug in DATA.keys()]

    entries = []
    for path, priority in pages:
        loc = url(path)
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

