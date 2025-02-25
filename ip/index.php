<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADRESSE IP</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzFhNzNlOCI+PHBhdGggZD0iTTE2IDFINGMtMS4xIDAtMiAuOS0yIDJ2MTRoMlYzaDEyVjF6bTMgNEg4Yy0xLjEgMC0yIC45LTIgMnYxNGMwIDEuMS45IDIgMiAyaDExYzEuMSAwIDItLjkgMi0yVjdjMC0xLjEtLjktMi0yLTJ6bTAgMTZIOFY3aDExdjE0eiIvPjwvc3ZnPg==">
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }
        .ip-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .ip-text {
            color: #1a73e8;
            font-size: 1.5rem;
            margin: 0;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .label {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        .copy-button {
            background: none;
            border: none;
            cursor: pointer;
            padding: 5px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s;
        }
        .copy-button:hover {
            transform: scale(1.1);
        }
        .copy-button svg {
            width: 20px;
            height: 20px;
            fill: #1a73e8;
        }
        .copy-notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #4caf50;
            color: white;
            padding: 1rem;
            border-radius: 5px;
            display: none;
            animation: fadeIn 0.3s, fadeOut 0.3s 1.7s;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeOut {
            from { opacity: 1; transform: translateY(0); }
            to { opacity: 0; transform: translateY(-20px); }
        }
    </style>
</head>
<body>
    <div class="ip-container">
        <div class="label">VOTRE ADRESSE IP</div>
        <p class="ip-text">
            <?php echo $_SERVER['REMOTE_ADDR']; ?>
            <button class="copy-button" onclick="copyIP()" title="Copier l'IP">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                </svg>
            </button>
        </p>
    </div>
    <div class="copy-notification" id="notification">IP copiée !</div>

    <script>
        function copyIP() {
            navigator.clipboard.writeText('<?php echo $_SERVER['REMOTE_ADDR']; ?>');
            const notification = document.getElementById('notification');
            notification.style.display = 'block';
            setTimeout(() => {
                notification.style.display = 'none';
            }, 2000);
        }
    </script>
</body>
</html>