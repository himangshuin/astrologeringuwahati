# Best Astrologer in Guwahati — Himu Astrology

Celestial-premium themed site (dark cosmic background, warm gold + rose accents,
Fraunces + Manrope typography), covering Guwahati and all 35 districts of Assam
with local SEO content and structured data on every page.

## Folder structure

```
.
├── index.html               → Homepage (Guwahati / Kamrup Metropolitan)
├── locations.html           → "Areas We Serve" hub, all 35 districts
├── blog.html                → Blog index
├── post1.html                → Blog post
├── robots.txt                → Must stay at site root
├── sitemap.xml                → Must stay at site root
├── districts/                → 34 district landing pages
│   ├── best-astrologer-in-barpeta.html
│   ├── best-astrologer-in-silchar.html
│   └── ... (32 more)
├── assets/
│   ├── css/style.css
│   └── js/script.js
├── data/
│   └── cities_data.json      → Single source of truth for all district page content
│                                (copy, meta tags, FAQs, and the towns/sub-areas
│                                covered within each district)
└── scripts/
    ├── generate.py            → Builds the whole site from data/cities_data.json
    └── add_towns.py            → One-off helper that seeded the "towns" field per district
```

**Nothing is ever hand-edited in `index.html`, `locations.html`, or any `districts/*.html`
file** — they're all generated output. Edit `data/cities_data.json` (or the section builders
inside `scripts/generate.py`) and regenerate instead, so every page stays consistent.

## Why this structure

- `districts/` keeps the 34 SEO landing pages out of the repo root so the file listing
  stays scannable, without changing what those URLs mean (still one page per district).
- `assets/` separates CSS/JS from content, the standard convention for static sites.
- `data/` isolates the content model from the templates, so adding a town, a FAQ, or a new
  district is a JSON edit, not an HTML edit.
- `robots.txt` and `sitemap.xml` **must** stay at the repo root — that's a hard requirement
  for search engines to find them via `https://yourdomain/robots.txt`.
- All internal links (nav, footer, breadcrumbs) and asset references (`<link>`, `<script>`)
  are built with `url()` / `asset()` helpers in `generate.py`, so pages resolve correctly
  regardless of how deep they live in the folder tree — no broken links from moving files
  into `districts/`.

## Local SEO coverage

- All 35 districts of Assam are covered: 34 dedicated `districts/*.html` pages + Guwahati
  as the homepage (Kamrup Metropolitan).
- Every district page also lists the smaller towns/revenue circles within that district
  (e.g. Digboi, Naharkatiya, Dergaon) as an on-page "Areas & Towns Covered" section —
  folded into that page's meta keywords and `areaServed` structured data — rather than as
  separate thin pages, which search engines can flag as doorway pages.

## Regenerating the site

```bash
python3 scripts/generate.py
```

This reads `data/cities_data.json`, rebuilds `index.html`, `locations.html`, `blog.html`,
`post1.html`, every file in `districts/`, and refreshes `sitemap.xml` + `robots.txt`.
To add a new district/town, edit `data/cities_data.json` and re-run the script — don't hand-edit
generated HTML, it will be overwritten.

## Deploying

Static site, GitHub Pages compatible. Push everything in this folder to the repo root and
confirm HTTPS/custom domain in GitHub Pages settings. `sitemap.xml` is already
submitted-ready at `/sitemap.xml`.

## Contact

Himu Astrology — Anandapur Rd, Krishnanagar, Guwahati, Assam 781005
Phone/WhatsApp: +91 6901529861 · support@tarotwithhimu.com
