# Tarot With Himu — Site (v4 redesign)

**Celestial-premium redesign** — dark cosmic theme (deep ink background, warm gold + rose accents),
Fraunces + Manrope typography, fully responsive with a mobile slide-in nav.

All SEO content from the previous version is preserved and carried over:
- Unique title/meta description/keywords per page
- ProfessionalService, FAQPage and BreadcrumbList JSON-LD structured data on every page
- Local landmark/fact content for all 34 Assam district pages (not thin/duplicate content)
- sitemap.xml (38 URLs) and robots.txt unchanged in structure, still valid

## What changed in this redesign
- Full visual overhaul: dark "celestial premium" theme replacing the previous warm-ivory palette
- New typography pairing (Fraunces display + Manrope body)
- Redesigned navigation with a working mobile hamburger menu + slide-in panel
- Redesigned cards, buttons, FAQ accordions, CTA bands, and location grids
- theme-color meta tag, twitter:card upgraded to summary_large_image, robots meta added per page
- style.css and script.js rewritten; site structure/URLs unchanged so nothing breaks in Search Console

## Regenerating the site
The homepage, locations hub, blog, blog post, and all 34 city pages are produced by
`generate.py`, which reads city data from `cities_data.json` (extracted from the previous
version so no local SEO content was lost). To change copy or add a new town:
1. Edit `cities_data.json` (or regenerate it from source HTML via `extract.py`)
2. Re-run `python3 generate.py`
3. Commit the new HTML + sitemap.xml if URLs changed

## Deploying
Static site, GitHub Pages compatible. Push all files to the repo root and confirm the
custom domain `tarotwithhimu.com` + HTTPS in GitHub Pages settings. Sitemap is already
submitted-ready at `/sitemap.xml`.

## Contact
Tarot With Himu — Anandapur Rd, Krishnanagar, Guwahati, Assam 781005
Phone/WhatsApp: +91 6901529861 · support@tarotwithhimu.com
