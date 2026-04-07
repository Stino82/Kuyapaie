import streamlit as st

# 1. CONFIGURATION DE LA PLATEFORME
st.set_page_config(
    page_title="KUYApaie - Global Dashboard",
    page_icon="🏛️",
    layout="wide"
)

# Style CSS pour le design "Haut de Gamme"
st.markdown("""
    <style>
    .main { background-color: #0b0e11; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #f0b90b; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. BARRE DE NAVIGATION (Le sélecteur de menus)
st.sidebar.title("🏛️ KUYApaie HQ")
st.sidebar.subheader("Navigation Souveraine")

# Liste des menus basée sur vos fichiers
menu_options = [
    "Tableau de Bord", "BCC & Change", "Comptabilité SYSCOHADA", 
    "Bons du Trésor GPRS", "Hedging Protection", "AML/CFT Sentinel", 
    "Épargne Or", "Réconciliation & Paie", "Services & Recharge", 
    "HQ Superviseur", "Portefeuille Commissions", "Paramètres & Support"
]

selection = st.sidebar.radio("Aller vers :", menu_options)

# 3. LOGIQUE D'IMPORTATION DYNAMIQUE
# Ici, nous lions votre sélection aux fichiers présents sur votre GitHub

if selection == "Tableau de Bord":
    import apptableaubord as tab
    st.title("Bienvenue sur KUYApaie")
    # Si votre fichier a une fonction main(), on l'appelle ici

elif selection == "BCC & Change":
    import memu1 as m1
    st.header("📊 Monitoring BCC & Taux de Change")
    # Appel du code de memu1.py

elif selection == "Comptabilité SYSCOHADA":
    import memu2 as m2
    st.header("📑 Justification SYSCOHADA")

elif selection == "Bons du Trésor GPRS":
    import memu3 as m3
    st.header("📡 Bons du Trésor & GPRS")

elif selection == "Hedging Protection":
    import memu4 as m4
    st.header("🛡️ Protection Hedging")

elif selection == "AML/CFT Sentinel":
    import memu5 as m5
    st.header("🚨 Surveillance AML/CFT")

elif selection == "Épargne Or":
    import memu6 as m6
    st.header("🟡 Épargne Or Digital")

elif selection == "Réconciliation & Paie":
    import memu7 as m7
    st.header("⚙️ Réconciliation & Paie de Masse")

elif selection == "Services & Recharge":
    import memu8 as m8
    st.header("📱 Services en Ligne & Data")

elif selection == "HQ Superviseur":
    import memu9 as m9
    st.header("👁️ HQ Command Center")

elif selection == "Portefeuille Commissions":
    import portefeuille as pf
    st.header("💰 Revenus & Chiffre d'Affaires")

elif selection == "Paramètres & Support":
    import parametre as par
    st.header("⚙️ Paramètres & KYC")

# Bas de page pour le Patron
st.sidebar.markdown("---")
st.sidebar.write("👤 **Statut : Administrateur Principal**")
st.sidebar.write("🌍 **Réseau : RDC - Serveur Sécurisé**")