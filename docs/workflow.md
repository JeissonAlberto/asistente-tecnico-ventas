# Flujos de Trabajo - Asistente IA Avidtel

## 1. Flujo de Soporte Técnico
1. **Entrada:** Usuario reporta falla vía WhatsApp.
2. **Identificación:** Se busca el número en SmartOLT/DB local.
3. **Diagnóstico:**
    - Si ONU Offline: Sugerir revisión de energía.
    - Si Señal > -27dBm: Sugerir reinicio de router.
    - Si Señal <= -27dBm: Alerta automática (Fibra comprometida).
4. **Resolución:** Si el problema persiste tras reinicio, escalar a ticket humano.

## 2. Flujo de Ventas (Upselling)
1. **Entrada:** Usuario pregunta por precios o el soporte termina exitosamente.
2. **Calificación:** IA revisa el plan actual del cliente.
3. **Oferta:** Si tiene Plan 50MB, ofrecer 100MB o 200MB con descuento por 3 meses.
4. **Conversión:** Si acepta, enviar link de pago o registrar solicitud en CRM.
