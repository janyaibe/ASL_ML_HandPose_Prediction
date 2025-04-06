import cv2
import sqlite3
import argparse
import mediapipe as mp
import os

# === SETUP MEDIAPIPE HAND DETECTION ===
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# === CONNECT TO DATABASE ===
DB_PATH = "data/database.db"
def connect_db():
    return sqlite3.connect(DB_PATH)

# === PROCESS VIDEO FILE ===
def process_video(video_path):
    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        return

    video_name = os.path.basename(video_path)
    cap = cv2.VideoCapture(video_path)
    frame_number = 0

    conn = connect_db()
    cursor = conn.cursor()

    print(f"🚀 Processing {video_name}...")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i, lm in enumerate(hand_landmarks.landmark):
                    cursor.execute("""
                        INSERT INTO hand_landmarks (video_name, frame_number, landmark_index, x, y, z)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (video_name, frame_number, i, lm.x, lm.y, lm.z))

        frame_number += 1

    conn.commit()
    conn.close()
    cap.release()
    print(f"✅ Finished processing {video_name}. {frame_number} frames analyzed.")

# === MAIN ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract hand landmarks from video and store in SQLite DB.")
    parser.add_argument("--video", required=True, help="Path to the video file")
    args = parser.parse_args()

    process_video(args.video)
