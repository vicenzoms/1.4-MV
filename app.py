import streamlit as st
import streamlit.components.v1 as components

# Configuração da página Streamlit
st.set_page_config(
    page_title="Feliz Mesversário 1.4 Anos ❤️",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Oculta elementos padrão do Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nosso 1.4 Anos de Amor ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 50%, #fff0f3 100%);
            font-family: 'Montserrat', sans-serif;
            color: #4a3b32;
            overflow: hidden;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Canvas para chuva de corações */
        #heartCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 10;
        }

        /* Tela Inicial / Portal */
        #intro-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            text-align: center;
            color: white;
            padding: 20px;
            transition: opacity 0.8s ease, visibility 0.8s ease;
        }

        #intro-screen.hidden {
            opacity: 0;
            visibility: hidden;
        }

        .intro-title {
            font-family: 'Great Vibes', cursive;
            font-size: 3.8rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }

        .intro-subtitle {
            font-size: 1.1rem;
            margin-bottom: 30px;
            max-width: 500px;
            line-height: 1.6;
            font-weight: 300;
        }

        .start-btn {
            padding: 14px 32px;
            font-size: 1.1rem;
            background: white;
            color: #ff4757;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
        }

        .start-btn:hover {
            transform: translateY(-2px) scale(1.05);
            background: #fff0f3;
        }

        /* Container Principal com Telas */
        #main-container {
            display: none;
            width: 100%;
            max-width: 750px;
            height: 90vh;
            padding: 20px;
            position: relative;
            z-index: 20;
        }

        .screen-wrapper {
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(12px);
            border-radius: 24px;
            border: 1px solid rgba(255, 182, 193, 0.5);
            box-shadow: 0 15px 35px rgba(0,0,0,0.08);
            height: calc(100% - 70px);
            padding: 25px;
            overflow-y: auto;
            position: relative;
        }

        /* Estrutura das Telas Separadas */
        .screen {
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100%;
            opacity: 0;
            transform: translateY(15px);
            transition: opacity 0.4s ease, transform 0.4s ease;
        }

        .screen.active {
            display: flex;
            opacity: 1;
            transform: translateY(0);
        }

        /* Estilização dos Componentes */
        .main-title {
            font-family: 'Great Vibes', cursive;
            font-size: 3.2rem;
            color: #d63031;
            margin-bottom: 10px;
            text-align: center;
        }

        .badge {
            background: #ff4757;
            color: white;
            padding: 6px 18px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 1px;
            margin-bottom: 15px;
        }

        .spotify-container {
            width: 100%;
            max-width: 500px;
            text-align: center;
        }

        .spotify-title {
            font-size: 1rem;
            font-weight: 600;
            color: #d63031;
            margin-bottom: 15px;
        }

        .counter-card {
            text-align: center;
            width: 100%;
        }

        .counter-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.4rem;
            color: #2d3436;
            margin-bottom: 20px;
        }

        .timer-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            width: 100%;
            max-width: 500px;
        }

        .timer-box {
            background: #fff0f3;
            padding: 15px 8px;
            border-radius: 14px;
            border: 1px solid #ffccd5;
        }

        .timer-number {
            font-size: 1.6rem;
            font-weight: 700;
            color: #d63031;
            display: block;
        }

        .timer-label {
            font-size: 0.75rem;
            color: #636e72;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        .polaroid-card {
            background: white;
            padding: 15px 15px 20px 15px;
            border-radius: 6px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 420px;
            width: 100%;
        }

        .polaroid-img {
            width: 100%;
            max-height: 320px;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 12px;
        }

        .polaroid-caption {
            font-family: 'Great Vibes', cursive;
            font-size: 2rem;
            color: #2d3436;
        }

        .letter-content {
            font-family: 'Playfair Display', serif;
            font-size: 1rem;
            line-height: 1.8;
            color: #333;
            white-space: pre-line;
            background: #fffaf0;
            padding: 22px;
            border-radius: 12px;
            border-left: 4px solid #ff4757;
            max-width: 550px;
            width: 100%;
        }

        .reasons-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            width: 100%;
        }

        .reason-card {
            background: white;
            padding: 18px;
            border-radius: 14px;
            text-align: center;
            box-shadow: 0 6px 15px rgba(0,0,0,0.04);
            border: 1px solid #ffe6e6;
        }

        .reason-icon {
            font-size: 1.8rem;
            margin-bottom: 8px;
            display: block;
        }

        .reason-text {
            font-size: 0.85rem;
            line-height: 1.4;
            color: #4a3b32;
        }

        /* Controles de Navegação das Telas */
        .nav-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 15px;
            padding: 0 10px;
        }

        .nav-btn {
            background: #ff4757;
            color: white;
            border: none;
            padding: 10px 22px;
            font-size: 0.95rem;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 5px 15px rgba(255, 71, 87, 0.3);
            transition: all 0.2s ease;
        }

        .nav-btn:hover:not(:disabled) {
            background: #ff6b81;
            transform: scale(1.03);
        }

        .nav-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
            box-shadow: none;
            opacity: 0.6;
        }

        .page-indicator {
            font-size: 0.9rem;
            font-weight: 600;
            color: #d63031;
        }

        @media (max-width: 600px) {
            .main-title { font-size: 2.4rem; }
            .intro-title { font-size: 2.8rem; }
            .timer-grid { grid-template-columns: repeat(2, 1fr); }
            #main-container { height: 95vh; padding: 10px; }
            .screen-wrapper { padding: 15px; }
        }
    </style>
