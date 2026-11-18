# 🐕‍🦺 Sistema de Navegación Asistida y Guía Auditiva — Robot Unitree Go2

Sistema robótico asistencial desarrollado sobre la plataforma cuadrúpeda **Unitree Go2**, diseñado para asistir en el desplazamiento seguro de **personas no videntes** en entornos interiores mediante mapeo autónomo, detección de obstáculos en tiempo real y control interactivo por comandos de voz.

---

## 📋 Descripción del Proyecto

Este proyecto forma parte de las iniciativas de innovación tecnológica de **UTA-DICI** en el Departamento de Ingeniería en Computación e Informática de la **Universidad de Tarapacá (Arica, Chile)**. 

El sistema aprovecha los sensores integrados del Unitree Go2 (LiDAR 4D, cámaras y ultrasonido) junto con interfaces parlantes para ofrecer:
* **Mapeo de entornos interiores:** Escaneo y registro de zonas navegables para establecer rutas seguras.
* **Detección y evasión de obstáculos:** Monitoreo continuo del camino con alertas tempranas por voz.
* **Control por comandos de voz:** Interacción intuitiva para el usuario (*pausar*, *reanudar*, *reiniciar*, *apagar*) y protocolos exclusivos para el administrador.
* **Restricciones de inactividad:** Temporizadores de seguridad para resguardar la operatividad del robot.

---

## 📂 Estructura del Repositorio

```text
Robot-Unitree-Go2-no-videntes/
├── unitree_sdk2_python-master/   # SDK oficial de Unitree en Python para comunicación con el robot
├── voz_pc.py                     # Módulo principal de reconocimiento y síntesis de comandos por voz
└── README.md                     # Documentación del proyecto
```

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.x:** Lenguaje principal para el desarrollo de la lógica de control y procesamiento de voz.
* **Unitree SDK2 Python:** Librerías oficiales para la comunicación con los actuadores y sensores del cuadrúpedo.
* **CycloneDDS:** Middleware de comunicación en tiempo real para el intercambio de mensajes internos.
* **WebRTC:** Protocolo de baja latencia para la transmisión de datos de sensores y comandos de control.

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/reznov07/Robot-Unitree-Go2-no-videntes.git
cd Robot-Unitree-Go2-no-videntes
```

### 2. Configurar el SDK de Unitree
Ingresa a la carpeta del SDK e instala las dependencias necesarias según la documentación oficial de Unitree:
```bash
cd unitree_sdk2_python-master
pip install -e .
```

### 3. Ejecutar el módulo de control por voz
Asegúrate de estar conectado a la red del robot Unitree Go2 y ejecuta el script de voz desde la raíz del proyecto:
```bash
cd ..
python voz_pc.py
```

---

## 🎙️ Protocolos de Comandos por Voz

### Modo Usuario
* **`"Pausar"`**: Detiene temporalmente el recorrido del robot (tiempo límite de espera: 10 minutos).
* **`"Reanudar"`**: Continúa el desplazamiento hacia el punto de destino.
* **`"Reiniciar"`**: Vuelve al menú inicial de selección de ruta.
* **`"Apagar"`**: Desactiva los módulos operativos del robot de forma segura.

### Modo Administrador
* **`"Administrador"`**: Habilita los protocolos de configuración y prueba.
* **`"Escaneo del lugar"`**: Inicia el mapeo del terreno mediante sensores LiDAR.
* **`"Prueba de rutas"` / `"Prueba de proximidad de objetos"`**: Permite calibrar distancias y sensores antes de operar con el usuario.

---

## 👥 Equipo y Créditos

* **Autor / Desarrollador:** Ivan Callasaya
* **Profesor Asignatura (Proyecto 4):** Diego Aracena
* **Dirección y Supervisión (UTA-DICI):** Ricardo Valdivia Pinto / Miguel Trigo Zapata
* **Institución:** Facultad de Ingeniería — Universidad de Tarapacá, Arica, Chile.
