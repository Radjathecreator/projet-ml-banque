import streamlit as st
import joblib

# Chargement du modèle
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

artefact = load_model()
modele = artefact["model"]
version_modele = artefact["version"]

# Interface visuelle
st.title("Outil de Détection de Fraude Bancaire")
st.write("Veuillez entrer les informations de la transaction ci-dessous :")

amt = st.number_input("Montant de la transaction ($)", min_value=0.0, value=100.0)
city_pop = st.number_input("Population de la ville", min_value=0, value=50000)
gender = st.selectbox("Genre du client", options=[0, 1], format_func=lambda x: "Homme (1)" if x == 1 else "Femme (0)")

# Prédiction
if st.button("Lancer l'analyse"):
    donnees_entree = [[amt, city_pop, gender]]
    prediction = modele.predict(donnees_entree)[0]
    
    st.markdown("---")
    if prediction == 1:
        st.error("ALERTE : Transaction suspecte (Fraude potentielle) !")
    else:
        st.success("Transaction normale (Aucune anomalie détectée).")
        
    st.info(f"Information technique - Version du modèle : {version_modele}")
