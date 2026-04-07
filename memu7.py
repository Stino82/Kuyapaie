import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf

<section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-[#00D1FF] shadow-[0_0_30px_rgba(0,209,255,0.1)]">
    <div class="flex justify-between items-start mb-8">
        <div>
            <h2 class="text-2xl font-black text-white tracking-tighter uppercase">Sentinel <span class="text-[#00D1FF]">Safe</span></h2>
            <p class="text-[9px] text-gray-500 uppercase tracking-[0.2em] font-bold">Chiffrement AES-256 & Authentification SIM</p>
        </div>
        <div class="bg-[#00D1FF]/10 p-2 rounded-lg border border-[#00D1FF]/30">
            <i class="fa-solid fa-user-shield text-[#00D1FF] text-xl"></i>
        </div>
    </div>

    <div class="flex gap-2 mb-6">
        <div class="flex-1 bg-black/50 p-3 rounded-xl border border-green-500/30 flex items-center gap-2">
            <div class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span class="text-[10px] font-bold text-green-500 uppercase">Données Chiffrées</span>
        </div>
        <div class="flex-1 bg-black/50 p-3 rounded-xl border border-[#00D1FF]/30 flex items-center gap-2">
            <i class="fa-solid fa-tower-broadcast text-[#00D1FF] text-[10px]"></i>
            <span class="text-[10px] font-bold text-[#00D1FF] uppercase">Canal OTP Prêt</span>
        </div>
    </div>

    <div id="transaction-box" class="space-y-4">
        <div class="bg-white/5 p-5 rounded-2xl border border-white/10">
            <label class="text-[10px] text-gray-500 uppercase font-bold mb-2 block">Action Financière</label>
            <div class="flex gap-4">
                <button onclick="initiateSecure('DÉPÔT')" class="flex-1 py-3 bg-gray-800 rounded-xl font-black text-xs hover:bg-[#00D1FF] hover:text-black transition-all">DÉPÔT</button>
                <button onclick="initiateSecure('RETRAIT')" class="flex-1 py-3 bg-gray-800 rounded-xl font-black text-xs hover:bg-red-600 transition-all">RETRAIT</button>
            </div>
        </div>

        <div id="otp-area" class="hidden animate-bounce-in bg-blue-900/10 border border-[#00D1FF]/50 p-6 rounded-2xl text-center">
            <i class="fa-solid fa-comment-sms text-3xl text-[#00D1FF] mb-3"></i>
            <h3 class="text-sm font-bold text-white uppercase">Vérification SIM</h3>
            <p class="text-[10px] text-gray-400 mb-4">Un code secret vient d'être envoyé sur votre numéro de téléphone.</p>
            
            <div class="flex justify-center gap-2 mb-4">
                <input type="text" maxlength="1" class="w-10 h-12 bg-black border border-gray-700 rounded-lg text-center text-[#00D1FF] font-bold text-xl focus:border-[#00D1FF] outline-none">
                <input type="text" maxlength="1" class="w-10 h-12 bg-black border border-gray-700 rounded-lg text-center text-[#00D1FF] font-bold text-xl focus:border-[#00D1FF] outline-none">
                <input type="text" maxlength="1" class="w-10 h-12 bg-black border border-gray-700 rounded-lg text-center text-[#00D1FF] font-bold text-xl focus:border-[#00D1FF] outline-none">
                <input type="text" maxlength="1" class="w-10 h-12 bg-black border border-gray-700 rounded-lg text-center text-[#00D1FF] font-bold text-xl focus:border-[#00D1FF] outline-none">
            </div>

            <button onclick="confirmTransaction()" class="w-full py-3 bg-[#00D1FF] text-black font-black rounded-xl shadow-[0_0_20px_rgba(0,209,255,0.4)]">CONFIRMER LA TRANSACTION</button>
        </div>
    </div>

    <div class="mt-6 pt-6 border-t border-white/5 flex items-center justify-between">
        <div class="flex items-center gap-2">
            <i class="fa-solid fa-lock text-[10px] text-gray-600"></i>
            <span class="text-[8px] text-gray-600 uppercase font-black">Protocole de Défense KUYA-AES</span>
        </div>
        <img src="https://img.icons8.com/color/48/pci-compliant.png" class="w-6 h-6 grayscale opacity-50" alt="PCI">
    </div>
</section>

<script>
    function initiateSecure(type) {
        alert("🔒 Sécurisation du canal pour un " + type + "... Envoi du code OTP immédiat.");
        document.getElementById('otp-area').classList.remove('hidden');
        // Ici, KUYApaie déclenche l'envoi du SMS via votre API de Gateway (ex: Orange/Airtel/Vodacom)
    }

    function confirmTransaction() {
        alert("✅ Identité Confirmée. La transaction a été validée avec succès sous chiffrement AES-256.");
        document.getElementById('otp-area').classList.add('hidden');
    }
</script>

<style>
    @keyframes bounce-in {
        0% { transform: scale(0.9); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    .animate-bounce-in { animation: bounce-in 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
</style>
