import os
import subprocess
import sys

# --- FORCE INSTALLATION SYSTEM (Méthode de secours) ---
def force_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# On force l'installation de scipy et yfinance avant d'importer quoi que ce soit
force_install("scipy")
force_install("yfinance")

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
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10 text-white">
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10 text-center">
                <span class="text-[9px] text-gray-500 uppercase">Volume 24h</span>
                <div class="text-xl font-black text-white">$1,284,500</div>
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
                <span class="text-[9px] text-gray-500 uppercase">Or Digital</span>
                <div class="text-xl font-black text-[#f0b90b]">12.45 Kg</div>
            </div>
        </div>
    </section>
    """
    inject_component(hq_html, height=450)

elif menu == "Revenue Vault":
    vault_html = """
    <section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-yellow-500 bg-gradient-to-br from-[#0b0e11] to-[#1a1d23] shadow-2xl">
        <div class="flex justify-between items-center mb-8">
            <h2 class="text-2xl font-black text-white tracking-tighter uppercase italic">Revenue <span class="text-yellow-500">Vault</span></h2>
            <i class="fa-solid fa-vault text-yellow-500 text-xl"></i>
        </div>
        <div class="bg-black/60 p-6 rounded-2xl border border-white/5 text-white mb-8">
            <span class="text-[10px] text-gray-500 uppercase font-bold">Chiffre d'Affaires Cumulé</span>
            <div class="text-4xl font-black text-white mt-2">$1,450.00</div>
            <div class="mt-4 w-full bg-gray-800 h-1.5 rounded-full"><div class="bg-yellow-500 h-full w-[45%]"></div></div>
        </div>
    </section>
    """
    inject_component(vault_html, height=400)

elif menu == "Hedging & Taux BCC":
    st.subheader("📈 Analyse de Risque USD/CDF")
    taux_actuel = st.number_input("Taux Marché actuel", value=2850)
    if taux_actuel < 2800:
        st.success("🟢 ZONE VERTE : Stabilité")
    elif taux_actuel < 2900:
        st.warning("🟠 ZONE ORANGE : Vigilance")
    else:
        st.error("🔴 ZONE ROUGE : Hedging requis")
    
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['BCC', 'KUYApaie'])
    st.line_chart(chart_data)

elif menu == "Profil Utilisateur":
    profil_html = """
    <section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-gray-600 bg-[#0b0e11] shadow-2xl">
        <div class="flex items-center gap-4 mb-8 p-4 bg-white/5 rounded-2xl text-white">
            <div class="w-14 h-14 bg-yellow-500 rounded-full flex items-center justify-center text-black font-black text-xl">JD</div>
            <div>
                <h3 class="text-lg font-black text-white">Jean Dupont</h3>
                <p class="text-[10px] text-gray-500 font-bold uppercase">ID: KP-243-99201</p>
            </div>
        </div>
        <div class="mt-6 p-6 bg-blue-600 rounded-3xl text-white">
            <h4 class="font-black italic uppercase">Support Client 24h/24</h4>
            <p class="text-[10px] mt-1">Cliquez pour contacter un expert.</p>
        </div>
    </section>
    """
    inject_component(profil_html, height=450)

elif menu == "Paramètres Système":
    st.subheader("⚙️ Paramètres de Sécurité")
    st.text_input("Clé API (Lecture seule)", "********-****-4992-8821-**********", disabled=True)
    if st.button("🚨 RÉINITIALISER LE SYSTÈME"):
        st.error("AUTORISATION DU SUPERVISEUR REQUISE")
