# Analizador de Logs SSH (Proyecto ESOC)

## Descripción

Este proyecto consiste en un script en Python orientado al análisis básico de logs de autenticación SSH (`auth.log`), simulando tareas realizadas por un Analista ESOC / SOC Tier 1. El objetivo es identificar intentos fallidos de autenticación, detectar posibles ataques de fuerza bruta, reconocer IPs atacantes y generar un reporte automático con los hallazgos.

El proyecto está enfocado en el análisis inicial de eventos de seguridad y en la generación de información útil para la toma de decisiones operativas.

---

## Objetivos del proyecto

* Analizar logs SSH reales en formato `auth.log`.
* Contar intentos fallidos de inicio de sesión.
* Identificar direcciones IP con actividad sospechosa.
* Detectar posibles ataques de fuerza bruta.
* Identificar intentos de acceso con usuarios inválidos.
* Generar un reporte automático consolidado.

---

## Tecnologías utilizadas

* Python 3
* Logs de autenticación SSH (Linux `auth.log`)

---

## Estructura del proyecto

```
analizador-ssh/
│── auth.log
│── analizador.py
│── reporte_ssh.txt
│── README.md
```

---

## Funcionamiento

El script realiza las siguientes acciones:

1. Lee el archivo `auth.log` línea por línea.
2. Identifica eventos de tipo `Failed password`.
3. Cuenta el total de intentos fallidos.
4. Extrae y contabiliza las direcciones IP origen de los intentos fallidos.
5. Determina la IP con mayor número de intentos (posible fuerza bruta).
6. Detecta usuarios inválidos utilizados en intentos de acceso.
7. Genera un archivo `reporte_ssh.txt` con el resumen del análisis.

---

## Ejecución

Requisitos:

* Python 3 instalado

Ejecutar el script desde la carpeta del proyecto:

```bash
python analizador.py
```

Al finalizar, se mostrará la información por consola y se generará automáticamente el archivo `reporte_ssh.txt`.

---

## Ejemplo de salida

```
Intentos fallidos de login: 12

IPs atacantes y cantidad de intentos:
185.244.25.22: 4 intentos
103.152.18.2: 2 intentos
...

Posible ataque de fuerza bruta:
La IP más agresiva es 185.244.25.22 con 4 intentos.

Usuarios inválidos detectados:
admin: 2 veces
oracle: 1 vez
backup: 1 vez
...
```

---

## Aplicación en un entorno ESOC

Este proyecto simula actividades reales de un Analista ESOC, tales como:

* Monitoreo de eventos de autenticación.
* Identificación temprana de amenazas.
* Análisis de patrones de ataque.
* Generación de reportes operativos.

---

## Autor

Jasnier Andrés Pérez Usuga
Ingeniero de Sistemas

---

## Nota

Proyecto desarrollado con fines educativos y de aprendizaje práctico en análisis de seguridad y monitoreo de eventos.
