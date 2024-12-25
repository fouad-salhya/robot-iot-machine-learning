import joblib
import m2cgen as m2c

# Charger le modèle
model = joblib.load('robot.pkl')

# Convertir le modèle en code C++
code = m2c.export_to_c(model)

# Écrire le code C++ dans un fichier
with open('model_arduino.cpp', 'w') as f:
    f.write(code)
