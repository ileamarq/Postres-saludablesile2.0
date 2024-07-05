import streamlit as st
import requests
import os

st.header("Asistente para obtener Postres Saludables")

text = st.text_area("Ingresa uno o varios ingredientes:")

my_secret = os.environ['DIFY_APP_SECRET']


headers = {
    'Authorization': f'Bearer {my_secret}',
    'Content-Type': 'application/json'
}

data = {
    "inputs": {
        "text": text
    },
    "response_mode": "blocking",
    "user": "ilepostres2"
}

if st.button('Consultar'):
    base_url = "https://api.dify.ai/v1"
    path = "/completion-messages"
    response = requests.post(base_url + path, json=data, headers=headers)
                       
    if response.status_code == 200:
          st.success('Consulta enviada con exito')
    
    result = response.json()
    st.markdown('### Resultado de la solicitud:')
    st.markdown(result['answer'])

    print(response.content)

    st.write("¡Gracias por usar la aplicación! ¡Hasta luego!")
