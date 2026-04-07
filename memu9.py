import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf

def show():
<section class="glass-card rounded-3xl p-8 mt-6 border-2 border-red-600/30 bg-gradient-to-b from-black to-[#0b0e11] shadow-[0_20px_50px_rgba(220,38,38,0.1)]">
    
    <div class="flex justify-between items-center mb-10">
        <div>
            <h2 class="text-3xl font-black text-white tracking-tighter uppercase italic">HQ <span class="text-red-600">SUPERVISEUR</span></h2>
            <p class="text-[10px] text-gray-500 uppercase tracking-[0.3em] font-bold">Contrôle Souverain & Audit en Millisecondes</p>
        </div>
        <div class="text-right">
            <div class="text-[10px] text-green-500 font-black mb-1 flex items-center justify-end gap-2">
                <span class="w-2 h-2 bg-green-500 rounded-full animate-ping"></span> SERVEUR RDC : EN LIGNE
            </div>
            <button onclick="generate24hReport()" class="bg-white text-black text-[10px] font-black px-4 py-2 rounded-full hover:bg-red-600 hover:text-white transition-all shadow-lg">
                GÉNÉRER RAPPORT 24H
            </button>
        </div>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
        <div class="bg-white/5 p-4 rounded-2xl border border-white/10">
            <span class="text-[9px] text-gray-500 uppercase">Volume 24h</span>
            <div class="text-xl font-black text-white">$1,284,500</div>
        </div>
        <div class="bg-white/5 p-4 rounded-2xl border border-white/10">
            <span class="text-[9px] text-gray-500 uppercase">Utilisateurs Actifs</span>
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
        <div id="live-activity-log" class="font-mono text-[10px] h-48 overflow-y-auto space-y-1 pr-2">
            <div class="text-green-400 opacity-80">[17:01:22] - USER_992 : Retrait 500$ - OTP Validé - AES_OK</div>
            <div class="text-blue-400 opacity-80">[17:01:15] - USER_102 : Achat Forfait Orange 10$ - Succès</div>
            <div class="text-[#f0b90b] opacity-80">[17:01:05] - CORP_88 : Paie Salaires (45 agents) - En cours...</div>
            <div class="text-gray-500 italic">[17:00:58] - SYS : Sauvegarde base de données effectuée</div>
        </div>
    </div>

    <div class="mt-10 p-6 bg-red-950/10 border border-red-900/20 rounded-3xl">
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 bg-red-600 text-white rounded-2xl flex items-center justify-center shadow-lg shadow-red-900/40">
                <i class="fa-solid fa-briefcase text-xl"></i>
            </div>
            <div>
                <h4 class="text-sm font-black text-white uppercase italic">Export Partenaire</h4>
                <p class="text-[10px] text-gray-500 leading-tight">
                    Ce module compile automatiquement les données SYSCOHADA et AML pour vos rapports trimestriels. <strong>Tout est rangé, prêt pour l'audit.</strong>
                </p>
            </div>
        </div>
    </div>
</section>

<script>
    // Simulation du flux en direct pour le Patron
    function simulateActivity() {
        const log = document.getElementById('live-activity-log');
        const activities = [
            "Achat Or Digital 50g - USER_44",
            "Réconciliation Bancaire RAWBANK - SUCCESS",
            "Transfert ID KP-202 vers KP-505 - OTP_OK",
            "Souscription Bons du Trésor - $5,000"
        ];
        const time = new Date().toLocaleTimeString();
        const randomAct = activities[Math.floor(Math.random() * activities.length)];
        
        const newEntry = document.createElement('div');
        newEntry.className = "text-white border-l border-red-600 pl-2 animate-pulse";
        newEntry.innerHTML = `[${time}] - ${randomAct}`;
        
        log.prepend(newEntry);
        if (log.childNodes.length > 10) log.removeChild(log.lastChild);
    }
    setInterval(simulateActivity, 3000);

    function generate24hReport() {
        alert("📊 GÉNÉRATION DU RAPPORT EXÉCUTIF...\n\n- Analyse des flux\n- Justificatifs SYSCOHADA\n- Rapport de conformité CENAREF\n- Statistiques de pénétration rurale\n\nPrêt pour envoi aux partenaires.");
    }
</script>
