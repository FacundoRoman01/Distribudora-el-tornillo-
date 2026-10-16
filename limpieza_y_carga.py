import pandas as pd
from sqlalchemy import create_engine

print("🧹 [INICIO] Iniciando pipeline de validación y limpieza...")

# 1. Cargamos el archivo real de datos sucios
df = pd.read_csv("ventas_distribuidora_caos.csv")

print("Columnas encontradas en el archivo:", df.columns.tolist())

# ==============================================================================
# 2. TRANSFORMACIÓN Y LIMPIEZA DE TIPOS DE DATOS
# ==============================================================================
# Limpiamos 'monto_total' por si trae símbolos o texto y lo convertimos a número
df['monto_total'] = (
    df['monto_total']
    .astype(str)
    .str.replace('$', '', regex=False)
    .str.replace(' ', '', regex=False)
    .str.replace(',', '.', regex=False)
)
df['monto_total'] = pd.to_numeric(df['monto_total'], errors='coerce')


# ==============================================================================
# 3. 🔍 DATA QUALITY CHECKS (Controles de Calidad)
# ==============================================================================
# Buscamos si hay precios menores o iguales a 0, o valores nulos (NaN)
filas_con_error_precio = df[(df['monto_total'] <= 0) | (df['monto_total'].isna())]

if not filas_con_error_precio.empty:
    print("⚠️ ¡ALERTA DE DATA QUALITY! Se detectaron anomalías en los montos:")
    print(filas_con_error_precio)
    raise ValueError("❌ El pipeline se detuvo: El archivo 'ventas_distribuidora_caos.csv' contiene datos corruptos.")
else:
    print("✅ ¡Validación superada con éxito! Todos los montos son correctos.")


# ==============================================================================
# 4. CARGA A LA BASE DE DATOS (Load)
# ==============================================================================
# Si pasa los controles de calidad, guardamos los datos limpios en SQLite
engine = create_engine('sqlite:///ventas_ferreteria.db')
df.to_sql('tb_ventas', con=engine, if_exists='replace', index=False)

print("💾 [FIN] Datos limpios cargados exitosamente en la base de datos SQLite.")