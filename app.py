import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Nosso 1.4 Anos de Amor 💖",
    page_icon="💖",
    layout="centered"
)

# Estilos CSS customizados para visual romântico
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 50%, #ffb3c1 100%);
    }
    .main-title {
        color: #c9184a;
        text-align: center;
        font-family: 'Georgia', serif;
        font-weight: bold;
        font-size: 2.4rem;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #800f2f;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .letter-box {
        background-color: #ffffffd6;
        backdrop-filter: blur(5px);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(201, 24, 74, 0.15);
        border: 2px solid #ff4d6d;
        line-height: 1.8;
        font-size: 1.15rem;
        color: #590d22;
        white-space: pre-wrap;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Efeito especial de entrada
st.snow()

# Cabeçalho
st.markdown("<h1 class='main-title'>💖 Feliz 1.4 Anos de Amor! 💖</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Nossa história, nossas memórias e todo o meu amor em um só lugar</p>", unsafe_allow_html=True)

# --- 1. MÚSICA DE FUNDO / PLAYER DE ÁUDIO ---
st.subheader("🎵 Nossa Trilha Sonora")
st.write("Aperte o play para ouvir a música enquanto lê a carta e vê nossas fotos:")

# Opção 1: Enviar um arquivo .mp3 direto pela interface
audio_file = st.file_uploader("🎵 Envie a música de vocês (.mp3):", type=["mp3", "wav"])

if audio_file is not None:
    st.audio(audio_file, format="audio/mp3")
else:
    # Tenta carregar um arquivo local 'musica.mp3' se existir na mesma pasta
    try:
        st.audio("musica.mp3", format="audio/mp3")
    except:
        # Link de áudio demonstrativo (substitua pelo link da sua música favorita ou arquivo local 'musica.mp3')
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.markdown("---")

# --- 2. ÁLBUM DE FOTOS / GALERIA ---
st.subheader("📸 Nosso Álbum de Memórias")

uploaded_images = st.file_uploader("📸 Adicione fotos do casal para o álbum:", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_images:
    cols = st.columns(min(len(uploaded_images), 3))
    for idx, img in enumerate(uploaded_images):
        with cols[idx % 3]:
            st.image(img, use_column_width=True, caption=f"Momento Especial ❤️")
else:
    # Fotos demonstrativas / inspiração (coloque o caminho das suas imagens locais ou URLs)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=500", caption="Momentos Inesquecíveis ❤️", use_column_width=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=500", caption="Sorrisos e Felicidade 💕", use_column_width=True)
    with col3:
        st.image("https://images.unsplash.com/photo-1522673607200-164d1b6ce486?q=80&w=500", caption="Nosso Futuro Juntos ✨", use_column_width=True)

st.caption("💡 *Dica:* Você pode fazer o upload das fotos reais do casal pelo botão acima ou colocar arquivos de imagem (.jpg/.png) na mesma pasta do código!")

st.markdown("---")

# --- 3. CARTA DE AMOR COMPLETA ---
st.subheader("💌 Minha Carta Para Você")

texto_amor = """Meu amor, nesse nosso MesVersário de 1.4 anos eu me sinto o homem mais sortudo que já pisou nesse mundo, e não acredito como venho sendo a pessoa mais feliz do universo desde que voce entrou na minha vida. Eu não possivelmente conseguria colocar todo meu amor e oque sinto por voce em algumas palavras, mas sempre tento expressar o maximo que consigo sempre que escrevo texto para voce ler, e espero que voce consiga ter uma dimensão de como voce é especial para mim e como voce me faz bem. A cada dia que passa eu me encanto e fico ansioso com nosso futuro juntos, pode ser um excesso de otimismo da minha parte mas só consigo enxergar o quão boa e gostosa vai ser nossa vida daqui a uns anos, morando juntos, vivendo coladinhas, fazendo e pensando tudo juntos. Ao tentar fugir do otimismo exagerado eu ainda me sinto feliz pois mesmo se tempos ruins aparecerem eu tenho a absoluta certeza que é você que quero do meu lado nas complicações e baixos, pois sei que sempre superamos tudo e nosso final vai ser o mais feliz e iluminado possível. Enquanto reviso esse texto no meio do meu estágio eu não consigo pensar em como essa rotina puxada de faculdade e trabalho seria melhor se no fim do dia você estivesse me esperando voltar para casa todo dia, esse sentimento é uma mistura de tristeza por essa não ser nossa realidade agora, mas de felicidade também pois o amor que sinto por você me enche de razões para viver."""

# Exibição do texto formatado com estilo elegante de carta
st.markdown(f'<div class="letter-box">{texto_amor}</div>', unsafe_allow_html=True)

# --- 4. BOTOES INTERATIVOS DE SURPRESA ---
st.markdown("---")
col_b1, col_b2 = st.columns(2)
with col_b1:
    if st.button("🎉 Celebrar Nosso Amor"):
        st.balloons()
        st.success("1.4 anos de muitos que virão! Te amo infinitamente! 💕")
with col_b2:
    if st.button("✨ Um Desejo para o Futuro"):
        st.snow()
        st.info("Mal posso esperar para estarmos morando juntos todo dia! 🏠❤️")
