import logging
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger("Orchestrator")

class SalesSupportOrchestrator:
    def __init__(self, smartolt, ai, db, config: Dict[str, Any] = None):
        self.smartolt = smartolt
        self.ai = ai
        self.db = db
        # Configuración por defecto de umbrales técnicos
        self.config = config or {
            "critical_dbm": -27.0,
            "warning_dbm": -25.0
        }

    def process_incoming_event(self, phone: str, text: str) -> str:
        """Punto de entrada con manejo de excepciones y logging de auditoría."""
        try:
            start_time = datetime.now()
            client = self.db.get_client_by_phone(phone)
            
            # 1. Detección de Intención Avanzada (Zero-Shot)
            intent_data = self.ai.classify_intent(text)
            intent = intent_data['intent']
            confidence = intent_data['confidence']
            
            logger.info(f"Event: {phone} | Intent: {intent} ({confidence}) | Text: {text}")

            # 2. Ruteo de Lógica
            if intent == "SUPPORT":
                response = self._handle_support_logic(client, text)
            elif intent == "SALES":
                response = self._handle_sales_logic(client, text)
            else:
                response = self.ai.generate_conversational_response(text, context=client)

            # 3. Auditoría de tiempo de respuesta
            duration = (datetime.now() - start_time).total_seconds()
            logger.info(f"Response sent in {duration}s")
            
            return response
        except Exception as e:
            logger.critical(f"FATAL ERROR in Orchestrator: {e}", exc_info=True)
            return "Lo siento, estoy experimentando una falla técnica momentánea. Un agente humano revisará tu caso."

    def _handle_support_logic(self, client: Optional[Dict], text: str) -> str:
        if not client or not client.get("onu_external_id"):
            return self.ai.ask_for_identifier()

        status = self.smartolt.get_onu_status(client["onu_external_id"])
        if not status:
            return "No pude conectar con tu equipo en este momento. Por favor, reintenta en un minuto."

        # Diagnóstico técnico experto
        rx_power = float(status.get("rx_power", 0))
        phase = status.get("phase_state", "Unknown")

        # Casos de falla
        if phase != "Working":
            return self.ai.format_response("OFFLINE_ERROR", status)
        
        if rx_power <= self.config["critical_dbm"]:
            return self.ai.format_response("CRITICAL_SIGNAL", {"power": rx_power})

        # Si todo está bien pero el cliente se queja, aplicar troubleshooting lógico
        return self.ai.generate_troubleshooting(status)

    def _handle_sales_logic(self, client: Optional[Dict], text: str) -> str:
        # Analizar consumo histórico si la API lo permite, o simplemente ofrecer upgrade
        current_plan = client.get("plan_name", "Básico") if client else "Nuevo Cliente"
        return self.ai.generate_smart_offer(current_plan, is_lead=(client is None))
