import os
import json
from integrations.smartolt import SmartOLTIntegration
from integrations.custom_api import CustomAPIIntegrator
from backend.orchestrator import SalesSupportOrchestrator

# --- MOTOR DE IA MEJORADO (SIMULACIÓN DE ALTO NIVEL) ---
class HighLevelAI:
    """Simula una integración con GPT-4 o similar con prompts especializados."""
    def classify_intent(self, text: str) -> dict:
        t = text.lower()
        if any(x in t for x in ["lento", "internet", "wifi", "falla", "rojo", "luz"]):
            return {"intent": "SUPPORT", "confidence": 0.98}
        if any(x in t for x in ["megas", "plan", "precio", "cuanto", "mejorar", "promo"]):
            return {"intent": "SALES", "confidence": 0.95}
        return {"intent": "GENERAL", "confidence": 0.80}

    def format_response(self, template: str, data: dict) -> str:
        templates = {
            "OFFLINE_ERROR": "Detecto que tu equipo está desconectado o sin energía. ¿Podrías revisar si la luz 'PON' o 'LOS' está en rojo?",
            "CRITICAL_SIGNAL": f"Tu señal óptica está muy baja ({data.get('power')} dBm). Esto indica un posible daño en el cable de fibra. He solicitado una revisión técnica técnica prioritaria.",
        }
        return templates.get(template, "Entendido, estoy revisando.")

    def generate_troubleshooting(self, status):
        return "Tu señal es óptima. Vamos a reiniciar tu conexión desde aquí. Por favor espera 2 minutos y prueba de nuevo."

    def generate_smart_offer(self, plan, is_lead):
        if is_lead: return "¡Hola! Veo que quieres internet de alta velocidad. Tenemos planes desde 100MB con fibra óptica. ¿Te gustaría ver los precios?"
        return f"Noté que usas mucho tu plan de {plan}. Tengo una oferta exclusiva para que saltes a 300MB por un precio especial. ¿Te interesa?"

    def ask_for_identifier(self):
        return "Para ayudarte, necesito tu número de documento o el ID de contrato que aparece en tu factura."

# --- MOCK DB CON PERSISTENCIA SIMPLE ---
class JsonDatabase:
    def __init__(self, path="data/clients.json"):
        self.path = path
        if not os.path.exists("data"): os.makedirs("data")
        if not os.path.exists(path):
            with open(path, "w") as f: json.dump({}, f)

    def get_client_by_phone(self, phone: str):
        with open(self.path, "r") as f:
            db = json.load(f)
        return db.get(phone)

def run_audit_mode():
    print("=== AUDIT MODE: AVIDTEL AI AGENT 2.0 ===")
    
    # Inyectar dependencias
    smartolt = SmartOLTIntegration(api_key="MOCK_KEY", domain="avidtel.smartolt.com")
    ai = HighLevelAI()
    db = JsonDatabase()
    
    # Crear cliente de prueba si no existe
    with open("data/clients.json", "w") as f:
        json.dump({"573132497317": {
            "name": "Jeisson Alberto",
            "onu_external_id": "AVDTL001",
            "plan_name": "100 Mega Hogar"
        }}, f)

    orchestrator = SalesSupportOrchestrator(smartolt, ai, db)

    # Test de Soporte
    print("\nTest 1: Soporte Técnico")
    print(f"User: 'Mi internet está muy lento'\nAI: {orchestrator.process_incoming_event('573132497317', 'Mi internet está muy lento')}")

    # Test de Venta
    print("\nTest 2: Venta")
    print(f"User: '¿Cuánto cuesta el plan de 300 megas?'\nAI: {orchestrator.process_incoming_event('573132497317', '¿Cuánto cuesta el plan de 300 megas?')}")

if __name__ == "__main__":
    run_audit_mode()
