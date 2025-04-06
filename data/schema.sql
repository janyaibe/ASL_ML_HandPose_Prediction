-- Table for storing hand landmark data per video frame
CREATE TABLE IF NOT EXISTS hand_landmarks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_name TEXT NOT NULL,
    frame_number INTEGER NOT NULL,
    landmark_index INTEGER NOT NULL,  -- 0–20 for MediaPipe landmarks
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing predictions made by the ML model
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_name TEXT NOT NULL,
    frame_number INTEGER NOT NULL,
    predicted_letter TEXT NOT NULL,
    confidence_score REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
