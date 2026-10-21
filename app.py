import streamlit as st
import streamlit.components.v1 as components

# Configuração da página Streamlit
st.set_page_config(
    page_title="Feliz Mesversário 1.4 Anos ❤️",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Oculta elementos padrão do Streamlit para uma experiência imersiva
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
            overflow-x: hidden;
            position: relative;
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
            transition: opacity 1.2s ease, visibility 1.2s ease;
        }

        #intro-screen.hidden {
            opacity: 0;
            visibility: hidden;
        }

        .intro-title {
            font-family: 'Great Vibes', cursive;
            font-size: 4rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }

        .intro-subtitle {
            font-size: 1.2rem;
            margin-bottom: 30px;
            max-width: 500px;
            line-height: 1.6;
            font-weight: 300;
        }

        .start-btn {
            padding: 16px 36px;
            font-size: 1.2rem;
            background: white;
            color: #ff4757;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .start-btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 30px rgba(0,0,0,0.25);
            background: #fff0f3;
        }

        /* Container Principal */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px 80px 20px;
        }

        /* Header Principal */
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding-top: 20px;
        }

        .main-title {
            font-family: 'Great Vibes', cursive;
            font-size: 3.8rem;
            color: #d63031;
            margin-bottom: 10px;
        }

        .badge {
            display: inline-block;
            background: #ff4757;
            color: white;
            padding: 6px 18px;
            border-radius: 20px;
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 1px;
            box-shadow: 0 4px 12px rgba(255, 71, 87, 0.3);
        }

        /* Seção Spotify Embed */
        .spotify-container {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 50px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            border: 1px solid rgba(255, 182, 193, 0.4);
            text-align: center;
        }

        .spotify-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #d63031;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        /* Contador de Tempo */
        .counter-card {
            background: white;
            border-radius: 20px;
            padding: 30px 20px;
            margin-bottom: 50px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            border: 1px solid #ffe6e6;
        }

        .counter-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            color: #2d3436;
            margin-bottom: 20px;
        }

        .timer-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
        }

        .timer-box {
            background: #fff0f3;
            padding: 15px 10px;
            border-radius: 12px;
            border: 1px solid #ffccd5;
        }

        .timer-number {
            font-size: 1.8rem;
            font-weight: 700;
            color: #d63031;
            display: block;
        }

        .timer-label {
            font-size: 0.8rem;
            color: #636e72;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        /* Galeria de Fotos Polaroid */
        .gallery-title {
            text-align: center;
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #d63031;
            margin-bottom: 30px;
        }

        .polaroid-grid {
            display: flex;
            flex-direction: column;
            gap: 40px;
            margin-bottom: 60px;
        }

        .polaroid-card {
            background: white;
            padding: 20px 20px 30px 20px;
            border-radius: 4px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.08);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            position: relative;
        }

        .polaroid-card:nth-child(odd) {
            transform: rotate(-1.5deg);
        }

        .polaroid-card:nth-child(even) {
            transform: rotate(1.5deg);
        }

        .polaroid-card:hover {
            transform: rotate(0deg) scale(1.02);
            box-shadow: 0 18px 45px rgba(0,0,0,0.15);
            z-index: 5;
        }

        .polaroid-img {
            width: 100%;
            max-height: 520px;
            object-fit: cover;
            border-radius: 2px;
            display: block;
            margin-bottom: 18px;
        }

        .polaroid-caption {
            font-family: 'Great Vibes', cursive;
            font-size: 2.2rem;
            text-align: center;
            color: #2d3436;
        }

        /* Envelope / Carta de Amor 3D */
        .letter-section {
            margin-bottom: 60px;
            text-align: center;
        }

        .envelope-wrapper {
            background: white;
            border-radius: 20px;
            padding: 40px 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.07);
            border: 2px dashed #ff8fa3;
            position: relative;
        }

        .envelope-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #d63031;
            margin-bottom: 20px;
        }

        .letter-content {
            font-family: 'Playfair Display', serif;
            font-size: 1.15rem;
            line-height: 1.9;
            color: #333;
            text-align: left;
            white-space: pre-line;
            background: #fffaf0;
            padding: 30px;
            border-radius: 12px;
            border-left: 5px solid #ff4757;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
        }

        /* Motivos para amar */
        .reasons-section {
            margin-bottom: 60px;
        }

        .reasons-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 20px;
        }

        .reason-card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.05);
            border: 1px solid #ffe6e6;
            transition: all 0.3s ease;
        }

        .reason-card:hover {
            transform: translateY(-50%);
            border-color: #ff4757;
            box-shadow: 0 12px 25px rgba(255,71,87,0.15);
        }

        .reason-icon {
            font-size: 2.2rem;
            margin-bottom: 12px;
            display: block;
        }

        .reason-text {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #4a3b32;
        }

        /* Nova Seção de Texto Final */
        .final-text-section {
            margin-bottom: 60px;
            text-align: center;
        }

        .final-text-card {
            background: white;
            border-radius: 20px;
            padding: 40px 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.07);
            border: 1px solid #ffe6e6;
        }

        .final-text-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #d63031;
            margin-bottom: 25px;
        }

        .final-text-body {
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            line-height: 1.9;
            color: #333;
            text-align: left;
            white-space: pre-line;
            background: #fffaf0;
            padding: 30px;
            border-radius: 12px;
            border-left: 5px solid #d63031;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
        }

        /* Botão Flutuante de Amor */
        .love-btn-container {
            text-align: center;
            margin-top: 40px;
        }

        .send-love-btn {
            background: linear-gradient(135deg, #ff4757, #ff6b81);
            color: white;
            padding: 16px 32px;
            font-size: 1.1rem;
            font-weight: 600;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(255, 71, 87, 0.35);
            transition: all 0.3s ease;
        }

        .send-love-btn:hover {
            transform: scale(1.08);
            box-shadow: 0 15px 30px rgba(255, 71, 87, 0.5);
        }

        footer {
            text-align: center;
            padding-top: 40px;
            font-size: 0.9rem;
            color: #b2bec3;
        }

        @media (max-width: 600px) {
            .main-title { font-size: 2.8rem; }
            .intro-title { font-size: 3rem; }
            .timer-grid { grid-template-columns: repeat(2, 1fr); }
            .polaroid-caption { font-size: 1.8rem; }
            .letter-content { padding: 20px; font-size: 1rem; }
            .final-text-body { padding: 20px; font-size: 1rem; }
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
            <span>Aperte aqui para entrar, meu amor ✨</span>
        </button>
    </div>

    <!-- Conteúdo Principal -->
    <div class="container">
        
        <header class="header">
            <div class="badge">Nossos 1.4 Anos Juntos 💖</div>
            <h1 class="main-title">Para o Amor da Minha Vida</h1>
        </header>

        <!-- Player do Spotify Integrado -->
        <div class="spotify-container">
            <div class="spotify-title">🎵 A Nossa Trilha Sonora Especial</div>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/2t0wwvR15fc3K1ey8OiOaN?utm_source=generator&si=f9e2906b727144e8" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>

        <!-- Contador de Tempo -->
        <div class="counter-card">
            <h2 class="counter-title">Construindo nossa história há...</h2>
            <div class="timer-grid">
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

        <!-- Galeria de Fotos -->
        <h2 class="gallery-title">Nossa Galeria de Momentos 📸</h2>
        <div class="polaroid-grid">
            
            <div class="polaroid-card">

# Configuração da página Streamlit
st.set_page_config(
    page_title="Feliz Mesversário 1.4 Anos ❤️",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Oculta elementos padrão do Streamlit para uma experiência imersiva
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
            overflow-x: hidden;
            position: relative;
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
            transition: opacity 1.2s ease, visibility 1.2s ease;
        }

        #intro-screen.hidden {
            opacity: 0;
            visibility: hidden;
        }

        .intro-title {
            font-family: 'Great Vibes', cursive;
            font-size: 4rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }

        .intro-subtitle {
            font-size: 1.2rem;
            margin-bottom: 30px;
            max-width: 500px;
            line-height: 1.6;
            font-weight: 300;
        }

        .start-btn {
            padding: 16px 36px;
            font-size: 1.2rem;
            background: white;
            color: #ff4757;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .start-btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 30px rgba(0,0,0,0.25);
            background: #fff0f3;
        }

        /* Container Principal */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px 80px 20px;
        }

        /* Header Principal */
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding-top: 20px;
        }

        .main-title {
            font-family: 'Great Vibes', cursive;
            font-size: 3.8rem;
            color: #d63031;
            margin-bottom: 10px;
        }

        .badge {
            display: inline-block;
            background: #ff4757;
            color: white;
            padding: 6px 18px;
            border-radius: 20px;
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 1px;
            box-shadow: 0 4px 12px rgba(255, 71, 87, 0.3);
        }

        /* Seção Spotify Embed */
        .spotify-container {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 50px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            border: 1px solid rgba(255, 182, 193, 0.4);
            text-align: center;
        }

        .spotify-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #d63031;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        /* Contador de Tempo */
        .counter-card {
            background: white;
            border-radius: 20px;
            padding: 30px 20px;
            margin-bottom: 50px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            border: 1px solid #ffe6e6;
        }

        .counter-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            color: #2d3436;
            margin-bottom: 20px;
        }

        .timer-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
        }

        .timer-box {
            background: #fff0f3;
            padding: 15px 10px;
            border-radius: 12px;
            border: 1px solid #ffccd5;
        }

        .timer-number {
            font-size: 1.8rem;
            font-weight: 700;
            color: #d63031;
            display: block;
        }

        .timer-label {
            font-size: 0.8rem;
            color: #636e72;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        /* Galeria de Fotos Polaroid */
        .gallery-title {
            text-align: center;
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #d63031;
            margin-bottom: 30px;
        }

        .polaroid-grid {
            display: flex;
            flex-direction: column;
            gap: 40px;
            margin-bottom: 60px;
        }

        .polaroid-card {
            background: white;
            padding: 20px 20px 30px 20px;
            border-radius: 4px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.08);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            position: relative;
        }

        .polaroid-card:nth-child(odd) {
            transform: rotate(-1.5deg);
        }

        .polaroid-card:nth-child(even) {
            transform: rotate(1.5deg);
        }

        .polaroid-card:hover {
            transform: rotate(0deg) scale(1.02);
            box-shadow: 0 18px 45px rgba(0,0,0,0.15);
            z-index: 5;
        }

        .polaroid-img {
            width: 100%;
            max-height: 520px;
            object-fit: cover;
            border-radius: 2px;
            display: block;
            margin-bottom: 18px;
        }

        .polaroid-caption {
            font-family: 'Great Vibes', cursive;
            font-size: 2.2rem;
            text-align: center;
            color: #2d3436;
        }

        /* Envelope / Carta de Amor 3D */
        .letter-section {
            margin-bottom: 60px;
            text-align: center;
        }

        .envelope-wrapper {
            background: white;
            border-radius: 20px;
            padding: 40px 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.07);
            border: 2px dashed #ff8fa3;
            position: relative;
        }

        .envelope-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #d63031;
            margin-bottom: 20px;
        }

        .letter-content {
            font-family: 'Playfair Display', serif;
            font-size: 1.15rem;
            line-height: 1.9;
            color: #333;
            text-align: left;
            white-space: pre-line;
            background: #fffaf0;
            padding: 30px;
            border-radius: 12px;
            border-left: 5px solid #ff4757;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
        }

        /* Motivos para amar */
        .reasons-section {
            margin-bottom: 60px;
        }

        .reasons-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 20px;
        }

        .reason-card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.05);
            border: 1px solid #ffe6e6;
            transition: all 0.3s ease;
        }

        .reason-card:hover {
            transform: translateY(-50%);
            border-color: #ff4757;
            box-shadow: 0 12px 25px rgba(255,71,87,0.15);
        }

        .reason-icon {
            font-size: 2.2rem;
            margin-bottom: 12px;
            display: block;
        }

        .reason-text {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #4a3b32;
        }

        /* Nova Seção de Texto Final */
        .final-text-section {
            margin-bottom: 60px;
            text-align: center;
        }

        .final-text-card {
            background: white;
            border-radius: 20px;
            padding: 40px 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.07);
            border: 1px solid #ffe6e6;
        }

        .final-text-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #d63031;
            margin-bottom: 25px;
        }

        .final-text-body {
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            line-height: 1.9;
            color: #333;
            text-align: left;
            white-space: pre-line;
            background: #fffaf0;
            padding: 30px;
            border-radius: 12px;
            border-left: 5px solid #d63031;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
        }

        /* Botão Flutuante de Amor */
        .love-btn-container {
            text-align: center;
            margin-top: 40px;
        }

        .send-love-btn {
            background: linear-gradient(135deg, #ff4757, #ff6b81);
            color: white;
            padding: 16px 32px;
            font-size: 1.1rem;
            font-weight: 600;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(255, 71, 87, 0.35);
            transition: all 0.3s ease;
        }

        .send-love-btn:hover {
            transform: scale(1.08);
            box-shadow: 0 15px 30px rgba(255, 71, 87, 0.5);
        }

        footer {
            text-align: center;
            padding-top: 40px;
            font-size: 0.9rem;
            color: #b2bec3;
        }

        @media (max-width: 600px) {
            .main-title { font-size: 2.8rem; }
            .intro-title { font-size: 3rem; }
            .timer-grid { grid-template-columns: repeat(2, 1fr); }
            .polaroid-caption { font-size: 1.8rem; }
            .letter-content { padding: 20px; font-size: 1rem; }
            .final-text-body { padding: 20px; font-size: 1rem; }
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
            <span>Aperte aqui para entrar, meu amor ✨</span>
        </button>
    </div>

    <!-- Conteúdo Principal -->
    <div class="container">
        
        <header class="header">
            <div class="badge">Nossos 1.4 Anos Juntos 💖</div>
            <h1 class="main-title">Para o Amor da Minha Vida</h1>
        </header>

        <!-- Player do Spotify Integrado -->
        <div class="spotify-container">
            <div class="spotify-title">🎵 A Nossa Trilha Sonora Especial</div>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/2t0wwvR15fc3K1ey8OiOaN?utm_source=generator&si=f9e2906b727144e8" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>

        <!-- Contador de Tempo -->
        <div class="counter-card">
            <h2 class="counter-title">Construindo nossa história há...</h2>
            <div class="timer-grid">
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

        <!-- Galeria de Fotos -->
        <h2 class="gallery-title">Nossa Galeria de Momentos 📸</h2>
        <div class="polaroid-grid">
            
            <div class="polaroid-card">
                <img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/2wBDAQICAgICAgUDAwUKBwYHCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgr/wAARCAQAAwADASIAAhEBAxEB/8QAHgAAAAcBAQEBAAAAAAAAAAAAAgMEBQYHCAEJAAr/xABOEAACAQIFAgQEAwUFBwMacro5p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p3p
