from flask import Flask, render_template, request
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
        
        variant_to_keep = 'Medium' 
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
@app.route('/', methods=['GET', 'POST'])
def index():
    countries, min_year, max_year = [], 0, 0
    if life_expectancy_df is not None and not life_expectancy_df.empty:
        countries = sorted(life_expectancy_df['country'].unique())
        min_year = int(life_expectancy_df['year'].min())
        max_year = int(life_expectancy_df['year'].max())

    result = None
    error = None
    selected_data = {}  # Inicia vacío

    if request.method == 'POST':
        try:
            user_country = request.form['country']
            user_age = int(request.form['age'])
            year1 = int(request.form['year1'])
            year2 = int(request.form['year2'])

            # Guardamos todos los datos del formulario para la persistencia
            selected_data = {
                'country': user_country,
                'age': user_age,
                'year1': year1,
                'year2': year2
            }

            le_year1_series = life_expectancy_df[(life_expectancy_df['country'] == user_country) & (life_expectancy_df['year'] == year1)]['life_expectancy']
            le_year2_series = life_expectancy_df[(life_expectancy_df['country'] == user_country) & (life_expectancy_df['year'] == year2)]['life_expectancy']

            if le_year1_series.empty or le_year2_series.empty:
                error = f"No se encontraron datos de esperanza de vida para {user_country} en los años {year1} y/o {year2}."
            else:
                le_year1 = le_year1_series.iloc[0]
                le_year2 = le_year2_series.iloc[0]

                if le_year1 > 0:
                    equivalent_age = (user_age / le_year1) * le_year2
                    result = {
                        'user_age': user_age,
                        'user_country': user_country,
                        'year1': year1,
                        'le_year1': round(le_year1, 1),
                        'year2': year2,
                        'le_year2': round(le_year2, 1),
                        'equivalent_age': round(equivalent_age, 1)
                    }
                else:
                    error = f"La esperanza de vida en {year1} para {user_country} es cero, no se puede realizar el cálculo."

        except (ValueError, KeyError):
            error = "Por favor, completa todos los campos del formulario correctamente."
        except Exception as e:
            error = f"Ocurrió un error inesperado: {e}"

    return render_template('index.html', 
                           countries=countries, 
                           min_year=min_year, 
                           max_year=max_year, 
                           result=result,
                           error=error,
                           selected_data=selected_data)
# 5. Asegurarse de que el servidor se ejecute solo cuando se llama al script
if __name__ == '__main__':
    app.run(debug=True)