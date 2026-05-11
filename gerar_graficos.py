import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do seu CSV
arquivo_csv = "resumo_resultados.csv"

# Pasta onde os gráficos serão salvos
pasta_saida = "graficos"
os.makedirs(pasta_saida, exist_ok=True)

# Lê o CSV
df = pd.read_csv(arquivo_csv)

# Garante ordenação correta das cargas
ordem_cargas = {"leve": 1, "media": 2, "pesada": 3}
df["ordem_carga"] = df["carga"].map(ordem_cargas)
df = df.sort_values(by=["cenario", "instancias", "ordem_carga"])

# Métricas que serão plotadas
metricas = {
    "p95_ms": "P95 do Tempo de Resposta (ms)",
    "taxa_falha_%": "Taxa de Erro (%)",
    "tempo_medio_ms": "Tempo Médio de Resposta (ms)"
}

# Cenários existentes no CSV
cenarios = df["cenario"].unique()

# ==============================
# GRÁFICOS COM USUÁRIOS NO EIXO X
# ==============================

for metrica, titulo_metrica in metricas.items():
    for cenario in cenarios:
        dados_cenario = df[df["cenario"] == cenario]

        plt.figure(figsize=(10, 6))

        for instancia in sorted(dados_cenario["instancias"].unique()):
            dados = dados_cenario[dados_cenario["instancias"] == instancia]

            plt.plot(
                dados["usuarios"],
                dados[metrica],
                marker="o",
                label=f"{instancia} instância(s)"
            )

        plt.title(f"{titulo_metrica} por Usuários - {cenario}")
        plt.xlabel("Número de Usuários")
        plt.ylabel(titulo_metrica)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()
        plt.tight_layout()

        nome_arquivo = f"{pasta_saida}/{metrica}usuarios{cenario}.png"
        plt.savefig(nome_arquivo, dpi=300)
        plt.close()

# ==================================
# GRÁFICOS COM INSTÂNCIAS NO EIXO X
# ==================================

for metrica, titulo_metrica in metricas.items():
    for cenario in cenarios:
        dados_cenario = df[df["cenario"] == cenario]

        plt.figure(figsize=(10, 6))

        for carga in ["leve", "media", "pesada"]:
            dados = dados_cenario[dados_cenario["carga"] == carga]

            plt.plot(
                dados["instancias"],
                dados[metrica],
                marker="o",
                label=f"Carga {carga}"
            )

        plt.title(f"{titulo_metrica} por Instâncias - {cenario}")
        plt.xlabel("Quantidade de Instâncias do WordPress")
        plt.ylabel(titulo_metrica)
        plt.xticks([1, 2, 3])
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()
        plt.tight_layout()

        nome_arquivo = f"{pasta_saida}/{metrica}instancias{cenario}.png"
        plt.savefig(nome_arquivo, dpi=300)
        plt.close()

print("Gráficos gerados com sucesso na pasta 'graficos'.")