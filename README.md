---

# 🌐 Documentation

---

## 🎯 Features (Fonctionnalités)

Wifi-Stalker détecte le mouvement humain en utilisant les variations du signal Wi-Fi RSSI :

- **Détection de mouvement**: Détection automatique de personnes en mouvement
- **Analyse en temps réel**: Surveillance continue du signal Wi-Fi
- **Visualisation**: Affichage des indicateurs de mouvement et seuils
- **Calibration intelligente**: 15 échantillons pour une meilleure précision
- **Sensibilité ajustable**: Marge de détection configurable (5 dBm par défaut)

---

## 📋 Requirements (Configuration requise)

- **Système d'exploitation**: Linux (testé sur Arch Linux)
- **Dépendances**: Python 3.7+, outil en ligne de commande `networkmanager`
- **NetworkManager**: Doit être installé et en cours d'exécution

### Installation (Installation)

```bash
# Installer les dépendances
pip install pandas matplotlib

# Vérifier que NetworkManager est installé
nmcli --version
```

---

## 🚀 Usage (Utilisation)

Lancez le détecteur en passant le nom du réseau Wi-Fi (SSID) à surveiller :

```bash
python detector.py "Votre_Nom_WiFi"
```

### Example (Exemple)

```bash
# Surveiller un réseau Wi-Fi spécifique
python detector.py "Mon_WiFi_Maison"

# Surveiller un réseau Wi-Fi public
python detector.py "Free_WiFi_Public"
```

---

## 📊 Data Analysis (Analyse des données)

Les valeurs du signal sont automatiquement stockées dans `data.csv` pour une analyse ultérieure. Le script génère également des visualisations en temps réel :

- **Stabilité du signal**: Surveillance des fluctuations RSSI au fil du temps
- **Détection de mouvement**: Indicateurs visuels lors de la détection de mouvement
- **Surveillance des seuils**: Affichage de la moyenne de calibration et du seuil de détection

### Sample Output (Exemple de sortie)

```
[PHASE DE CALIBRATION]
Calibration [1/15] [|] RSSI: -45.23
Calibration [2/15] [/] RSSI: -44.89
Calibration [3/15] [-] RSSI: -45.67
...
Calibration termine. Moyenne: -45.12

Seuil de détection: -50.12 dBm (Moyenne: -45.12 - Marge: 5)

[PHASE DE SURVEILLANCE]
#MOUVEMENT DETECTE # RSSI: -51.23 < -50.12 [|]
```

---

## 🔧 Technical Details (Détails techniques)

### RSSI (Received Signal Strength Indicator)

- Mesuré en dBm (décibels par milliwatt)
- Plus les valeurs sont négatives, plus le signal est faible
- Plage Wi-Fi typique intérieure : -30 dBm à -90 dBm
- La moyenne de calibration détermine le seuil de détection

### Algorithme de détection (Algorithme de détection)

1. **Phase de calibration** (15 échantillons, délai de 0,5s chacun) :
   - Collecte la moyenne de RSSI de base
   - Établit le seuil de détection (moyenne - 5 dBm)

2. **Phase de surveillance** :
   - Lit continuellement le RSSI depuis NetworkManager
   - Compare le RSSI actuel au seuil
   - Vérifie le mouvement après 3 chutes consécutives
   - Feedback visuel avec indicateurs animés

### Configuration Options (Options de configuration)

Les paramètres de détection peuvent être ajustés dans `detector.py` :

```python
# Échantillons de calibration (défaut: 15)
for i in range(1, 16):

# Marge de détection (défaut: 5 dBm)
margin = 5

# Délai d'échantillonnage en secondes (défaut: 0.5)
time.sleep(0.5)
```

---

## 🛡️ Use Cases (Cas d'utilisation)

- **Détection d'occupation de pièce**: Détection automatique lorsque une pièce devient occupée
- **Domotique**: Déclencher des lumières ou autres appareils lorsqu'une personne entre
- **Gestion énergétique**: Optimiser le chauffage/refroidissement en fonction de l'occupation
- **Surveillance de sécurité**: Détecter les mouvements non autorisés dans les zones sécurisées
- **Surveillance de la confidentialité**: Observer les motifs de mouvement dans votre propre espace

---

## ⚠️ Known Limitations (Limitations connues)

### Problèmes de sensibilité

- **Dépendant de l'environnement**: La performance varie significativement selon la disposition de la pièce, le matériel Wi-Fi et les interférences
- **Limitations matérielles**: Différents adaptateurs Wi-Fi peuvent avoir des sensibilités différentes
- **Obstacles**: Murs épais, objets métalliques et autres interférences peuvent causer des fausses positives

### Fausses positives

- **Objets métalliques**: Les meubles en mouvement peuvent créer des fluctuations de signal
- **Dispositifs électroniques**: Appareils émettant des signaux RF (micro-ondes, téléphones sans fil)
- **Interférence externe**: Autres réseaux Wi-Fi fonctionnant à proximité

### Limitations pratiques

- **Distance**: La plage de détection dépend de la force du signal Wi-Fi et de la taille de la pièce
- **Position du corps**: L'efficacité de la détection varie selon la position du corps par rapport au routeur Wi-Fi
- **Type de mouvement**: La détection fonctionne mieux avec un mouvement direct vers/à partir du routeur

---

## 📄 License (Licence)

Ce projet est sous licence GNU GPLv3 - voir le fichier LICENSE pour plus de détails.

---

## 🤝 Contributing (Contribuer)

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir des issues pour les bugs ou demandes de fonctionnalités
- Soumettre des pull requests pour les améliorations
- Suggérer des améliorations de l'algorithme de détection

