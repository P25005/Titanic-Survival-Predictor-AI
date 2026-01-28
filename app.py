import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. CARGA DEL MODELO
# -------------------------------------------
try:
    modelo = joblib.load('modelo_titanic.pkl')
except:
    st.error("⚠️ No encuentro el archivo 'modelo_titanic.pkl'. Asegúrate de que está en la misma carpeta.")
    st.stop()

# 2. INTERFAZ: TÍTULO Y DESCRIPCIÓN
# -------------------------------------------
st.title("🚢 Titanic AI: ¿Sobrevivirías?")
st.markdown("""
Esta Inteligencia Artificial ha aprendido patrones de **891 pasajeros reales**.
Introduce tus datos y descubre tu destino.
""")

# 3. INTERFAZ: BARRA LATERAL (INPUTS)
# -------------------------------------------
st.sidebar.header("Tus Datos de Pasajero")

# --- AQUI SE DEFINEN LAS VARIABLES (IMPORTANTE EL ORDEN) ---
edad = st.sidebar.slider("Tu Edad", 0, 100, 30)
sexo = st.sidebar.radio("Tu Sexo", ["Hombre", "Mujer"])
clase_social = st.sidebar.selectbox("Clase del Billete", ["Primera (Cara)", "Segunda", "Tercera (Barata)"])
puerto = st.sidebar.selectbox("Puerto de Embarque", ["Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"])
# Añadimos estos para evitar el error anterior, aunque los dejamos ocultos/fijos por simplicidad
viaja_solo = st.sidebar.checkbox("¿Viajas solo?", value=True)


# 4. LÓGICA DE NEGOCIO (TRANSFORMACIÓN DE DATOS)
# -------------------------------------------

# Convertir Clase Social a número (Pclass)
pclass = 3
if clase_social == "Primera (Cara)":
    pclass = 1
elif clase_social == "Segunda":
    pclass = 2

# Convertir Sexo a número
sex_num = 1 if sexo == "Hombre" else 0

# Convertir Puerto a One-Hot Encoding
embarked_Q = 1 if puerto == "Queenstown (Q)" else 0
embarked_S = 1 if puerto == "Southampton (S)" else 0

# Definir precio (Fare) estimado según clase
fare = 15 # Precio base
if pclass == 1:
    fare = 150
elif pclass == 2:
    fare = 60

# Definir familiares (SibSp y Parch)
sibsp = 0
parch = 0
if not viaja_solo:
    sibsp = 1 # Ponemos 1 por defecto si no viaja solo para simular

# 5. PREPARAR DATOS PARA LA IA
# -------------------------------------------
# El orden de las columnas debe coincidir con el entrenamiento.
# Basado en tu limpieza anterior, el orden probable es este. 
# Si falla, miraremos tu X_train.columns
columnas = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S']

input_data = pd.DataFrame([[pclass, sex_num, edad, sibsp, parch, fare, embarked_Q, embarked_S]],
                          columns=columnas)

# Mostramos los datos técnicos (útil para depurar)
st.write("Datos procesados que recibe el modelo:", input_data)

# 6. PREDICCIÓN
# -------------------------------------------
if st.button("CALCULAR DESTINO 🔮"):
    try:
        prediction = modelo.predict(input_data)
        probability = modelo.predict_proba(input_data)
        
        # probability devuelve [[prob_0, prob_1]] -> prob_1 es vivir
        prob_vivir = probability[0][1]
        
        st.divider() # Línea separadora
        
        if prediction[0] == 1:
            st.success(f"¡SOBREVIVES! 🟢")
            st.write(f"Probabilidad de supervivencia: **{prob_vivir:.1%}**")
            st.balloons()
        else:
            st.error(f"FALLECES 🔴")
            st.write(f"Probabilidad de supervivencia: **{prob_vivir:.1%}**")
            st.info("💡 Consejo: Prueba a cambiar a 'Mujer' o a 'Primera Clase' para ver cómo cambia la predicción.")
            
    except Exception as e:
        st.error(f"Error en la predicción: {e}")
        st.warning("Posible causa: El orden de columnas no coincide con tu modelo entrenado.")