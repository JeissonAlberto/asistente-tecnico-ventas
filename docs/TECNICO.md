# Documentación Técnica: Asistente IA Avidtel (Nivel Experto)

Este sistema es una infraestructura de automatización de red y ventas diseñada para operar como un "Digital Worker" 24/7.

## 1. Arquitectura del Sistema
El software utiliza una arquitectura **Event-Driven** (basada en eventos). Cada mensaje de WhatsApp dispara un flujo de análisis en el orquestador.

- **Backend (Python 3.10+):** Gestiona la lógica de decisión, el estado de la conversación y la integración de IA.
- **Integrations:** Capa de abstracción para comunicarse con SmartOLT (API) y ONTs (Acceso Directo).
- **Frontend (HTML5/Tailwind):** Dashboard de monitoreo en tiempo real.

## 2. Flujo de Decisión (Logic Tree)

### Escenario A: Soporte Técnico
1. **Detección:** El usuario menciona palabras clave (lento, falla, luz roja).
2. **Diagnóstico SmartOLT:**
    - Si `rx_power` < -27 dBm: **Falla Física.** El bot informa al usuario y genera una alerta técnica.
    - Si `phase_state` != 'Working': **Falla de Energía.** El bot pide revisar la conexión eléctrica.
    - Si todo es OK: **Reinicio Lógico.** El bot envía un comando de reboot vía API y monitorea reconexión.

### Escenario B: Gestión de WiFi (TR-069 / Directo)
1. El usuario solicita cambio de clave.
2. El bot solicita **ID de Abonado** o Nombre.
3. El bot accede a la ONT usando las credenciales administrativas (`admin` / `Js92112751000*`).
4. Navega automáticamente a la sección WLAN y aplica los cambios.

### Escenario C: Ventas (Upselling)
1. Si el usuario pregunta por planes o tras una resolución exitosa de soporte.
2. La IA consulta el `plan_name` actual.
3. Ofrece el siguiente plan superior basado en un script de conversión optimizado.

## 3. Configuración de Variables de Entorno (.env)
Para que el sistema funcione en producción, debes configurar:
```bash
SMARTOLT_API_KEY=tu_api_key
ONT_ADMIN_USER=admin
ONT_ADMIN_PASS=Js92112751000*
DB_PATH=data/clients.json
WHATSAPP_API_TOKEN=tu_token_de_whatsapp
```

## 4. Estructura de Archivos
- `backend/main.py`: Punto de entrada y simulación de IA.
- `backend/orchestrator.py`: El "cerebro" que decide qué hacer según el mensaje.
- `integrations/smartolt.py`: Conector con la plataforma SmartOLT.
- `integrations/ont_direct.py`: Lógica para entrar a las ONTs por IP.
- `integrations/custom_api.py`: Puerto abierto para conectar CRMs o Pasarelas de Pago.
- `frontend/index.html`: Dashboard administrativo.

## 5. Escalabilidad
El sistema está diseñado para que puedas añadir nuevos "módulos de intención". Si mañana quieres que el bot también gestione agendamiento de citas, solo debes añadir la intención en `main.py` y crear el conector en `integrations/`.
