import os

# ---------- Base Directories ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_DIR = os.path.join(BASE_DIR, "dataset")          # captured face images
ENCODINGS_DIR = os.path.join(BASE_DIR, "encodings")       # stored encodings.pkl
ATTENDANCE_DIR = os.path.join(BASE_DIR, "attendance_logs")  # daily CSV logs

ENCODINGS_FILE = os.path.join(ENCODINGS_DIR, "encodings.pkl")

# ---------- Camera Settings ----------
CAMERA_INDEX = 0          # 0 = default webcam, change if you have multiple cameras
FRAME_RESIZE_SCALE = 0.25  # smaller = faster face detection, less accurate

# ---------- Recognition Settings ----------
FACE_MATCH_TOLERANCE = 0.5  # lower = stricter match (0.4 - 0.6 is a good range)

# create required folders if they don't exist
for folder in (DATASET_DIR, ENCODINGS_DIR, ATTENDANCE_DIR):
    os.makedirs(folder, exist_ok=True)
