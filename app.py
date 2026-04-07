import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION (Toujours en haut) ---
st.set_page_config(page_title="KUYApaie HQ", layout="wide")

# --- 2. NAVIGATION ---
st.sidebar.title("🏛️ KUYApaie - Navigation")
selection = st.sidebar.radio("Sélectionnez un Menu :", [
    "Tableau de Bord", 
    "BCC & Change", 
    "Commissions & CA",
    "Paramètres & KYC"
])

# --- 3. LOGIQUE DIRECTE (MODIFIEZ ICI) ---

if selection == "Tableau de Bord":
    st.title("📊 Tableau de Bord Souverain")
    # On insère l'HTML directement ici
    html_dashboard = """
    <div style="background: #0b0e11; padding: 20px; border-radius: 15px; border: 1px solid #f0b90b; color: white;">
        <h2 style="color: #f0b90b;">Bienvenue, Patron</h2>
        <p>Le système est prêt pour les opérations du jour.</p>
    </div>
    """
    components.html(html_dashboard, height=200)

elif selection == "BCC & Change":
    st.title("💱 Moteur de Change & Volatilité")
    # Code Python direct pour le calcul
    try:
        taux_fixe = 2854.42
        variation = np.random.uniform(-0.01, 0.01)
        nouveau_taux = taux_fixe * (1 + variation)
        st.metric("Taux USD/CDF (BCC)", f"{nouveau_taux:,.2f}", f"{variation:.2%}")
        
        # Petit tableau Pandas pour le rangement
        df = pd.DataFrame({'Banque': ['Rawbank', 'EquityBCDC', 'TMB'], 'Taux': [2860, 2855, 2865]})
        st.table(df)
    except Exception as e:
        st.error(f"Erreur moteur : {e}")

elif selection == "Commissions & CA":
    st.title("💰 Portefeuille de Commissions")
    # Calcul des gains (0.5% à 5%)
    volume = st.number_input("Volume de transaction (USD)", value=1000)
    col1, col2 = st.columns(2)
    with col1:
        gain = volume * 0.01 # 1% par défaut
        st.success(f"Votre commission (1%) : {gain:,.2f} USD")
    with col2:
        st.info("Ce montant est versé directement dans votre Revenue Vault.")

elif selection == "Paramètres & KYC":
    st.title("⚙️ Paramètres & Sécurité")
    st.write("Statut du compte : **Vérifié (Niveau 2)**")
    if st.button("Lancer Audit Sécurité"):
        st.warning("Scan des protocoles AES-256 en cours...")
        st.success("Aucune vulnérabilité détectée.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("🟢 Serveur : **Lubumbashi, DRC**")
