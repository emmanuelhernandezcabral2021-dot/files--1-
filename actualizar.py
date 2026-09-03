import json
import requests

<<<<<<< HEAD
# Esta es la dirección limpia, real y sin errores
=======
>>>>>>> 9b2e5fcd22130df6ff5327dd35bc74737e37a57e
URL_API = "https://githubusercontent.com"

print("🤖 El robot en la nube está buscando los partidos reales...")

try:
    respuesta = requests.get(URL_API)
    datos_api = respuesta.json()
    partidos_nuevos = []
    
    if "rounds" in datos_api:
        ultima_jornada = datos_api["rounds"][-1]
        for juego in ultima_jornada.get("matches", [])[:10]:
            partidos_nuevos.append([
                juego["team1"],  
                juego["team2"],  
                "0-0"            
            ])

    leagues_actualizado = {
        "epl": {
            "label": "Premier League",
            "hasPlayers": True,
            "teams": [],
            "fixtures": partidos_nuevos,  
            "upcoming": [],
            "standings": []
        },
        "laliga": { "label": "La Liga", "teams": [], "fixtures": [], "upcoming": [], "standings": [] },
        "seriea": { "label": "Serie A", "teams": [], "fixtures": [], "upcoming": [], "standings": [] },
        "bundesliga": { "label": "Bundesliga", "teams": [], "fixtures": [], "upcoming": [], "standings": [] },
        "ligue1": { "label": "Ligue 1", "teams": [], "fixtures": [], "upcoming": [], "standings": [] },
        "mls": { "label": "MLS", "teams": [], "fixtures": [], "upcoming": [], "standings": [] }
    }

    with open("datos.js", "w", encoding="utf-8") as archivo:
        archivo.write(f"const LEAGUES = {json.dumps(leagues_actualizado, ensure_ascii=False, indent=2)};\n")
        archivo.write("window.LEAGUES = LEAGUES;")
        
    print("✅ ¡Éxito! Archivo guardado correctamente.")

except Exception as error:
    print(f"❌ Hubo un problema: {error}")
