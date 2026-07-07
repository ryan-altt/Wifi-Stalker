# Wifi-tracker

Un petit outil en Python pour détecter des mouvements dans une pièce en surveillant les variations du signal RSSI d'un réseau Wi-Fi.

## Le principe
L'idée est simple : le corps humain absorbe et réfléchit les ondes radio (2.4GHz/5GHz). Quand quelqu'un passe entre la borne Wi-Fi et le récepteur, le RSSI fluctue.

Le script fonctionne en deux temps :
1. **Calibrage** : On échantillonne le signal dans une pièce vide pour établir une moyenne de base.
2. **Surveillance** : On monitor le signal en continu. Si le RSSI chute significativement sous la moyenne calibrée, on considère qu'il y a un mouvement.

## Setup rapide

Le projet tourne sous Linux (nécessite `nmcli` et `NetworkManager`).

```bash
# Installation des dépendances
pip install pandas matplotlib
```

## Utilisation

Lancer le détecteur en passant le nom (SSID) du réseau à surveiller :

```bash
python detector.py "Ton_Wifi_Name"
```

## Analyse des données
Les valeurs de signal sont stockées dans `data.csv`. Le script permet également de générer des graphiques via Matplotlib pour analyser la stabilité du signal et l'impact réel des mouvements.

## Limites connues
- **Sensibilité** : Dépend fortement de l'environnement et du matériel Wi-Fi utilisé.
- **Faux positifs** : D'autres objets métalliques en mouvement ou des appareils électroniques peuvent perturber le signal.
