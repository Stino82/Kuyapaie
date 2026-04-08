import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="KUYApaie | Système Souverain",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. STYLE GLOBAL CSS ---
st.markdown("""
    <style>
    .main { background-color: #0b0e11; }
    [data-testid="stSidebar"] { background-color: #0b0e11; border-right: 1px solid #1a1d23; }
    .stApp { color: white; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. FONCTION D'AFFICHAGE HTML/JS ---
def display_html(html_content, h=600):
    custom_style = """
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style> 
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        body { background: transparent; color: white; font-family: 'Inter', sans-serif; margin: 0; } 
        .glass-card { backdrop-filter: blur(16px); background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); }
    </style>
    """
    components.html(custom_style + html_content, height=h, scrolling=False)

# --- 4. NAVIGATION SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80) 
    st.title("KUYApaie HQ")
    st.markdown("---")
    menu = st.radio(
        "CENTRE DE CONTRÔLE",
        ["Tableau de Bord", "BCC & Analyse Change", "Revenue Vault", "Profil & Support"],
        index=0
    )
    st.markdown("---")
    st.success("AES-256 SECURED")
    st.caption("📍 Kinshasa - Lubumbashi | 2026")

# --- 5. LOGIQUE DES MENUS ---

if menu == "Tableau de Bord":
    st.header("📊 Supervision Globale")
    hq_content = """
    <div class="glass-card rounded-3xl p-8 border-l-4 border-red-600 shadow-2xl">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-black italic uppercase tracking-tighter">HQ <span class="text-red-600">Superviseur</span></h2>
            <span class="text-[10px] bg-green-500/20 text-green-500 px-3 py-1 rounded-full animate-pulse">LIVE RDC SERVER</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="p-4 bg-white/5 rounded-2xl border border-white/10 text-center">
                <p class="text-[9px] text-gray-400 uppercase">Volume 24h</p>
                <p class="text-xl font-bold">$1.2M</p>
            </div>
            <div class="p-4 bg-white/5 rounded-2xl border border-white/10 text-center">
                <p class="text-[9px] text-gray-400 uppercase">Alertes</p>
                <p class="text-xl font-bold text-red-500">0</p>
            </div>
            <div class="p-4 bg-white/5 rounded-2xl border border-white/10 text-center">
                <p class="text-[9px] text-gray-400 uppercase">Utilisateurs</p>
                <p class="text-xl font-bold text-blue-400">42,809</p>
            </div>
            <div class="p-4 bg-white/5 rounded-2xl border border-white/10 text-center">
                <p class="text-[9px] text-gray-400 uppercase">Or Digital</p>
                <p class="text-xl font-bold text-yellow-500">12.4kg</p>
            </div>
        </div>
    </div>
    """
    display_html(hq_content, h=300)

elif menu == "BCC & Analyse Change":
    st.header("📈 Analyse des Taux & Hedging")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Intégration de votre méthode de calcul Green/Orange/Red Zone
        taux = st.number_input("Taux Marché USD/CDF", value=2850)
        
        if taux < 2800:
            st.success("🟢 ZONE VERTE : Stabilité détectée")
        elif 2800 <= taux < 2900:
            st.warning("🟠 ZONE ORANGE : Risque modéré")
        else:
            st.error("🔴 ZONE ROUGE : Couverture requise")
        
        st.metric("Taux BCC Officiel", f"{taux} CDF", "Officiel")

    with col2:
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['BCC', 'Marché'])
        st.line_chart(chart_data)

elif menu == "Revenue Vault":
    st.header("💰 Gestion des Commissions")
    vault_content = """
    <div class="glass-card rounded-3xl p-8 border-t-4 border-yellow-500 bg-gradient-to-br from-black to-[#111]">
        <h2 class="text-2xl font-black text-white mb-6 uppercase italic">Revenue <span class="text-yellow-500">Vault</span></h2>
        <div class="bg-black/40 p-6 rounded-2xl border border-white/10 mb-6">
            <p class="text-xs text-gray-500 uppercase font-bold">Chiffre d'Affaires Cumulé</p>
            <p class="text-4xl font-black text-white mt-1">$12,450.00</p>
            <div class="w-full bg-gray-800 h-1.5 rounded-full mt-4">
                <div class="bg-yellow-500 h-full w-[65%] shadow-[0_0_15px_#f0b90b]"></div>
            </div>
        </div>
        <div class="space-y-3">
            <div class="flex justify-between p-3 bg-white/5 rounded-xl">
                <span class="text-sm font-bold">Produits Dérivés (3%)</span>
                <span class="text-yellow-500 font-black">$373.50</span>
            </div>
            <div class="flex justify-between p-3 bg-white/5 rounded-xl">
                <span class="text-sm font-bold">Bons & Obligations (5%)</span>
                <span class="text-yellow-500 font-black">$622.50</span>
            </div>
        </div>
        <button class="w-full mt-8 py-4 bg-yellow-500 text-black font-black rounded-2xl hover:bg-yellow-400 transition-all uppercase text-xs">
            Retirer les fonds vers compte principal
        </button>
    </div>
    """
    display_html(vault_content, h=550)

elif menu == "Profil & Support":
    profil_content = """
    <div class="glass-card rounded-3xl p-8 border border-white/10">
        <div class="flex items-center gap-6 mb-8">
            <div class="w-20 h-20 bg-gradient-to-tr from-yellow-500 to-orange-400 rounded-full flex items-center justify-center text-3xl font-black text-black">JD</div>
            <div>
                <h3 class="text-2xl font-black">Jean Dupont</h3>
                <p class="text-gray-500 text-xs font-bold uppercase tracking-widest">ID: KP-243-99201</p>
                <span class="text-[10px] bg-blue-500/20 text-blue-400 px-2 py-1 rounded-full">KYC NIVEAU 2</span>
            </div>
        </div>
        <div onclick="alert('Liaison avec un agent KUYApaie...')" class="p-6 bg-blue-600 rounded-3xl cursor-pointer hover:bg-blue-500 transition-all shadow-xl shadow-blue-900/20">
            <h4 class="text-lg font-black italic uppercase">Support VIP 24h/7</h4>
            <p class="text-xs text-blue-100 mt-1">Cliquez pour ouvrir une session de chat sécurisée.</p>
        </div>
    </div>
    """
    display_html(profil_content, h=400)
