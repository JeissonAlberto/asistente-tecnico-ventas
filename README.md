# 🚀 Avidtel AI Agent: Sistema de Soporte Técnico & Ventas Proactivas

## 📖 ¿Para qué sirve?
Este software es un **Digital Worker** (Trabajador Digital) diseñado específicamente para ISPs. Su función principal es automatizar el ciclo de vida del cliente: desde la resolución de fallas técnicas y cambios de configuración de red, hasta la detección de oportunidades de venta (upselling) basadas en el uso del servicio.

**El objetivo:** Reducir la carga operativa del equipo de soporte en un 80% y aumentar los ingresos por cliente de forma automática.

---

## 🛠️ ¿Qué hace el sistema? (Funcionalidades)

### 1. Soporte Técnico Autónomo
- **Diagnóstico en Tiempo Real:** Se conecta a **SmartOLT** para verificar potencia (dBm), estado de la fibra y uptime de la ONT.
- **Auto-Resolución:** Si detecta una falla lógica, envía comandos de reinicio (Reboot) a través de la API.
- **Identificación de Fallas Físicas:** Detecta niveles críticos de señal y alerta proactivamente sobre posibles daños en el cableado.

### 2. Gestión de Red WiFi (TR-069 & Acceso Directo)
- **Cambio de Clave y SSID:** Permite al usuario final cambiar el nombre y la contraseña de su red WiFi mediante un menú interactivo en WhatsApp.
- **Acceso Administrativo:** Utiliza credenciales maestras para entrar a la ONT y realizar cambios sin intervención humana.

### 3. Motor de Ventas (Upselling)
- **Análisis de Planes:** Identifica el plan actual del abonado.
- **Ofertas Proactivas:** Ofrece mejoras de velocidad en momentos estratégicos (ej. tras solucionar un problema técnico o cuando detecta alto consumo).

### 4. Dashboard Administrativo
- **Monitoreo:** Panel visual para supervisar la actividad de la IA, ventas generadas y alertas de red críticas.

---

## 🏗️ Construcción y Arquitectura
El sistema ha sido construido bajo estándares de ingeniería de alto rendimiento (Top 0.01%):

- **Lenguaje:** Python 3.10+
- **Arquitectura:** Modular y agnóstica (puedes cambiar de proveedor de WhatsApp sin tocar el cerebro del bot).
- **Frontend:** Dashboard responsivo construido con Tailwind CSS.
- **Integraciones:**
    - `SmartOLT API`: Para telemetría de red.
    - `Requests Session`: Para navegación administrativa en ONTs.
    - `Custom API Bridge`: Casilla abierta para conectar cualquier CRM o pasarela de pago.

---

## 🔗 Cómo Integrar (Paso a Paso)

### 1. Requisitos Previos
- Cuenta activa en **SmartOLT** con API habilitada.
- Credenciales administrativas de las ONTs.
- Proveedor de API de WhatsApp (ej. Wati, Twilio, o Meta Direct).

### 2. Configuración de Variables
Crea un archivo `.env` en la raíz del proyecto:
```bash
SMARTOLT_API_KEY=tu_llave_aqui
ONT_ADMIN_USER=admin
ONT_ADMIN_PASS=tu_clave_maestra
WHATSAPP_TOKEN=token_del_proveedor
```

### 3. Despliegue
1. **Clonar:** `git clone https://github.com/JeissonAlberto/avidtel-ai-agent.git`
2. **Instalar Dependencias:** `pip install -r requirements.txt` (Próximamente disponible).
3. **Ejecutar:** `python backend/main.py`

### 4. Conexión con WhatsApp
Apunta el Webhook de tu proveedor de WhatsApp a la dirección IP donde corras este backend. El orquestador se encargará de procesar cada mensaje entrante.

---

## 📂 Estructura del Repositorio
- `/backend`: Lógica de decisión y orquestación de IA.
- `/integrations`: Conectores técnicos (SmartOLT, ONT Direct, Custom API).
- `/frontend`: Dashboard visual del sistema.
- `/docs`: Guías detalladas de flujo de trabajo.

---
**Desarrollado para Avidtel por Zapia AI.**
