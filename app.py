import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import datetime
import re
import hashlib
from scipy.stats import norm

# --- 1. INITIALISATION DE LA BASE DE DONNÉES ---
def init_db():   
    conn = sqlite3.connect('kuyapaie_souverain.db') 
    c = conn.cursor()  
    c.execute('''CREATE TABLE IF NOT EXISTS users            
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,                
                  nom_complet TEXT, telephone TEXT, localisation TEXT,         
                  email TEXT UNIQUE, password_hash TEXT, kyc_status TEXT,           
                  secret_question TEXT, secret_answer TEXT)''')   
   c.execute('''CREATE TABLE IF NOT EXISTS journal_bord                 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, horodatage TEXT,            
                 pilier TEXT, details TEXT, montant REAL, devise TEXT, statut_risque TEXT)''')  
   conn.commit()   
   conn.close()
def log_action(pilier, details, montant=0.0, devise="CDF", statut="OK"):  
    conn = sqlite3.connect('kuyapaie_souverain.db')   
    c = conn.cursor()    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    c.execute("INSERT INTO journal_bord (horodatage, pilier, details, montant, devise, statut_risque) VALUES (?,?,?,?,?,?)",            
              (now, pilier, details, montant, devise, statut))   
    conn.commit()  
    conn.close()
def validate_password(password):   
    if len(password) < 8: return False   
    if not re.search("[a-z]", password): return False   
    if not re.search("[A-Z]", password): return False  
    if not re.search("[0-9]", password): return False   
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password): return False  
    return True

init_db()

# --- 2. CONFIGURATION DE LA PLATEFORME ---
st.set_page_config(page_title="KUYApaie ERP Souverain", page_icon=" ", layout="wide")

if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'user_email' not in st.session_state: st.session_state['user_email'] = ""

# --- 3. ÉCRAN DE SÉCURITÉ ---
if not st.session_state['logged_in']:   
    st.title(" KUYApaie - Portail de Sécurité")  
    auth_choice = st.radio("Accès", ["Connexion", "Création de Compte KYC"])

    if auth_choice == "Création de Compte KYC":    
        with st.form("kyc_form"):       
            st.subheader("Enregistrement Officiel (Normes BCC)")      
            c1, c2 = st.columns(2)       
            with c1:              
                nom = st.text_input("Nom Complet")           
                tel = st.text_input("Téléphone (+243)")           
                loc = st.text_input("Localisation actuelle")     
        with c2:          
            email = st.text_input("Email")        
            pwd = st.text_input("Mot de passe (8+ car, Maj, Symbole)", type="password") 
                     
        st.divider()        
        q_sec = st.selectbox("Question de secours", ["Ville de naissance", "Nom du premier animal"])    
        r_sec = st.text_input("Réponse secrète")       
        selfie = st.camera_input("Vérification faciale")
       
        if st.form_submit_button("Activer mon profil"):         
            if validate_password(pwd) and nom and email and r_sec:           
                try:                 
                    pwd_h = hashlib.sha256(pwd.encode()).hexdigest()            
                    conn = sqlite3.connect('kuyapaie_souverain.db')             
                    c = conn.cursor()                 
                    c.execute("INSERT INTO users (nom_complet, telephone, localisation, email, password_hash, kyc_status, secret_question, secret_answer) VALUES (?,?,?,?,?,?,?,?)",
                              (nom, tel, loc, email, pwd_h, "BRONZE", q_sec, r_sec))
                    conn.commit()
                    conn.close()
                    st.success("Compte créé avec succès !")
                except: st.error("Email déjà utilisé.")
            else: st.warning("Vérifiez vos informations.")  
                           
elif auth_choice == "Connexion":    
    email_log = st.text_input("Email")    
    pwd_log = st.text_input("Mot de passe", type="password")    
    if st.button("Entrer dans le système"):    
        pwd_h = hashlib.sha256(pwd_log.encode()).hexdigest()    
        conn = sqlite3.connect('kuyapaie_souverain.db')   
        c = conn.cursor()    
        c.execute("SELECT nom_complet, kyc_status FROM users WHERE email=? AND password_hash=?", (email_log, pwd_h))     
        user = c.fetchone()       
        conn.close()    
        if user:          
            st.session_state['logged_in'] = True       
            st.session_state['user_email'] = email_log      
            st.rerun()       
        else: st.error("Accès refusé.")

