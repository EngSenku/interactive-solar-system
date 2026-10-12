# Interactive Solar System

An interactive 3D solar system visualization built with Flask and Model Viewer. Explore planets, dwarf planets, comets, and meteors in 3D, visualize solar system data with interactive charts, generate AI-powered text about celestial bodies, apply alien voice effects to audio, and remove backgrounds from images.

![Python](https://img.shields.io/badge/Python-3.12.8-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?style=for-the-badge&logo=flask)
![Three.js](https://img.shields.io/badge/Model%20Viewer-3D-orange?style=for-the-badge)
![Highcharts](https://img.shields.io/badge/Highcharts-Charts-2F9CFF?style=for-the-badge)

## ✨ Features

- **3D Visualization**: Interactive solar system rendered with WebGL using `<model-viewer>`, featuring all planets, dwarf planets, comets, and meteors
- **Data Visualization**: Dynamic charts powered by Highcharts showing surface temperatures, moon counts, gravity, and orbital vs. rotation periods
- **AI Text Generation**: N-gram language model that generates contextual text based on selected celestial objects
- **Audio Processing**: Upload audio files and apply an alien voice effect using pitch shifting and modulation
- **Image Processing**: Remove backgrounds from images and composite them with space-themed backgrounds
- **Immersive UI**: Animated starfield, particle effects, and ambient space audio

## 📅 Project Info

- **Developed**: September 2025
- **Status**: Working demo

## 🚀 Getting Started

### Prerequisites

- Python 3.12.8 (recommended for compatibility)
- [FFmpeg](https://ffmpeg.org/download.html) (required for audio processing)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/EngSenku/interactive-solar-system.git
   cd interactive-solar-system
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   ```

   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**

   - **Ubuntu/Debian**: `sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

### Usage

Run the Flask development server:

```bash
python app.py
```

Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

## 📁 Project Structure

```text
interactive-solar-system/
├── app.py                    # Flask application with routes and logic
├── solar_system_data.csv    # Celestial body data and statistics
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore rules
├── README.md               # Project documentation
├── backgrounds/            # Background images for image processing
│   ├── solar_system_background.jpg
│   └── space_background.jpg
├── static/                 # Static assets (models, CSS, JS, audio)
│   ├── *.glb               # 3D models (planets, comets, meteors)
│   ├── space.css           # Styles and animations
│   ├── space.js            # Interactive frontend logic
│   └── Interstellar.mp3    # Ambient background music
├── templates/              # HTML templates
│   └── index.html          # Main application template
└── uploads/                # Temporary storage for processed files
```

## 🛠️ Technologies Used

- **Backend**: [Flask](https://flask.palletsprojects.com/) - Web framework
- **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [scikit-learn](https://scikit-learn.org/)
- **Audio Processing**: [librosa](https://librosa.org/), [pydub](https://github.com/jiaaro/pydub), [soundfile](https://python-soundfile.readthedocs.io/)
- **Image Processing**: [Pillow](https://python-pillow.org/), [rembg](https://github.com/danielgatis/rembg) (ONNX Runtime)
- **3D Rendering**: [Model Viewer](https://modelviewer.dev/) by Google
- **Data Visualization**: [Highcharts](https://www.highcharts.com/)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)

## 📝 Notes

- This repository contains only the source code and assets needed to run the project.
- Uploaded files are temporarily stored in the `uploads/` directory and are not tracked in git.
