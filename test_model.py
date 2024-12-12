import joblib
import pandas as pd

# Charger le modèle sauvegardé
model = joblib.load('robot.pkl')

# Demander à l'utilisateur d'entrer la valeur du capteur gauche
capteur_gauche = float(input("Entrez la valeur du capteur gauche : "))

# Demander à l'utilisateur d'entrer la valeur du capteur droit
capteur_droite = float(input("Entrez la valeur du capteur droit : "))

# Créer un DataFrame pour inclure les noms de colonnes comme attendu par le modèle
nouvelles_donnees = pd.DataFrame([[capteur_gauche, capteur_droite]], columns=['capteur_gauche', 'capteur_droite'])

# Faire la prédiction avec le modèle chargé
prediction = model.predict(nouvelles_donnees)

# Afficher le résultat de la prédiction
print("La prédiction pour l'action est :", prediction[0])
