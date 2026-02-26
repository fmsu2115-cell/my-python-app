from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Python App</title>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

        :root {
            --bg: #0a0a0f;
            --surface: #13131a;
            --accent: #7fff6e;
            --accent2: #3d9eff;
            --text: #e8e8f0;
            --muted: #6b6b80;
        }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'DM Sans', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .bg-grid {
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(127,255,110,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(127,255,110,0.03) 1px, transparent 1px);
            background-size: 48px 48px;
            pointer-events: none;
        }

        .glow {
            position: fixed;
            width: 600px;
            height: 600px;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.15;
            pointer-events: none;
        }
        .glow-1 { background: var(--accent); top: -200px; left: -100px; }
        .glow-2 { background: var(--accent2); bottom: -200px; right: -100px; }

        .card {
            position: relative;
            z-index: 10;
            background: var(--surface);
            border: 1px solid rgba(127,255,110,0.15);
            border-radius: 24px;
            padding: 60px 70px;
            max-width: 560px;
            width: 90%;
            text-align: center;
            animation: rise 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
            box-shadow: 0 0 0 1px rgba(255,255,255,0.03), 0 40px 80px rgba(0,0,0,0.5);
        }

        @keyframes rise {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .badge {
            display: inline-block;
            background: rgba(127,255,110,0.1);
            border: 1px solid rgba(127,255,110,0.3);
            color: var(--accent);
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            padding: 6px 14px;
            border-radius: 100px;
            margin-bottom: 28px;
            animation: rise 0.8s 0.1s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        .dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            background: var(--accent);
            border-radius: 50%;
            margin-right: 7px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }

        h1 {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2.2rem, 5vw, 3rem);
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 20px;
            animation: rise 0.8s 0.2s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        h1 span {
            background: linear-gradient(135deg, var(--accent), var(--accent2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        p {
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.7;
            font-weight: 300;
            margin-bottom: 40px;
            animation: rise 0.8s 0.3s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        .stats {
            display: flex;
            gap: 1px;
            background: rgba(255,255,255,0.06);
            border-radius: 14px;
            overflow: hidden;
            animation: rise 0.8s 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        .stat {
            flex: 1;
            background: var(--surface);
            padding: 20px 16px;
            transition: background 0.2s;
        }

        .stat:hover { background: rgba(127,255,110,0.05); }

        .stat-value {
            font-family: 'Syne', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent);
        }

        .stat-label {
            font-size: 0.72rem;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-top: 4px;
        }
    </style>
</head>
<body>
    <div class="bg-grid"></div>
    <div class="glow glow-1"></div>
    <div class="glow glow-2"></div>

    <div class="card">
        <div class="badge"><span class="dot"></span>Live on Railway</div>
        <h1>Hello,<br><span>World!</span></h1>
        <p>Your first Python Flask app is up and running. Built with Python, deployed on Railway — no coding experience needed.</p>
        <div class="stats">
            <div class="stat">
                <div class="stat-value">🐍</div>
                <div class="stat-label">Python</div>
            </div>
            <div class="stat">
                <div class="stat-value">⚡</div>
                <div class="stat-label">Flask</div>
            </div>
            <div class="stat">
                <div class="stat-value">🚀</div>
                <div class="stat-label">Railway</div>
            </div>
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