</head>
<body>

    <canvas id="heartCanvas"></canvas>

    <!-- Tela de Abertura / Portal -->
    <div id="intro-screen">
        <div class="intro-title">Feliz Mesversário! ❤️</div>
        <div class="intro-subtitle">
            1.4 anos (1 ano e 4 meses) vivendo a história de amor mais linda do mundo ao seu lado...
        </div>
        <button class="start-btn" onclick="enterSite()">
            Aperte aqui para entrar, meu amor ✨
        </button>
    </div>

    <!-- Container com Navegação em Telas Separadas -->
    <div id="main-container">
        <div class="screen-wrapper">
            
            <!-- TELA 1: Capa & Trilha Sonora -->
            <div class="screen active" id="screen-0">
                <div class="badge">Nossos 1.4 Anos Juntos 💖</div>
                <h1 class="main-title">Para o Amor da Minha Vida</h1>
                <div class="spotify-container" style="margin-top: 20px;">
                    <div class="spotify-title">🎵 A Nossa Trilha Sonora Especial</div>
                    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/2t0wwvR15fc3K1ey8OiOaN?utm_source=generator&si=f9e2906b727144e8" width="100%" height="152" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                </div>
            </div>

            <!-- TELA 2: Contador de Tempo -->
            <div class="screen" id="screen-1">
                <div class="counter-card">
                    <h2 class="counter-title">Construindo nossa história há...</h2>
                    <div class="timer-grid" style="margin: 0 auto;">
                        <div class="timer-box">
                            <span class="timer-number" id="days">486</span>
                            <span class="timer-label">Dias</span>
                        </div>
                        <div class="timer-box">
                            <span class="timer-number" id="hours">11</span>
                            <span class="timer-label">Horas</span>
                        </div>
                        <div class="timer-box">
                            <span class="timer-number" id="minutes">34</span>
                            <span class="timer-label">Minutos</span>
                        </div>
                        <div class="timer-box">
                            <span class="timer-number" id="seconds">22</span>
                            <span class="timer-label">Segundos</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TELA 3: Galeria de Fotos -->
            <div class="screen" id="screen-2">
                <h2 style="font-family: 'Playfair Display', serif; color: #d63031; margin-bottom: 15px; text-align: center;">Momento Especial 📸</h2>
                <div class="polaroid-card">
                    <img class="polaroid-img" src="https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&w=600&q=80" alt="Nosso momento">
                    <div class="polaroid-caption">Eu & Você Sempre ❤️</div>
                </div>
            </div>

            <!-- TELA 4: Carta de Amor -->
            <div class="screen" id="screen-3">
                <h2 style="font-family: 'Playfair Display', serif; color: #d63031; margin-bottom: 15px; text-align: center;">Minha Carta Para Você ✉️</h2>
                <div class="letter-content">
                    Meu amor,
                    
                    Cada segundo ao seu lado nesses 1.4 anos tem sido uma bênção inexplicável. Obrigado por trazer cor, alegria e tanto carinho para a minha vida. 
                    
                    Que este seja apenas o começo de uma eternidade que vamos construir juntos. Te amo infinitamente!
                </div>
            </div>

            <!-- TELA 5: Motivos para Amar -->
            <div class="screen" id="screen-4">
                <h2 style="font-family: 'Playfair Display', serif; color: #d63031; margin-bottom: 15px; text-align: center;">Por que eu te amo? 💖</h2>
                <div class="reasons-grid">
                    <div class="reason-card">
                        <span class="reason-icon">😊</span>
                        <div class="reason-text">O seu sorriso ilumina até o meu dia mais difícil.</div>
                    </div>
                    <div class="reason-card">
                        <span class="reason-icon">🤗</span>
                        <div class="reason-text">O seu abraço é o meu lugar favorito no mundo.</div>
                    </div>
                    <div class="reason-card">
                        <span class="reason-icon">✨</span>
                        <div class="reason-text">Você me faz querer ser uma pessoa melhor todos os dias.</div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Botões de Navegação -->
        <div class="nav-controls">
            <button class="nav-btn" id="prevBtn" onclick="navigateScreen(-1)" disabled>← Anterior</button>
            <span class="page-indicator" id="pageIndicator">1 / 5</span>
            <button class="nav-btn" id="nextBtn" onclick="navigateScreen(1)">Próximo →</button>
        </div>
    </div>

    <script>
        let currentScreen = 0;
        const screens = document.querySelectorAll('.screen');
        const totalScreens = screens.length;

        function updateNavigation() {
            screens.forEach((screen, index) => {
                screen.classList.toggle('active', index === currentScreen);
            });
            document.getElementById('prevBtn').disabled = (currentScreen === 0);
            document.getElementById('nextBtn').disabled = (currentScreen === totalScreens - 1);
            document.getElementById('pageIndicator').innerText = `${currentScreen + 1} / ${totalScreens}`;
        }

        function navigateScreen(direction) {
            currentScreen += direction;
            if (currentScreen < 0) currentScreen = 0;
            if (currentScreen >= totalScreens) currentScreen = totalScreens - 1;
            updateNavigation();
        }

        function enterSite() {
            document.getElementById('intro-screen').classList.add('hidden');
            document.getElementById('main-container').style.display = 'block';
            updateNavigation();
        }

        // Animação dos Corações
        const canvas = document.getElementById('heartCanvas');
        const ctx = canvas.getContext('2d');
        let hearts = [];

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        class Heart {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = canvas.height + 20;
                this.size = Math.random() * 15 + 10;
                this.speed = Math.random() * 1.5 + 0.8;
                this.opacity = Math.random() * 0.5 + 0.3;
            }
            draw() {
                ctx.globalAlpha = this.opacity;
                ctx.fillStyle = '#ff4757';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size / 2, Math.PI, 0, false);
                ctx.arc(this.x + this.size / 2, this.y, this.size / 2, Math.PI, 0, false);
                ctx.lineTo(this.x + this.size / 4, this.y + this.size);
                ctx.closePath();
                ctx.fill();
            }
            update() {
                this.y -= this.speed;
            }
        }

        function animateHearts() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if (hearts.length < 25 && Math.random() < 0.05) {
                hearts.push(new Heart());
            }
            hearts.forEach((heart, i) => {
                heart.update();
                heart.draw();
                if (heart.y < -20) hearts.splice(i, 1);
            });
            requestAnimationFrame(animateHearts);
        }
        animateHearts();
    </script>
</body>
</html>
"""

components.html(html_content, height=720, scrolling=False)
