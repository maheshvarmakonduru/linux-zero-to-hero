# Slides — Quick Review Material

This folder contains short slide-style lesson notes and a combined presentation deck (`deck.md`).

- `01-introduction.md`: course intro and learning path
- `deck.md`: single-file Reveal.js-compatible slide deck for presentations

Render locally (two quick options):

1) `reveal-md` (recommended, live reload):

```bash
npx reveal-md slides/deck.md --theme beige
```

Install globally with `npm install -g reveal-md` if you prefer.

2) `pandoc` → HTML (static export):

```bash
pandoc -t revealjs -s slides/deck.md -o slides/deck.html
```

Open `slides/deck.html` in a browser.

Speaker notes & assets

Speaker notes are supported via `<aside class="notes">...</aside>` in the deck; use the `s` key in Reveal.js to open presenter view.
Add images to `slides/assets/` and reference them with markdown: `![alt](assets/my-image.png)`.

Example assets included (placeholders):
 - slides/assets/terminal.svg — terminal snapshot (SVG)
 - slides/assets/terminal.gif — placeholder GIF file (replace with a real GIF for live demos)
 - slides/assets/architecture.svg — architecture visual

Keep images under 3MB for fast live demos.

Tips

- To regenerate the static preview (used earlier): `npx --yes reveal-md slides/deck.md --theme beige --static slides/deck_static && cp -r slides/deck_static slides/deck_html_preview`.
- Replace `terminal.gif` with a short terminal-recording GIF for live workshop demos.
