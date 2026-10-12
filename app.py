#!/usr/bin/env python3
"""
Interactive Solar System - Flask Application
A web application for exploring the solar system in 3D with data visualization,
audio processing, and image manipulation features.
"""

import os
import random
from pathlib import Path

import librosa
import numpy as np
import pandas as pd
import soundfile as sf
from flask import Flask, jsonify, render_template, request, send_file
from PIL import Image
from pydub import AudioSegment
from rembg import remove
from sklearn.feature_extraction.text import CountVectorizer

# Initialize Flask app
app = Flask(__name__)

# Configuration
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
UPLOAD_DIR = BASE_DIR / "uploads"
BACKGROUND_DIR = BASE_DIR / "backgrounds"
DATA_FILE = BASE_DIR / "solar_system_data.csv"

# Ensure directories exist
UPLOAD_DIR.mkdir(exist_ok=True)
BACKGROUND_DIR.mkdir(exist_ok=True)

# Model mapping for 3D celestial objects
STATIC_MODELS = {
    "solar system": "Solar_system.glb",
    "sun": "Sun.glb",
    "mercury": "Mercury.glb",
    "venus": "Venus.glb",
    "earth": "Earth.glb",
    "moon": "Luna.glb",
    "mars": "Mars.glb",
    "jupiter": "Jupiter.glb",
    "saturn": "Saturn.glb",
    "uranus": "Uranus.glb",
    "neptune": "Neptune.glb",
    "pluto": "Pluto.glb",
    "ceres": "Ceres.glb",
    "haumea": "Haumea.glb",
    "makemake": "Makemake.glb",
    "eris": "Eris.glb",
    "Halleys Comet": "Halley's Comet.glb",
    "Chelyabinsk Meteor": "Chelyabinsk Meteor.glb",
    "67P_Churyumov-Gerasimenko": "67P_Churyumov-Gerasimenko.glb",
}

# Background images for image processing
BACKGROUND_IMAGES = {
    "space": "space_background.jpg",
    "solar_system": "solar_system_background.jpg",
}

# Text corpus for n-gram language model
SOLAR_SYSTEM_CORPUS = [
    "The star is shining brightly in the night sky.",
    "Planets orbit around the sun in our solar system.",
    "The solar system consists of the sun, planets, and other celestial objects.",
    "Stars are massive celestial bodies made of hydrogen and helium.",
    "The planet Earth is the third planet from the sun.",
    "The sun is the center of our solar system and provides energy for all life on Earth.",
    "Mercury is the closest planet to the sun and has extreme temperature variations.",
    "Venus is known as Earth's twin due to its similar size, but it has a toxic atmosphere.",
    "Mars is called the Red Planet because of its reddish appearance caused by iron oxide.",
    "Jupiter is the largest planet in the solar system and has a prominent Great Red Spot.",
    "Saturn is famous for its stunning ring system made of ice and rock particles.",
    "Uranus is an ice giant with a unique sideways rotation.",
    "Neptune is the farthest planet from the sun and has the strongest winds in the solar system.",
    "Pluto, once considered the ninth planet, is now classified as a dwarf planet.",
    "Ceres is the largest object in the asteroid belt and is also classified as a dwarf planet.",
    "Haumea is a dwarf planet with an elongated shape and a rapid rotation.",
    "Makemake is a dwarf planet located in the Kuiper Belt.",
    "Eris is a dwarf planet that is more massive than Pluto and sparked the debate about planetary classification.",
    "Halleys Comet is a famous comet that is visible from Earth every 76 years.",
    "Chelyabinsk Meteor was a large meteor that exploded over Russia in 2013.",
    "Comet 67P_Churyumov-Gerasimenko was visited by the Rosetta spacecraft in 2014.",
    "The moon is Earth's only natural satellite and influences tides on our planet.",
    "Asteroids are rocky objects that orbit the sun, mostly found in the asteroid belt.",
    "Meteoroids are small rocky or metallic bodies in space that become meteors when they enter Earth's atmosphere.",
    "The Kuiper Belt is a region beyond Neptune that contains many icy bodies and dwarf planets.",
    "The Oort Cloud is a theoretical cloud of icy objects surrounding the solar system at a great distance.",
    "Astronauts have walked on the moon during the Apollo missions.",
]

# Train n-gram model
def train_ngram_model(corpus, n=2):
    """
    Train a bigram/trigram model using CountVectorizer.
    
    Args:
        corpus (list): List of text strings to train on
        n (int): Size of n-grams
        
    Returns:
        tuple: (ngrams, vectorizer)
    """
    vectorizer = CountVectorizer(ngram_range=(n, n))
    vectorizer.fit_transform(corpus)
    ngrams = vectorizer.get_feature_names_out()
    return ngrams, vectorizer

# Initialize n-gram model
NGRAMS, _ = train_ngram_model(SOLAR_SYSTEM_CORPUS, n=2)

def load_data():
    """
    Load solar system data from CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing solar system data
    """
    df = pd.read_csv(DATA_FILE)
    df.columns = df.columns.str.strip()
    return df

