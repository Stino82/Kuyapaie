import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf

def show():
<section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-blue-600 shadow-2xl">
    <div class="flex justify-between items-center mb-6">
        <div>
            <h2 class="text-2xl font-black text-white tracking-tighter uppercase">Terminal Entreprise</h2>
            <p class="text-[9px] text-blue-400 uppercase tracking-widest font-bold">Réconciliation Bancaire & Paie Mobile Money</p>
        </div>
        <div class="flex gap-2">
            <span class="bg-blue-900/40 text-blue-400 text-[10px] px-3 py-1 rounded-full border border-blue-500/30">Connecté aux Banques</span>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
        <div class="bg-white/5 p-5 rounded-2xl border border-dashed border-gray-700 hover:border-blue-500 transition-all cursor-pointer text-center group">
            <i class="fa-solid fa-file-import text-2xl text-gray-500 group-hover:text-blue-500 mb-3"></i>
            <h4 class="text-xs font-bold text-white uppercase">Réconciliation CSV/API</h4>
            <p class="text-[9px] text-gray-500 mt-1">Glissez votre relevé bancaire pour valider les paiements clients en 2 secondes.</p>
        </div>

        <div class="bg-blue-600 p-5 rounded-2xl shadow-lg shadow-blue-900/20 hover:bg-blue-700 transition-all cursor-pointer">
            <div class="flex justify-between items-start mb-2">
                <i class="fa-solid fa-users-gear text-white text-xl"></i>
                <span class="text-[8px] bg-white/20 text-white px-2 py-0.5 rounded uppercase">Salaires</span>
            </div>
            <h4 class="text-sm font-black text-white uppercase italic">Payer les Agents</h4>
            <div class="text-xl font-bold text-white mt-1">Bulk Mobile Pay</div>
        </div>
    </div>

    <div class="space-y-3">
        <div class="flex justify-between items-center px-2">
            <h3 class="text-[10px] font-bold text-gray-400 uppercase">Flux en cours de traitement</h3>
            <span class="text-[9px] text-blue-500 font-bold">98% Matché</span>
        </div>

        <div class="flex items-center justify-between p-4 bg-black/40 rounded-xl border border-green-500/20">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-green-500/10 rounded-lg flex items-center justify-center text-green-500">
                    <i class="fa-solid fa-check-double"></i>
                </div>
                <div>
                    <div class="text-[11px] font-bold text-white uppercase italic">Virement Client Validé</div>
                    <div class="text-[9px] text-gray-500">REF: KUYA-8821 | Source: Rawbank | 15,000 USD</div>
                </div>
            </div>
            <div class="text-right">
                <div class="text-[10px] font-bold text-green-500">RÉCONCILIÉ</div>
                <div class="text-[8px] text-gray-600">Auto-Match (0.4s)</div>
            </div>
        </div>

        <div class="flex items-center justify-between p-4 bg-black/40 rounded-xl border border-red-500/20">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-red-500/10 rounded-lg flex items-center justify-center text-red-500">
                    <i class="fa-solid fa-circle-exclamation"></i>
                </div>
                <div>
                    <div class="text-[11px] font-bold text-white uppercase italic">Écart de Montant Détecté</div>
                    <div class="text-[9px] text-gray-500">REF: KUYA-990 | Attendu: 500$ | Reçu: 495$</div>
                </div>
            </div>
            <button class="bg-red-600 text-white text-[9px] px-3 py-1.5 rounded-lg font-bold uppercase">Ajuster</button>
        </div>
    </div>

    <div class="mt-8 p-4 bg-blue-900/10 rounded-2xl border border-blue-800/30">
        <p class="text-[10px] text-gray-400 leading-tight">
            <strong>Efficacité Supérieure :</strong> Finis les jours d'attente. Avec le Hub KUYApaie, votre comptabilité est à jour avant même que l'agent de la banque ne traite votre dossier. <strong>Le rangement financier devient automatique.</strong>
        </p>
    </div>
</section>
