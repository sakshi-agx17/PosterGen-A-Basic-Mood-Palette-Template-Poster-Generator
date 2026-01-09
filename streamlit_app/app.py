
# Streamlit UI 
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.tfidf_extractor import TfidfKeywordExtractor
from backend.template_family_model import TemplateFamilyModel
from backend.mood_palette_mapper import map_moods_to_palettes
from backend.palette_showcase import show_palette_swatches, generate_palette_variation

# Example training data for the model
captions = [
    "playful spring sale", "bold summer event", "elegant winter gala", "retro pop party",
    "tech future expo", "calm nature retreat", "urban night market", "cozy autumn fair"
]
families = [
    "Playful", "Bold", "Elegant", "Retro",
    "Tech", "Calm", "Modern", "Warm"
]

# Initialize extractors and model
extractor = TfidfKeywordExtractor()
model = TemplateFamilyModel(captions, families)

st.title("PosterGen: Mood Palette & Template Poster Generator")
st.write("Paste a short brief (e.g., 'playful spring sale') and get a poster template + palette ranked by predicted fit.")

caption = st.text_input("Enter your caption:", "playful spring sale")

if caption:
    # Extract keywords
    keywords = extractor.extract_keywords(caption)
    st.write(f"**Extracted keywords:** {keywords}")

    # Predict template family
    family = model.predict_family(caption)
    st.write(f"**Predicted template family:** {family}")

    # Map mood words to palettes
    palettes = map_moods_to_palettes(keywords)
    st.write(f"**Matching palettes:** {palettes if palettes else 'No direct palette match'}")

    # Generative Variation Section
    st.subheader("🎨 Generative Variation")
    if st.button("Generate Palette Variation"):
        variation = generate_palette_variation(family, keywords, palettes)
        if variation:
            st.write("**Generated Palette Variation:**")
            st.write(variation)
            show_palette_swatches([variation])
        else:
            st.write("No generative variation could be created.")
    else:
        show_palette_swatches(palettes)

    # Show template and palette preview
    import os
    from PIL import Image
    import streamlit.components.v1 as components

    # Try to display the SVG template for the predicted family
    template_file = None
    template_map = {
        "Playful": "playful_spring.svg",
        "Bold": "bold_sale.svg",
        "Elegant": "elegant_minimal.svg",
        "Modern": "modern_grid.svg",
        "Retro": "retro_pop.svg",
        "Classic": "classic_frame.svg",
        "Calm": "calm_nature.svg",
        "Warm": "cozy_autumn.svg",
        "Tech": "tech_future.svg",
        "Artistic": "artistic_collage.svg",
        "Youthful": "youthful_burst.svg",
        "Urban": "urban_night.svg"
    }
    # Find the template SVG file
    if family in template_map:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_path = os.path.join(base_dir, "assets", template_map[family])
        if os.path.exists(template_path):
            with open(template_path, "r") as f:
                svg_content = f.read()

            # --- Dynamic SVG Customization ---
            palette_name = palettes[0] if palettes else None
            from backend.palette_showcase import palette_colors
            colors = palette_colors.get(palette_name, ["#FDE68A", "#A7F3D0", "#F59E42", "#F472B6", "#F9F6F0"])
            # Map colors to SVG placeholders
            color_map = {
                "{{bg_color}}": colors[0],
                "{{accent1}}": colors[1] if len(colors) > 1 else colors[0],
                "{{accent2}}": colors[2] if len(colors) > 2 else colors[0],
                "{{accent3}}": colors[3] if len(colors) > 3 else colors[0],
                "{{headline_color}}": "#22223B",
                "{{cta_bg}}": colors[4] if len(colors) > 4 else colors[0],
                "{{cta_color}}": "#fff"
            }
            # Replace color placeholders
            for k, v in color_map.items():
                svg_content = svg_content.replace(k, v)
            # Replace text placeholders
            svg_content = svg_content.replace("{{headline}}", caption.title())
            svg_content = svg_content.replace("{{cta}}", "Shop Now")
            st.write("**Template Preview:**")
            components.html(svg_content, height=400)
        else:
            st.info(f"SVG template not found: {template_map[family]}")
    else:
        st.info("No template preview available for this family.")