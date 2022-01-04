from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Meu Site", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Usar loca CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("C:/Users/pablo/Documents/github/Site_Pablo/style/style.css")


# -------------------- CARREGAR ASSETS ----------
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_buopyjyz.json")
img_contact_form = Image.open("C:/Users/pablo/Documents/github/Site_Pablo/images/4616175.png")
image_yt_data = Image.open("C:/Users/pablo/Documents/github/Site_Pablo/images/oRJEmL95ph0-HD.jpg")


# --------
with st.container():
    st.subheader("Olá, sou o Pablo :wave:")
    st.title("Um estudante de Ciências Economicas")
    st.write("Sou apaixonado por análise de dados e automação de processos para gerar mais eficiência.")
    st.write("[Veja mais >](https://github.com/Cenismo)")


# ----- O que eu faço

with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("O que eu faço?")
            st.write("##")
            st.write(
                """
                No meu github eu publico algumas das coisas que faço no meu estágio e no meu tempo livre
                - Crio projetos com a intenção de agilizar o trabalho
                - Faço extração e análise de dados
                
                
                
                
                """
            )
            st.write("[Youtube Channel >](https://www.linkedin.com/in/datapablo/)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


# ------ Projetos ------
with st.container():
    st.write("---")
    st.header("Meus Pojetos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_yt_data)
    with text_column:
        st.subheader("Variáveis aleatórias, discretas e continuas")
        st.write(
            """
            Aprenda a como interpretar e diferenciar estes três tipos de variáveis
            
            
            """
        )
        st.markdown("[Assista...](https://www.youtube.com/watch?v=oRJEmL95ph0&t=18s)")


# --- CONTATO ---

with st.container():
    st.write("---")
    st.header("Entre em contato comigo")
    st.write("##")


    # Documention:
    contact_form = """
    <form action="https://formsubmit.co/pablors.microcamp@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Seu nome" required>
         <input type="email" name="email" placeholder="Seu e-mail" required>
         <textarea name ="mensagem" placeholder="Escreva sua mensagem" required></textarea>
         <button type="submit">Send</button>
   </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


