# fikset dict value med fillna bbfil og ffill for å bli kvitt NaN som ikke blir borte med .mean:

<!-- Fyller inn gjennomsnittsverdier hvor det egentlig er NaN verdier -->
 df["Verdi"] = df["Verdi"].fillna(df["Verdi"].rolling(7, min_periods=1).mean())


<!-- Resterende Nan verdier som ikke blir borte, håndteres ved å kopiere tallene ved siden av seg -->
        df["Verdi"] = df["Verdi"].ffill().bfill()


# Svare på hvorfor median, mean og standardavvik er viktig:
Median gir tallet i midten og blir mindre påvirket av, så den gir et annet perspektiv enn mean og begge samtidig kan gi et perspektiv på sjevfordelingen i dataen. Og årsaker til at dataen kan være sjevfordelt er manglende verdier, problemer med datainnsamplingen eller at det er nye funn.
Standardavvik regner hvor nøyaktig dataene er.   


