import streamlit as st
import pandas as pd
import numpy as np

def show():
    # 1. On encapsule TOUT le code HTML/CSS dans une variable triple guillemets """
    # Cela permet à Python de lire le point (.) du CSS sans faire d'erreur.
    
    html_dashboard = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Vos styles CSS qui causaient l'erreur de syntaxe */
            body { background-color: #0b0e11; font-family: sans-serif; color: white; }
            .glass-card { 
                background: rgba(30, 35, 41, 0.9); 
                padding: 20px; 
                border-radius: 20px; 
                border: 1px solid rgba(255,255,255,0.1);
            }
            .gold-text { color: #f0b90b; font-weight: bold; }
            .news-slide { display: block; animation: fade 1s; }
        </style>
    </head>
    <body>
        <div class="glass-card">
            <h1 class="gold-text">🏛️ KUYApaie - Tableau de Bord</h1>
            <p>Bienvenue dans votre centre de commandement souverain.</p>
            <hr style="opacity: 0.1">
            <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div>
                    <small>STATUT SYSTÈME</small>
                    <div style="color: #22c55e;">● OPÉRATIONNEL</div>
                </div>
                <div style="text-align: right;">
                    <small>DERNIÈRE MISE À JOUR</              <div id="clock">Chargement...</div>
                </div>
            </div>
        </div>

        <script>
            function updateClock() {
                const now = new Date();
                document.getElementById('clock').innerText = now.toLocaleTimeString();
            }
            setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """

    # 2. On affiche le composant HTML dans Streamlit
    # Ajustez 'height' selon la longueur de votre tableau de bord
    components.html(html_dashboard, height=600, scrolling=True)
