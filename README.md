# SDQ-CAS (Strengths and Difficulties Questionnaire - Child and Adolescent Self-Report)

El **SDQ-CAS** es una herramienta de evaluación psicológica diseñada para medir varios aspectos del comportamiento y las dificultades emocionales en niños y adolescentes. Este script en Python permite realizar la evaluación basada en 25 ítems, con opciones de respuesta para cada ítem que ayudan a calcular puntajes en diferentes subescalas.

## Descripción del Proyecto

El proyecto proporciona un método automatizado para recopilar respuestas de participantes, calcular puntajes para cuatro subescalas diferentes, y mostrar los resultados. Las subescalas incluidas son:

- **Emotional Scale**
- **Conduct Problem Scale**
- **Hyperactivity Scale**
- **Peer Problem Scale**

Cada subescala está compuesta por un conjunto específico de ítems, y las respuestas se puntúan de manera diferente dependiendo de la subescala.

## Requisitos Previos

Este proyecto requiere Python 3.6 o superior. No es necesario instalar bibliotecas adicionales.

## Cómo Ejecutar el Script

Sigue estos pasos para ejecutar el script:

1. **Clona el repositorio**: 
   ```bash
   git clone https://github.com/AndresQuinto5/SDQ-CAS.git
   cd SDQ-CAS```

2. Ejecuta el script:

```python sdq_calculator.py
```

3. Ingresa la información del participante:
    - Se te pedirá que ingreses el nombre completo y la edad del participante. Si no se conoce la edad, puedes ingresar "NA".

4. Responde los ítems del cuestionario:

El script te guiará para ingresar respuestas para cada uno de los 25 ítems. Las respuestas deben ingresarse como:

1. para "not true"
2. para "somewhat true"
3. para "certainly true"

5. Revisa los resultados:

- Una vez que se hayan ingresado todas las respuestas, el script calculará y mostrará los puntajes para cada subescala.