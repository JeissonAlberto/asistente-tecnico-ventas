# Asistente Técnico y de Ventas (Replica Mejorada IABOT)

Software diseñado para ISPs (Internet Service Providers) enfocado en automatizar el soporte técnico y maximizar las ventas mediante Inteligencia Artificial e integración directa con **SmartOLT**.

## Características Principales
- **Diagnóstico Automático:** Consulta el estado de la fibra, potencia (dBm) y uptime de la ONU en tiempo real.
- **Soporte Resolutivo:** Aplica protocolos de solución (Troubleshooting) antes de escalar a un humano.
- **Venta Proactiva (Upselling):** Analiza el plan actual del cliente y ofrece mejoras basadas en datos.
- **Multicanal:** Preparado para integrarse con la API de WhatsApp Business.
- **Extensible:** Módulo de "Casilla de APIs" para conectar pagos, CRMs y más.

## Estructura del Proyecto
- `backend/`: El núcleo de lógica y orquestación.
- `integrations/`: Conectores con servicios externos (SmartOLT, WhatsApp, APIs Custom).
- `docs/`: Documentación técnica y flujos de soporte.

## Configuración
1. Clonar el repositorio.
2. Configurar la `SMARTOLT_API_KEY` en el archivo de configuración o variables de entorno.
3. Ejecutar `python backend/main.py` para el modo de prueba.

---
Desarrollado con estándares de alto rendimiento para Jeisson Alberto.
