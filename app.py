# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components

# Configuração da página no Streamlit
st.set_page_config(
    page_title="Uma História de Amor Especial",
    page_icon="❤️",
    layout="wide"
)

def get_html_content():
    return """<!DOCTYPE html>
<html lang="pt-PT" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uma História de Amor Especial &#x2764;&#xFE0F;</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Great+Vibes&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Poppins:wght@300;400;500;600;700&family=Sacramento&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Canvas Confetti Library -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        cream: '#FAF4F0',
                        blush: '#FFE6E8',
                        roseSoft: '#FFF0F3',
                        deepRose: '#9D0208',
                        passionRed: '#D00000',
                        warmGold: '#D4AF37',
                    },
                    fontFamily: {
                        serif: ['"Playfair Display"', 'serif'],
                        cursive: ['"Dancing Script"', '"Sacramento"', '"Great Vibes"', 'cursive'],
                        sans: ['"Poppins"', 'sans-serif'],
                    }
                }
            }
        }
    </script>

    <style>
        body {
            background-color: #FAF4F0;
            color: #4A3B32;
            overflow-x: hidden;
        }

        #heart-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 1;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 230, 232, 0.9);
            box-shadow: 0 10px 30px rgba(157, 2, 8, 0.06);
        }

        .polaroid-frame {
            background: #ffffff;
            padding: 14px 14px 45px 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.12);
            border-radius: 6px;
            transition: all 0.4s ease;
        }
        .polaroid-frame:hover {
            transform: scale(1.03) rotate(0deg) !important;
            box-shadow: 0 20px 40px rgba(157, 2, 8, 0.2);
        }

        .perspective-1000 {
            perspective: 1000px;
        }
        .transform-style-3d {
            transform-style: preserve-3d;
        }
        .backface-hidden {
            backface-visibility: hidden;
        }
        .rotate-y-180 {
            transform: rotateY(180deg);
        }

        .gold-border {
            border: 2px solid transparent;
            background: linear-gradient(white, white) padding-box,
                        linear-gradient(135deg, #e6c875, #d4af37, #997819) border-box;
        }

        @keyframes customPulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.08); }
        }
        .animate-love-pulse {
            animation: customPulse 2.2s infinite ease-in-out;
        }
    </style>
</head>
<body class="font-sans antialiased selection:bg-roseSoft selection:text-deepRose">

    <!-- Canvas de Corações Flutuantes -->
    <canvas id="heart-canvas"></canvas>

    <!-- 1. TELA DE BOAS-VINDAS / OVERLAY INICIAL -->
    <div id="welcome-overlay" class="fixed inset-0 z-50 flex flex-col items-center justify-center bg-gradient-to-br from-rose-950 via-rose-900 to-rose-950 text-white p-6 transition-all duration-1000 text-center">
        <div class="text-center max-w-xl space-y-8 px-4">
            <div class="relative inline-block">
                <i class="fa-solid fa-heart text-7xl md:text-8xl text-rose-400 animate-love-pulse"></i>
                <i class="fa-solid fa-sparkles text-3xl text-warmGold absolute -top-2 -right-2 animate-bounce"></i>
            </div>
            
            <div class="space-y-3">
                <span class="text-xs font-semibold uppercase tracking-widest text-warmGold">Celebração de Namoro</span>
                <h1 class="font-cursive text-5xl md:text-7xl text-blush tracking-wide">
                    Feliz Mesversário de 1.4 Anos! &#x2764;&#xFE0F;
                </h1>
                <p class="text-sm font-medium text-rose-200">1 Ano e 4 Meses da Nossa Linda História de Amor</p>
            </div>
            
            <p class="font-serif italic text-lg md:text-xl text-rose-200">
                Para a mulher mais incrível do universo, que faz de mim o homem mais sortudo do mundo...
            </p>

            <div class="p-4 rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 text-sm text-rose-100 space-y-1 max-w-md mx-auto">
                <p><i class="fa-solid fa-headphones mr-2 text-warmGold"></i>Aumenta o som do teu telemóvel/computador</p>
                <p><i class="fa-solid fa-music mr-2 text-warmGold"></i>A nossa música oficial está pronta no topo!</p>
            </div>

            <button id="start-btn" onclick="openOurWorld()" class="mt-6 px-9 py-4 bg-gradient-to-r from-passionRed to-deepRose hover:from-rose-600 hover:to-passionRed text-white font-semibold text-lg rounded-full shadow-2xl hover:shadow-rose-500/50 transform hover:scale-105 transition-all duration-300 flex items-center justify-center gap-3 mx-auto border border-warmGold/40 group">
                <span>Clica aqui para abrir o meu coração ✨</span>
                <i class="fa-solid fa-heart group-hover:scale-125 transition-transform"></i>
            </button>
        </div>
    </div>

    <!-- 2. REPRODUTOR DE MÚSICA DO SPOTIFY NO TOPO -->
    <div id="sticky-spotify" class="sticky top-0 z-40 w-full bg-white/95 backdrop-blur-md border-b border-rose-100 shadow-sm transition-all duration-500">
        <div class="max-w-4xl mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-roseSoft flex items-center justify-center text-passionRed animate-spin" style="animation-duration: 9s;">
                    <i class="fa-solid fa-compact-disc text-2xl"></i>
                </div>
                <div>
                    <span class="text-xs font-bold text-deepRose uppercase tracking-widest block">A Nossa Trilha Sonora</span>
                    <span class="text-xs font-medium text-gray-600 hidden sm:inline">Carrega no Play no leitor do Spotify abaixo 🎶</span>
                </div>
            </div>

            <button onclick="togglePlayer()" class="text-xs px-3.5 py-1.5 rounded-full bg-roseSoft text-deepRose hover:bg-rose-200 font-semibold transition-colors flex items-center gap-1.5">
                <i class="fa-solid fa-music"></i>
                <span id="player-toggle-text">Ocultar Leitor</span>
            </button>
        </div>

        <!-- iframe Oficial do Spotify -->
        <div id="spotify-player-container" class="max-w-3xl mx-auto px-4 pb-3 transition-all duration-300">
            <iframe id="spotify-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/2t0wwvR15fc3K1ey8OiOaN?utm_source=generator&si=f9e2906b727144e8" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
    </div>

    <!-- CONTEÚDO PRINCIPAL -->
    <main class="relative z-10 max-w-4xl mx-auto px-4 py-12 space-y-24">

        <!-- PAINEL DE PERSONALIZAÇÃO RÁPIDA -->
        <div class="glass-card p-4 rounded-2xl flex flex-wrap items-center justify-between gap-4 border-l-4 border-l-warmGold">
            <div class="flex items-center gap-3">
                <i class="fa-solid fa-wand-magic-sparkles text-warmGold text-xl"></i>
                <div>
                    <h4 class="font-semibold text-xs md:text-sm text-gray-800">Celebração de 1.4 Anos (16 Meses de Amor)</h4>
                    <p class="text-xs text-gray-500">Podes editar textos ou ajustar a data inicial a qualquer momento!</p>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <label class="text-xs text-gray-600 font-medium">Data do Início:</label>
                <input type="date" id="start-date-input" value="2025-06-21" onchange="updateStartDate(this.value)" class="text-xs p-1.5 rounded-lg border border-rose-200 focus:outline-none focus:ring-1 focus:ring-passionRed bg-white">
            </div>
        </div>

        <!-- 3. CONTADOR DE TEMPO DE NAMORO -->
        <section class="text-center space-y-8 pt-4">
            <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-roseSoft text-passionRed text-xs font-bold uppercase tracking-wider border border-rose-200">
                <i class="fa-solid fa-infinity text-sm"></i>
                <span>1.4 Anos Juntos • 16 Meses Incríveis</span>
            </div>

            <h2 class="font-serif text-3xl md:text-5xl font-bold text-gray-900 leading-tight">
                Já se passaram...
            </h2>

            <!-- Relógio do Amor -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-2xl mx-auto">
                <div class="glass-card p-5 rounded-2xl gold-border transform hover:-translate-y-1 transition-all">
                    <span id="counter-days" class="font-serif text-3xl md:text-5xl font-bold text-deepRose block">00</span>
                    <span class="text-xs uppercase tracking-wider text-gray-500 font-semibold mt-1 block">Dias</span>
                </div>
                <div class="glass-card p-5 rounded-2xl gold-border transform hover:-translate-y-1 transition-all">
                    <span id="counter-hours" class="font-serif text-3xl md:text-5xl font-bold text-deepRose block">00</span>
                    <span class="text-xs uppercase tracking-wider text-gray-500 font-semibold mt-1 block">Horas</span>
                </div>
                <div class="glass-card p-5 rounded-2xl gold-border transform hover:-translate-y-1 transition-all">
                    <span id="counter-minutes" class="font-serif text-3xl md:text-5xl font-bold text-deepRose block">00</span>
                    <span class="text-xs uppercase tracking-wider text-gray-500 font-semibold mt-1 block">Minutos</span>
                </div>
                <div class="glass-card p-5 rounded-2xl gold-border transform hover:-translate-y-1 transition-all">
                    <span id="counter-seconds" class="font-serif text-3xl md:text-5xl font-bold text-passionRed block">00</span>
                    <span class="text-xs uppercase tracking-wider text-gray-500 font-semibold mt-1 block">Segundos</span>
                </div>
            </div>

            <p contenteditable="true" class="font-serif italic text-base md:text-lg text-gray-600 max-w-xl mx-auto border-b border-rose-200 pb-4 focus:outline-none focus:bg-white/60 rounded p-2">
                "...e nestes 1.4 anos, cada segundo ao teu lado reafirma que és o grande amor da minha vida."
            </p>
        </section>

        <!-- 4. LINHA DO TEMPO VISUAL / GALERIA ROMÂNTICA -->
        <section class="space-y-20">
            <div class="text-center space-y-2">
                <h3 class="font-cursive text-5xl text-passionRed">Nossa Galeria Polaroid</h3>
                <h2 class="font-serif text-3xl md:text-4xl text-gray-800 font-bold">1.4 Anos em Fotografias</h2>
                <div class="w-20 h-1 bg-warmGold mx-auto rounded-full mt-2"></div>
            </div>

            <!-- FOTO 1: O SORRISO -->
            <div class="glass-card rounded-3xl overflow-hidden p-6 md:p-8 grid md:grid-cols-2 gap-8 items-center">
                <div class="relative group polaroid-frame -rotate-2 mx-auto w-full max-w-sm">
                    <div class="aspect-3/4 overflow-hidden rounded bg-roseSoft relative cursor-pointer" onclick="openLightbox('image_7ce6c7.jpg', 'O sorriso que ilumina os meus dias')">
                        <img id="img-moment-1" src="image_7ce6c7.jpg" alt="O sorriso que ilumina os meus dias" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://images.unsplash.com/photo-1522673607200-164d1b6ce486?q=80&w=800&auto=format&fit=crop'">
                        
                        <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center text-white p-4 text-center">
                            <i class="fa-solid fa-expand text-2xl mb-1"></i>
                            <span class="text-xs font-semibold">Clica para ampliar</span>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <span contenteditable="true" class="font-cursive text-2xl text-deepRose block">O sorriso que ilumina os meus dias ✨</span>
                    </div>
                </div>

                <div class="space-y-4">
                    <div class="inline-block px-3 py-1 rounded-full bg-roseSoft text-deepRose text-xs font-bold uppercase tracking-wider">
                        <i class="fa-solid fa-face-smile mr-1"></i>
                        <span>Foto I</span>
                    </div>
                    <h4 contenteditable="true" class="font-serif text-2xl md:text-3xl font-bold text-gray-900 focus:outline-none">
                        O Sorriso Que Ilumina Os Meus Dias
                    </h4>
                    <p contenteditable="true" class="text-gray-600 leading-relaxed text-sm md:text-base focus:outline-none">
                        Olhar para ti e ver esse teu sorriso sincero é a minha maior felicidade. Nestes 1.4 anos juntos, o teu olhar alegre continua a ser o meu refúgio diário e a luz que ilumina qualquer dia.
                    </p>
                    <div class="p-3 bg-roseSoft/60 border-l-4 border-passionRed rounded-r-xl">
                        <p contenteditable="true" class="text-xs md:text-sm text-deepRose font-serif italic focus:outline-none">
                            "A tua alegria é e sempre será a minha maior conquista."
                        </p>
                    </div>
                </div>
            </div>

            <!-- FOTO 2: O CARINHO -->
            <div class="glass-card rounded-3xl overflow-hidden p-6 md:p-8 grid md:grid-cols-2 gap-8 items-center">
                <div class="space-y-4 md:order-1 order-2">
                    <div class="inline-block px-3 py-1 rounded-full bg-roseSoft text-deepRose text-xs font-bold uppercase tracking-wider">
                        <i class="fa-solid fa-heart-pulse mr-1"></i>
                        <span>Foto II</span>
                    </div>
                    <h4 contenteditable="true" class="font-serif text-2xl md:text-3xl font-bold text-gray-900 focus:outline-none">
                        O Teu Carinho Único
                    </h4>
                    <p contenteditable="true" class="text-gray-600 leading-relaxed text-sm md:text-base focus:outline-none">
                        O teu beijo carinhoso na bochecha, o teu abraço quente e a forma doce como me trutas me fazem sentir o homem mais sortudo de todo este mundo.
                    </p>
                    <div class="p-3 bg-roseSoft/60 border-l-4 border-passionRed rounded-r-xl">
                        <p contenteditable="true" class="text-xs md:text-sm text-deepRose font-serif italic focus:outline-none">
                            "O teu carinho único que me faz o homem mais sortudo."
                        </p>
                    </div>
                </div>

                <div class="relative group polaroid-frame rotate-2 mx-auto w-full max-w-sm md:order-2 order-1">
                    <div class="aspect-3/4 overflow-hidden rounded bg-roseSoft relative cursor-pointer" onclick="openLightbox('image_7ce6a6.jpg', 'O teu carinho único que me faz o homem mais sortudo')">
                        <img id="img-moment-2" src="image_7ce6a6.jpg" alt="O teu carinho único que me faz o homem mais sortudo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=800&auto=format&fit=crop'">
                        
                        <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center text-white p-4 text-center">
                            <i class="fa-solid fa-expand text-2xl mb-1"></i>
                            <span class="text-xs font-semibold">Clica para ampliar</span>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <span contenteditable="true" class="font-cursive text-2xl text-deepRose block">O teu carinho único &#128150;</span>
                    </div>
                </div>
            </div>

            <!-- FOTO 3: O BEIJO -->
            <div class="glass-card rounded-3xl overflow-hidden p-6 md:p-8 grid md:grid-cols-2 gap-8 items-center">
                <div class="relative group polaroid-frame -rotate-1 mx-auto w-full max-w-sm">
                    <div class="aspect-3/4 overflow-hidden rounded bg-roseSoft relative cursor-pointer" onclick="openLightbox('image_7ce6e6.jpg', 'O nosso beijo especial')">
                        <img id="img-moment-3" src="image_7ce6e6.jpg" alt="O nosso beijo especial" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=800&auto=format&fit=crop'">
                        
                        <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center text-white p-4 text-center">
                            <i class="fa-solid fa-expand text-2xl mb-1"></i>
                            <span class="text-xs font-semibold">Clica para ampliar</span>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <span contenteditable="true" class="font-cursive text-2xl text-deepRose block">O nosso beijo especial 🔥</span>
                    </div>
                </div>

                <div class="space-y-4">
                    <div class="inline-block px-3 py-1 rounded-full bg-roseSoft text-deepRose text-xs font-bold uppercase tracking-wider">
                        <i class="fa-solid fa-fire-flame-curved mr-1"></i>
                        <span>Foto III</span>
                    </div>
                    <h4 contenteditable="true" class="font-serif text-2xl md:text-3xl font-bold text-gray-900 focus:outline-none">
                        O Nosso Beijo Especial
                    </h4>
                    <p contenteditable="true" class="text-gray-600 leading-relaxed text-sm md:text-base focus:outline-none">
                        Cada beijo nosso carrega todo o amor, cumplicidade e a certeza de que fomos feitos um para o outro. Nestes 1.4 anos, o teu beijo continua a fazer o meu coração acelerar como no primeiro dia.
                    </p>
                    <div class="p-3 bg-roseSoft/60 border-l-4 border-passionRed rounded-r-xl">
                        <p contenteditable="true" class="text-xs md:text-sm text-deepRose font-serif italic focus:outline-none">
                            "Contigo, até o infinito parece pouco tempo para o nosso amor."
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. CARTA DE AMOR INTERATIVA EM 3D -->
        <section class="space-y-8 text-center">
            <div class="space-y-2">
                <h3 class="font-cursive text-5xl text-passionRed">Carta do Meu Coração</h3>
                <h2 class="font-serif text-3xl text-gray-800 font-bold">Carta do Nosso Mesversário de 1.4 Anos ✉️</h2>
                <p class="text-xs text-gray-500">Clica no envelope para abrir e ler a mensagem completa!</p>
            </div>

            <!-- ENVELOPE CONTAINER FLIP 3D -->
            <div class="max-w-2xl mx-auto perspective-1000 cursor-pointer" onclick="toggleCardFlip(this)">
                <div id="envelope-card" class="relative w-full min-h-[520px] rounded-3xl transition-transform duration-700 transform-style-3d shadow-xl">
                    
                    <!-- FRENTE DO ENVELOPE -->
                    <div class="absolute inset-0 w-full h-full rounded-3xl bg-gradient-to-br from-rose-100 via-rose-50 to-white gold-border p-8 flex flex-col items-center justify-center text-center backface-hidden shadow-2xl">
                        <div class="w-20 h-20 rounded-full bg-roseSoft flex items-center justify-center text-passionRed text-4xl mb-4 border border-rose-200 animate-pulse">
                            <i class="fa-solid fa-envelope-open-text"></i>
                        </div>
                        <h4 class="font-serif text-2xl font-bold text-deepRose mb-1">Para o Amor da Minha Vida &#x2764;&#xFE0F;</h4>
                        <p class="text-xs font-semibold text-warmGold uppercase tracking-widest mb-6">Especial 1.4 Anos de Namoro</p>
                        <span class="inline-flex items-center gap-2 text-xs font-semibold px-6 py-3 rounded-full bg-passionRed text-white shadow-md hover:bg-rose-700 transition-colors">
                            <i class="fa-solid fa-hand-pointer"></i> Clica para Abrir a Tua Carta
                        </span>
                    </div>

                    <!-- VERSO / A CARTA REVELADA -->
                    <div class="absolute inset-0 w-full h-full rounded-3xl bg-white border-2 border-rose-200 p-8 flex flex-col justify-between text-left rotate-y-180 backface-hidden shadow-2xl overflow-y-auto">
                        <div class="space-y-4">
                            <div class="flex justify-between items-center border-b border-rose-100 pb-3">
                                <span class="font-cursive text-3xl text-passionRed">Meu amor,</span>
                                <span class="text-xs font-bold text-warmGold uppercase tracking-wider">1.4 Anos</span>
                            </div>
                            
                            <p contenteditable="true" class="text-xs md:text-sm text-gray-700 leading-relaxed font-serif italic focus:outline-none space-y-2">
                                Meu amor, neste nosso Mesversário de 1.4 anos eu sinto-me o homem mais sortudo que já pisou neste mundo, e não acredito como tenho sido a pessoa mais feliz do universo desde que entraste na minha vida. Eu não conseguiria colocar todo o meu amor e o que sinto por ti em algumas palavras, mas tento sempre expressar o máximo que consigo sempre que escrevo um texto para leres, e espero que consigas ter uma dimensão de como és especial para mim e como me fazes bem. A cada dia que passa eu me encanto e fico ansioso com o nosso futuro juntos; pode ser um excesso de otimismo da minha parte, mas só consigo enxergar o quão boa e maravilhosa vai ser a nossa vida daqui a uns anos, morando juntos, vivendo coladinhos, fazendo e pensando tudo juntos. Ao tentar fugir do otimismo exagerado ainda me sinto feliz, pois mesmo se tempos difíceis aparecerem, tenho a absoluta certeza de que és tu quem quero ao meu lado nos momentos complicados, pois sei que superamos sempre tudo e o nosso final vai ser o mais feliz e iluminado possível. Enquanto reviso este texto no meio do meu estágio, não consigo deixar de pensar em como esta rotina exigente de faculdade e trabalho seria melhor se no fim do dia estivesses à minha espera ao voltar para casa. Este sentimento é uma mistura de saudade por essa ainda não ser a nossa realidade agora, mas de felicidade também, pois o amor que sinto por ti enche-me de razões para viver.
                            </p>
                        </div>
                        <div class="text-right pt-4 border-t border-rose-100 mt-4">
                            <span contenteditable="true" class="font-cursive text-2xl text-deepRose block">Para Sempre Teu &#x2764;&#xFE0F;</span>
                            <span class="text-xs text-gray-400">Clica para fechar a carta</span>
                        </div>
                    </div>

                </div>
            </div>
        </section>
    </main>

    <!-- LIGHTBOX MODAL PARA EXPANDIR FOTOS -->
    <div id="lightbox-modal" class="fixed inset-0 z-50 bg-black/90 hidden backdrop-blur-md flex flex-col items-center justify-center p-4" onclick="closeLightbox()">
        <button class="absolute top-6 right-6 text-white text-3xl hover:text-rose-400 transition-colors">
            <i class="fa-solid fa-xmark"></i>
        </button>
        <div class="max-w-3xl max-h-[80vh] p-2 bg-white rounded-2xl shadow-2xl overflow-hidden" onclick="event.stopPropagation()">
            <img id="lightbox-img" src="" alt="Foto Ampliada" class="max-w-full max-h-[70vh] object-contain rounded-xl mx-auto">
            <p id="lightbox-caption" class="text-center font-cursive text-2xl text-deepRose mt-3 pb-1"></p>
        </div>
    </div>

    <!-- RODAPÉ -->
    <footer class="relative z-10 border-t border-rose-100 py-6 text-center text-xs text-gray-500 bg-white/60">
        <p>Comemoração do Nosso Mesversário de 1.4 Anos ✨ Feito com todo o amor do mundo!</p>
    </footer>

    <!-- LÓGICA JAVASCRIPT INTERATIVA -->
    <script>
        function openOurWorld() {
            const overlay = document.getElementById('welcome-overlay');
            if (overlay) {
                overlay.style.opacity = '0';
                setTimeout(() => {
                    overlay.style.display = 'none';
                }, 1000);
            }
            triggerLoveShower();
        }

        function openLightbox(src, caption) {
            const modal = document.getElementById('lightbox-modal');
            document.getElementById('lightbox-img').src = src;
            document.getElementById('lightbox-caption').innerText = caption;
            modal.classList.remove('hidden');
        }

        function closeLightbox() {
            document.getElementById('lightbox-modal').classList.add('hidden');
        }

        let loveStartDate = new Date('2025-06-21T00:00:00');

        function updateStartDate(newDateString) {
            if (newDateString) {
                loveStartDate = new Date(newDateString + 'T00:00:00');
                calculateLoveTime();
            }
        }

        function calculateLoveTime() {
            const now = new Date();
            const diffMs = now - loveStartDate;

            if (diffMs < 0) {
                document.getElementById('counter-days').innerText = '00';
                document.getElementById('counter-hours').innerText = '00';
                document.getElementById('counter-minutes').innerText = '00';
                document.getElementById('counter-seconds').innerText = '00';
                return;
            }

            const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diffMs / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((diffMs / (1000 * 60)) % 60);
            const seconds = Math.floor((diffMs / 1000) % 60);

            document.getElementById('counter-days').innerText = String(days).padStart(2, '0');
            document.getElementById('counter-hours').innerText = String(hours).padStart(2, '0');
            document.getElementById('counter-minutes').innerText = String(minutes).padStart(2, '0');
            document.getElementById('counter-seconds').innerText = String(seconds).padStart(2, '0');
        }

        setInterval(calculateLoveTime, 1000);
        calculateLoveTime();

        let isPlayerVisible = true;
        function togglePlayer() {
            const container = document.getElementById('spotify-player-container');
            const toggleText = document.getElementById('player-toggle-text');
            
            if (isPlayerVisible) {
                container.style.display = 'none';
                toggleText.innerText = 'Mostrar Leitor';
                isPlayerVisible = false;
            } else {
                container.style.display = 'block';
                toggleText.innerText = 'Ocultar Leitor';
                isPlayerVisible = true;
            }
        }

        function toggleCardFlip(element) {
            const card = document.getElementById('envelope-card');
            if (card) {
                card.classList.toggle('rotate-y-180');
            }
        }

        function triggerLoveShower() {
            if (typeof confetti === 'function') {
                var scalar = 2;
                var heart = confetti.shapeFromText({ text: '❤️', scalar });

                confetti({
                    shapes: [heart],
                    particleCount: 45,
                    spread: 120,
                    origin: { y: 0.65 },
                    scalar: 2
                });
            }
        }

        const canvas = document.getElementById('heart-canvas');
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        const hearts = [];
        const heartCount = 22;

        class FloatingHeart {
            constructor() {
                this.reset();
            }
            reset() {
                this.x = Math.random() * canvas.width;
                this.y = canvas.height + Math.random() * 80;
                this.size = Math.random() * 14 + 8;
                this.speedY = Math.random() * 0.9 + 0.4;
                this.opacity = Math.random() * 0.4 + 0.2;
                this.swing = Math.random() * 0.02;
                this.swingAngle = Math.random() * Math.PI * 2;
            }
            update() {
                this.y -= this.speedY;
                this.swingAngle += this.swing;
                this.x += Math.sin(this.swingAngle) * 0.4;
                if (this.y < -20) {
                    this.reset();
                }
            }
            draw() {
                ctx.save();
                ctx.globalAlpha = this.opacity;
                ctx.font = `${this.size}px sans-serif`;
                ctx.fillText('❤️', this.x, this.y);
                ctx.restore();
            }
        }

        for (let i = 0; i < heartCount; i++) {
            hearts.push(new FloatingHeart());
        }

        function animateHearts() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            hearts.forEach(h => {
                h.update();
                h.draw();
            });
            requestAnimationFrame(animateHearts);
        }
        animateHearts();
    </script>
</body>
</html>"""

# Renderiza o conteúdo HTML via Streamlit
components.html(get_html_content(), height=3500, scrolling=True)
