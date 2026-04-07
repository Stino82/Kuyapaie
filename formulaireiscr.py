<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KUYApaie | Inscription Sécurisée</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background: #0b0e11; color: #eaecef; } /* Couleurs type Binance */
        .input-field { background: #1e2329; border: 1px solid #474d57; border-radius: 4px; padding: 12px; width: 100%; color: white; transition: 0.3s; }
        .input-field:focus { border-color: #f0b90b; outline: none; }
        .btn-gold { background: #f0b90b; color: #1e2329; font-weight: 600; padding: 14px; border-radius: 4px; width: 100%; transition: 0.8s; }
        .btn-gold:hover { background: #d9a508; }
        .step { display: none; }
        .step.active { display: block; }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen p-4">

<div class="max-w-2xl w-full bg-[#1e2329] p-8 rounded-xl shadow-2xl">
    <div class="text-center mb-8">
        <h1 class="text-2xl font-bold text-[#f0b90b]">Créer un compte KUYApaie</h1>
        <p class="text-gray-400 text-sm">Rejoignez l'élite financière de la RDC</p>
    </div>

    <div class="flex justify-end mb-4">
        <select class="bg-transparent border-none text-xs text-gray-400 outline-none">
            <option>Français</option><option>English</option><option>Lingala</option>
            <option>Swahili</option><option>Tshiluba</option><option>Kikongo</option>
        </select>
    </div>

    <form id="regForm">
        <div class="step active" id="step1">
            <h3 class="mb-4 text-gray-300 border-b border-gray-700 pb-2">1. Identité & Sexe</h3>
            <div class="grid grid-cols-2 gap-4">
                <input type="text" placeholder="Nom" class="input-field" required>
                <input type="text" placeholder="Post-nom" class="input-field" required>
                <input type="text" placeholder="Prénom" class="input-field" required>
                <select class="input-field">
                    <option value="">Sexe</option>
                    <option>Homme</option><option>Femme</option>
                </select>
            </div>
            <button type="button" onclick="nextStep(2)" class="btn-gold mt-6">Suivant</button>
        </div>

        <div class="step" id="step2">
            <h3 class="mb-4 text-gray-300 border-b border-gray-700 pb-2">2. Localisation Géographique</h3>
            <div class="grid grid-cols-2 gap-4">
                <select class="input-field"><option>République Démocratique du Congo</option></select>
                <select class="input-field" id="province">
                    <option>Province (26)</option>
                    <option>Kinshasa</option><option>Haut-Katanga</option><option>Lualaba</option> </select>
                <input type="text" placeholder="Ville / Territoire" class="input-field">
                <input type="text" placeholder="Commune / District" class="input-field">
                <input type="text" placeholder="Quartier" class="input-field">
                <input type="text" placeholder="Avenue & Numéro" class="input-field">
            </div>
            <div class="flex gap-2 mt-6">
                <button type="button" onclick="nextStep(1)" class="bg-gray-600 p-3 rounded w-1/3">Retour</button>
                <button type="button" onclick="nextStep(3)" class="btn-gold w-2/3">Suivant</button>
            </div>
        </div>

        <div class="step" id="step3">
            <h3 class="mb-4 text-gray-300 border-b border-gray-700 pb-2">3. Sécurité & Profession</h3>
            <div class="space-y-4">
                <select class="input-field">
                    <option>Service / Statut</option>
                    <option>Travailleur</option><option>Indépendant (Libéral)</option>
                    <option>Étudiant</option><option>Chômeur</option>
                </select>
                <input type="email" placeholder="Gmail (Validation requise)" class="input-field" required>
                <input type="tel" placeholder="+243 Numéro de téléphone" class="input-field" required>
                
                <div class="relative">
                    <input type="password" id="pass" placeholder="Mot de passe (8+ char, Maj, Symbole)" class="input-field" required>
                </div>
                <input type="password" id="confirm_pass" placeholder="Confirmer mot de passe" class="input-field" required>
                
                <div class="flex items-center gap-2 text-sm text-gray-400">
                    <input type="checkbox" id="remember"> <label for="remember">Se souvenir de moi</label>
                </div>

                <div class="bg-[#2b3139] p-3 rounded text-center text-xs">
                    <input type="checkbox" required> Je ne suis pas un robot
                </div>
            </div>

            <div class="flex gap-2 mt-6">
                <button type="button" onclick="nextStep(2)" class="bg-gray-600 p-3 rounded w-1/3">Retour</button>
                <button type="submit" class="btn-gold w-2/3">Finaliser l'inscription</button>
            </div>
        </div>
    </form>

    <div class="mt-6 text-center text-sm">
        <a href="#" class="text-[#f0b90b] hover:underline">Mot de passe oublié ?</a> | 
        <a href="#" class="text-[#f0b90b] hover:underline">Gmail perdu ?</a>
    </div>
</div>

<script>
    function nextStep(stepNumber) {
        document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
        document.getElementById('step' + stepNumber).classList.add('active');
    }

    document.getElementById('regForm').onsubmit = function(e) {
        e.preventDefault();
        alert("Succès ! Un mail d'activation a été envoyé à votre Gmail. Expire dans 2 min.");
        window.location.href = "#kyc-tab"; // Redirection vers onglet KYC
    };
</script>

</body>
</html>