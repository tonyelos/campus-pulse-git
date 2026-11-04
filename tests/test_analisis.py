"""Pruebas iniciales; ampliables por el alumnado."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from analisis import resumir_por_sensor  # noqa: E402


class TestAnalisis(unittest.TestCase):
    def test_media_y_recuento(self):
        filas = [
            {"id_sensor": "S01", "consumo_kwh": 10.0},
            {"id_sensor": "S01", "consumo_kwh": 20.0},
            {"id_sensor": "S02", "consumo_kwh": 7.0},
        ]
        resultado = resumir_por_sensor(filas)
        self.assertEqual(resultado["S01"]["n"], 2)
        self.assertEqual(resultado["S01"]["media"], 15.0)
        self.assertEqual(resultado["S02"]["media"], 7.0)


if __name__ == "__main__":
    unittest.main()
