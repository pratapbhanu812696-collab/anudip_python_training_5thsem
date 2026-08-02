"""
encode_faces.py
----------------
dataset/ folder ke andar har person ki images padhta hai,
face_recognition library se 128-d encoding banata hai,
aur encodings/encodings.pkl me save karta hai.

Run:
    python encode_faces.py
"""

import os
import pickle
import face_recognition
from config import DATASET_DIR, ENCODINGS_FILE


def encode_known_faces():
    known_encodings = []
    known_names = []

    people = [p for p in os.listdir(DATASET_DIR)
              if os.path.isdir(os.path.join(DATASET_DIR, p))]

    if not people:
        print("dataset/ folder khali hai. Pehle 'python register_face.py' chalayein.")
        return

    for person_name in people:
        person_dir = os.path.join(DATASET_DIR, person_name)
        image_files = [f for f in os.listdir(person_dir)
                       if f.lower().endswith((".jpg", ".jpeg", ".png"))]

        print(f"[PROCESSING] {person_name} ({len(image_files)} images)")

        for image_file in image_files:
            image_path = os.path.join(person_dir, image_file)
            image = face_recognition.load_image_file(image_path)

            boxes = face_recognition.face_locations(image, model="hog")
            encodings = face_recognition.face_encodings(image, boxes)

            for encoding in encodings:
                known_encodings.append(encoding)
                known_names.append(person_name)

    data = {"encodings": known_encodings, "names": known_names}
    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(data, f)

    print(f"\n[DONE] {len(known_encodings)} face encodings save ho gaye -> {ENCODINGS_FILE}")


if __name__ == "__main__":
    encode_known_faces()
