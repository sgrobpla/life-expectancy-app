from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# --- INICIO DE LA SECCIÓN MODIFICADA ---

# 3. Cargar y procesar los datos de la ONU
def load_data():
    """
    Carga, limpia y procesa los datos de esperanza de vida desde el archivo CSV.
    """
    try:
        # Leemos el archivo CSV que descargaste
        df = pd.read_csv('data/un_life_expectancy.csv')
        
        # Renombramos las columnas originales a nombres más simples y en minúsculas
        column_mapping = {
            'Country or Area': 'country',
            'Year(s)': 'year',
            'Variant': 'variant',
            'Value': 'life_expectancy'
        }
        df.rename(columns=column_mapping, inplace=True)
        
        # Filtramos para quedarnos solo con la variante de datos que nos interesa.
        # ¡¡¡IMPORTANTE!!! Debes reemplazar 'Estimates' con el valor que encontraste
        # en tu archivo CSV en el Paso 2.
        variant_to_keep = 'Estimates' 
        df = df[df['variant'] == variant_to_keep].copy()
        
        # Convertimos las columnas a tipos de datos numéricos para poder hacer cálculos.
        # 'coerce' convertirá cualquier valor no numérico en 'NaN' (Not a Number)
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df['life_expectancy'] = pd.to_numeric(df['life_expectancy'], errors='coerce')
        
        # Eliminamos cualquier fila que tenga valores nulos en columnas clave
        df.dropna(subset=['year', 'life_expectancy', 'country'], inplace=True)
        
        # Convertimos el año a un número entero (ej. 2021.0 -> 2021)
        df['year'] = df['year'].astype(int)
        
        print(f"Datos cargados y procesados exitosamente. {len(df)} registros válidos para la variante '{variant_to_keep}'.")
        return df

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data/un_life_expectancy.csv'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos: {e}")
        return None

# Cargamos los datos una sola vez cuando la aplicación se inicia
life_expectancy_df = load_data()

# --- FIN DE LA SECCIÓN MODIFICADA ---


# 4. Definir la ruta principal de la aplicación
@app.route('/')
def index():
    # Por ahora, solo mostramos la página principal
    return render_template('index.html')

# 5. Asegurarse de que el servidor se ejecute solo cuando se llama al script
if __name__ == '__main__':
    app.run(debug=True)