# fikset dict value med fillna bbfil og ffill for å bli kvitt NaN som ikke blir borte med .mean:

<!-- Fyller inn gjennomsnittsverdier hvor det egentlig er NaN verdier -->
 df["Verdi"] = df["Verdi"].fillna(df["Verdi"].rolling(7, min_periods=1).mean())


<!-- Resterende Nan verdier som ikke blir borte, håndteres ved å kopiere tallene ved siden av seg -->
        df["Verdi"] = df["Verdi"].ffill().bfill()



