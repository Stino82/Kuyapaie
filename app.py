import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf
import streamlit.components.v1 as components

# --- CONFIGURATION PROFESSIONNELLE ---
st.set_page_config(
    page_title="KUYApaie | Système Souverain",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE GLOBAL ---
st.markdown("""
    <style>
    .main { background-color: #0b0e11; }
    [data-testid="stSidebar"] { background-color: #0b0e11; border-right: 1px solid #1a1d23; }
    .stApp { color: white; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- BARRE DE NAVIGATION (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80) 
    st.title("KUYApaie HQ")
    st.markdown("---")
    menu = st.radio(
        "CENTRE DE CONTRÔLE",
        ["Tableau de Bord HQ", "Revenue Vault", "Hedging & Taux BCC", "Profil Utilisateur", "Paramètres Système"],
        index=0
    )
    st.markdown("---")
    st.success("Connexion Sécurisée : AES-256")
    st.caption("📍 Lubumbashi, RDC")
    st.caption("© 2026 KUYApaie - Système Souverain")

# --- FONCTION D'INJECTION DE COMPOSANTS ---
def inject_component(html_code, height=700):
    custom_css = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: transparent; margin: 0; }
        .glass-card { backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); }
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 10px; }
    </style>
    """
    components.html(custom_css + html_code, height=height, scrolling=False)

# --- LOGIQUE DES MODULES ---
if menu == "Tableau de Bord HQ":
    hq_html = """
    <section class="glass-card rounded-3xl p-8 mt-6 border-2 border-red-600/30 bg-gradient-to-b from-black to-[#0b0e11] shadow-[0_20px_50px_rgba(220,38,38,0.1)]">
        <div class="flex justify-between items-center mb-10">
            <div>
                <h2 class="text-3xl font-black text-white tracking-tighter uppercase italic">HQ <span class="text-red-600">SUPERVISEUR</span></h2>
                <p class="text-[10px] text-gray-500 uppercase tracking-[0.3em] font-bold">Contrôle Souverain & Audit en Millisecondes</p>
            </div>
            <div class="text-right text-white">
                <div class="text-[10px] text-green-500 font-black mb-1 flex items-center justify-end gap-2">
                    <span class="w-2 h-2 bg-green-500 rounded-full animate-ping"></span> SERVEUR RDC : EN LIGNE
                </div>
            </div>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10 text-center">
                <span class="text-[9px] text-gray-500 uppercase">Volume 24h</span>
                <div class="text-xl font-black">$1,284,500</div>
            </div>
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10 text-center">
                <span class="text-[9px] text-gray-500 uppercase">Utilisateurs</span>
                <div class="text-xl font-black text-blue-500">42,809</div>
            </div>
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10 text-center">
                <span class="text-[9px] text-gray-500 uppercase">Alertes</span>
                <div class="text-xl font-black text-red-500">0</div>
            </div>
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10 text-center">
                <span class="text-[9px] text-gray-500 uppercase">Réserves Or</span>
                <div class="text-xl font-black text-yellow-500">12.45 Kg</div>
            </div>
        </div>
    </section>
    """
    inject_component(hq_html, height=400)

elif menu == "Revenue Vault":
    st.header("💰 Revenue Vault")
    st.info("Statistiques des commissions en cours de chargement...")

elif menu == "Hedging & Taux BCC":
    st.subheader("📈 Hedging USD/CDF")
    taux = st.number_input("Taux Marché actuel", value=2850)
    if taux < 2800:
        st.success("🟢 ZONE VERTE : Stabilité")
    else:
        st.warning("🟠 ZONE ORANGE/ROUGE : Vigilance")

elif menu == "Paramètres Système":
    if st.button("🚨 RÉINITIALISER LE SYSTÈME"):
        st.error("Accès refusé : Empreinte biométrique requise.")
