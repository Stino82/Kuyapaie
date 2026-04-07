import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf

def show():
<section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-[#8B5CF6] shadow-[0_10px_30px_rgba(139,92,246,0.15)]">
    <div class="flex justify-between items-start mb-6">
        <div>
            <h2 class="text-2xl font-black text-white tracking-tighter uppercase">Services <span class="text-[#8B5CF6]">Live</span></h2>
            <p class="text-[9px] text-gray-500 uppercase tracking-[0.2em] font-bold">Recharge Unités, Data & Transfert ID</p>
        </div>
        <div class="bg-[#8B5CF6]/10 p-2 rounded-xl border border-[#8B5CF6]/30">
            <i class="fa-solid fa-tower-cell text-[#8B5CF6] text-xl"></i>
        </div>
    </div>

    <div class="flex justify-between gap-2 mb-8">
        <button class="flex-1 flex flex-col items-center p-3 bg-white/5 rounded-2xl border border-orange-500/20 hover:bg-orange-500/10 transition-all">
            <div class="w-8 h-8 bg-orange-500 rounded-full mb-2 flex items-center justify-center font-bold text-xs text-white">O</div>
            <span class="text-[8px] font-bold text-gray-400">ORANGE</span>
        </button>
        <button class="flex-1 flex flex-col items-center p-3 bg-white/5 rounded-2xl border border-red-600/20 hover:bg-red-600/10 transition-all">
            <div class="w-8 h-8 bg-red-600 rounded-full mb-2 flex items-center justify-center font-bold text-xs text-white">A</div>
            <span class="text-[8px] font-bold text-gray-400">AIRTEL</span>
        </button>
        <button class="flex-1 flex flex-col items-center p-3 bg-white/5 rounded-2xl border border-blue-600/20 hover:bg-blue-600/10 transition-all">
            <div class="w-8 h-8 bg-blue-600 rounded-full mb-2 flex items-center justify-center font-bold text-xs text-white">V</div>
            <span class="text-[8px] font-bold text-gray-400">VODACOM</span>
        </button>
        <button class="flex-1 flex flex-col items-center p-3 bg-white/5 rounded-2xl border border-purple-600/20 hover:bg-purple-600/10 transition-all">
            <div class="w-8 h-8 bg-purple-600 rounded-full mb-2 flex items-center justify-center font-bold text-xs text-white">Af</div>
            <span class="text-[8px] font-bold text-gray-400">AFRICELL</span>
        </button>
    </div>

    <div class="space-y-4">
        <div class="bg-black/40 p-5 rounded-2xl border border-white/5 group hover:border-[#8B5CF6] transition-all">
            <div class="flex items-center gap-4 mb-4">
                <i class="fa-solid fa-paper-plane text-[#8B5CF6]"></i>
                <h4 class="text-xs font-black text-white uppercase italic">Transfert Flash (ID KUYA)</h4>
            </div>
            <div class="flex gap-2">
                <input type="text" placeholder="ID Destinataire (ex: KP-992)" class="flex-1 bg-transparent border-b border-gray-800 text-sm font-bold text-[#8B5CF6] focus:outline-none focus:border-[#8B5CF6] pb-1">
                <input type="number" placeholder="Montant" class="w-24 bg-transparent border-b border-gray-800 text-sm font-bold text-white focus:outline-none pb-1">
                <button onclick="requestSIMAuth()" class="bg-[#8B5CF6] text-white px-4 py-1.5 rounded-lg text-[10px] font-black uppercase shadow-lg shadow-[#8B5CF6]/20">Envoyer</button>
            </div>
        </div>

        <div class="bg-black/40 p-5 rounded-2xl border border-white/5 group hover:border-green-500 transition-all">
            <div class="flex items-center gap-4 mb-4">
                <i class="fa-solid fa-wifi text-green-500"></i>
                <h4 class="text-xs font-black text-white uppercase italic">Recharge Data & Unités</h4>
            </div>
            <div class="grid grid-cols-2 gap-3">
                <button onclick="requestSIMAuth()" class="py-3 bg-gray-800/50 rounded-xl text-[10px] font-bold text-gray-300 border border-white/5 hover:border-green-500 transition-all">UNITÉS DIRECTES</button>
                <button onclick="requestSIMAuth()" class="py-3 bg-gray-800/50 rounded-xl text-[10px] font-bold text-gray-300 border border-white/5 hover:border-green-500 transition-all">FORFAIT INTERNET</button>
            </div>
        </div>
    </div>

    <div class="mt-6 flex items-center gap-3 p-3 bg-purple-900/10 rounded-xl border border-purple-500/20">
        <i class="fa-solid fa-fingerprint text-[#8B5CF6]"></i>
        <p class="text-[9px] text-gray-500 leading-tight">
            Chaque achat ou transfert nécessite une confirmation par <strong>Code Secret SIM</strong>. Votre solde KUYApaie est votre coffre-fort mobile.
        </p>
    </div>
</section>

<script>
    function requestSIMAuth() {
        // Appelle la fonction de sécurité du Menu 7
        if (typeof initiateSecure === "function") {
            initiateSecure('SERVICE EN LIGNE');
        } else {
            alert("🔒 Sécurisation de la transaction... Envoi du code OTP sur votre SIM.");
        }
    }
</script>
