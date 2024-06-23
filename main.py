import streamlit as st
import requests
import os

st.header ("Aplicacion Postres Saludables") 
consulta = st.text_input("Ingrese su consulta")

if st.button('Enviar consulta'):
      st.write(consulta)
      
base_url = "https://api.dify.ai/v1"
path = "/completion-messages"

my_secret = os.environ['DIFY_APP_SECRET']

headers = {
'Authorization': f'Bearer {my_secret}', 
 'Content-Type': 'application/json' 
}

data = {
      "inputs": {"text": "consuta"},
      "response_mode": "blocking",
      "user": "ilepostres2"
  }

response = requests.post(f'{base_url}{path}', json=data, headers=headers)

if response.status_code == 200:
      st.success('Consulta enviada con exito')
      st.json(response.json())
      
result = response.json()
st.markdown('### Resultado de la solicitud:')
st.markdown(result['answer'])


      







