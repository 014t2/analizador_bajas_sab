# Churn Prediction

Este proyecto es una **aplicación práctica de IA y Data Science**, cuyo objetivo es anticiparse a problemas de clientes y detectar oportunidades de crecimiento.

La idea es aprovechar los datos que ya tenemos de los clientes (uso, tickets, actividad, funcionalidades, medios de pago, etc.) para identificar patrones que indiquen riesgo de abandono (churn) o clientes preparados para nuevas funcionalidades o productos. El enfoque no automatiza decisiones críticas, sino que **proporciona información clara y accionable** para que el equipo comercial y de producto pueda actuar a tiempo.

---

## Contenido del proyecto

- `data/` : Carpeta con datasets ficticios o de ejemplo.
- `notebooks/`
  - `01_EDA.ipynb` : Análisis exploratorio de datos.
  - `02_churn_analysis_smote.ipynb` : Preprocesamiento, escalado y preparación de datos. Modelos de predicción (Logistic Regression, Random Forest, XGBoost) y evaluación.
- `models/` : Carpeta para almacenar modelos entrenados.
- `src/`
  - `main.py` : Lógica de FastAPI y Endpoints
  - `schema.py` : Definición de esquemas de datos (Pydantic)
- `README.md` : Este documento.

---

## Requisitos e instalación

Se recomienda crear un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Dependencias principales utilizadas:

- `numpy`
- `pandas`
- `scikit-learn`
- `imbalanced-learn` (para SMOTE)
- `xgboost`
- `matplotlib` / `seaborn` (visualización)
- `fastapi` (para despliegue de API)

---

## Uso

1. Cargar y explorar los datos en `01_EDA.ipynb`.
2. Preprocesar los datos con `02_churn_analysis_smote.ipynb` (escalado, codificación, balanceo con SMOTE). Entrenar y evaluar modelos en `03_model_churn.ipynb`.
3. Guardar el modelo final en `models/` para futuras predicciones.
4. (Opcional) Integrar el modelo en un servicio API con FastAPI para predicciones en tiempo real.

---

## Objetivo del proyecto

El proyecto tiene como finalidad:

- **Anticiparse al churn**: identificar clientes con riesgo de baja antes de que se manifieste.
- **Generar oportunidades de upselling**: detectar clientes preparados para nuevas funcionalidades o productos.
- **Aplicar conocimientos de IA y Data Science** en un contexto real de negocio.
- Servir como **PoC** para evaluar impacto y viabilidad antes de una integración más amplia.

---

## Contribución

Este proyecto es un ejemplo de cómo convertir teoría de IA y Data Science en valor para el negocio. Se pueden añadir:

- Nuevos modelos de predicción.
- Integración con datos facticios.
- Notificaciones automáticas a comerciales o dashboards internos.

---