---

## 📧 Contact (Contact)

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub ou à nous contacter directement à ryansama.tech@gmail.com

---

## 🙏 Acknowledgments (Remerciements)

Cet outil a été créé pour démontrer l'utilisation de l'API NetworkManager pour les applications IoT et l'analyse de signaux. Le concept est inspiré par des recherches sur l'utilisation des variations de signal Wi-Fi pour la détection d'occupation.

---

## 📚 References (Références)

- [Documentation NetworkManager](https://developer.gnome.org/NetworkManager/stable/)
- [RSSI Wikipedia](https://en.wikipedia.org/wiki/Received-Signal-Strength_Indicator)
- [WiFi Occupancy Detection Research](https://arxiv.org/abs/1802.08527)

---

# 🇬🇧 English Documentation

## 🎯 Features

Wifi-Stalker detects human movement by monitoring Wi-Fi signal RSSI variations:

- **Movement Detection**: Automatically detect people in motion
- **Real-time Analysis**: Continuous monitoring of Wi-Fi signal
- **Visualization**: Display movement indicators and thresholds
- **Intelligent Calibration**: 15 samples for better accuracy
- **Adjustable Sensitivity**: Configurable detection margin (5 dBm default)

---

## 📋 Requirements

- **Operating System**: Linux (tested on Arch Linux)
- **Dependencies**: Python 3.7+, `networkmanager` command-line tool
- **NetworkManager**: Must be installed and running

### Installation

```bash
# Install dependencies
pip install pandas matplotlib

# Verify NetworkManager is installed
nmcli --version
```

---

## 🚀 Usage

Run the detector by passing the Wi-Fi network name (SSID) to monitor:

```bash
python detector.py "Your_WiFi_Name"
```

### Example

```bash
# Monitor a specific Wi-Fi network
python detector.py "My_Home_WiFi"

# Monitor a public Wi-Fi network
python detector.py "Free_WiFi_Public"
```

---

## 📊 Data Analysis

Signal values are automatically stored in `data.csv` for later analysis. The script also generates real-time visualizations:

- **Signal Stability**: Monitors RSSI fluctuations over time
- **Movement Detection**: Visual indicators show when movement is detected
- **Threshold Monitoring**: Displays calibration baseline and detection threshold

### Sample Output

```
[PHASE DE CALIBRATION]
Calibration [1/15] [|] RSSI: -45.23
Calibration [2/15] [/] RSSI: -44.89
Calibration [3/15] [-] RSSI: -45.67
...
Calibration termine. Moyenne: -45.12

Seuil de détection: -50.12 dBm (Moyenne: -45.12 - Marge: 5)

[PHASE DE SURVEILLANCE]
#MOUVEMENT DETECTE # RSSI: -51.23 < -50.12 [|]
```

---

## 🔧 Technical Details

### RSSI (Received Signal Strength Indicator)

- Measured in dBm (decibels per milliwatt)
- More negative values indicate weaker signals
- Typical indoor Wi-Fi range: -30 dBm to -90 dBm
- Calibration baseline determines the detection threshold

### Detection Algorithm

1. **Calibration Phase** (15 samples, 0.5s delay each):
   - Collects baseline RSSI average
   - Establishes detection threshold (baseline - 5 dBm)

2. **Monitoring Phase**:
   - Continuously reads RSSI from NetworkManager
   - Compares current RSSI to threshold
   - Verifies movement after 3 consecutive drops
   - Visual feedback with animated indicators

### Configuration Options

The detection parameters can be adjusted in `detector.py`:

```python
# Calibration samples (default: 15)
for i in range(1, 16):

# Detection margin (default: 5 dBm)
margin = 5

# Sample delay in seconds (default: 0.5)
time.sleep(0.5)
```

---

## 🛡️ Use Cases

- **Room Occupancy Detection**: Automatically detect when a room becomes occupied
- **Home Automation**: Trigger lights or other devices when someone enters
- **Energy Management**: Optimize heating/cooling based on room occupancy
- **Security Monitoring**: Detect unauthorized movement in secured areas
- **Privacy Monitoring**: Observe patterns of movement in your own space

---

## ⚠️ Known Limitations

### Sensitivity Issues
- **Environment Dependent**: Performance varies significantly based on room layout, Wi-Fi hardware, and interference
- **Hardware Limitations**: Different WiFi adapters may have different sensitivity
- **Obstacles**: Thick walls, metal objects, and other interference can cause false positives

### False Positives
- **Metal Objects**: Moving metal furniture can create signal fluctuations
- **Electronic Devices**: Devices emitting RF signals (microwaves, cordless phones)
- **External Interference**: Other Wi-Fi networks operating nearby

### Practical Limitations
- **Distance**: Detection range depends on WiFi signal strength and room size
- **Body Position**: Detection effectiveness varies based on body position relative to WiFi router
- **Movement Type**: Detection works best with direct movement toward/away from router

---

## 📄 License

This project is licensed under the GNU GPLv3 License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Suggest enhancements to the detection algorithm

---

## 📧 Contact

For any questions or suggestions, please open an issue on GitHub or contact directly at ryansama.tech@gmail.com

---

## 🙏 Acknowledgments

This tool was created to demonstrate the use of NetworkManager API for IoT applications and signal analysis. The concept is inspired by research on using WiFi signal variations for occupancy detection.

---

## 📚 References

- [NetworkManager Documentation](https://developer.gnome.org/NetworkManager/stable/)
- [RSSI Wikipedia](https://en.wikipedia.org/wiki/Received-Signal-Strength_Indicator)
- [WiFi Occupancy Detection Research](https://arxiv.org/abs/1802.08527)
