function createStars() {
    const starsContainer = document.querySelector('.stars');
    for (let i = 0; i < 1500; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.setProperty('--duration', `${Math.random() * 3 + 1}s`);
        starsContainer.appendChild(star);
    }
}


function createParticles() {
    const particlesContainer = document.querySelector('.particles');
    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.width = `${Math.random() * 3 + 1}px`;
        particle.style.height = particle.style.width;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.animationDuration = `${Math.random() * 10 + 5}s`;
        particlesContainer.appendChild(particle);
    }
}

createStars();
createParticles();

const audio = document.getElementById('spaceAudio');
let isMuted = false;

// Démarrer la musique automatiquement
audio.play().catch(error => {
    console.log('Autoplay bloqué - Cliquez pour activer');
    isMuted = true;
    updateButton();
});

function toggleMute() {
    isMuted = !isMuted;
    audio.muted = isMuted;
    updateButton();
    if (audio.paused) {
        audio.play();
    }
}

function updateButton() {
    const icon = document.querySelector('.music-btn i');
    icon.classList = isMuted ? 'fas fa-volume-mute' : 'fas fa-volume-up';
}

function togglePlanets() {
    const container = document.getElementById('planetsContainer');
    container.style.display = container.style.display === 'flex' ? 'none' : 'flex';
}

function toggleDrawContainer() {
    let container = document.getElementById('drawContainer');
    if (container.style.display === 'none' || container.style.display === '') {
        container.style.display = 'flex';
    } else {
        container.style.display = 'none';
    }
}

function toggleContainers(containerId) {
    // Sélectionner tous les conteneurs possibles
    const allContainers = document.querySelectorAll('.planets-container, .draw-container');

    // Masquer tous les conteneurs
    allContainers.forEach(container => {
        container.classList.remove('active'); // Retirer la classe active
    });

    // Afficher le conteneur spécifié
    const selectedContainer = document.getElementById(containerId);
    if (selectedContainer) {
        selectedContainer.classList.add('active'); // Ajouter la classe active
    }
}