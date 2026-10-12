# The Interactive Solar System

An interactive 3D solar system visualization built with Flask and model-viewer. Explore planets, dwarf planets, comets and meteors in 3D, view solar system data through interactive charts, generate text about celestial bodies, process audio with alien voice effects, and remove backgrounds from images.

## Project Information

- Developed: September 2025
- Status: Working demo (as submitted)

## Features

- Interactive 3D solar system using WebGL (model-viewer) with GLB models
- Detailed data visualization using Highcharts (temperature, moons, gravity, orbital/rotation data)
- AI-generated text snippets based on selected celestial objects (n-gram model)
- Audio processing: apply alien voice effect to uploaded audio files
- Image processing: remove background and composite with space backgrounds
- Responsive UI with animated starfield and ambient space audio

## Prerequisites

- Python 3.12.8 (recommended for compatibility)
- FFmpeg (required for audio processing with pydub/librosa)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd interactive-solar-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

- Linux: `sudo apt install ffmpeg`
- macOS: `brew install ffmpeg`
- Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

## Usage

Run the Flask app:

```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000`.

## Project Structure

```
.
├── app.py                    # Flask application with routes and logic
├── solar_system_data.csv    # Celestial body data
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md              # Project documentation
├── backgrounds/           # Background images for image processing
├── static/                # Static assets (GLB models, CSS, JS, audio)
├── templates/             # HTML templates
└── uploads/               # Temporary storage for processed files
```

## Notes

- Large media files (videos) and reports from the original submission are not included in this repository.
- Uploaded files are stored temporarily in the `uploads/` directory.
