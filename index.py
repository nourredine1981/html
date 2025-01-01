# Paramètres d'entrée pour le dimensionnement du réservoir
débit_eau = 1000  # en m3/jour
temps_retention = 5  # en jours

# Calcul du volume du réservoir
volume_reservoir = débit_eau * temps_retention
print(f"Le volume du réservoir nécessaire est de {volume_reservoir} m3")
