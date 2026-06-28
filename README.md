# Stardance Cinema Camera

An open-source, custom-built hardware and software project designing a portable DIY cinematic filmmaking camera. This repository contains the core software engine responsible for managing the camera system, processing inputs, and driving the custom user interface.

---

## 🚀 Project Overview

The objective of this project is to build a functional, compact cinema camera rig using single-board computing paired with dedicated imaging hardware. 

Instead of relying on heavy pre-built applications, this project utilizes a custom-coded Python software stack to control the system. The software serves as the central brain of the build, managing everything from real-time display feedback and UI rendering to input detection and internal camera logic.

---

## 🛠️ Software Architecture (`snakepy.py`)

The primary script (`snakepy.py`) acts as the custom operating engine for the cinema camera interface. It handles several crucial background tasks simultaneously:

* **Real-Time Display Logic:** Manages the graphic frame rendering and screen coordinates, ensuring the camera interface refreshes smoothly on a portable monitor or display module.
* **Control Event Loop:** Runs a high-performance continuous loop to scan for user actions, input updates, and system state changes instantly without lagging the camera preview.
* **State Management:** Tracks critical variables across the camera system, acting as a foundational codebase that can be expanded to toggle active camera settings and capture commands.

---

## ⚙️ Hardware Integration & Future Roadmap
* **Sensor Calibration:** Interfacing the Python control engine with a high-quality dedicated camera image sensor.
* **Camera GUI Overlay:** Expanding the visual script to render real-time video monitoring overlays, including essential filmmaking metrics (ISO, Shutter Speed, Frame Rate, and Battery Life).
* **Storage & Portability:** Engineering a custom physical rig featuring high-speed SSD storage capture and a mobile power distribution system.
