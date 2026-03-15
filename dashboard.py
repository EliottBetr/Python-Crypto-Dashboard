import requests
from datetime import datetime

def fetch_crypto_data():
    """Récupère les données depuis l'API publique de CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Paramètres de notre requête (les cryptos qu'on veut, et les monnaies)
    params = {
        "ids": "bitcoin,ethereum,solana,ripple,cardano",
        "vs_currencies": "usd,eur",
        "include_24hr_change": "true"
    }
    
    try:
        # Envoi de la requête HTTP GET
        response = requests.get(url, params=params)
        response.raise_for_status() # Vérifie s'il y a une erreur HTTP (ex: 404, 500)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à l'API : {e}")
        return None

def display_dashboard(data):
    """Affiche les données sous forme de tableau dans la console."""
    if not data:
        print("Aucune donnée à afficher.")
        return
        
    print("=" * 65)
    print(f"DASHBOARD CRYPTO EN TEMPS RÉEL - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 65)
    print(f"{'Cryptomonnaie':<15} | {'Prix (USD)':<12} | {'Prix (EUR)':<12} | {'Var 24h (%)':<10}")
    print("-" * 65)
    
    # Parcours des données récupérées
    for crypto, info in data.items():
        name = crypto.capitalize()
        usd_price = f"${info.get('usd', 0):,.2f}"
        eur_price = f"€{info.get('eur', 0):,.2f}"
        change_24h = info.get('usd_24h_change', 0)
        
        # Ajout d'un '+' pour les valeurs positives pour plus de clarté
        change_str = f"{'+' if change_24h > 0 else ''}{change_24h:.2f}%"
        
        print(f"{name:<15} | {usd_price:<12} | {eur_price:<12} | {change_str:<10}")
    
    print("=" * 65)
    print("Données fournies par l'API CoinGecko")

if __name__ == "__main__":
    print("Récupération des données en cours depuis le serveur...")
    crypto_data = fetch_crypto_data()
    display_dashboard(crypto_data)