<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KUYApaie Dashboard | Souveraineté & Confiance</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
    <style>
        :root { --kuyagold: #f0b90b; --dark-bg: #0b0e11; --card-bg: #1e2329; }
        body { background-color: var(--dark-bg); color: white; font-family: 'Inter', sans-serif; }
        
        /* Animation du Panneau Publicitaire */
        .news-slide { display: none; animation: fade 1.5s; }
        .news-slide.active { display: block; }
        @keyframes fade { from {opacity: .4} to {opacity: 1} }

        .glass-card { background: rgba(30, 35, 41, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }
        .balance-blur { filter: blur(8px); transition: filter 0.3s ease; }
        
        /* Custom scrollbar pour mobile */
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
    </style>
</head>
<body class="pb-24">

    <header class="p-4 flex justify-between items-center border-b border-gray-800 sticky top-0 z-50 bg-[#0b0e11]/90 backdrop-blur-md">
        <div class="flex items-center gap-2">
            <div class="w-10 h-10 bg-[#f0b90b] rounded-full flex items-center justify-center text-black font-bold shadow-[0_0_15px_rgba(240,185,11,0.3)]">K</div>
            <span class="font-bold text-xl tracking-tight uppercase">KUYA<span class="text-[#f0b90b]">paie</span></span>
        </div>
        <div class="flex gap-4 items-center">
            <i class="fa-solid fa-magnifying-glass text-gray-400"></i>
            <div class="relative">
                <i class="fa-solid fa-bell text-gray-400 text-xl"></i>
                <span class="absolute -top-1 -right-1 bg-red-500 w-2 h-2 rounded-full"></span>
            </div>
        </div>
    </header>

    <main class="p-4 max-w-lg mx-auto space-y-6">
        
        <section class="glass-card rounded-2xl p-6 shadow-2xl relative overflow-hidden border-t border-white/10">
            <div class="flex justify-between items-center mb-4">
                <div class="flex items-center gap-2">
                    <i class="fa-solid fa-wallet text-[#f0b90b] text-xs"></i>
                    <span class="text-gray-400 text-xs uppercase tracking-wider font-semibold">Solde Total Estimé</span>
                </div>
                <button onclick="toggleBalance()" class="text-gray-400 hover:text-[#f0b90b] transition-colors">
                    <i id="eyeIcon" class="fa-solid fa-eye-slash"></i>
                </button>
            </div>
            
            <div id="balanceContainer" class="space-y-3 transition-all duration-300">
                <div class="text-4xl font-black tracking-tight">0.00 <span class="text-sm text-gray-500 font-medium">USD</span></div>
                <div class="text-xl text-gray-400 font-medium">0.00 <span class="text-xs text-gray-600 uppercase">CDF</span></div>
            </div>
            
            <div class="absolute -right-6 -bottom-6 opacity-[0.03] rotate-12">
                <i class="fa-solid fa-shield-halved text-9xl"></i>
            </div>
        </section>

        <section class="space-y-3">
            <div class="glass-card rounded-xl p-4 flex items-center justify-between border-l-4 border-green-500">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span class="relative flex h-2 w-2">
                            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                            <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                        </span>
                        <span class="text-[10px] text-gray-400 uppercase font-bold tracking-widest">Taux Direct BCC 24/7</span>
                    </div>
                    <div class="text-2xl font-black" id="bcc-rate">2,854.42 <span class="text-xs text-gray-500 font-normal">CDF/USD</span></div>
                </div>
                <div class="text-right">
                    <div class="text-green-500 text-xs font-bold">+0.04% ▲</div>
                    <div class="text-[9px] text-gray-500 mt-1" id="last-sync">--:--:--</div>
                </div>
            </div>

            <div class="glass-card rounded-xl overflow-hidden border border-white/5">
                <div class="p-3 bg-white/5 flex justify-between items-center">
                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-chart-line text-[#f0b90b] text-xs"></i>
                        <span class="text-[10px] font-bold text-gray-300">COURS TEMPS RÉEL (BOUGIES)</span>
                    </div>
                    <div class="flex gap-1">
                        <span class="text-[8px] px-2 py-0.5 rounded bg-[#f0b90b] text-black font-bold">LIVE</span>
                    </div>
                </div>
                <div id="chartContainer" style="height: 180px; width: 100%;"></div>
            </div>
        </section>

        <section>
            <div class="relative w-full h-44 rounded-2xl overflow-hidden shadow-2xl border border-white/5">
                <div class="news-slide active h-full bg-gradient-to-tr from-blue-900 via-blue-950 to-black p-6 flex flex-col justify-end">
                    <span class="bg-blue-600 text-[9px] px-2 py-0.5 rounded-full w-fit mb-2 font-bold">ÉCONOMIE RDC</span>
                    <h3 class="font-bold text-lg leading-tight">Stabilité du Franc : Le rôle de KUYApaie dans la couverture de change.</h3>
                </div>
                <div class="news-slide h-full bg-gradient-to-tr from-amber-800 via-amber-950 to-black p-6 flex flex-col justify-end">
                    <span class="bg-amber-600 text-[9px] px-2 py-0.5 rounded-full w-fit mb-2 font-bold">SOUVERAINETÉ</span>
                    <h3 class="font-bold text-lg leading-tight">Inspiration Tesla : L'automatisation financière au service de la Nation.</h3>
                </div>
                
                <div class="absolute bottom-3 right-6 flex gap-1.5">
                    <div class="w-1.5 h-1.5 bg-white rounded-full"></div>
                    <div class="w-1.5 h-1.5 bg-white/30 rounded-full"></div>
                </div>
            </div>
        </section>

        <section class="bg-gradient-to-r from-[#1e2329] to-transparent border-l-4 border-[#f0b90b] p-5 rounded-r-2xl">
            <div class="flex items-start gap-4">
                <div class="text-[#f0b90b] animate-pulse">
                    <i class="fa-solid fa-handshake-angle text-2xl"></i>
                </div>
                <div>
                    <h4 class="font-bold text-sm mb-1 text-white">Engagement & Souveraineté</h4>
                    <p class="text-gray-400 text-[11px] leading-relaxed">
                        Le rangement stratégique de <strong>KUYApaie</strong> assure une traçabilité sans faille. 
                        Aujourd'hui, la population congolaise nous accorde sa confiance pour transformer chaque virement en un levier de développement national.
                    </p>
                </div>
            </div>
        </section>

    </main>

    <nav class="fixed bottom-0 w-full bg-[#181a20]/95 backdrop-blur-lg border-t border-gray-800 flex justify-around p-4 z-50">
        <div class="flex flex-col items-center text-[#f0b90b] scale-110">
            <i class="fa-solid fa-house"></i>
            <span class="text-[9px] mt-1 font-medium">Accueil</span>
        </div>
        <div class="flex flex-col items-center text-gray-500 hover:text-white transition-colors">
            <i class="fa-solid fa-chart-pie"></i>
            <span class="text-[9px] mt-1 font-medium">Marchés</span>
        </div>
        <div class="flex flex-col items-center text-gray-500 hover:text-white transition-colors">
            <i class="fa-solid fa-shield-halved"></i>
            <span class="text-[9px] mt-1 font-medium">Sécurité</span>
        </div>
        <div class="flex flex-col items-center text-gray-500 hover:text-white transition-colors">
            <i class="fa-solid fa-user-gear"></i>
            <span class="text-[9px] mt-1 font-medium">Profil</span>
        </div>
    </nav>

    <script>
        // --- GESTION DU SOLDE ---
        function toggleBalance() {
            const container = document.getElementById('balanceContainer');
            const icon = document.getElementById('eyeIcon');
            container.classList.toggle('balance-blur');
            icon.classList.toggle('fa-eye-slash');
            icon.classList.toggle('fa-eye');
        }

        // --- CARROUSEL NEWS ---
        let slideIndex = 0;
        function showSlides() {
            let slides = document.getElementsByClassName("news-slide");
            for (let i = 0; i < slides.length; i++) slides[i].classList.remove('active');
            slideIndex++;
            if (slideIndex > slides.length) slideIndex = 1;
            slides[slideIndex-1].classList.add('active');
            setTimeout(showSlides, 6000);
        }
        showSlides();

        // --- GRAPHIQUE TRADINGVIEW (Lightweight Charts) ---
        const chart = LightweightCharts.createChart(document.getElementById('chartContainer'), {
            layout: { background: { color: 'transparent' }, textColor: '#64748b' },
            grid: { vertLines: { color: 'rgba(255, 255, 255, 0.05)' }, horzLines: { color: 'rgba(255, 255, 255, 0.05)' } },
            rightPriceScale: { borderVisible: false },
            timeScale: { borderVisible: false, timeVisible: true },
            handleScroll: false, handleScale: false, // Fixe pour mobile
        });

        const candlestickSeries = chart.addCandlestickSeries({
            upColor: '#22c55e', downColor: '#ef4444', borderVisible: false,
            wickUpColor: '#22c55e', wickDownColor: '#ef4444'
        });

        // Données historiques simulées
        const data = [
            { time: '2026-04-01', open: 2840, high: 2855, low: 2835, close: 2850 },
            { time: '2026-04-02', open: 2850, high: 2860, low: 2845, close: 2858 },
            { time: '2026-04-03', open: 2858, high: 2858, low: 2840, close: 2842 },
            { time: '2026-04-04', open: 2842, high: 2865, low: 2840, close: 2860 },
            { time: '2026-04-05', open: 2860, high: 2870, low: 2855, close: 2865 },
            { time: '2026-04-06', open: 2865, high: 2868, low: 2850, close: 2854 },
            { time: '2026-04-07', open: 2854, high: 2860, low: 2850, close: 2854.42 },
        ];
        candlestickSeries.setData(data);
        chart.timeScale().fitContent();

        // --- SIMULATION TAUX BCC LIVE ---
        function updateBCC() {
            const base = 2854.42;
            const fluctuation = (Math.random() * 2) - 1;
            const finalRate = (base + fluctuation).toLocaleString('fr-FR', { minimumFractionDigits: 2 });
            document.getElementById('bcc-rate').innerHTML = `${finalRate} <span class="text-xs text-gray-500 font-normal">CDF/USD</span>`;
            document.getElementById('last-sync').innerText = new Date().toLocaleTimeString();
        }
        setInterval(updateBCC, 3000);
        updateBCC();
    </script>
</body>
</html>