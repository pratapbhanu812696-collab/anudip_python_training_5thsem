"""
main.py
-------
Live webcam feed se faces detect + recognize karta hai aur
match hone par automatically attendance mark karta hai.

Run:
    python main.py

Pehle yeh run kar chuke ho:
    python register_face.py   -> naya face register karne ke liye
    python encode_faces.py    -> registered faces ki encodings banane ke liye
"""

import os
import pickle
import cv2
import face_recognition
import numpy as np

from config import (
    ENCODINGS_FILE,
    CAMERA_INDEX,
    FRAME_RESIZE_SCALE,
    FACE_MATCH_TOLERANCE,
)
from attendance import mark_attendance


def load_encodings():
    if not os.path.exists(ENCODINGS_FILE):
        print("Encodings file nahi mili. Pehle 'python encode_faces.py' chalayein.")
        return None
    with open(ENCODINGS_FILE, "rb") as f:
        return pickle.load(f)


def run_attendance_system():
    data = load_encodings()
    if data is None:
        return

    known_encodings = data["encodings"]
    known_names = data["names"]

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("Camera open nahi ho paaya. CAMERA_INDEX check karein.")
        return

    print("[INFO] Attendance system chalu ho gaya. 'q' dabaye band karne ke liye.\n")

    marked_this_session = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=FRAME_RESIZE_SCALE, fy=FRAME_RESIZE_SCALE)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for encoding, location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(
                known_encodings, encoding, tolerance=FACE_MATCH_TOLERANCE
            )
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_names[best_match_index]

            # scale face location back up since frame was resized
            top, right, bottom, left = location
            scale = int(1 / FRAME_RESIZE_SCALE)
            top, right, bottom, left = top * scale, right * scale, bottom * scale, left * scale

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), color, cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

            if name != "Unknown" and name not in marked_this_session:
                was_marked = mark_attendance(name)
                marked_this_session.add(name)
                if was_marked:
                    print(f"[ATTENDANCE MARKED] {name}")
                else:
                    print(f"[ALREADY MARKED TODAY] {name}")

        cv2.imshow("Face Recognition Attendance System - press 'q' to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_attendance_system()
