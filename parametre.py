<section class="glass-card rounded-3xl p-6 mt-6 border-t-4 border-gray-600 bg-[#0b0e11] shadow-2xl pb-10">
    
    <div class="flex items-center gap-4 mb-8 p-4 bg-white/5 rounded-2xl border border-white/5">
        <div class="relative">
            <div class="w-14 h-14 bg-gradient-to-tr from-[#f0b90b] to-yellow-200 rounded-full flex items-center justify-center text-black font-black text-xl">
                JD
            </div>
            <div class="absolute -bottom-1 -right-1 w-5 h-5 bg-green-500 border-2 border-[#0b0e11] rounded-full flex items-center justify-center">
                <i class="fa-solid fa-check text-[10px] text-white"></i>
            </div>
        </div>
        <div>
            <h3 class="text-lg font-black text-white">Jean Dupont</h3>
            <p class="text-[10px] text-gray-500 font-bold uppercase tracking-widest">ID: KP-243-99201</p>
            <span class="text-[9px] bg-green-500/20 text-green-500 px-2 py-0.5 rounded-full font-bold">Compte Vérifié (KYC)</span>
        </div>
    </div>

    <div class="space-y-2">
        
        <div class="flex items-center justify-between p-4 bg-white/5 rounded-2xl hover:bg-white/10 transition-all cursor-pointer group">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-blue-500/10 rounded-xl flex items-center justify-center text-blue-500">
                    <i class="fa-solid fa-id-card"></i>
                </div>
                <div>
                    <div class="text-sm font-bold text-white">Vérification d'identité</div>
                    <div class="text-[10px] text-gray-500">Niveau 2 : Limite 50,000 USD/jour</div>
                </div>
            </div>
            <i class="fa-solid fa-chevron-right text-gray-600 group-hover:text-white transition-colors"></i>
        </div>

        <div class="flex items-center justify-between p-4 bg-white/5 rounded-2xl hover:bg-white/10 transition-all cursor-pointer group">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-red-500/10 rounded-xl flex items-center justify-center text-red-500">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
                <div>
                    <div class="text-sm font-bold text-white">Sécurité & OTP</div>
                    <div class="text-[10px] text-gray-500">SIM Bind : +243 81... | AES-256 Actif</div>
                </div>
            </div>
            <i class="fa-solid fa-chevron-right text-gray-600 group-hover:text-white transition-colors"></i>
        </div>

        <div class="flex items-center justify-between p-4 bg-white/5 rounded-2xl hover:bg-white/10 transition-all cursor-pointer group">
            <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-gray-500/10 rounded-xl flex items-center justify-center text-gray-400">
                    <i class="fa-solid fa-gears"></i>
                </div>
                <div>
                    <div class="text-sm font-bold text-white">Paramètres Généraux</div>
                    <div class="text-[10px] text-gray-500">Langue: Français | Devise: USD/CDF</div>
                </div>
            </div>
            <i class="fa-solid fa-chevron-right text-gray-600 group-hover:text-white transition-colors"></i>
        </div>

        <div onclick="openSupport()" class="mt-6 p-6 bg-gradient-to-r from-blue-600 to-blue-800 rounded-3xl shadow-xl shadow-blue-900/20 cursor-pointer active:scale-95 transition-all">
            <div class="flex justify-between items-start mb-4">
                <div class="w-12 h-12 bg-white/20 rounded-2xl flex items-center justify-center">
                    <i class="fa-solid fa-headset text-white text-2xl animate-pulse"></i>
                </div>
                <span class="text-[9px] bg-green-400 text-black px-2 py-1 rounded-full font-black">EN LIGNE</span>
            </div>
            <h4 class="text-lg font-black text-white uppercase italic tracking-tighter">Support Client 24h/24</h4>
            <p class="text-[10px] text-blue-100 mt-1">Un expert KUYApaie résout vos problèmes en moins de 2 minutes.</p>
        </div>

    </div>

    <div class="mt-10 grid grid-cols-2 gap-4 text-center">
        <div class="p-4 border border-white/5 rounded-2xl">
            <i class="fa-solid fa-file-contract text-gray-600 mb-2"></i>
            <div class="text-[8px] text-gray-500 uppercase font-bold">Mentions Légales</div>
        </div>
        <div class="p-4 border border-white/5 rounded-2xl">
            <i class="fa-solid fa-building-columns text-gray-600 mb-2"></i>
            <div class="text-[8px] text-gray-500 uppercase font-bold">Licence BCC</div>
        </div>
    </div>

    <button class="w-full mt-10 py-4 text-red-500 font-bold text-xs uppercase tracking-widest border border-red-500/20 rounded-2xl hover:bg-red-500 hover:text-white transition-all">
        Déconnexion Sécurisée
    </button>
</section>

<script>
    function openSupport() {
        alert("🎧 Connexion au Centre de Support KUYApaie...\n\nUn conseiller va analyser votre dossier (ID: KP-243-99201) et vous répondre immédiatement.\n\nTemps d'attente estimé : 45 secondes.");
    }
</script>