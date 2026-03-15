# Crypto Dashboard (Python CLI)

Un script Python léger permettant d'afficher en temps réel le cours des principales cryptomonnaies directement dans le terminal. 

Ce projet personnel a pour but de démontrer ma capacité à consommer une API REST publique et à traiter des données au format JSON.

## Stack Technique
- **Langage :** Python 3
- **Librairie HTTP :** `requests`
- **API utilisée :** [CoinGecko API V3](https://www.coingecko.com/en/api) (Données en temps réel, gratuite et sans clé API)

## Fonctionnalités
- Requête HTTP GET vers l'API CoinGecko.
- Récupération des prix en USD ($) et EUR (€).
- Calcul et affichage de la variation sur les dernières 24 heures.
- Formatage des données dans un tableau ASCII clair et lisible.
- Gestion des erreurs de connexion (Try/Except).

## Installation et Utilisation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone [https://github.com/EliottBetr/Python-Crypto-Dashboard.git](https://github.com/EliottBetr/Python-Crypto-Dashboard.git)
