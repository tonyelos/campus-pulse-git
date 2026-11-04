# CampusPulse — Proyecto base para Git from Zero to Hero

**Estado del proyecto: TALLER GIT**

Proyecto didáctico de la asignatura **Proyecto Big Data I**. Simula un pequeño pipeline que lee mediciones de consumo energético de sensores de distintos edificios de un campus universitario, calcula resúmenes sencillos y aplica un umbral de alerta configurable.

## Estructura

```text
CampusPulse/
├── .github/PULL_REQUEST_TEMPLATE.md
├── .gitignore
├── config/pipeline.ini
├── data/mediciones.csv
├── docs/decisiones.md
├── src/analisis.py
└── tests/test_analisis.py
```

## Ejecutar (solo biblioteca estándar de Python)

Desde la raíz del proyecto:

```bash
python src/analisis.py
python -m unittest discover -s tests -v
```

En Windows, si `python` no está disponible, probad `py`.

## Normas de colaboración

- `main` representa una versión estable. Tras el commit inicial, los cambios se integran por **Pull Request**.
- Crear ramas breves a partir de `main` actualizado: `feature/metricas`, `fix/validacion`, `docs/operacion`, etc.
- Antes de una PR, comprobar que el código funciona y escribir qué se ha probado.
- Otra persona revisa la PR y deja, como mínimo, un comentario sustantivo.
- No introducir contraseñas, tokens, datos personales ni archivos generados.

El objetivo del taller es **entender Git**. La complejidad del programa Python es secundaria.
