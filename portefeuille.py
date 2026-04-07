<section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-yellow-500 bg-gradient-to-br from-[#0b0e11] to-[#1a1d23] shadow-2xl">
    <div class="flex justify-between items-center mb-8">
        <div>
            <h2 class="text-2xl font-black text-white tracking-tighter uppercase italic">Revenue <span class="text-yellow-500">Vault</span></h2>
            <p class="text-[9px] text-gray-500 uppercase tracking-widest font-bold">Accumulation des Commissions & CA</p>
        </div>
        <div class="h-12 w-12 bg-yellow-500/10 rounded-2xl flex items-center justify-center border border-yellow-500/30">
            <i class="fa-solid fa-vault text-yellow-500 text-xl"></i>
        </div>
    </div>

    <div class="grid grid-cols-1 gap-4 mb-8">
        <div class="bg-black/60 p-6 rounded-2xl border border-white/5 relative overflow-hidden">
            <span class="text-[10px] text-gray-500 uppercase font-bold">Chiffre d'Affaires Total (Commissions)</span>
            <div class="flex items-end gap-2 mt-2">
                <div id="total-ca" class="text-4xl font-black text-white">0.00</div>
                <div class="text-yellow-500 font-bold mb-1">USD</div>
            </div>
            <div class="mt-4 w-full bg-gray-800 h-1.5 rounded-full overflow-hidden">
                <div class="bg-yellow-500 h-full w-[45%] shadow-[0_0_10px_#f0b90b]"></div>
            </div>
            <div class="flex justify-between mt-1 text-[8px] text-gray-600 font-bold">
                <span>OBJECTIF MENSUEL</span>
                <span>45% ATTEINT</span>
            </div>
        </div>
    </div>

    <div class="space-y-3">
        <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-[0.2em] mb-4">Répartition des Gains</h3>
        
        <div class="flex items-center justify-between p-3 bg-white/5 rounded-xl border-l-2 border-blue-500">
            <div class="flex items-center gap-3">
                <i class="fa-solid fa-mobile-screen text-blue-500 text-xs"></i>
                <span class="text-[10px] font-bold text-gray-300">Data & Change (0.5%)</span>
            </div>
            <div class="text-[11px] font-black text-white" id="gain-data">$0.00</div>
        </div>

        <div class="flex items-center justify-between p-3 bg-white/5 rounded-xl border-l-2 border-purple-500">
            <div class="flex items-center gap-3">
                <i class="fa-solid fa-paper-plane text-purple-500 text-xs"></i>
                <span class="text-[10px] font-bold text-gray-300">Envois & Paiements (1%)</span>
            </div>
            <div class="text-[11px] font-black text-white" id="gain-transfer">$0.00</div>
        </div>

        <div class="flex items-center justify-between p-3 bg-white/5 rounded-xl border-l-2 border-orange-500">
            <div class="flex items-center gap-3">
                <i class="fa-solid fa-chart-line text-orange-500 text-xs"></i>
                <span class="text-[10px] font-bold text-gray-300">Produits Dérivés (3%)</span>
            </div>
            <div class="text-[11px] font-black text-white" id="gain-deriv">$0.00</div>
        </div>

        <div class="flex items-center justify-between p-3 bg-white/5 rounded-xl border-l-2 border-yellow-500">
            <div class="flex items-center gap-3">
                <i class="fa-solid fa-building-columns text-yellow-500 text-xs"></i>
                <span class="text-[10px] font-bold text-gray-300">Bons & Obligations (5%)</span>
            </div>
            <div class="text-[11px] font-black text-white" id="gain-bons">$0.00</div>
        </div>
    </div>

    <button class="w-full mt-8 py-4 bg-yellow-500 text-black font-black text-xs rounded-2xl uppercase shadow-xl shadow-yellow-950/20 active:scale-95 transition-all">
        Retirer les Commissions vers Compte Principal
    </button>
</section>

<script>
    // MOTEUR DE CALCUL DES COMMISSIONS AUTOMATIQUE
    const KuyapaieEngine = {
        ca_total: 0,
        stats: { data: 0, transfer: 0, deriv: 0, bons: 0 },

        // Fonction appelée à chaque transaction dans l'app
        processTransaction: function(amount, type) {
            let commission = 0;
            
            switch(type) {
                case 'DATA_CHANGE': 
                    commission = amount * 0.005; 
                    this.stats.data += commission;
                    break;
                case 'TRANSFERT_PAIEMENT': 
                    commission = amount * 0.01; 
                    this.stats.transfer += commission;
                    break;
                case 'DERIVES_BANQUE': 
                    commission = amount * 0.03; 
                    this.stats.deriv += commission;
                    break;
                case 'BONS_TRESOR': 
                    commission = amount * 0.05; 
                    this.stats.bons += commission;
                    break;
            }

            this.ca_total += commission;
            this.updateDisplay();
        },

        updateDisplay: function() {
            document.getElementById('total-ca').innerText = this.ca_total.toLocaleString('en-US', {minimumFractionDigits: 2});
            document.getElementById('gain-data').innerText = `$${this.stats.data.toFixed(2)}`;
            document.getElementById('gain-transfer').innerText = `$${this.stats.transfer.toFixed(2)}`;
            document.getElementById('gain-deriv').innerText = `$${this.stats.deriv.toFixed(2)}`;
            document.getElementById('gain-bons').innerText = `$${this.stats.bons.toFixed(2)}`;
        }
    };

    // Exemple de simulation : Le patron reçoit des commissions en temps réel
    setTimeout(() => KuyapaieEngine.processTransaction(1000, 'BONS_TRESOR'), 2000); // Gagne 50$
    setTimeout(() => KuyapaieEngine.processTransaction(500, 'TRANSFERT_PAIEMENT'), 4000); // Gagne 5$
</script>