# ==============================================================================
# PIPELINE ETL AUTOMATIZADO - REPORTE DE VENTAS FERRETERÍA
# ==============================================================================

import pandas as pd
from sqlalchemy import create_engine

print(" [INICIO] Arrancando el proceso de generación de reportes...")

# ------------------------------------------------------------------------------
# 1. CONEXIÓN AL MOTOR DE BASE DE DATA
# ------------------------------------------------------------------------------
engine = create_engine('sqlite:///ventas_ferreteria.db')


# ------------------------------------------------------------------------------
# 2. FASE DE CONSULTAS SQL ANALÍTICAS (Métricas clave de negocio)
# ------------------------------------------------------------------------------

# Consulta 1: Rendimiento por Provincia
query_provincia = """
    SELECT 
        provincia, 
        COUNT(id_venta) AS cantidad_ventas,
        SUM(monto_total) AS facturacion_total,
        ROUND(AVG(monto_total), 2) AS ticket_promedio
    FROM tb_ventas
    GROUP BY provincia
    ORDER BY facturacion_total DESC;
"""

# Consulta 2: Ranking de Productos
query_productos = """
    SELECT 
        producto,
        SUM(cantidad) AS unidades_vendidas,
        SUM(monto_total) AS facturacion_producto
    FROM tb_ventas
    GROUP BY producto
    ORDER BY facturacion_producto DESC;
"""

# Consulta 3: Análisis por Método de Pago
query_pagos = """
    SELECT 
        metodo_pago,
        COUNT(id_venta) AS cantidad_transacciones,
        SUM(monto_total) AS total_recaudado
    FROM tb_ventas
    GROUP BY metodo_pago
    ORDER BY total_recaudado DESC;
"""

# Consulta 4: Ticket Promedio por Cliente
query_clientes = """
    SELECT 
        cliente,
        COUNT(id_venta) AS total_compras,
        SUM(monto_total) AS facturacion_total,
        ROUND(AVG(monto_total), 2) AS ticket_promedio
    FROM tb_ventas
    GROUP BY cliente
    ORDER BY ticket_promedio DESC;
"""

# Consulta 5: Evolución Temporal Mensual
query_evolucion = """
    SELECT 
        strftime('%Y-%m', fecha_venta) AS mes_venta,
        COUNT(id_venta) AS cantidad_ventas,
        SUM(monto_total) AS facturacion_mensual,
        ROUND(AVG(monto_total), 2) AS ticket_promedio_mensual
    FROM tb_ventas
    GROUP BY mes_venta
    ORDER BY mes_venta ASC;
"""


# ------------------------------------------------------------------------------
# 3. FASE DE EXTRACCIÓN Y CARGA A DATAFRAMES
# ------------------------------------------------------------------------------
print("⚙️ Procesando consultas SQL en la base de datos...")
df_provincia = pd.read_sql(query_provincia, con=engine)
df_productos = pd.read_sql(query_productos, con=engine)
df_pagos = pd.read_sql(query_pagos, con=engine)
df_clientes = pd.read_sql(query_clientes, con=engine)
df_evolucion = pd.read_sql(query_evolucion, con=engine)


# ------------------------------------------------------------------------------
# 4. FASE DE SALIDA / REPORTE MULTIPESTAÑA A EXCEL
# ------------------------------------------------------------------------------
nombre_archivo = "reporte_ventas_ferreteria.xlsx"

print(f" Guardando resultados en el archivo Excel multipestaña: {nombre_archivo}...")

with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
    df_provincia.to_excel(writer, sheet_name='Ventas por Provincia', index=False)
    df_productos.to_excel(writer, sheet_name='Ranking Productos', index=False)
    df_pagos.to_excel(writer, sheet_name='Metodos de Pago', index=False)
    df_clientes.to_excel(writer, sheet_name='Ticket por Cliente', index=False)
    df_evolucion.to_excel(writer, sheet_name='Evolucion Mensual', index=False)

print("✅  ¡Pipeline ejecutado con éxito! Archivo Excel listo para Looker Studio.")