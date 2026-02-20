# Real-Time People Counting System using YOLOv8

## 📌 Project Objective
The objective of this project is to build a real-time computer vision pipeline capable of accessing live webcam input and preparing the environment for implementing people detection and counting using the YOLOv8 model.

This project establishes the foundational setup required for real-time object detection systems.

---

## 🧠 Problem Statement
Manual monitoring and counting of people in live environments is inefficient and error-prone.  
This project aims to automate the process using computer vision techniques, enabling scalable and real-time monitoring.

---

## ⚙️ Current Implementation
- Configured isolated Python virtual environment
- Installed and managed dependencies using pip
- Implemented real-time webcam capture using OpenCV
- Resolved Windows camera backend issue using DirectShow (CAP_DSHOW)
- Structured project following professional development practices
- Version controlled using Git

---

## 🛠️ Tech Stack
- Python 3.x
- OpenCV
- NumPy
- Git (Version Control)

---

## 📂 Project Structure

```

RealTime_People_Counting_YOLOv8/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/

```

---

## ▶️ How to Run the Project

1. Clone the repository
2. Navigate to the project directory
3. Create virtual environment:
```

python -m venv venv

```
4. Activate environment:
```

venv\Scripts\activate

```
5. Install dependencies:
```

pip install -r requirements.txt

```
6. Run the application:
```

python main.py

```

Press **'q'** to close the webcam window.

---

## 🚀 Future Enhancements
- Integration of YOLOv8 for real-time person detection
- Implementation of object tracking
- Real-time people counting logic
- Performance optimization for CPU-based systems
- Deployment-ready pipeline

---

## 📌 Author
Developed as part of a structured computer vision project setup.
