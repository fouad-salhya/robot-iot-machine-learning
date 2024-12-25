import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import joblib  
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données depuis le fichier CSV existant
data = pd.read_csv('rebot.csv')


X = data.drop('action',axis=1)
y = data['action']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Étape 2 : Création du modèle
model = DecisionTreeClassifier(random_state=42)

# Étape 3 : Entraînement du modèle
model.fit(X_train, y_train)

# Étape 4 : Évaluation du modèle
y_pred = model.predict(X_test)

print("Score de précision :", accuracy_score(y_test, y_pred))
# print("Rapport de classification :\n", classification_report(y_test, y_pred))

#sauvegarder le model 
joblib.dump(model, 'robot.pkl')

# # Matrice de confusion
# conf_matrix = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(10, 7))
# sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
# plt.title('Matrice de confusion')
# plt.xlabel('Prédictions')
# plt.ylabel('Vérités terrain')
# plt.show()

# # Courbe ROC (si la sortie est binaire, sinon ajuster la courbe pour multiclasses)
# if len(model.classes_) == 2:
#     # Calcul de la courbe ROC
#     y_prob = model.predict_proba(X_test)[:, 1]  # Probabilités pour la classe positive
#     fpr, tpr, _ = roc_curve(y_test, y_prob)
#     roc_auc = auc(fpr, tpr)

#     plt.figure(figsize=(10, 7))
#     plt.plot(fpr, tpr, color='darkorange', lw=2, label='Courbe ROC (AUC = {:.2f})'.format(roc_auc))
#     plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
#     plt.xlabel('Taux de faux positifs')
#     plt.ylabel('Taux de vrais positifs')
#     plt.title('Courbe ROC')
#     plt.legend(loc='lower right')
#     plt.show()

# # Visualiser les résultats avec un graphique en barres
# comparison_df = pd.DataFrame({'Vérités terrain': y_test, 'Prédictions': y_pred})
# comparison_df = comparison_df.melt(value_vars=['Vérités terrain', 'Prédictions'], var_name='Type', value_name='Action')

# plt.figure(figsize=(12, 6))
# sns.countplot(data=comparison_df, x='Action', hue='Type')
# plt.title('Comparaison entre Vérités terrain et Prédictions')
# plt.xlabel('Action')
# plt.ylabel('Nombre de cas')
# plt.legend(title='Type')
# plt.show()
