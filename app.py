import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Nosso 1.4 Anos de Amor 💖",
    page_icon="💌",
    layout="centered"
)

# Estilo personalizado com CSS
st.markdown("""
    <style>
    .main {
        background-color: #fff5f7;
    }
    .stApp {
        background: linear-gradient(135deg, #fff5f7 0%, #ffe6ea 100%);
    }
    .title-text {
        color: #d63384;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: bold;
    }
    .subtitle-text {
        color: #6c757d;
        text-align: center;
        margin-bottom: 30px;
    }
    .letter-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(214, 51, 132, 0.15);
        border: 2px solid #f8d7da;
        line-height: 1.8;
        font-size: 1.15rem;
        color: #2c3e50;
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# Animação de corações / chuva de festejos
st.snow()  # Efeito visual suave

# Título principal
st.markdown("<h1 class='title-text'>❤️ Feliz 1.4 Anos de Namoro! ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Uma declaração especial para o amor da minha vida</p>", unsafe_allow_html=True)

# Texto completo
texto_amor = """Meu amor, nesse nosso MesVersário de 1.4 anos eu me sinto o homem mais sortudo que já pisou nesse mundo, e não acredito como venho sendo a pessoa mais feliz do universo desde que voce entrou na minha vida. Eu não possivelmente conseguria colocar todo meu amor e oque sinto por voce em algumas palavras, mas sempre tento expressar o maximo que consigo sempre que escrevo texto para voce ler, e espero que voce consiga ter uma dimensão de como voce é especial para mim e como voce me faz bem. A cada dia que passa eu me encanto e fico ansioso com nosso futuro juntos, pode ser um excesso de otimismo da minha parte mas só consigo enxergar o quão boa e gostosa vai ser nossa vida daqui a uns anos, morando juntos, vivendo coladinhas, fazendo e pensando tudo juntos. Ao tentar fugir do otimismo exagerado eu ainda me sinto feliz pois mesmo se tempos ruins aparecerem eu tenho a absoluta certeza que é você que quero do meu lado nas complicações e baixos, pois sei que sempre superamos tudo e nosso final vai ser o mais feliz e iluminado possível. Enquanto reviso esse texto no meio do meu estágio eu não consigo pensar em como essa rotina puxada de faculdade e trabalho seria melhor se no fim do dia você estivesse me esperando voltar para casa todo dia, esse sentimento é uma mistura de tristeza por essa não ser nossa realidade agora, mas de felicidade também pois o amor que sinto por você me enche de razões para viver."""

# Abas interativas para exibição
tab1, tab2, tab3 = st.tabs(["💌 Carta Completa", "📖 Leitura Retrátil", "📝 Caixa de Texto"])

with tab1:
    st.subheader("Carta de Amor 💖")
    st.markdown(f'<div class="letter-box">{texto_amor}</div>', unsafe_allow_html=True)

with tab2:
    with st.expander("Clique para abrir e ler o texto", expanded=True):
        st.write(texto_amor)

with tab3:
    st.text_area(
        label="Texto em caixa com rolagem:",
        value=texto_amor,
        height=300
    )

st.markdown("---")
if st.button("Clique para receber um carinho virtual 💖"):
    st.balloons()
    st.success("Te amo infinitamente! Obrigado por cada segundo ao meu lado. 💕")
