-- Sample data for templates, palettes, and mood-to-palette mappings

-- Templates
INSERT INTO templates (name, family, description, file_name) VALUES
('Playful Spring', 'Playful', 'Wavy shapes, large headline, flower icons', 'playful_spring.svg'),
('Bold Sale', 'Bold', 'Thick borders, big hero, strong CTA', 'bold_sale.svg'),
('Elegant Minimal', 'Elegant', 'Thin lines, lots of whitespace, serif font', 'elegant_minimal.svg'),
('Modern Grid', 'Modern', 'Grid layout, geometric shapes, sans-serif', 'modern_grid.svg'),
('Retro Pop', 'Retro', 'Dotted background, pop-art colors, fun font', 'retro_pop.svg'),
('Classic Frame', 'Classic', 'Ornate border, centered headline, gold accent', 'classic_frame.svg'),
('Youthful Burst', 'Playful', 'Starbursts, playful font, angled text', 'youthful_burst.svg'),
('Calm Nature', 'Calm', 'Leaf icons, soft colors, gentle curves', 'calm_nature.svg'),
('Urban Night', 'Modern', 'Dark background, neon lines, cityscape', 'urban_night.svg'),
('Cozy Autumn', 'Warm', 'Warm palette, leaf icons, hand-drawn look', 'cozy_autumn.svg'),
('Tech Future', 'Tech', 'Futuristic lines, blue palette, digital font', 'tech_future.svg'),
('Artistic Collage', 'Artistic', 'Torn paper edges, mixed media, layered look', 'artistic_collage.svg');

-- Palettes
INSERT INTO palettes (name, moods, colors) VALUES
('Spring Fling', 'spring,playful', '#FDE68A,#A7F3D0,#F59E42,#F472B6,#F9F6F0'),
('Bold Sunset', 'bold,energetic', '#FF5E13,#FFB800,#FFD6A5,#FF006E,#8338EC'),
('Elegant Pearl', 'elegant,minimal', '#F8F9FA,#E9ECEF,#CED4DA,#495057,#B197FC'),
('Modern Neon', 'modern,tech', '#0AFFEF,#1B1B1B,#F5F5F5,#FF61A6,#00B4D8'),
('Retro Pop', 'retro,fun', '#F72585,#B5179E,#7209B7,#3A0CA3,#4361EE'),
('Classic Gold', 'classic,luxury', '#FFD700,#FFF8DC,#BDB76B,#8B8000,#F5DEB3'),
('Youthful Burst', 'playful,youth', '#FFB5E8,#B28DFF,#AFF8DB,#FFFFB5,#FFABAB'),
('Calm Forest', 'calm,nature', '#A3C9A8,#84B59F,#69A297,#50808E,#3A606E'),
('Urban Night', 'modern,urban,night', '#22223B,#4A4E69,#9A8C98,#C9ADA7,#F2E9E4'),
('Cozy Autumn', 'warm,autumn', '#FFB385,#FF7F51,#CE4257,#6D6875,#B5EAD7'),
('Tech Blue', 'tech,cool', '#00B4D8,#48CAE4,#90E0EF,#CAF0F8,#03045E'),
('Artistic Mix', 'artistic,creative', '#F6E7CB,#E2CFC3,#B6B6B6,#A2A2A1,#7D7D7D');

-- Example for Mood to Palette Mapping
INSERT INTO mood_palette_map (mood, palette_id) VALUES
('spring', 1),
('playful', 1),
('bold', 2),
('energetic', 2),
('elegant', 3),
('minimal', 3),
('modern', 4),
('tech', 4),
('retro', 5),
('fun', 5),
('classic', 6),
('luxury', 6),
('youth', 7),
('calm', 8),
('nature', 8),
('urban', 9),
('night', 9),
('warm', 10),
('autumn', 10),
('cool', 11),
('artistic', 12),
('creative', 12);
