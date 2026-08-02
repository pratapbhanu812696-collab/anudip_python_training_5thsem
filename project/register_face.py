"""
register_face.py
-----------------
Naya student/employee register karne ke liye webcam se unke
face ke multiple photos capture karta hai aur dataset/<name>/
folder me save karta hai.

Run:
    python register_face.py
"""

import os
import cv2
from config import DATASET_DIR, CAMERA_INDEX


def register_new_face():
    name = input("Naam / ID enter karein (e.g. Rahul_101): ").strip()
    if not name:
        print("Naam khali nahi ho sakta.")
        return

    person_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(person_dir, exist_ok=True)

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("Camera open nahi ho paaya. CAMERA_INDEX check karein.")
        return

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    print("\n[INFO] Camera on ho gaya hai.")
    print("[INFO] 'c' dabaye photo capture karne ke liye, 'q' dabaye exit karne ke liye.")
    print("[INFO] Kam se kam 10-15 photos alag angles/expressions me capture karein.\n")

    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame, f"Captured: {count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Register Face - press 'c' to capture, 'q' to quit", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c') and len(faces) > 0:
            count += 1
            img_path = os.path.join(person_dir, f"{name}_{count}.jpg")
            cv2.imwrite(img_path, frame)
            print(f"[SAVED] {img_path}")
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if count == 0:
        print("Koi photo capture nahi hui. Folder delete kar rahe hain.")
        os.rmdir(person_dir)
    else:
        print(f"\n[DONE] {count} photos '{name}' ke liye save ho gayi.")
        print("Ab 'python encode_faces.py' run karein taaki encodings ban jaye.")


if __name__ == "__main__":
    register_new_face()
