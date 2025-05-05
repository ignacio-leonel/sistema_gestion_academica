# 🎓 Sistema de Gestión Académica

Este es un sistema en desarrollo para gestionar alumnos, carreras y materias en una institución académica. Está construido con Python, utilizando principios de programación estructurada y orientada a objetos, y cuenta con persistencia de datos mediante SQLite.

# 👥 Roles de usuario (en planificación)

El sistema contará con distintos permisos según el tipo de usuario:

- 👨‍💼 **Administrador**: acceso completo a todas las funciones (altas, bajas, modificaciones y reportes).
- 👩‍🏫 **Docente**: podrá ver la lista de alumnos y cargar/modificar notas.
- 👨‍🎓 **Alumno**: acceso restringido solo a su propia información (estado académico, materias, etc.).

---

---

## ✅ Funcionalidades implementadas

- 📋 **Alta de alumno**
- 🔍 **Búsqueda de alumnos por DNI o por carrera**
- 🔄 **Modificación de datos del alumno**
- 🚫 **Baja lógica de alumno (cambio de estado a inactivo)**
- 🧾 **Listar alumnos activos/inactivos**
- 🗃️ **Persistencia en base de datos SQLite**

---

## 🛠️ En desarrollo

- 📚 Gestión de carreras y materias
- 📈 Cálculo del porcentaje de materias cursadas por alumno
- 🖼️ Subida de imagen (foto) del alumno
- 🧪 Validaciones más robustas en formularios
- 🧱 Estructura modular y separación en capas (backend - interfaz)
- 🔐 Validación de usuario para ingreso al sistema

---

## 📂 Estructura del proyecto
sistema_gestion_academica/
│
├── base_datos/
│ └── conexion.py
│
├── funciones/
│ ├── alumnos.py
│ └── validaciones.py
│
├── main.py
└── README.md




---

## ⚙️ Tecnologías utilizadas

- Python 3.x
- SQLite
- Visual Studio Code

---

## 💡 Autor

Ignacio Leonel – [LinkedIn](https://www.linkedin.com/in/ignacio-leonel/)  
Repositorio: [GitHub](https://github.com/ignacio-leonel/sistema_gestion_academica)

---

## ✉️ Contacto

> Si estás buscando a alguien comprometido con el aprendizaje continuo y la mejora constante, ¡no dudes en escribirme!

