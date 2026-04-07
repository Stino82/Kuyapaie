import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf
import streamlit.components.v1 as components

<section class="glass-card rounded-2xl p-6 mt-6 border-l-4 border-blue-500">
    <div class="flex justify-between items-center mb-6">
        <div>
            <h2 class="text-xl font-bold text-white">📑 Journal d'Audit SYSCOHADA</h2>
            <p class="text-xs text-gray-400">Conformité Art. 54 - Corridor de la BCC en temps réel</p>
        </div>
        <button onclick="generatePDF()" class="bg-blue-600 hover:bg-blue-700 text-white text-xs px-4 py-2 rounded flex items-center gap-2 transition">
            <i class="fa-solid fa-file-pdf"></i> GENERER BORDEREAU EXPERTISE
        </button>
    </div>

    <div class="overflow-x-auto">
        <table class="w-full text-left text-sm">
            <thead class="text-gray-500 uppercase text-[10px] border-b border-gray-800">
                <tr>
                    <th class="pb-3">Date</th>
                    <th class="pb-3">Compte</th>
                    <th class="pb-3">N° Pièce</th>
                    <th class="pb-3">Débit</th>
                    <th class="pb-3">Crédit</th>
                    <th class="pb-3">Analyse Écart</th>
                </tr>
            </thead>
            <tbody class="text-gray-300">
                <tr class="border-b border-gray-800/50 hover:bg-white/5 transition">
                    <td class="py-4">07/04/2026</td>
                    <td class="py-4 font-mono text-blue-400">656000</td>
                    <td class="py-4">EXP-BCC-992</td>
                    <td class="py-4">450 000</td>
                    <td class="py-4">-</td>
                    <td class="py-4">
                        <span class="bg-green-900/30 text-green-400 px-2 py-1 rounded text-[10px]">CORRIDOR OK</span>
                    </td>
                </tr>
                <tr class="border-b border-gray-800/50 hover:bg-white/5 transition">
                    <td class="py-4">07/04/2026</td>
                    <td class="py-4 font-mono text-blue-400">401100</td>
                    <td class="py-4">FAC-IMP-001</td>
                    <td class="py-4">-</td>
                    <td class="py-4">28 500 000</td>
                    <td class="py-4"><i class="fa-solid fa-circle-check text-blue-500 text-[10px]"></i> Justifié</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="mt-6 p-4 bg-blue-900/10 rounded-lg border border-blue-800/30 flex items-center gap-3">
        <i class="fa-solid fa-gavel text-blue-500"></i>
        <p class="text-[11px] text-gray-400">
            <strong>Rangement Certifié :</strong> Chaque écriture est horodatée et scellée numériquement. En cas de contrôle fiscal, le <strong>Bordereau KUYApaie</strong> fait foi de votre bonne foi et de la traçabilité des taux appliqués.
        </p>
    </div>
</section>

<script>
    function generatePDF() {
        alert("Génération du Bordereau d'Expertise PDF en cours...\nInclusion des preuves de taux BCC et signatures numériques.");
    }
</script>
