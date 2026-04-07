import streamlit as st

# 1. Configuration de base
st.set_page_config(page_title="KUYApaie Dashboard", layout="wide")

# 2. Barre latérale de navigation
st.sidebar.title("🏛️ KUYApaie HQ")
choix = st.sidebar.radio("Navigation", [
    "Tableau de Bord", 
    "BCC & Change", 
    "Comptabilité", 
    "Bons du Trésor",
    "Hedging",
    "Sécurité Sentinel",
    "Épargne Or",
    "Réconciliation",
    "Services Data",
    "HQ Control"
])

# 3. LE MOTEUR DE LECTURE (L'aiguillage)
# Chaque bloc 'import' va lire le fichier correspondant sur votre GitHub

if choix == "Tableau de Bord":
    import apptableaubord
    apptableaubord.show()

elif choix == "BCC & Change":
    import memu1
    memu1.show()

elif choix == "Comptabilité":
    import memu2
    memu2.show()

elif choix == "Bons du Trésor":
    import memu3
    memu3.show()

elif choix == "Hedging":
    import memu4
    memu4.show()

elif choix == "Sécurité Sentinel":
    import memu5
    memu5.show()

elif choix == "Épargne Or":
    import memu6
    memu6.show()

elif choix == "Réconciliation":
    import memu7
    memu7.show()

elif choix == "Services Data":
    import memu8
    memu8.show()

elif choix == "HQ Control":
    import memu9
    memu9.show()
