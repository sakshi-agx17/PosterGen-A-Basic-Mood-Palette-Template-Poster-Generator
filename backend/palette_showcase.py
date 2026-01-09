import random
import streamlit as st
import colorsys

# Example palette color
palette_colors = {
    "Spring Fling": ["#FDE68A", "#A7F3D0", "#F59E42", "#F472B6", "#F9F6F0"],
    "Bold Sunset": ["#FF5E13", "#FFB800", "#FFD6A5", "#FF006E", "#8338EC"],
    "Elegant Pearl": ["#F8F9FA", "#E9ECEF", "#CED4DA", "#495057", "#B197FC"],
    "Modern Neon": ["#0AFFEF", "#1B1B1B", "#F5F5F5", "#FF61A6", "#00B4D8"],
    "Retro Pop": ["#F72585", "#B5179E", "#7209B7", "#3A0CA3", "#4361EE"],
    "Classic Gold": ["#FFD700", "#FFF8DC", "#BDB76B", "#8B8000", "#F5DEB3"],
    "Youthful Burst": ["#FFB5E8", "#B28DFF", "#AFF8DB", "#FFFFB5", "#FFABAB"],
    "Calm Forest": ["#A3C9A8", "#84B59F", "#69A297", "#50808E", "#3A606E"],
    "Urban Night": ["#22223B", "#4A4E69", "#9A8C98", "#C9ADA7", "#F2E9E4"],
    "Cozy Autumn": ["#FFB385", "#FF7F51", "#CE4257", "#6D6875", "#B5EAD7"],
    "Tech Blue": ["#00B4D8", "#48CAE4", "#90E0EF", "#CAF0F8", "#03045E"],
    "Artistic Mix": ["#F6E7CB", "#E2CFC3", "#B6B6B6", "#A2A2A1", "#7D7D7D"]
}

def show_palette_swatches(palettes):
    # display color swatches for each palette
    if not palettes:
        st.write("No palettes to display.")
        return
    for palette in palettes:
        st.write(f"Palette: {palette}")
        cols = st.columns(len(palette))
        for idx, color in enumerate(palette):
            with cols[idx]:
                st.markdown(
                    f'<div style="width:40px;height:40px;background:{color};border-radius:5px;border:1px solid #ccc"></div>',
                    unsafe_allow_html=True
                )

def generate_palette_variation(family, keywords, palettes):
    # Generate a slight variation of an existing palette
    def mutate_palette(palette):
        new_palette = []
        for color in palette:
            if not isinstance(color, str):
                new_palette.append('#{:06x}'.format(random.randint(0, 0xFFFFFF)))
                continue
            color = color.lstrip('#')
            lv = len(color)
            # Only process valid 6-character hex colors
            if lv != 6 or any(c not in '0123456789abcdefABCDEF' for c in color):
                new_palette.append('#{:06x}'.format(random.randint(0, 0xFFFFFF)))
                continue
            try:
                rgb = tuple(int(color[i:i + 2], 16) / 255.0 for i in range(0, 6, 2))
                h, l, s = colorsys.rgb_to_hls(*rgb)
                h = (h + random.uniform(-0.05, 0.05)) % 1.0
                r, g, b = colorsys.hls_to_rgb(h, l, s)
                new_palette.append('#{:02x}{:02x}{:02x}'.format(int(r*255), int(g*255), int(b*255)))
            except Exception:
                new_palette.append('#{:06x}'.format(random.randint(0, 0xFFFFFF)))
        # If the palette is empty or all invalid, return a random palette
        if not new_palette:
            return ['#{:06x}'.format(random.randint(0, 0xFFFFFF)) for _ in range(5)]
        return new_palette

    # ensure palettes is a non-empty list of non-empty lists
    if not palettes or not any(pal and isinstance(pal, (list, tuple)) and len(pal) > 0 for pal in palettes):
        # Generate a random palette if none exist
        def random_color():
            return '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        return [random_color() for _ in range(5)]
    # Pick a palette that is not empty
    valid_palettes = [pal for pal in palettes if pal and isinstance(pal, (list, tuple)) and len(pal) > 0]
    base_palette = random.choice(valid_palettes)
    #if base_palette is empty, use a random palette
    if not base_palette:
        return ['#{:06x}'.format(random.randint(0, 0xFFFFFF)) for _ in range(5)]
    return mutate_palette(base_palette)