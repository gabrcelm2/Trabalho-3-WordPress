import os
from locust import HttpUser, task, between

CENARIO = os.getenv("CENARIO", "hibrido").lower()

ROTAS = {
    "imagem_300kb": "/wp-content/uploads/2026/05/nabor300kb.png",
    "texto_400kb": "/?page_id=10",
    "imagem_1mb": "/wp-content/uploads/2026/05/gatinhosjpgnovo.jpg"
}

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    def get_ok(self, rota, nome):
        with self.client.get(rota, name=nome, catch_response=True, timeout=20) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Erro HTTP {response.status_code}")

    def acessar_img_300kb(self):
        self.get_ok(ROTAS["imagem_300kb"], "imagem_300kb")

    def acessar_texto(self):
        self.get_ok(ROTAS["texto_400kb"], "texto_400kb")

    def acessar_img_1mb(self):
        self.get_ok(ROTAS["imagem_1mb"], "imagem_1mb")

    def acessar_hibrido(self):
        self.acessar_img_1mb()
        self.acessar_texto()
        self.acessar_img_300kb()

    @task
    def executar_cenario(self):
        if CENARIO == "imagem_300kb":
            self.acessar_img_300kb()
        elif CENARIO == "texto_400kb":
            self.acessar_texto()
        elif CENARIO == "imagem_1mb":
            self.acessar_img_1mb()
        elif CENARIO == "hibrido":
            self.acessar_hibrido()
        else:
            self.acessar_hibrido()