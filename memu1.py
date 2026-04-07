<div class="hedging-tool bg-[#161a1e] p-6 rounded-lg border border-[#f0b90b]/30">
    <div class="flex justify-between items-center mb-6">
        <h2 class="text-[#f0b90b] font-bold text-xl uppercase">🛡️ Hedging Engine (Black-Scholes)</h2>
        <span class="bg-green-900 text-green-400 px-3 py-1 rounded-full text-xs">Direct Bank Link: ACTIVE</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="space-y-4">
            <label class="block text-gray-400 text-sm">Montant de la Facture (USD)</label>
            <input type="number" id="usd_amount" value="100000" class="input-field-dark">
            
            <label class="block text-gray-400 text-sm">Échéance (Jours)</label>
            <select id="tenor" class="input-field-dark">
                <option value="30">30 Jours (Spot + 1)</option>
                <option value="60">60 Jours (Standard)</option>
                <option value="90">90 Jours (Long Terme)</option>
            </select>
        </div>

        <div class="bg-[#1e2329] p-4 rounded border border-gray-700">
            <div class="text-xs text-gray-500 mb-2">ANALYSE DE LA CONVEXITÉ (GAMMA)</div>
            <div class="flex justify-between items-end h-24 gap-1">
                <div class="bg-blue-500 w-full" style="height: 40%"></div>
                <div class="bg-blue-500 w-full" style="height: 60%"></div>
                <div class="bg-[#f0b90b] w-full" style="height: 95%"></div> <div class="bg-blue-500 w-full" style="height: 50%"></div>
            </div>
            <p class="text-[10px] mt-2 text-center text-gray-400">Courbe de volatilité CDF/USD sur 24h</p>
        </div>
    </div>

    <div class="mt-8 flex gap-4">
        <button onclick="lockForward()" class="btn-outline-gold flex-1">BLOQUER TAUX FORWARD (2865 CDF)</button>
        <button onclick="buyCall()" class="btn-gold flex-1">ACHETER OPTION CALL (Protection)</button>
    </div>
</div>

<style>
    .input-field-dark { background: #0b0e11; border: 1px solid #474d57; padding: 10px; width: 100%; border-radius: 4px; color: #f0b90b; font-weight: bold; }
    .btn-outline-gold { border: 1px solid #f0b90b; color: #f0b90b; padding: 15px; border-radius: 4px; font-weight: bold; transition: 0.3s; }
    .btn-outline-gold:hover { background: rgba(240, 185, 11, 0.1); }
</style>