def get_chart_data(df):
    """
    Generate chart data for visualizations.
    
    Args:
        df (pd.DataFrame): Solar system data
        
    Returns:
        dict: Dictionary containing chart data for Highcharts
    """
    # Surface Temperature Radar Chart
    temperature_data = {
        "categories": df["Name"].tolist(),
        "data": df["Surface Temperature (°C)"].tolist(),
    }

    # Number of Moons Bar Chart
    moons_data = {
        "categories": df["Name"].tolist(),
        "values": df["Moons"].fillna(0).astype(int).tolist(),
    }

    # Surface Gravity Chart
    gravity_data = {
        "categories": df["Name"].tolist(),
        "values": df["Surface Gravity (m/s²)"].tolist(),
    }

    # Orbital Period vs Rotation Period Bubble Chart
    orbital_rotation_data = []
    for _, row in df.iterrows():
        orbital_rotation_data.append(
            {
                "x": row["Orbital Period (Earth years)"],
                "y": row["Rotation Period (hours)"],
                "z": row["Rotation Period (hours)"],
                "name": row["Name"],
                "type": row["Type"],
            }
        )

    return {
        "temperature_data": temperature_data,
        "moons_data": moons_data,
        "gravity_data": gravity_data,
        "orbital_rotation_data": orbital_rotation_data,
    }

def generate_text_from_seed(seed_word, length=10):
    """
    Generate text using n-gram model starting from seed word.
    
    Args:
        seed_word (str): Starting word for text generation
        length (int): Number of words to generate
        
    Returns:
        str: Generated text
    """
    words = seed_word.split()
    for _ in range(length):
        # Find candidates that start with last word
        candidates = [
            ngram for ngram in NGRAMS if ngram.startswith(words[-1] + " ")
        ]
        if not candidates:
            break
        next_ngram = random.choice(candidates)
        next_word = next_ngram.split()[-1]
        words.append(next_word)
    return " ".join(words)

@app.route("/")
def index():
    """Render the main page with solar system visualization."""
    df = load_data()
    chart_data = get_chart_data(df)
    return render_template(
        "index.html",
        initial_model=STATIC_MODELS["solar system"],
        chart_data=chart_data,
    )


@app.route("/get_model", methods=["POST"])
def get_model():
    """Get 3D model path based on model type."""
    try:
        model_type = request.json.get("model_type")
        if not model_type:
            return jsonify({"error": "Invalid model type"}), 400

        model_filename = STATIC_MODELS.get(model_type, STATIC_MODELS["solar system"])
        return jsonify({"model_path": f"/static/{model_filename}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/process-audio", methods=["POST"])
def process_audio():
    """Process uploaded audio with alien voice effect."""
    if "audio" not in request.files:
        return "No file uploaded", 400

    file = request.files["audio"]
    if file.filename == "":
        return "No file selected", 400

    # Save uploaded file
    input_path = UPLOAD_DIR / file.filename
    file.save(input_path)

    try:
        # Convert to WAV
        audio = AudioSegment.from_file(input_path)
        wav_path = UPLOAD_DIR / "converted.wav"
        audio.export(wav_path, format="wav")

        # Process with librosa
        y, sr = librosa.load(wav_path, sr=None)

        # Apply alien voice effect
        alien_voice = librosa.effects.pitch_shift(y, sr=sr, n_steps=12)
        carrier = np.sin(2 * np.pi * 100 * np.linspace(0, len(y) / sr, len(y)))
        alien_voice = alien_voice * carrier

        # Save processed audio
        output_path = UPLOAD_DIR / "alien_voice.wav"
        sf.write(output_path, alien_voice, sr)

        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f"Error processing audio: {str(e)}", 500


@app.route("/process-image", methods=["POST"])
def process_image():
    """Remove background from uploaded image and composite with selected background."""
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    upload_path = UPLOAD_DIR / file.filename
    file.save(upload_path)

    try:
        # Remove background
        input_image = Image.open(upload_path)
        output_image = remove(input_image)

        # Get selected background
        background_choice = request.form.get("background", "space_background.jpg")
        background_key = "space" if background_choice == "space" else "solar_system"
        background_image_path = BACKGROUND_DIR / BACKGROUND_IMAGES[background_key]
        background_image = Image.open(background_image_path)

        # Resize and composite
        background_image = background_image.resize(
            output_image.size, Image.Resampling.LANCZOS
        )
        final_image = Image.alpha_composite(
            background_image.convert("RGBA"), output_image
        )

        # Save result
        final_image_path = UPLOAD_DIR / f"final_{file.filename}"
        final_image.save(final_image_path, format="PNG")

        return send_file(final_image_path, mimetype="image/png")
    except Exception as e:
        return f"Error processing image: {str(e)}", 500


@app.route("/generate_text", methods=["POST"])
def generate_text_endpoint():
    """Generate text based on selected celestial body."""
    model_type = request.json.get("model_type", "space")
    generated_text = generate_text_from_seed(model_type, length=10)
    return jsonify({"generated_text": generated_text})


if __name__ == "__main__":
    app.run(debug=True)
