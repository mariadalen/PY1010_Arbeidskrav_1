# PY1010 Arbeidskrav 1
# Maria Andriana Dalen, MAD
# 2024-11-02

# Python-program som beregner og presenterer de årlige totalkostnadene for elbil og bensinbil, 
# samt årlig kostnadsdifferanse basert på informasjonen under.

# Årlig kjørelengde
km_per_aar = 10000   # km/år for både bensin- og elbil

# Forsikringskostnader per år
forsikring_elbil = 5000  # kr/år for elbil
forsikring_bensinbil = 7500  # kr/år for bensinbil

#Trafikkforsikringsavgift per dag og per år
trafikkforsikringsavgift_per_dag = 8.38  # kr/dag for både bensin- og elbil
trafikkforsikringsavgift_per_aar = trafikkforsikringsavgift_per_dag * 365  # årlig trafikkforsikringsavgift = kr/dag * 365 dager

# Drivstofforbruk
drivstoff_elbil_per_km = 0.2  # kWh/km for elbil
strompris_per_kwh = 2.0  # kr pr kWh
drivstoff_bensinbil_per_km = 1.0  # kr/km for bensinbil

# Bomavgifter
bomavgift_elbil_per_km = 0.1  # kr/km for elbil
bomavgift_bensinbil_per_km = 0.3  # kr/km for bensinbil

# Årlige totalkostnader for elbil
aarlig_drivstoff_elbil = drivstoff_elbil_per_km * strompris_per_kwh * km_per_aar  # årlige drivstoffkostnader elbil = drivstoff/km * strømpris/km * årlig kjørelengde
aarlig_bomavgift_elbil = bomavgift_elbil_per_km * km_per_aar  # årlig bomavgift elbil = bomavgift/km * årlig kjørelengde

totalkostnad_elbil = forsikring_elbil + trafikkforsikringsavgift_per_aar + aarlig_drivstoff_elbil + aarlig_bomavgift_elbil

# Årlige totalkostnader for bensinbil
aarlig_drivstoff_bensinbil = drivstoff_bensinbil_per_km * km_per_aar  # årlig drivstoffkostnader bensinbil = drivstoff/km * årlig kjørelengde
aarlig_bomavgift_bensinbil = bomavgift_bensinbil_per_km * km_per_aar  # årlig bomavgift bensinfil = bomavgift/km * årlig kjørelengde

totalkostnad_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_per_aar + aarlig_drivstoff_bensinbil + aarlig_bomavgift_bensinbil

# Årlig kostnadsdifferanse mellom bensinbil og elbil
kostnadskifferanse = totalkostnad_bensinbil - totalkostnad_elbil  # totalkostnad bensinbil minus totalkostnad elbil

print ("Årlige totalkostnader for elbil =", totalkostnad_elbil)
print ("Arlige totalkostnader for bensinbil =", totalkostnad_bensinbil)
print ("Årlig kostnadsdifferanse =", kostnadskifferanse)
