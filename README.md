# 🛠️ Pipeline ETL End-to-End & Business Intelligence: Distribuidora "El Tornillo"

> Proyecto integral de ingeniería de datos y analítica comercial diseñado para procesar, validar, transformar y visualizar información transaccional caótica de una ferretería mayorista, transformándola en un dashboard ejecutivo de alta disponibilidad.

---

## 📌 Contexto del Negocio
Las PyMEs y distribuidoras operan frecuentemente con registros transaccionales descentralizados, incompletos y con errores de formato. Este proyecto simula un caso de negocio real para **"Distribuidora El Tornillo"**, estructurando un flujo de datos profesional que garantiza la confiabilidad de la información antes de su explotación comercial en una plataforma de Business Intelligence.

---

## 🏗️ Arquitectura de la Solución (Data Pipeline Flow)

El pipeline opera bajo un esquema estructurado en capas bien definidas:


[ 📥 Archivo Crudo (CSV) ] 
       │
       ▼
[ 🛡️ Data Quality Validation ]  ──(Filtra nulos, rangos y tipos incorrectos)
       │
       ▼
[ 🔄 Pipeline ETL (Python / Pandas / SQLAlchemy) ]
       │
       ▼
[ 🗄️ Base de Datos Relacional (SQLite) ]
       │
       ▼
[ 📊 Capa de Visualización (Looker Studio - Multi-pestaña) ]

Etapas de Desarrollo Técnico
1. Ingesta y Validación de Calidad de Datos (Data Quality)
Antes de persistir cualquier registro, se implementó una capa de validación en Python inspirada en prácticas de ingeniería de datos robustas (similares a los pilares expuestos por The Seattle Data Guy):

Null Tests: Verificación de campos críticos obligatorios (id_venta, cliente, producto, monto).

Range Checks: Detección y filtrado de montos negativos, precios absurdos o unidades atípicas.

Category Checks: Normalización de valores categóricos cerrados (provincias válidas, métodos de pago estandarizados).

Data Type Enforcement: Aseguramiento de conversiones estrictas en fechas y tipos numéricos para evitar corrupciones de tipos al leer archivos planos.

2. Transformación y Modelado (ETL con Python & SQLAlchemy)
Limpieza y saneamiento de cadenas de texto y formatos de fecha.

Generación de agregaciones analíticas intermedias divididas en datasets específicos:

Ventas por Provincia (análisis geográfico).

Ranking de Productos (identificación de artículos estrella).

Recaudación por Método de Pago (perspectiva de flujo de caja).

Evolución Temporal & KPIs Mensuales (facturación, transacciones y ticket promedio).

Persistencia automatizada en una base de datos relacional local SQLite y exportación estructurada hacia un reporte multipestaña en Excel.

3. Business Intelligence & Analítica Visual (Looker Studio)
Conexión directa de las fuentes estructuradas hacia un dashboard ejecutivo interactivo que incluye:

Fila Superior de KPIs: Facturación Total, Volumen de Transacciones y Ticket Promedio global.

Serie Temporal: Evolución cronológica de la facturación mes a mes.

Análisis Geográfico: Distribución de ingresos por provincia.

Mix de Productos: Gráfico de torta interactivo con el top de artículos más vendidos.

Flujo Financiero: Desglose de recaudación según el método de pago (Efectivo, Cuenta Corriente, Transferencia, Tarjeta).

Top Clientes (VIP): Tabla analítica estructurada de mayor a menor facturación que detalla cuentas clave, cantidad de compras y ticket individual.

💻 Stack Tecnológico
Lenguaje: Python 3.x

Manipulación y Análisis: Pandas, Openpyxl

Capa de Datos y ORM: SQLAlchemy, SQLite

Visualización & BI: Looker Studio

Control de Versiones: Git & GitHub

📊 Vista Previa del Dashboard
<img width="1920" height="3046" alt="screencapture-datastudio-google-u-0-reporting-5a9fb1f9-7d97-4a8c-838d-43ab906c8edf-page-r7SBG-2026-10-16-15_19_51" src="https://github.com/user-attachments/assets/194c119b-8986-407f-b322-4f3355cabf8c" />


👤 Autor
Facundo Román

Systems Analysis & Data / Backend Developer


