# 🚢 Titanic Survival Predictor | Web App de Machine Learning

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Model-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 🚀 Demo en Vivo

¡Prueba la aplicación directamente en la nube sin instalar nada!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://titanic-survival-predictor-ai-p25005.streamlit.app/) 
*(Haz clic el botón de arriba para ver la demo)*

---

## 📋 Descripción General

**Titanic Survival Predictor** es una aplicación web interactiva que utiliza Machine Learning para predecir la probabilidad de supervivencia de un pasajero en el Titanic.

Este proyecto une el mundo de la **Ciencia de Datos** con el **Desarrollo Web**, desplegando un modelo **Random Forest Classifier** entrenado con datos históricos reales. La aplicación demuestra habilidades de desarrollo "End-to-End", desde el preprocesamiento de datos hasta el despliegue del modelo en un entorno productivo.

> *Diseñado y desarrollado por un estudiante de Desarrollo de Aplicaciones Multiplataforma/Web (DAM/DAW).*

---

## ✨ Características Clave

-   **🤖 Motor de Inferencia ML**: Utiliza un modelo `Random Forest` pre-entrenado (`modelo_titanic.pkl`) para realizar predicciones en tiempo real.
-   **📊 Interfaz Interactiva**: Construida con **Streamlit**, permite la manipulación de variables (edad, clase, puerto) con feedback instantáneo.
-   **🧠 Procesamiento Inteligente**: El backend transforma automáticamente los inputs del usuario (One-Hot Encoding, normalización) al formato vectorial que requiere el modelo.
-   **📉 Visualización de Probabilidad**: No solo predice vivo/muerto, sino que calcula y muestra el porcentaje exacto de confianza del modelo.
-   **⚡ Feedback Visual**: Uso de componentes dinámicos como globos y mensajes de estado para mejorar la experiencia de usuario (UX).

---

## #️⃣ Stack Tecnológico

| Categoría | Tecnologías |
|----------|-------------|
| **Lenguaje** | Python 3.10+ |
| **Frontend** | Streamlit |
| **Librerías ML** | Scikit-learn, Joblib, Pandas, NumPy |
| **Visualización** | Matplotlib |
| **Serialización** | Pickle (.pkl) |

---

## 📂 Estructura del Proyecto

```bash
titanic-ai-demo/
├── 📄 app.py              # Punto de entrada principal (Lógica Streamlit)
├── 📦 modelo_titanic.pkl  # Modelo Random Forest serializado
├── 📄 requirements.txt    # Dependencias del proyecto
└── 📄 README.md           # Documentación
```

---

## 🔧 Instalación y Ejecución Local

Si prefieres ejecutar el código en tu propia máquina:

### 1. Clonar el repositorio
```bash
git clone https://github.com/P25005/Titanic-Survival-Predictor-AI.git
cd Titanic-Survival-Predictor-AI
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en `http://localhost:8501`.

---

## 🧠 Insights del Modelo

El modelo ha sido entrenado analizando patrones en el dataset oficial del Titanic, ponderando factores críticos:
-   **Clase Social (Pclass)**: El estatus socioeconómico fue determinante.
-   **Sexo (Sex)**: Las mujeres tuvieron prioridad en los botes salvavidas ("Mujeres y niños primero").
-   **Edad (Age)**: Factor cruzar para la supervivencia.
-   **Tarifa (Fare)**: Correlacionada con la ubicación de los camarotes.

La aplicación realiza ingeniería de características interna para convertir datos humanos (ej: "Queenstown") en tensores matemáticos (`[0, 1]`) que el modelo puede interpretar.

---

## 👤 Autor

**Pau Mateo**  
*Estudiante de Desarrollo de Aplicaciones Multiplataforma y Web (DAM/DAW)*

Conecta conmigo en [LinkedIn](https://www.linkedin.com/in/pau-mateo-150471262/) | Mira mi [GitHub](https://github.com/P25005)
