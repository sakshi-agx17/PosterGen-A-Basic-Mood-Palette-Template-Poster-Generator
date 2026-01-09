-- Database Schema for Template and Palette Management

-- Table: templates
CREATE TABLE IF NOT EXISTS templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    family TEXT NOT NULL,
    description TEXT,
    file_name TEXT NOT NULL
);

-- Table: palettes
CREATE TABLE IF NOT EXISTS palettes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    moods TEXT NOT NULL, -- comma-separated moods
    colors TEXT NOT NULL -- comma-separated hex codes
);

-- Table: template_palette_map
CREATE TABLE IF NOT EXISTS template_palette_map (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    template_id INTEGER NOT NULL,
    palette_id INTEGER NOT NULL,
    FOREIGN KEY (template_id) REFERENCES templates(id),
    FOREIGN KEY (palette_id) REFERENCES palettes(id)
);

-- Table: mood_palette_map
CREATE TABLE IF NOT EXISTS mood_palette_map (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mood TEXT NOT NULL,
    palette_id INTEGER NOT NULL,
    FOREIGN KEY (palette_id) REFERENCES palettes(id)
);
