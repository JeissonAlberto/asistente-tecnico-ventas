import requests
from typing import Dict, Any

class CustomAPIIntegrator:
    """
    Casilla de integración universal para conectar herramientas externas.
    """
    def __init__(self):
        self.services = {}

    def register_service(self, name: str, base_url: str, auth_token: str = None):
        self.services[name] = {
            "url": base_url,
            "token": auth_token
        }

    def post_to_service(self, service_name: str, endpoint: str, data: Dict[str, Any]):
        service = self.services.get(service_name)
        if not service:
            return {"error": f"Service {service_name} not found"}
        
        headers = {"Authorization": f"Bearer {service['token']}"} if service['token'] else {}
        url = f"{service['url']}{endpoint}"
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            return {"error": str(e)}
