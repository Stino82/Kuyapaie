<section class="glass-card rounded-2xl p-6 mt-6 border-t-4 border-red-600 shadow-[0_0_20px_rgba(220,38,38,0.15)]">
    <div class="flex justify-between items-center mb-6">
        <div>
            <h2 class="text-xl font-black text-white tracking-tighter flex items-center gap-2">
                <i class="fa-solid fa-shield-virus text-red-500 animate-pulse"></i> 
                MOTEUR DE CONFORMITÉ CENAREF
            </h2>
            <p class="text-[9px] text-gray-500 uppercase tracking-widest font-bold">Surveillance Anti-Blanchiment & Terrorisme (Standard GAFI)</p>
        </div>
        <div class="bg-red-950/30 border border-red-500/50 px-3 py-1 rounded">
            <span class="text-[10px] text-red-500 font-bold uppercase">Risque Pays : ÉLEVÉ</span>
        </div>
    </div>

    <div class="grid grid-cols-3 gap-3 mb-6">
        <div class="bg-black/40 p-3 rounded-xl border border-white/5">
            <div class="text-[8px] text-gray-500 uppercase mb-1">Filtrage Listes Noires</div>
            <div class="text-xs font-bold text-green-500">ACTIF (100%)</div>
        </div>
        <div class="bg-black/40 p-3 rounded-xl border border-white/5">
            <div class="text-[8px] text-gray-500 uppercase mb-1">Seuil Alerte (BCC)</div>
            <div class="text-xs font-bold text-white">10,000 USD</div>
        </div>
        <div class="bg-black/40 p-3 rounded-xl border border-white/5">
            <div class="text-[8px] text-gray-500 uppercase mb-1">Scan GPRS (Flux)</div>
            <div class="text-xs font-bold text-blue-400">EN DIRECT</div>
        </div>
    </div>

    <div class="space-y-3">
        <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-2">Alertes de Risque Récentes</h3>
        
        <div class="flex items-center justify-between p-3 bg-red-900/10 border border-red-900/30 rounded-lg">
            <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-red-600/20 rounded-full flex items-center justify-center text-red-500">
                    <i class="fa-solid fa-triangle-exclamation"></i>
                </div>
                <div>
                    <div class="text-[11px] font-bold text-white uppercase">Blocage Préventif : Seuil Atteint</div>
                    <div class="text-[9px] text-gray-500">ID: TX-992 | Montant: 12,500 USD | Client: KP-002</div>
                </div>
            </div>
            <button class="text-[9px] font-bold text-red-500 underline uppercase">Justifier</button>
        </div>

        <div class="flex items-center justify-between p-3 bg-orange-900/10 border border-orange-900/30 rounded-lg">
            <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-orange-600/20 rounded-full flex items-center justify-center text-orange-500">
                    <i class="fa-solid fa-user-slash"></i>
                </div>
                <div>
                    <div class="text-[11px] font-bold text-white uppercase">Suspicion d'Identité (PEP)</div>
                    <div class="text-[9px] text-gray-500">Match partiel sur la liste CENAREF | Investigation requise</div>
                </div>
            </div>
            <button class="text-[9px] font-bold text-orange-500 underline uppercase">Signaler</button>
        </div>
    </div>

    <div class="mt-6 p-4 bg-gray-900/50 rounded-xl flex items-start gap-3">
        <i class="fa-solid fa-info-circle text-blue-400 text-sm mt-1"></i>
        <p class="text-[10px] text-gray-500 leading-relaxed italic">
            <strong>Transparence KUYApaie :</strong> Ce moteur ne sert pas à restreindre vos libertés, mais à protéger l'économie nationale. En respectant les normes <strong>AML/CFT</strong>, nous redonnons à la RDC sa place dans le concert des nations financières fiables.
        </p>
    </div>
</section>