import streamlit as st
import snakefile
import zipfile
import shutil
import io
import os
optimized = False

with open("BC.zip", "rb") as file:
    button = st.download_button(
                    label="Baixar arquivo de exemplo",
                    data=file,
                    file_name="data.zip",
                    mime="application/zip"
                ),


data = st.file_uploader("Selecione o zip de arquivos", type="zip")
config = st.file_uploader("Selecione o arquivo de configuração do oToole")
model = st.file_uploader("Selecione o modelo OSeMOSYS")
script = st.file_uploader("Selecione o script de preprocessamento")

model = "model_BCNexus.txt"
processedModel = "processedModel.txt"
config = "configs/otoole_config.yaml"
script = "preprocess.py"
processedData = "processedData.txt"
output = "results/output.lp"

optimizer = snakefile.OSeMOSYS()

def unpack(data, temp_dir):
    os.makedirs(temp_dir, exist_ok=True)

    zip_contents = data.read()

    with zipfile.ZipFile(io.BytesIO(zip_contents), 'r') as zip_ref:
        zip_ref.extractall(temp_dir)


    data = os.listdir(temp_dir)

    st.success("Arquivo descompactado com sucesso!")

    return data[0]

dataPath = None
if st.button("Descompactar"):    
    if data is not None:
        dataPath = unpack(data, "data")

dataDir = "data/BC"

if st.button("Otimizar"):
    model = "assets\models\model.txt"
    processedModel = "assets\models\processed\processedModel.txt"
    config = "assets/configs/otoole_config.yaml"
    combedData = "assets\data\combedData.txt"
    script = "preprocess.py"
    processedData = "assets\data\processedData.txt"
    output = "results/output.lp"
    processedOutput = "processedOutput.txt"
    optimizeLog = True
    if dataDir:
        optimizer.optimize(dataDir, model, config, combedData, processedData, script, output, processedModel, processedOutput, optimizeLog)
        optimized = True
    else:
        st.error("Nenhum arquivo selecionado")

if optimized:
    with open("results/output.lp", "rb") as file:
        btn = st.download_button(
                label="Baixar arquivo otimizado",
                data=file,
                file_name="output.lp",
                mime="df/lp"
            )