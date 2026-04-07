<section class="glass-card rounded-2xl p-6 mt-6 border-t-4 border-[#f0b90b]">
    <div class="flex justify-between items-center mb-6">
        <div>
            <h2 class="text-xl font-extrabold text-white tracking-tight">🏛️ ADJUDICATION DÉMOCRATISÉE</h2>
            <p class="text-[10px] text-gray-400 uppercase tracking-widest">Financement des Infrastructures Nationales</p>
        </div>
        <div class="text-right">
            <span class="text-[10px] bg-[#f0b90b]/20 text-[#f0b90b] px-2 py-1 rounded font-bold">CERTIFIÉ ÉTAT</span>
        </div>
    </div>

    <div class="grid grid-cols-2 gap-4 mb-8 bg-black/30 p-4 rounded-xl border border-white/5">
        <div class="space-y-1">
            <label class="text-[10px] text-gray-500 uppercase">Montant à Investir</label>
            <input type="number" id="invest_amount" value="100000" class="w-full bg-transparent text-xl font-bold text-white focus:outline-none">
            <select id="currency" class="bg-transparent text-[10px] text-[#f0b90b] font-bold">
                <option value="CDF">CDF (Franc Congolais)</option>
                <option value="USD">USD (Dollar US)</option>
            </select>
        </div>
        <div class="text-right flex flex-col justify-center">
            <span class="text-[10px] text-gray-500 uppercase">Bénéfice Estimé</span>
            <div id="est_profit" class="text-xl font-bold text-green-500">+8,500.00</div>
            <span class="text-[9px] text-gray-400">Taux: 8.5% | 365 Jours</span>
        </div>
    </div>

    <div class="space-y-4">
        <h3 class="text-xs font-bold text-gray-300 flex items-center gap-2">
            <i class="fa-solid fa-list-check text-[#f0b90b]"></i> MES SOUSCRIPTIONS ACTIVES
        </h3>
        
        <div class="bg-white/5 p-4 rounded-xl border border-white/10 hover:border-[#f0b90b]/50 transition-all">
            <div class="flex justify-between items-start mb-3">
                <div>
                    <div class="text-[11px] font-bold text-white">BON DU TRÉSOR #BT-243-88</div>
                    <div class="text-[9px] text-gray-500">ID: KP-USER-99201</div>
                </div>
                <div class="text-right">
                    <div class="text-xs font-bold text-[#f0b90b]">12.5% p.a</div>
                    <div class="text-[8px] text-gray-500">MATURITÉ: 180 JRS</div>
                </div>
            </div>
            
            <div class="flex justify-between items-end">
                <div>
                    <div class="text-[9px] text-gray-500 mb-1">PROJET FINANCÉ (SUIVI GPRS)</div>
                    <div class="flex items-center gap-2">
                        <span class="bg-blue-900/40 text-blue-400 text-[9px] px-2 py-0.5 rounded">📍 Pont Gombe</span>
                        <div class="w-16 bg-gray-800 h-1 rounded-full overflow-hidden">
                            <div class="bg-blue-500 h-full w-[65%]"></div>
                        </div>
                        <span class="text-[8px] text-gray-400">65%</span>
                    </div>
                </div>
                <button class="bg-[#f0b90b] text-black text-[10px] font-bold px-3 py-1.5 rounded-lg shadow-lg">DÉTAILS</button>
            </div>
        </div>
    </div>
</section>

<script>
    // Logique de calcul dynamique
    const amountInput = document.getElementById('invest_amount');
    const profitDisplay = document.getElementById('est_profit');
    const rate = 0.085; // 8.5%

    function calculateImpact() {
        const amount = parseFloat(amountInput.value) || 0;
        const profit = (amount * rate).toLocaleString('fr-FR', { minimumFractionDigits: 2 });
        profitDisplay.innerText = `+${profit}`;
    }

    amountInput.addEventListener('input', calculateImpact);
</script>