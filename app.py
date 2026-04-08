import streamlit as st
import numpy as np
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="KUYApaie HQ", layout="wide", page_icon="📊")

# --- 1. INITIALISATION DE L'ÉTAT ---
if 'connected' not in st.session_state:
    st.session_state['connected'] = False

# --- 2. FONCTIONS DE CALCUL BCC ---
def analyze_bcc(rate):
    """Logique de calcul des zones Green/Orange/Red"""
    if rate <= 0.95:
        return "🟢 GREEN ZONE", "Optimal - Performance stable", "normal"
    elif 0.95 < rate <= 1.20:
        return "🟠 ORANGE ZONE", "Alerte - Surveillance requise", "inverse"
    else:
        return "🔴 RED ZONE", "Critique - Risque élevé", "normal"

# --- 3. INTERFACE DE CONNEXION ET ABONNEMENT ---
if not st.session_state['connected']:
    st.title("🚀 KUYApaie HQ - Plateforme Data")
    
    tab_login, tab_sub = st.tabs(["🔐 Connexion Membre", "📲 Devenir Abonné (Mobile Money)"])

    with tab_login:
        st.subheader("Accès sécurisé")
        user = st.text_input("Identifiant")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter", use_container_width=True):
            # Liste des accès (Tu peux en ajouter ici)
            if user == "admin" and password == "Kuyapaie2026":
                st.session_state['connected'] = True
                st.session_state['user'] = user
                st.success("Connexion réussie !")
                st.rerun()
            else:
                st.error("Identifiants incorrects ou compte expiré.")

    with tab_sub:
        st.subheader("💳 Acheter un accès via Mobile Money")
        st.write("Choisissez votre forfait pour débloquer les analyses BCC en temps réel.")
        
        forfait = st.radio("Sélectionnez votre offre :", 
                          ["Pass 24h - 5$", "Pass Mensuel - 50$", "Pass Annuel - 450$"])
        
        # REMPLACE CE LIEN par ton lien Flutterwave ou Paystack plus tard
        url_paiement = "https://flutterwave.com/pay/kuyapaie_access" 

        st.info(f"Forfait sélectionné : **{forfait}**")
        
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Payer par Mobile Money 📲", url_paiement, type="primary", use_container_width=True)
            st.caption("Orange Money, M-Pesa, Airtel Money, Visa/Mastercard")
        
        with c2:
            st.write("**Procédure :**")
            st.write("1. Cliquez sur le bouton de paiement.")
            st.write("2. Finalisez l'opération sur votre téléphone.")
            st.write("3. Envoyez l'ID de transaction via WhatsApp.")

        st.divider()
        st.write("📧 **Support Technique & Validation :**")
        st.write("WhatsApp : **+243 XXX XXX XXX**")

# --- 4. INTERFACE APPRÈS CONNEXION (Dashboard) ---
else:
    # Barre latérale de navigation
    st.sidebar.title(f"👤 {st.session_state['user']}")
    if st.sidebar.button("Se déconnecter"):
        st.session_state['connected'] = False
        st.rerun()

    st.title("📊 Tableau de Bord - Analyses BCC")
    st.write("Bienvenue dans votre espace membre privilégié.")

    # Section Calculateur
    st.divider()
    st.subheader("🔎 Analyseur de Taux en Temps Réel")
    
    val_rate = st.number_input("Saisir le taux BCC à analyser :", min_value=0.0, value=1.0, step=0.01)
    
    zone, msg, col_logic = analyze_bcc(val_rate)
    
    # Affichage visuel des zones
    res1, res2 = st.columns([1, 2])
    with res1:
        st.metric(label="Statut du Taux", value=zone, delta=f"{val_rate:.2f}", delta_color=col_logic)
    with res2:
        if "GREEN" in zone:
            st.success(msg)
        elif "ORANGE" in zone:
            st.warning(msg)
        else:
            st.error(msg)

    # Graphique de tendance (Exemple)
    st.subheader("📈 Historique des Fluctuations")
    chart_data = pd.DataFrame(np.random.randn(15, 1) * 0.05 + val_rate, columns=['Taux'])
    st.line_chart(chart_data)
