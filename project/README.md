# Face Recognition Attendance System

Python + OpenCV + `face_recognition` library se bana ek simple
attendance system jo webcam se face pehchan kar attendance CSV
file me mark karta hai.

## Project Structure
```
face_attendance_system/
├── config.py            # settings (camera index, tolerance, paths)
├── register_face.py      # naya face register karne ke liye (webcam se photos)
├── encode_faces.py       # registered photos se face encodings banata hai
├── attendance.py          # attendance CSV me mark karne ka logic
├── main.py                # live recognition + attendance marking
├── requirements.txt
├── dataset/                # har person ke folder me unki photos
├── encodings/              # encodings.pkl yaha save hoti hai
└── attendance_logs/        # roz ki attendance CSV files
```

## VS Code me Setup

1. **Folder open karein**
   VS Code me `File > Open Folder` se `face_attendance_system` folder open karein.

2. **Python extension install karein**
   VS Code Extensions (Ctrl+Shift+X) me "Python" (by Microsoft) search karke install karein.

3. **Virtual environment banayein** (recommended)
   VS Code ka integrated terminal open karein (`` Ctrl+` ``) aur run karein:
   ```bash
   python -m venv venv
   ```
   Activate karein:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

   VS Code neeche-right corner me interpreter select karne ka prompt dega —
   `venv` wala interpreter select karein.

4. **Dependencies install karein**
   ```bash
   pip install -r requirements.txt
   ```

   > **Note (dlib install issues):** `face_recognition` library `dlib` par depend
   > karti hai jise install karne ke liye CMake aur C++ build tools chahiye.
   > - **Windows:** Pehle [CMake](https://cmake.org/download/) install karein aur
   >   "Visual Studio Build Tools" (C++ workload ke saath) install karein. Fir upar
   >   wala pip command chalayein. Agar phir bhi error aaye to
   >   `pip install dlib-binary` try karein ya conda use karein:
   >   `conda install -c conda-forge dlib`.
   > - **macOS:** `brew install cmake` chalayein pehle.
   > - **Linux:** `sudo apt install cmake build-essential` chalayein pehle.

5. **Webcam permission**
   Apne OS me VS Code/Terminal ko camera access permission de dein.

## Use Karne Ka Tarika

1. **Naye person ko register karein** (jitne log attendance dene wale hain, unke liye repeat karein):
   ```bash
   python register_face.py
   ```
   Naam/ID enter karein, `c` dabakar 10-15 photos alag angles se capture
   karein, `q` dabakar band karein.

2. **Face encodings generate karein** (har naye registration ke baad chalayein):
   ```bash
   python encode_faces.py
   ```

3. **Attendance system start karein**:
   ```bash
   python main.py
   ```
   Camera on hoga, jaisi hi koi registered face dikhegi, uska naam green
   box ke saath dikhega aur attendance automatically mark ho jayegi.
   `q` dabakar band karein.

4. **Attendance records dekhein**:
   `attendance_logs/` folder me roz ki tareekh wali CSV file ban jati hai
   (e.g. `2026-08-02.csv`) jisme Name, Time, Date columns hote hain.

## Customization

- `config.py` me `CAMERA_INDEX` change karein agar multiple cameras hain.
- `FACE_MATCH_TOLERANCE` (0.4-0.6) adjust karein — kam value = strict matching.
- Ek person din me sirf ek baar mark hota hai (duplicate entries nahi banti).

## Future Improvements (Optional)

- CSV ki jagah SQLite/MySQL database use karna
- Tkinter/Streamlit se GUI dashboard banana
- Check-in aur check-out dono time track karna
- Email/SMS notification bhejna attendance mark hone par
