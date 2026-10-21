import streamlit as st
import streamlit.components.v1 as components

# Configuração da página Streamlit
st.set_page_config(
    page_title="Feliz Mesversário 1.4 Anos ❤️",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Oculta menus padrão do Streamlit para visualização limpa
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

# Conteúdo completo do aplicativo
html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nosso 1.4 Anos de Amor ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 50%, #fff0f3 100%);
            font-family: 'Montserrat', sans-serif;
            color: #4a3b32;
            overflow-x: hidden;
        }
        #heartCanvas {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none; z-index: 10;
        }
        #intro-screen {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            z-index: 9999; text-align: center; color: white; padding: 20px;
            transition: opacity 1.2s ease, visibility 1.2s ease;
        }
        #intro-screen.hidden { opacity: 0; visibility: hidden; }
        .intro-title { font-family: 'Great Vibes', cursive; font-size: 4rem; margin-bottom: 10px; }
        .start-btn {
            padding: 16px 36px; font-size: 1.2rem; background: white; color: #ff4757;
            border: none; border-radius: 50px; cursor: pointer; font-weight: 600;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15); transition: all 0.3s ease;
        }
        .start-btn:hover { transform: translateY(-3px) scale(1.05); }
        .container { max-width: 800px; margin: 0 auto; padding: 40px 20px 80px 20px; }
        .header { text-align: center; margin-bottom: 40px; }
        .main-title { font-family: 'Great Vibes', cursive; font-size: 3.8rem; color: #d63031; }
        .badge {
            display: inline-block; background: #ff4757; color: white; padding: 6px 18px;
            border-radius: 20px; font-size: 0.95rem; font-weight: 600;
        }
        .spotify-container {
            background: rgba(255, 255, 255, 0.85); border-radius: 20px; padding: 20px;
            margin-bottom: 50px; border: 1px solid rgba(255, 182, 193, 0.4); text-align: center;
        }
        .counter-card {
            background: white; border-radius: 20px; padding: 30px 20px; margin-bottom: 50px;
            text-align: center; border: 1px solid #ffe6e6;
        }
        .timer-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
        .timer-box { background: #fff0f3; padding: 15px 10px; border-radius: 12px; }
        .timer-number { font-size: 1.8rem; font-weight: 700; color: #d63031; display: block; }
        .polaroid-grid { display: flex; flex-direction: column; gap: 40px; margin-bottom: 60px; }
        .polaroid-card {
            background: white; padding: 20px 20px 30px 20px; border-radius: 4px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.08); text-align: center;
        }
        .polaroid-img { width: 100%; max-height: 520px; object-fit: cover; border-radius: 2px; }
        .polaroid-caption { font-family: 'Great Vibes', cursive; font-size: 2.2rem; margin-top: 15px; }
        .letter-content {
            font-family: 'Playfair Display', serif; font-size: 1.15rem; line-height: 1.9;
            color: #333; white-space: pre-line; background: #fffaf0; padding: 30px;
            border-radius: 12px; border-left: 5px solid #ff4757; margin-top: 20px;
        }
        .send-love-btn {
            background: linear-gradient(135deg, #ff4757, #ff6b81); color: white;
            padding: 16px 32px; font-size: 1.1rem; border: none; border-radius: 50px; cursor: pointer;
        }
    </style>
</head>
<body>
    <canvas id="heartCanvas"></canvas>

    <div id="intro-screen">
        <div class="intro-title">Feliz Mesversário! ❤️</div>
        <p style="margin-bottom: 25px;">1.4 anos vivendo a história de amor mais linda do mundo ao seu lado...</p>
        <button class="start-btn" onclick="enterSite()">Aperte aqui para entrar, meu amor ✨</button>
    </div>

    <div class="container">
        <header class="header">
            <div class="badge">Nossos 1.4 Anos Juntos 💖</div>
            <h1 class="main-title">Para o Amor da Minha Vida</h1>
        </header>

        <div class="spotify-container">
            <h3 style="margin-bottom: 12px; color: #d63031;">🎵 A Nossa Trilha Sonora Especial</h3>
            <iframe src="https://open.spotify.com/embed/track/2t0wwvR15fc3K1ey8OiOaN?utm_source=generator&si=f9e2906b727144e8" width="100%" height="152" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>

        <div class="counter-card">
            <h2 style="font-family: 'Playfair Display', serif; margin-bottom: 20px;">Construindo nossa história há...</h2>
            <div class="timer-grid">
                <div class="timer-box"><span class="timer-number" id="days">486</span>Dias</div>
                <div class="timer-box"><span class="timer-number" id="hours">12</span>Horas</div>
                <div class="timer-box"><span class="timer-number" id="minutes">30</span>Minutos</div>
                <div class="timer-box"><span class="timer-number" id="seconds">00</span>Segundos</div>
            </div>
        </div>

        <div class="polaroid-grid">
            <div class="polaroid-card">
                <img src="https://via.placeholder.com/600x600?text=Foto+1" class="polaroid-img">
                <div class="polaroid-caption">O sorriso que ilumina os meus dias ✨</div>
            </div>
        </div>

        <div class="letter-content">
            Meu amor, nesse nosso MesVersário de 1.4 anos eu me sinto o homem mais sortudo que já pisou nesse mundo...
        </div>
    </div>

    <script>
        function enterSite() { document.getElementById('intro-screen').classList.add('hidden'); }
    </script>
</body>
</html>
"""

components.html(html_content, height=2800, scrolling=True)