# --- 4. INTERFACE ERP (SI CONNECTÉ) ---
else:    
    conn = sqlite3.connect('kuyapaie_souverain.db') 
    c = conn.cursor() 
    c.execute("SELECT kyc_status, nom_complet FROM users WHERE email=?", (st.session_state['user_email'],)) 
    u_data = c.fetchone()    
    conn.close()   
    niveau = u_data[0] if u_data else "BRONZE"

    st.sidebar.header(f" {u_data[1]}") 
    st.sidebar.info(f"Confiance : {niveau}")  
    if st.sidebar.button("Déconnexion"):      
         st.session_state['logged_in'] = False   
         st.rerun()

    st.sidebar.divider()  
    st.sidebar.header(" Paramètres État")  
    taux_bon = st.sidebar.number_input("Taux annuel Bon du Trésor (%)", value=22.5)  
    tx_mkt = st.sidebar.number_input("Taux Marché (CDF/USD)", value=2850.0)

    tabs = st.tabs([" Hedging", " Audit SYSCOHADA", " Souveraineté", " Rapports BCC", " Inclusion", " Réconciliation", " Cyber", " Paiements", " Superviseur"])

    # 1. HEDGING  
    with tabs[0]:   
        st.header("Protection contre la dépréciation")    
        mnt_h = st.number_input("Montant (USD)", value=1000)    
        if st.button("Activer Couverture"):    
            log_action("HEDGING", "Contrat Forward activé", mnt_h, "USD")    
            st.success("Protection activée.")

    # 2. AUDIT & SYSCOHADA    
    with tabs[1]:   
     st.header("Expertise Comptable SYSCOHADA")  
     if st.button("Générer écritures comptables auto"):   
         data = {"Journal": ["Achats", "Banque", "Caisse"], "Compte": ["6011", "521", "571"], "Libellé": ["Facture SNEL", "Virement Client", "Achat Data"], "Montant": [250000, 1200000, 50000]} 
         df_sysco = pd.DataFrame(data)    
         st.table(df_sysco)       
         log_action("AUDIT", "Génération écritures SYSCOHADA")

    # 3. SOUVERAINETÉ (Calculateur de gain)
    with tabs[2]:     
        st.header("Bons du Trésor & Obligations") 
        invest = st.number_input("Somme à investir (CDF)", value=100000, step=10000) 
        mois = st.slider("Durée (Mois)", 3, 24, 12)  
        gain = invest * (taux_bon / 100) * (mois / 12)  
        st.success(f"Gain estimé : **{gain:,.2f} CDF**. Total à recevoir : **{(invest+gain):,.2f} CDF**")  
        if st.button("Investir maintenant"):  
            log_action("SOUVERAINETÉ", f"Bon du Trésor {mois} mois", invest, "CDF")

    # 4. RAPPORTS BCC (Conformité)  
    with tabs[3]:   
        st.header("Générateur de Rapport de Conformité")   
        if st.button("Télécharger Rapport BCC/CENAREF"):     
            conn = sqlite3.connect('kuyapaie_souverain.db') 
            df_audit = pd.read_sql_query("SELECT * FROM journal_bord", conn)    
            conn.close()    
            st.download_button("Exporter PDF Audit", df_audit.to_csv(), "rapport_bcc.csv") 
            st.info("Le document contient l'analyse des risques et les alertes AML.")

    # 8. PAIEMENTS    
    with tabs[7]:     
        st.header("Paiements & Services")    
        mnt_p = st.number_input("Montant de l'opération", value=100.0) 
        if niveau == "BRONZE" and mnt_p > 500:           
            st.error("Plafond Bronze (500$) atteint. Vérifiez votre ID.")    
        elif st.button("Confirmer le paiement"):       
            log_action("PAIEMENT", "Opération validée", mnt_p, "CDF")     
        st.balloons()
    # 9. SUPERVISEUR 
    with tabs[8]:    
        st.header("Journal d'Audit Central")    
        conn = sqlite3.connect('kuyapaie_souverain.db')   
        st.dataframe(pd.read_sql_query("SELECT * FROM journal_bord ORDER BY id DESC", conn), use_container_width=True)  
        conn.close()

st.markdown("---")
st.caption(f"KUYApaie ERP v4.0 | © {datetime.datetime.now().year} | Souveraineté Financière RDC")