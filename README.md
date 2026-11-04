# CampusPulse — Taller «Git from Zero to Hero»

**Proyecto Big Data I · Universidad Europea de Valencia**
**Estado del proyecto: TALLER GIT COMPLETADO**

Repositorio con el taller guiado de Git resuelto de principio a fin: repositorio local, *staging*, commits, ramas, fusiones, conflicto controlado y publicación en GitHub mediante *Pull Request*.

- **Repositorio:** <https://github.com/tonyelos/campus-pulse-git>
- **Guía completa con capturas:** [`docs/GUIA_TALLER_GIT.docx`](docs/GUIA_TALLER_GIT.docx)
- **Capturas del proceso:** [`docs/capturas/`](docs/capturas/)
- **Decisiones del equipo:** [`docs/decisiones.md`](docs/decisiones.md)

---

## 1. Qué es CampusPulse

Proyecto didáctico que simula un pequeño pipeline de datos: lee mediciones de consumo energético de sensores de un campus, calcula la media por sensor y marca alertas cuando se supera un umbral configurable.

El objetivo del taller **no es el programa Python**, sino entender el modelo mental de Git:

```text
Working directory --add--> Staging --commit--> Repositorio local --push--> GitHub
```

## 2. Estructura del repositorio

```text
campus-pulse-git/
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── config/
│   └── pipeline.ini          # umbral_alerta = 75 (valor consensuado)
├── data/
│   └── mediciones.csv
├── docs/
│   ├── calidad.md            # política de calidad (rama feature/calidad-datos)
│   ├── resumen.md            # resumen de sensores (rama feature/resumen-sensores)
│   ├── decisiones.md         # decisiones y resolución del conflicto
│   ├── GUIA_TALLER_GIT.docx  # guía paso a paso con capturas
│   └── capturas/             # imágenes de cada fase del taller
├── src/
│   └── analisis.py
├── tests/
│   └── test_analisis.py
└── README.md
```

## 3. Requisitos y ejecución

Solo se necesita **Python 3.10+** (biblioteca estándar) y Git.

```bash
git clone https://github.com/tonyelos/campus-pulse-git.git
cd campus-pulse-git

python3 src/analisis.py
python3 -m unittest discover -s tests -v
```

Salida esperada del informe (umbral acordado en **75 kWh**):

```text
Informe CampusPulse | umbral: 75 kWh
- S03: 92.0 kWh (2 lecturas) [ALERTA]
- S02: 75.0 kWh (2 lecturas) [ALERTA]
- S01: 62.0 kWh (2 lecturas)
```

Pruebas:

```text
test_media_y_recuento (test_analisis.TestAnalisis.test_media_y_recuento) ... ok
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

> En macOS el intérprete suele llamarse `python3`; en Windows puede ser `py`.

## 4. Flujo de Git seguido en el taller

| Fase | Qué se hizo | Ramas implicadas |
|---|---|---|
| 1 | `git init -b main`, `add`, primer commit | `main` |
| 2 | `status` / `diff` / `diff --staged`, commit selectivo | `main` |
| 3 | Rama, documento nuevo y comprobación de que aparece/desaparece al cambiar de rama | `feature/calidad-datos` |
| 4 | Segunda rama independiente y grafo de historias | `feature/resumen-sensores` |
| 5 | Fusión sin conflicto con `--no-ff` | ambas → `main` |
| 6 | Conflicto provocado (70 vs 90) y resuelto en **75** | `feature/umbral-70`, `feature/umbral-90` |
| 7 | Publicación en GitHub y *Pull Request* | `feature/documentacion` → `main` |

### Grafo final del historial

```text
*   236ed7c (main) merge: resolver umbral acordado en 75
|\
| * e4d361e (feature/umbral-90) feat: proponer umbral 90
* |   f77728d merge: probar umbral 70
|\ \
| |/
|/|
| * 2beb21f (feature/umbral-70) feat: proponer umbral 70
|/
*   4c4837e merge: integrar resumen de sensores
|\
| * 0e234cb (feature/resumen-sensores) docs: explicar resumen de sensores
* |   581a11f merge: integrar calidad
|\ \
| |/
|/|
| * 6ba5cf6 (feature/calidad-datos) docs: proponer reglas de calidad
|/
* 99e84c8 docs: marcar estado del taller
* 6777c1f chore: iniciar CampusPulse
```

## 5. El conflicto, explicado

`feature/umbral-70` y `feature/umbral-90` modificaron **la misma línea** de `config/pipeline.ini` partiendo del mismo commit. Git no puede elegir por nosotros:

```ini
<<<<<<< HEAD
umbral_alerta = 70
=======
umbral_alerta = 90
>>>>>>> feature/umbral-90
```

Se eliminaron los marcadores y se acordó un **valor nuevo, 75**, que no es ninguna de las dos propuestas. Después se comprobó que el informe y las pruebas seguían funcionando y se cerró el merge con un commit propio. El detalle está en [`docs/decisiones.md`](docs/decisiones.md).

## 6. Documentación del proceso

La guía `docs/GUIA_TALLER_GIT.docx` recoge, fase por fase:

- el comando ejecutado y su salida real,
- una captura del terminal en cada paso,
- la explicación de qué ocurre en el *working tree*, el *staging* y el repositorio,
- el resultado comprobable de cada fase.

## 7. Normas de colaboración

- `main` es la versión estable; los cambios entran por *Pull Request*.
- Ramas cortas y con nombre descriptivo: `feature/...`, `fix/...`, `docs/...`.
- Antes de abrir una PR: `python3 src/analisis.py` y pruebas en verde.
- No subir `.env`, claves, datos personales ni archivos generados.

## 8. Autoría

- **Alumno:** tonyelos (<https://github.com/tonyelos>)
- **Asignatura:** Proyecto Big Data I — M31-9798 M3R-9798
- **Material de partida:** `CampusPulse_TALLER` y «Hoja de taller guiado» del aula virtual (UEV).
