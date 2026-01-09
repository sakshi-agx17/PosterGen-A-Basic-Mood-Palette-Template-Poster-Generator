# Poster Template Catalog

This file documents the initial set of poster templates for the recommender system. Each template is a simple SVG/PNG frame with a defined family and layout description.

| Template Name      | Family    | Description                                   | File Name           |
|--------------------|-----------|-----------------------------------------------|---------------------|
| Playful Spring     | Playful   | Wavy shapes, large headline, flower icons     | playful_spring.svg  |
| Bold Sale          | Bold      | Thick borders, big hero, strong CTA           | bold_sale.svg       |
| Elegant Minimal    | Elegant   | Thin lines, lots of whitespace, serif font    | elegant_minimal.svg |
| Modern Grid        | Modern    | Grid layout, geometric shapes, sans-serif     | modern_grid.svg     |
| Retro Pop          | Retro     | Dotted background, pop-art colors, fun font   | retro_pop.svg       |
| Classic Frame      | Classic   | Ornate border, centered headline, gold accent | classic_frame.svg   |
| Youthful Burst     | Playful   | Starbursts, playful font, angled text         | youthful_burst.svg  |
| Calm Nature        | Calm      | Leaf icons, soft colors, gentle curves        | calm_nature.svg     |
| Urban Night        | Modern    | Dark background, neon lines, cityscape        | urban_night.svg     |
| Cozy Autumn        | Warm      | Warm palette, leaf icons, hand-drawn look     | cozy_autumn.svg     |
| Tech Future        | Tech      | Futuristic lines, blue palette, digital font  | tech_future.svg     |
| Artistic Collage   | Artistic  | Torn paper edges, mixed media, layered look   | artistic_collage.svg|

## Things to remember
- SVG/PNG files stored in `assets/` folder.
- Each template should have a transparent area for hero image, headline, and CTA.

## Example SVG Template (Playful Spring)
```svg
<svg width="600" height="800" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#F9F6F0"/>
  <ellipse cx="150" cy="200" rx="120" ry="60" fill="#FDE68A"/>
  <ellipse cx="450" cy="600" rx="100" ry="50" fill="#A7F3D0"/>
  <text x="50%" y="120" text-anchor="middle" font-size="48" font-family="Comic Sans MS, cursive" fill="#F59E42">Headline</text>
  <circle cx="500" cy="100" r="30" fill="#F472B6"/>
  <rect x="200" y="700" width="200" height="60" rx="20" fill="#F59E42"/>
  <text x="300" y="740" text-anchor="middle" font-size="32" font-family="Arial" fill="#fff">CTA</text>
</svg>
```