"""CampusPulse: ejemplo didáctico para aprender Git (sin dependencias externas)."""
from collections import defaultdict
from configparser import ConfigParser
from csv import DictReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def leer_mediciones(ruta=ROOT / "data" / "mediciones.csv"):
    """Devuelve una lista de mediciones (consumo_kwh se convierte a float)."""
    with open(ruta, encoding="utf-8", newline="") as fichero:
        filas = list(DictReader(fichero))
    for fila in filas:
        fila["consumo_kwh"] = float(fila["consumo_kwh"])
    return filas


def resumir_por_sensor(mediciones):
    """Calcula nº de lecturas y media por sensor."""
    grupos = defaultdict(list)
    for fila in mediciones:
        grupos[fila["id_sensor"]].append(fila["consumo_kwh"])
    return {
        sensor: {"n": len(valores), "media": sum(valores) / len(valores)}
        for sensor, valores in grupos.items()
    }


def configurar(ruta=ROOT / "config" / "pipeline.ini"):
    config = ConfigParser()
    if not config.read(ruta, encoding="utf-8"):
        raise FileNotFoundError(ruta)
    return config


def main():
    config = configurar()
    titulo = config.get("informe", "nombre_informe")
    umbral = config.getfloat("alertas", "umbral_alerta")
    top_n = config.getint("informe", "top_n")
    estadisticas = resumir_por_sensor(leer_mediciones())
    print(f"{titulo} | umbral: {umbral:.0f} kWh")
    ranking = sorted(estadisticas.items(), key=lambda par: par[1]["media"], reverse=True)
    for sensor, datos in ranking[:top_n]:
        alerta = " [ALERTA]" if datos["media"] >= umbral else ""
        print(f"- {sensor}: {datos['media']:.1f} kWh ({datos['n']} lecturas){alerta}")


if __name__ == "__main__":
    main()
