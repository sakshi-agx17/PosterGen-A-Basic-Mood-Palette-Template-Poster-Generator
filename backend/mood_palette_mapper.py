# Mood to Palette Mapper

MOOD_TO_PALETTE = {
    'spring': 'Spring Fling',
    'playful': 'Spring Fling',
    'bold': 'Bold Sunset',
    'energetic': 'Bold Sunset',
    'elegant': 'Elegant Pearl',
    'minimal': 'Elegant Pearl',
    'modern': 'Modern Neon',
    'tech': 'Modern Neon',
    'retro': 'Retro Pop',
    'fun': 'Retro Pop',
    'classic': 'Classic Gold',
    'luxury': 'Classic Gold',
    'youth': 'Youthful Burst',
    'calm': 'Calm Forest',
    'nature': 'Calm Forest',
    'urban': 'Urban Night',
    'night': 'Urban Night',
    'warm': 'Cozy Autumn',
    'autumn': 'Cozy Autumn',
    'cool': 'Tech Blue',
    'artistic': 'Artistic Mix',
    'creative': 'Artistic Mix',
}

def map_moods_to_palettes(keywords):
    palettes = set()
    for word in keywords:
        palette = MOOD_TO_PALETTE.get(word.lower())
        if palette:
            palettes.add(palette)
    return list(palettes)

if __name__ == "__main__":
    keywords = ['playful', 'spring', 'bright']
    print("Matching palettes:", map_moods_to_palettes(keywords))
