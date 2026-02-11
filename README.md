# 🔐 Web API Authentication Threat Model

## 📝 Descripción del Proyecto

Este proyecto implementa un **Modelo de Amenazas (Threat Model)** para una **API web de autenticación**, permitiendo identificar, analizar y documentar vulnerabilidades potenciales en la arquitectura de seguridad.

Utilizamos la librería **PyTM** para crear una representación visual y documentada de los flujos de datos, límites de confianza y controles de seguridad.

---

## 🎯 Objetivos

✅ Identificar y mapear todos los componentes del sistema  
✅ Documentar flujos de datos y puntos de entrada  
✅ Evaluar controles de seguridad existentes  
✅ Detectar vulnerabilidades y amenazas potenciales  
✅ Proporcionar recomendaciones de mitigación

---

## 🏗️ Arquitectura del Sistema

### Límites de Confianza

| Límite          | Descripción                                  |
| --------------- | -------------------------------------------- |
| 🌐 **Internet** | Cliente y Web API (zona pública)             |
| ☁️ **Cloud**    | Base de datos y almacenamiento (zona segura) |
| 🔐 **Token**    | Motor de encriptación (zona aislada)         |

### Componentes

#### 👤 **Actores**

- **Cliente**: Usuario externo que accede a la plataforma

#### ⚙️ **Procesos**

- **Web API**: Punto de entrada, gestiona autenticación y solicitudes
- **Engine_encrypted**: Motor de encriptación de datos

#### 💾 **Almacenes de Datos**

- **Database**: Base de datos SQL en AWS con acceso de escritura

---

## 🔄 Flujos de Datos

```
┌─────────┐     HTTPS      ┌──────────┐
│ Cliente │ ─────────────➜ │ Web API  │
└─────────┘  Autenticado   └────┬─────┘
     ▲                           │
     │        Response           │
     └────────────────────────────┘
                                 │
                          HTTPS  │
                        Encriptado│
                                 ▼
                         ┌─────────────────┐
                         │ Engine Encrypted│
                         └────────┬────────┘
                                  │
                           HTTPS  │
                        Autenticado│
                                  ▼
                         ┌─────────────────┐
                         │    Database     │
                         │  (AWS - SQL)    │
                         └─────────────────┘
```

### Detalles de Flujos

| #   | Flujo                       | Protocolo | Encriptado | Autenticado | Tokens |
| --- | --------------------------- | --------- | ---------- | ----------- | ------ |
| 1️⃣  | Cliente → Web API           | HTTPS     | ✅         | ✅          | ✅     |
| 2️⃣  | Web API → Engine_encrypted  | HTTPS     | ✅         | ⚠️          | -      |
| 3️⃣  | Engine_encrypted → Database | HTTPS     | ✅         | ✅          | -      |
| 4️⃣  | Web API → Cliente           | HTTPS     | ✅         | ✅          | ✅     |

---

## 🛡️ Controles de Seguridad Implementados

| Control                        | Estado     | Descripción                                       |
| ------------------------------ | ---------- | ------------------------------------------------- |
| 🔒 **HTTPS**                   | ✅ Activo  | Encriptación en tránsito en todos los flujos      |
| 🔐 **Encriptación de Datos**   | ✅ Activo  | Datos encriptados en almacenamiento y transmisión |
| 🔑 **Tokens de Sesión**        | ✅ Activo  | Autenticación basada en tokens                    |
| ✔️ **Autenticación de Fuente** | ✅ Parcial | En flujos críticos                                |

---

## 📁 Estructura del Proyecto

```
Threat_Model_Api_Authentication/
├── model.py                 # Definición del modelo de amenazas
├── model-report.md          # Reporte automático generado
├── model-dfd.png            # Diagrama de Flujo de Datos
├── basic_template.md        # Plantilla base
├── requirements.txt         # Dependencias
├── Readme.md                # Este archivo
└── .gitignore              # Archivos ignorados por Git
```

---

## 📋 Requisitos

- **Python** 3.8 o superior
- **pytm** >= 1.0.0
- **Graphviz** (para generar diagramas)
- **PlantUML** (opcional, para diagramas adicionales)

---

## 🚀 Instalación y Uso

### 1️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2️⃣ Ejecutar el Modelo

```bash
python model.py --dfd | dot -Tpng -o model-dfd.png
```

### 3️⃣ Generar Reporte

```bash
python model.py --report basic_template.md > model-report.md
```

### 4️⃣ Resultado

Se generarán automáticamente:

- 📄 `model-report.md` - Reporte de amenazas detallado
- 🖼️ `model-dfd.png` - Diagrama visual del flujo de datos
- 📊 Otros artefactos de documentación

---

## 🛠 Tecnologías Utilizadas

| Tecnología       | Propósito                   |
| ---------------- | --------------------------- |
| 🐍 **Python**    | Lenguaje de programación    |
| 📦 **PyTM**      | Generación de threat models |
| 📊 **Graphviz**  | Visualización de diagramas  |
| ☁️ **AWS**       | Infraestructura en la nube  |
| 🔐 **HTTPS/TLS** | Encriptación en tránsito    |

## 📚 Recursos Adicionales

- 📖 [Documentación de PyTM](https://github.com/izar/pytm)
- 🔒 [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Model)
- 🎯 [Microsoft Threat Modeling Tool](https://microsoft.com/en-us/securityengineering/threatmodeling)
- 📊 [STRIDE Framework](<https://en.wikipedia.org/wiki/STRIDE_(security)>)

---

## 👨‍💻 Información del Proyecto

**Equipo:** HackTheWorld Security  
**Fecha de Creación:** 10 de Febrero de 2026  
**Estado:** 🟢 En Desarrollo  
**Versión:** 1.0.0

---

## 📄 Licencia

Este proyecto es de código abierto y está destinado a fines educativos e investigación de seguridad.

---

**Última actualización:** Febrero 10, 2026
