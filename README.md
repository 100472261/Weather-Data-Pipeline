<h1 align="center"> ⛈️ Weather Data Pipeline </h1>
<p align="justify">
Desarrollo de un pipeline automatizado de datos meteorológicos que extrae información del clima desde la API Weatherstack. Mediante Apache Airflow, los datos se almacenan de forma periódica en una base de datos PostgreSQL, asegurando la actualización continua de la información. Todo el sistema se ejecuta de manera aislada y reproducible dentro de un contenedor Docker, facilitando su despliegue y mantenimiento.
</p>
<h2> ● Pasos: </h2>
<p>1. En la terminal introducimos el comando <code>docker-compose up</code>.</p>
<p>2. Acceder a <code>http://localhost:8000/dags/weather-api-orchestrator/runs</code>. </p>
<p>3. Introducir el usuario <code>admin</code> y la contraseña generada por Airflow.</p>
<p align="left">
  <img src="./images/airflow.JPG" alt="6" width="1000"/>
</p>
<p>4. Ponemos en funcionamiento nuestro Pipeline. Este se ejecutará de forma automática cada minuto.</p>
<p align="left">
  <img src="./images/ejecuciones_airflow.JPG" alt="6" width="1000"/>
</p>
<p>5. Abrimos una nueva terminal e introducimos el comando <code>docker-compose exec db psql -U db_user -d db</code>.
<p>6. Entramos a la base de datos mediante el comando <code>\c db</code>.</p>
<p>7. Mediante el comando <code>\dt dev.*</code> se listan todas las tablas que se encuentran dentro del esquema <code>dev</code>.
<p align="left">
  <img src="./images/1.JPG" alt="6" width="300"/>
</p>
<p>- La tabla <code>raw_weather_data</code> contiene la información proveniente directamente de la API.</p>
<p align="left">
  <img src="./images/2.JPG" alt="6" width="750"/>
</p>
<p>- Mediante <code>dbt</code> se crea la tabla <code>stg_weather_data</code>. A diferencia de la tabla anterior, esta no contiene instancias con el mismo <code>time</code>.</p>
<p align="left">
  <img src="./images/3.JPG" alt="6" width="750"/>
</p>
<p>- Mediante <code>dbt</code> se crea la tabla <code>weather_report</code>. Esta contiene los atributos más relevantes para la información del tiempo.</p>
<p align="left">
  <img src="./images/4.JPG" alt="6" width="500"/>
</p>
<p>- Mediante <code>dbt</code> se crea la tabla <code>daily_average</code>. Esta recopila la información media diaria de los atributos <code>temperature</code> y <code>wind_speed</code>.</p>
<p align="left">
  <img src="./images/5.JPG" alt="6" width="400"/>
</p>
