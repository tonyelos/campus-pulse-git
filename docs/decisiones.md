# Decisiones del equipo

## 1. Conflicto de `umbral_alerta`: 70 frente a 90

- **Rama `feature/umbral-70`**: proponía bajar el umbral de 80 a **70** kWh.
- **Rama `feature/umbral-90`**: proponía subirlo a **90** kWh.
- Ambas parten del mismo commit de `main`, así que Git detecta un conflicto de contenido en `config/pipeline.ini`.

**Decisión:** se descartaron ambos valores y se acordó un valor intermedio, **75 kWh**, eliminando los marcadores `<<<<<<<`, `=======` y `>>>>>>>` y dejando una sola línea.

**Por qué 75:** mantiene la sensibilidad del 70 sin llegar a generar el volumen de alertas que produciría el 90; es un punto de partida revisable cuando haya más histórico de mediciones.

## 2. Verificación tras resolver

```bash
python3 src/analisis.py
# Informe CampusPulse | umbral: 75 kWh

python3 -m unittest discover -s tests -v
# Ran 1 test ... OK

git status
# nothing to commit, working tree clean
```

## 3. Trazabilidad

- El merge se cerró con el commit `merge: resolver umbral acordado en 75`, que documenta la decisión en el historial.
- La publicación y revisión de la documentación se hizo mediante una *Pull Request* a `main`.
- Guía completa del proceso: [`docs/GUIA_TALLER_GIT.docx`](GUIA_TALLER_GIT.docx).
