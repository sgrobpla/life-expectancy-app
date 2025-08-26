# Calculadora de Edad Equivalente / Equivalent Age Calculator

[English Version](#equivalent-age-calculator)

---

<h1 id="versión-en-español">Calculadora de Edad Equivalente</h1>

Esta es una aplicación web construida con Python y Flask que permite calcular la "edad equivalente" de una persona. El concepto se basa en comparar la proporción de la esperanza de vida que una persona ha vivido en una época determinada, con la edad que correspondería a esa misma proporción en otra época con una esperanza de vida diferente.

### ¿Cómo se usa?

La aplicación es muy intuitiva. Simplemente completa los siguientes campos:

1.  **País:** Escribe para buscar y seleccionar tu país en la lista.
2.  **Tu edad actual:** La edad que quieres usar como referencia.
3.  **Año de referencia:** El año específico en el que tenías (o tendrías) la edad del punto anterior.
4.  **Año de comparación:** El año con el que quieres comparar tu edad de referencia.

Haz clic en "Calcular Edad Equivalente" y la aplicación te mostrará el resultado.

### La Fórmula del Cálculo

La lógica central de la aplicación no es predecir el futuro, sino ofrecer una perspectiva sobre cómo ha cambiado la longevidad. Se calcula la proporción de vida vivida en el año de referencia y se aplica esa misma proporción a la esperanza de vida del año de comparación.

La fórmula utilizada es:

> **Edad Equivalente = (Tu Edad / Esperanza de Vida en Año 1) * Esperanza de Vida en Año 2**

**Ejemplo:**
- Si una persona tenía **30 años** en 1980, en un país donde la esperanza de vida era de **65 años**.
- Ha vivido un **46%** de su vida esperada (30 / 65).
- Si en 2020 la esperanza de vida en ese mismo país subió a **80 años**.
- La edad equivalente sería el 46% de 80, es decir, aproximadamente **37 años**.

### Fuente de Datos

Los datos de esperanza de vida utilizados en esta aplicación han sido obtenidos de la base de datos pública de las Naciones Unidas ([data.UN.org](http://data.UN.org/)). Específicamente, se utiliza el archivo que contiene las columnas `"Country or Area"`, `"Year(s)"`, `"Variant"` y `"Value"`. Para asegurar la consistencia, todos los cálculos se basan en la variante de datos **"Medium"**.

### Proceso de Desarrollo y Agradecimientos

Esta aplicación fue creada a través de un proceso de **vibecoding**: una sesión de desarrollo colaborativa, conversacional y guiada **con la ayuda de Gemini 2.5 de Google**. El objetivo fue seguir las mejores prácticas desde el principio, incluyendo el uso de entornos virtuales, control de versiones con Git/GitHub y un enfoque iterativo para resolver problemas y mejorar la experiencia de usuario.

### Próximas Características

Actualmente estoy trabajando en la implementación de traducciones para la interfaz de la aplicación. El objetivo es que esté disponible en múltiples idiomas, un proceso que se está acelerando mediante el uso de IA para la localización.

---

<h1 id="equivalent-age-calculator">Equivalent Age Calculator</h1>

This is a web application built with Python and Flask that allows you to calculate a person's "equivalent age." The concept is based on comparing the proportion of life expectancy a person has lived through in a given era, with the age that would correspond to that same proportion in another era with a different life expectancy.

### How to Use

The application is very intuitive. Simply fill out the following fields:

1.  **Country:** Start typing to search and select your country from the list.
2.  **Your current age:** The age you want to use as a reference.
3.  **Reference year:** The specific year in which you were (or would be) the age from the previous point.
4.  **Comparison year:** The year you want to compare your reference age against.

Click on "Calculate Equivalent Age" and the application will display the result.

### The Calculation Formula

The core logic of the app is not to predict the future, but to offer a perspective on how longevity has changed. It calculates the proportion of expected life lived in the reference year and applies that same proportion to the life expectancy of the comparison year.

The formula used is:

> **Equivalent Age = (Your Age / Life Expectancy in Year 1) * Life Expectancy in Year 2**

**Example:**
- If a person was **30 years old** in 1980, in a country where the life expectancy was **65 years**.
- They have lived **46%** of their expected life (30 / 65).
- If by 2020, the life expectancy in that same country increased to **80 years**.
- The equivalent age would be 46% of 80, which is approximately **37 years old**.

### Data Source

The life expectancy data used in this application was obtained from the United Nations' public database ([data.UN.org](http://data.UN.org/)). Specifically, it uses the dataset containing the columns `"Country or Area"`, `"Year(s)"`, `"Variant"`, and `"Value"`. To ensure consistency, all calculations are based on the **"Medium"** data variant.

### Development Process & Acknowledgements

This application was created through a process of **vibecoding**: a collaborative, conversational, and guided development session **with the help of Gemini 2.5 from Google**. The goal was to follow best practices from the outset, including the use of virtual environments, version control with Git/GitHub, and an iterative approach to problem-solving and improving the user experience.

### Future Features

I am currently working on implementing translations for the application's interface. The goal is to make it available in multiple languages, a process being accelerated by using AI for localization.