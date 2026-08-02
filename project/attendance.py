"""
attendance.py
-------------
Attendance CSV me mark karne ke helper functions.
Har din ke liye alag CSV file banti hai: attendance_logs/2026-08-02.csv
Ek person ek din me sirf ek baar mark hota hai.
"""

import os
import csv
from datetime import datetime
from config import ATTENDANCE_DIR


def _today_file():
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(ATTENDANCE_DIR, f"{today}.csv")


def _already_marked(name, filepath):
    if not os.path.exists(filepath):
        return False
    with open(filepath, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if row and row[0] == name:
                return True
    return False


def mark_attendance(name):
    """
    Diye gaye naam ke liye attendance mark karta hai (agar aaj already
    mark nahi hui hai). Return True agar naya entry hua, False agar
    already marked tha.
    """
    filepath = _today_file()
    file_exists = os.path.exists(filepath)

    if _already_marked(name, filepath):
        return False

    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Time", "Date"])
        now = datetime.now()
        writer.writerow([name, now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d")])

    return True
