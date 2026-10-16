# 🛠️ Proyecto de Análisis de Datos y BI: Ventas de Ferretería

Pipeline completo de datos de punta a punta (End-to-End): desde la limpieza de datos y modelado relacional en SQLite hasta consultas SQL analíticas y visualización de métricas en Looker Studio.

---

## 📋 Descripción del Proyecto
Este proyecto simula el análisis integral de las operaciones de una ferretería. El objetivo principal fue tomar datos transaccionales crudos, realizar un proceso de auditoría y limpieza (ETL), estructurarlos en una base de datos relacional y extraer conocimiento de negocio mediante consultas SQL estructuradas para alimentar un dashboard interactivo.
Arquitectura del Pipeline con Controles de Calidad (Data Quality): Implementación de validaciones previas para detección de nulos en columnas críticas, control de rangos en montos totales y saneamiento de tipos de datos antes de la persistencia en SQLite, evitando la propagación de anomalías hacia la capa de BI (Looker Studio).

---

## ⚙️ Stack Tecnológico
* **Lenguaje:** Python (Pandas, SQLAlchemy)
* **Base de Datos:** SQLite
* **Entorno de Desarrollo:** Jupyter Notebooks (`.ipynb`)
* **Visualización / BI:** Looker Studio (vía exportación de CSVs procesados)
* **Control de Versiones:** Git y GitHub

---

## 🔄 Fases del Proyecto

### 1. Limpieza y Auditoría de Datos (ETL)
* Carga y exploración inicial del dataset mediante Jupyter Notebook.
* Detección y tratamiento de valores nulos e inconsistencias (por ejemplo, normalización de provincias y corrección de registros clave como el `id_venta = 'V1027'`).
* Estandarización de formatos de fecha y tipos de datos numéricos (`monto_total`, `precio_unitario`).

### 2. Modelado y Almacenamiento
* Inserción de los datos limpios en una base de datos relacional local (`ventas_ferreteria.db`) bajo la tabla estructurada `tb_ventas`.

### 3. Análisis de Negocio (Consultas SQL)
Se desarrollaron consultas SQL puras para responder a las preguntas clave del negocio:
* **Facturación y Ticket Promedio por Provincia:** Identificación de zonas geográficas con mayor volumen de transacciones y rentabilidad (liderado por Buenos Aires).
* **Análisis de Métodos de Pago:** Auditoría de canales de cobro (Transferencia, Efectivo, Cuenta corriente).
* **Ranking de Productos:** Detección de los artículos de mayor impacto en la facturación total.
* **Ticket Promedio por Cliente:** Segmentación de clientes (VIP / recurrentes vs. minoristas).
* **Evolución Temporal:** Análisis de estacionalidad y comportamiento de ventas mes a mes.

---

## 📊 Principales Insights de Negocio
1. **Concentración Geográfica y de Clientes:** Buenos Aires concentra el mayor volumen operativo, con clientes clave como *Juan Pérez* traccionando los tickets promedio más altos de la cartera.
2. **Métodos de Pago Equilibrados:** Las transferencias y el efectivo mantienen una paridad muy alta en el flujo transaccional diario.
3. **Estacionalidad:** Se identificó una ventana de alta concentración de ventas durante mayo de 2026, lo que permite planificar campañas de reposición de stock y marketing estacional con precisión.

---

## 🚀 Visualización (Business Intelligence)
Los resultados obtenidos de las consultas SQL fueron exportados e integrados en un **Dashboard interactivo en Looker Studio** para facilitar la toma de decisiones ejecutivas en tiempo real.

---
*Desarrollado como parte del portfolio profesional de Análisis de Datos y Sistemas.*