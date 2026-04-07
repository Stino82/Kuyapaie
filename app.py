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
    /* Masquer le menu Streamlit par défaut pour plus de professionnalisme */
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

# --- MODULE 1 : HQ SUPERVISEUR ---
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
                <button onclick="alert('Génération du rapport exécutif en cours...')" class="bg-white text-black text-[10px] font-black px-4 py-2 rounded-full hover:bg-red-600 hover:text-white transition-all shadow-lg">
                    GÉNÉRER RAPPORT 24H
                </button>
            </div>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10 text-white">
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10">
                <span class="text-[9px] text-gray-500 uppercase">Volume 24h</span>
                <div class="text-xl font-black">$1,284,500</div>
            </div>
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10">
                <span class="text-[9px] text-gray-500 uppercase">Utilisateurs</span>
                <div class="text-xl font-black text-blue-500">42,809</div>
            </div>
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10">
                <span class="text-[9px] text-gray-500 uppercase">Alertes Fraude</span>
                <div class="text-xl font-black text-red-500">0</div>
            </div>
            <div class="bg-white/5 p-4 rounded-2xl border border-white/10">
                <span class="text-[9px] text-gray-500 uppercase">Réserves Or</span>
                <div class="text-xl font-black text-[#f0b90b]">12.45 Kg</div>
            </div>
        </div>

        <div class="space-y-2">
            <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-4">Flux d'activités en direct</h3>
            <div id="live-activity-log" class="font-mono text-[10px] h-48 overflow-y-auto space-y-1 pr-2 text-white">
                <div class="text-green-400 opacity-80">[17:01:22] - USER_992 : Retrait 500$ - Validé</div>
                <div class="text-blue-400 opacity-80">[17:01:15] - USER_102 : Achat Forfait 10$ - Succès</div>
            </div>
        </div>
    </section>
    <script>
        function simulateActivity() {
            const log = document.getElementById('live-activity-log');
            const activities = ["Achat Or Digital 50g - USER_44", "Réconciliation Bancaire - SUCCESS", "Transfert KP-202 vers KP-505", "Souscription Bons du Trésor"];
            const time = new Date().toLocaleTimeString();
            const randomAct = activities[Math.floor(Math.random() * activities.length)];
            const newEntry = document.createElement('div');
            newEntry.className = "text-white border-l border-red-600 pl-2 animate-pulse";
            newEntry.innerHTML = `[${time}] - ${randomAct}`;
            log.prepend(newEntry);
            if (log.childNodes.length > 8) log.removeChild(log.lastChild);
        }
        setInterval(simulateActivity, 3000);
    </script>
    """
    inject_component(hq_html, height=600)

# --- MODULE 2 : REVENUE VAULT ---
elif menu == "Revenue Vault":
    vault_html = """
    <section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-yellow-500 bg-gradient-to-br from-[#0b0e11] to-[#1a1d23] shadow-2xl">
        <div class="flex justify-between items-center mb-8">
            <div>
                <h2 class="text-2xl font-black text-white tracking-tighter uppercase italic">Revenue <span class="text-yellow-500">Vault</span></h2>
                <p class="text-[9px] text-gray-500 uppercase tracking-widest font-bold">Accumulation des Commissions & CA</p>
            </div>
            <div class="h-12 w-12 bg-yellow-500/10 rounded-2xl flex items-center justify-center border border-yellow-500/30">
                <i class="fa-solid fa-vault text-yellow-500 text-xl"></i>
            </div>
        </div>

        <div class="bg-black/60 p-6 rounded-2xl border border-white/5 text-white mb-8">
            <span class="text-[10px] text-gray-500 uppercase font-bold">Chiffre d'Affaires Total (Commissions)</span>
            <div class="flex items-end gap-2 mt-2">
                <div class="text-4xl font-black text-white" id="total-ca">1,450.00</div>
                <div class="text-yellow-500 font-bold mb-1 text-sm">USD</div>
            </div>
            <div class="mt-4 w-full bg-gray-800 h-1.5 rounded-full">
                <div class="bg-yellow-500 h-full w-[45%] shadow-[0_0_10px_#f0b90b]"></div>
            </div>
        </div>

        <div class="space-y-3">
            <div class="flex items-center justify-between p-3 bg-white/5 rounded-xl border-l-2 border-orange-500 text-white">
                <span class="text-[10px] font-bold text-gray-300">Produits Dérivés (3%)</span>
                <div class="text-[11px] font-black text-white">$435.00</div>
            </div>
            <div class="flex items-center justify-between p-3 bg-white/5 rounded-xl border-l-2 border-yellow-500 text-white">
                <span class="text-[10px] font-bold text-gray-300">Bons & Obligations (5%)</span>
                <div class="text-[11px] font-black text-white">$1,015.00</div>
            </div>
        </div>

        <button class="w-full mt-8 py-4 bg-yellow-500 text-black font-black text-xs rounded-2xl uppercase shadow-xl hover:bg-yellow-400 active:scale-95 transition-all">
            Retirer les Commissions vers Compte Principal
        </button>
    </section>
    """
    inject_component(vault_html, height=550)

# --- MODULE 3 : HEDGING & TAUX BCC ---
elif menu == "Hedging & Taux BCC":
    st.subheader("Analyse de Risque de Change (USD/CDF)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("### Calculateur de Zone")
        taux_actuel = st.number_input("Taux Marché actuel", value=2850)
        seuil_rouge = taux_actuel * 1.05
        
        st.metric("Taux BCC Officiel", f"{taux_actuel} CDF", "+1.2%")
        
        if taux_actuel < 2800:
            st.success("🟢 ZONE VERTE : Risque Faible")
        elif taux_actuel < 2900:
            st.warning("🟠 ZONE ORANGE : Vigilance Requise")
        else:
            st.error("🔴 ZONE ROUGE : Couverture (Hedging) Obligatoire")

    with col2:
        # Simulation d'un graphique de volatilité
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['BCC', 'Marché Noir', 'KUYApaie Fix']
        )
        st.line_chart(chart_data)

# --- MODULE 4 : PROFIL & SUPPORT ---
elif menu == "Profil Utilisateur":
    profil_html = """
    <section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-gray-600 bg-[#0b0e11] shadow-2xl">
        <div class="flex items-center gap-4 mb-8 p-4 bg-white/5 rounded-2xl border border-white/5 text-white">
            <div class="w-14 h-14 bg-gradient-to-tr from-[#f0b90b] to-yellow-200 rounded-full flex items-center justify-center text-black font-black text-xl">JD</div>
            <div>
                <h3 class="text-lg font-black text-white">Jean Dupont</h3>
                <p class="text-[10px] text-gray-500 font-bold uppercase tracking-widest">ID: KP-243-99201</p>
                <span class="text-[9px] bg-green-500/20 text-green-500 px-2 py-0.5 rounded-full font-bold">Compte Vérifié (KYC)</span>
            </div>
        </div>

        <div class="space-y-2">
            <div class="flex items-center justify-between p-4 bg-white/5 rounded-2xl hover:bg-white/10 transition-all cursor-pointer text-white">
                <div class="flex items-center gap-4">
                    <div class="w-10 h-10 bg-blue-500/10 rounded-xl flex items-center justify-center text-blue-500"><i class="fa-solid fa-id-card"></i></div>
                    <div><div class="text-sm font-bold">Vérification d'identité</div><div class="text-[10px] text-gray-500">Niveau 2 : Limite 50,000 USD/jour</div></div>
                </div>
                <i class="fa-solid fa-chevron-right text-gray-600"></i>
            </div>
            
            <div onclick="alert('🎧 Connexion au Centre de Support KUYApaie...')" class="mt-6 p-6 bg-gradient-to-r from-blue-600 to-blue-800 rounded-3xl shadow-xl shadow-blue-900/20 cursor-pointer active:scale-95 transition-all text-white">
                <div class="flex justify-between items-start mb-4">
                    <div class="w-12 h-12 bg-white/20 rounded-2xl flex items-center justify-center">
                        <i class="fa-solid fa-headset text-white text-2xl"></i>
                    </div>
                    <span class="text-[9px] bg-green-400 text-black px-2 py-1 rounded-full font-black uppercase">En Ligne</span>
                </div>
                <h4 class="text-lg font-black uppercase italic tracking-tighter">Support Client 24h/24</h4>
                <p class="text-[10px] text-blue-100 mt-1">Un expert résout vos problèmes en moins de 2 minutes.</p>
            </div>
        </div>

        <button class="w-full mt-10 py-4 text-red-500 font-bold text-xs uppercase tracking-widest border border-red-500/20 rounded-2xl hover:bg-red-500 hover:text-white transition-all">
            Déconnexion Sécurisée
        </button>
    </section>
    """
    inject_component(profil_html, height=600)

# --- MODULE 5 : PARAMÈTRES SYSTÈME ---
elif menu == "Paramètres Système":
    st.subheader("⚙️ Paramètres Haute Sécurité")
    
    with st.expander("🔐 Clés de Chiffrement & API"):
        st.text_input("Clé API BCC (Lecture seule)", "********-****-4992-8821-**********", disabled=True)
        st.button("Regénérer les clés de session AES")
        
    with st.expander("🛠️ Préférences de l'Interface"):
        st.toggle("Mode Sombre Profond", value=True)
        st.toggle("Notifications Push Activités")
        st.selectbox("Devise d'affichage par défaut", ["USD", "CDF", "XAF"])

    st.markdown("---")
    if st.button("🚨 RÉINITIALISER LE SYSTÈME", use_container_width=True):
        st.error("ACTION CRITIQUE : Cette opération nécessite l'empreinte biométrique du Superviseur.")
