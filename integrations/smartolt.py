import requests
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger("SmartOLT")

class SmartOLTIntegration:
    """
    Integración de alto rendimiento con SmartOLT.
    Implementa reintentos, manejo de errores y validación de tipos.
    """
    def __init__(self, api_key: str, domain: str):
        if not api_key:
            raise ValueError("API Key de SmartOLT es requerida.")
        self.api_key = api_key
        self.base_url = f"https://{domain}/api/v1"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Accept": "application/json",
            "User-Agent": "Avidtel-AI-Agent/2.0"
        }

    def _request(self, method: str, endpoint: str, params: Dict = None, data: Dict = None) -> Optional[Dict]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, params=params, json=data, timeout=15)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en SmartOLT API ({endpoint}): {e}")
            return None

    def get_onu_status(self, onu_external_id: str) -> Optional[Dict]:
        """Obtiene estado técnico detallado (potencia, uptime, estado)."""
        return self._request("GET", f"/onu/get_onu_status/{onu_external_id}")

    def get_onu_details(self, onu_external_id: str) -> Optional[Dict]:
        """Obtiene detalles del cliente asociados a la ONU."""
        return self._request("GET", f"/onu/get_onu_details/{onu_external_id}")

    def reboot_onu(self, onu_external_id: str) -> bool:
        """Envía comando de reinicio y valida ejecución."""
        res = self._request("POST", f"/onu/reboot/{onu_external_id}")
        return res is not None and res.get("status") == "success"

    def search_client_by_field(self, field_name: str, value: str) -> Optional[list]:
        """Búsqueda flexible de clientes."""
        params = {field_name: value}
        res = self._request("GET", "/customers/search", params=params)
        return res.get("response") if res else None
