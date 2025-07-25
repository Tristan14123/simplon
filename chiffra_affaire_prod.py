import plotly.express as px
import pandas as pd

# Charger les données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Calculer le chiffre d'affaires
données['ca'] = données['qte'] * données['prix']

# Créer le graphique en secteurs
figure = px.pie(données, values='ca', names='produit', title='Chiffre d\'affaires vendu par produit')

# Sauvegarder sous HTML
figure.write_html('ca-par-produit.html')

print('ca-par-produit.html généré avec succès !')
