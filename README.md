# PosterGen: 
A Basic Mood Palette & Template Poster Generator

## Problem
Designers and marketers often need to quickly generate visually appealing posters that match a specific mood or campaign theme. Manually selecting color palettes and templates is time-consuming and subjective.

## Approach
This app uses natural language processing (TF-IDF), template family prediction, and mood-to-palette mapping to recommend and dynamically generate poster previews. Users enter a caption, and the app:
- Extracts keywords from the caption
- Predicts the best template family
- Maps mood words to color palettes
- Dynamically customizes SVG templates with the caption and palette colors

## Metrics
- **Instant feedback:** Poster preview updates in real time as you type
- **Template coverage:** Supports 12+ template families and palettes
- **Customization:** SVGs are dynamically filled with user text and colors

---

## Project Structure
```
assets/
  palette_catalog.md         # Color palette catalog (Markdown)
  template_catalog.md        # Template catalog (Markdown)
  *.svg                      # SVG template files (with placeholders)
backend/
  mood_palette_mapper.py     # Palette-mood mapping logic
  palette_showcase.py        # Palette showcase logic
  template_family_model.py   # Template family model
  tfidf_extractor.py         # TF-IDF feature extraction
streamlit_app/
  app.py                     # Main Streamlit app
database/
  schema.sql                 # Database schema
  seed.sql                   # Seed data
README.md
```

## Requirements
- Python 3.8+
- Streamlit
- pandas, numpy, scikit-learn


Install requirements:
```sh
pip install streamlit pandas numpy scikit-learn
```

## Important Notes

- **Run the app from the project root directory** (the folder containing `streamlit_app/`, `backend/`, etc.), not from inside `streamlit_app`. This ensures Python can find the `backend` package.
- The `backend` directory is a Python package (it contains an `__init__.py` file). Do not remove this file.
- If you get `ModuleNotFoundError: No module named 'backend'`, make sure you are running the app from the project root and not from within a subfolder.
- The app automatically adjusts `sys.path` to help with imports, but running from the root is still recommended.



## Running the App
1. Ensure all requirements are installed.
2. Place SVG template files in the `assets/` folder (see below for format).
3. **From the project root directory**, start the app:
   ```sh
   streamlit run streamlit_app/app.py
   ```
4. Open your browser to [http://localhost:8501](http://localhost:8501)

## Troubleshooting

- **ModuleNotFoundError: No module named 'backend'**
  - Make sure you are running the command from the project root directory.
  - Ensure `backend/__init__.py` exists.
  - If using a virtual environment, activate it before running Streamlit.
  - If you still have issues, try running:
    ```sh
    python -m streamlit run streamlit_app/app.py
    ```


## Database Setup (Optional)
- To use the provided schema and seed data, set up a SQLite database using `database/schema.sql` and `database/seed.sql`.

---

## SVG Template Format (for Customization)

SVG files should use placeholders for dynamic content. The app will replace these with the user's caption and palette colors. Example SVG:

```xml
<svg width="600" height="800" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{{bg_color}}"/>
  <ellipse cx="150" cy="200" rx="120" ry="60" fill="{{accent1}}"/>
  <text x="50%" y="120" text-anchor="middle" font-size="48" fill="{{headline_color}}">{{headline}}</text>
  <rect x="200" y="700" width="200" height="60" rx="20" fill="{{cta_bg}}"/>
  <text x="300" y="740" text-anchor="middle" font-size="32" fill="{{cta_color}}">{{cta}}</text>
</svg>
```

**Supported placeholders:**
- `{{bg_color}}`, `{{accent1}}`, `{{accent2}}`, `{{accent3}}`, `{{headline_color}}`, `{{cta_bg}}`, `{{cta_color}}`, `{{headline}}`, `{{cta}}`

You can upload your own SVGs using these placeholders, or update existing SVGs to match this format for full customization.
