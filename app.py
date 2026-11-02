import os
import subprocess
import traceback
import streamlit as st

st.set_page_config(page_title="Spotify Downloader", page_icon="🎵")

st.title("🎵 Meu Downloader do Spotify")
st.write("Cole o link da música ou playlist do Spotify abaixo e clique em baixar.")

# Campo para colar o link na tela
link = st.text_input("Link do Spotify:")

if st.button("Baixar Música / Playlist"):
    if not link:
        st.warning("Por favor, cole um link válido antes de continuar.")
    else:
        with st.spinner("Baixando as músicas... Aguarde, isso pode levar alguns segundos."):
            try:
                # Define a pasta de Downloads oficial do Windows
                pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
                pasta_destino = os.path.join(pasta_downloads, "Musicas_Baixadas")
                
                os.makedirs(pasta_destino, exist_ok=True)
                os.chdir(pasta_destino)

                caminho_atual = os.path.abspath(".")
                
                # Executa o spotdl usando o mesmo comando do seu script
                comando = f'python -m spotdl "{link}"'
                resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

                if resultado.returncode == 0:
                    st.success(f"Concluído com sucesso! Suas músicas estão salvas na pasta: {caminho_atual}")
                else:
                    st.error("O comando falhou. Verifique se o link está correto ou se o spotdl está instalado.")
                    st.text(resultado.stderr) # Mostra o erro técnico se houver
                    
            except Exception as e:
                st.error("Ocorreu um erro fatal durante a execução:")
                st.text(traceback.format_exc())