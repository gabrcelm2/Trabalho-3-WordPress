# Trabalho 3 — Testes de Carga em WordPress com Locust

Projeto desenvolvido para avaliar o desempenho de uma aplicação **WordPress** executando em Docker, com requisições distribuídas pelo **Nginx** e geração de carga usando **Locust**.

A análise considera diferentes quantidades de usuários simultâneos, cenários de acesso e número de instâncias do WordPress.

---

## Integrantes

- Gabriel Costa — 2314515
- Lívia Catarina — 2315085
- Alanis Bitencourt — 2315059

---

## Objetivo do Trabalho

O objetivo principal foi simular acessos concorrentes ao WordPress e observar como a aplicação se comporta sob carga.

Foram analisadas três métricas principais:

| Métrica | O que representa |
|---|---|
| Tempo médio de resposta | Média do tempo que o servidor levou para responder |
| P95 | Tempo máximo observado para 95% das requisições |
| Taxa de erro | Percentual de requisições com falha |

---

## Arquitetura Utilizada

O ambiente foi montado com contêineres Docker.

```text
Locust → Nginx → WordPress
```

| Componente | Responsabilidade |
|---|---|
| Locust | Simular usuários acessando a aplicação |
| Nginx | Receber as requisições e balancear entre as instâncias |
| WordPress | Aplicação testada |

---

## Estrutura do Repositório

A organização principal do projeto ficou da seguinte forma:

```text
TRABALHO3_WORDPRESS/
│
├── graficos/
│   ├── p95_*.png
│   ├── taxa_falha_*.png
│   └── tempo_medio_*.png
│
├── locust_scripts/
│   └── locustfile.py
│
├── resultados/
│   └── arquivos gerados pelo Locust
│
├── consolidar_resultados.py
├── gerar_graficos.py
├── resumo_resultados.csv
├── docker-compose.yml
├── nginx.conf
├── testes.ps1
└── README.md
```

---

## Cenários Avaliados

Os testes foram separados de acordo com o tipo de conteúdo acessado:

| Cenário | Descrição |
|---|---|
| `imagem_1mb` | Acesso a uma imagem com aproximadamente 1 MB |
| `imagem_300kb` | Acesso a uma imagem com aproximadamente 300 KB |
| `texto_400kb` | Acesso a uma página com texto de aproximadamente 400 KB |
| `hibrido` | Fluxo misto com imagem 1 MB, texto 400 KB e imagem 300 KB |

O cenário híbrido foi usado para representar uma navegação mais próxima de um uso real, pois mistura conteúdos leves e mais pesados.

---

## Configuração dos Testes

Foram executados testes variando:

| Variável | Valores |
|---|---|
| Usuários virtuais | 100, 200 e 250 |
| Instâncias do WordPress | 1, 2 e 3 |
| Cenários | imagem_1mb, imagem_300kb, texto_400kb e híbrido |

Com isso, foi possível comparar o impacto do aumento da carga e da quantidade de instâncias no desempenho geral da aplicação.

---

## Como Executar o Projeto

### 1. Subir os contêineres

```bash
docker compose up -d
```

### 2. Verificar se os serviços estão ativos

```bash
docker ps
```

### 3. Executar os testes com Locust

Os testes podem ser executados pelo script:

```powershell
./testes.ps1
```

Depois disso, o painel do Locust pode ser acessado em:

```text
http://localhost:8089
```

---

## Geração dos Resultados

Após a execução dos testes, os arquivos brutos são consolidados em uma tabela única:

```bash
python consolidar_resultados.py
```

Em seguida, os gráficos são gerados com:

```bash
python gerar_graficos.py
```

Os principais arquivos produzidos são:

| Arquivo/Pasta | Conteúdo |
|---|---|
| `resumo_resultados.csv` | Tabela final com os resultados consolidados |
| `graficos/` | Gráficos de P95, taxa de falha e tempo médio |
| `resultados/` | Saídas individuais geradas pelos testes |

---

## Gráficos Gerados

As imagens dos gráficos gerados durante os testes estão disponíveis na pasta do Google Drive abaixo:

```text
https://drive.google.com/drive/folders/1qC98bwMhvVscoNyrX00uQ3oOERv1UXbp?usp=sharing
```

Foram criados gráficos para comparar os resultados por:

- quantidade de usuários;
- quantidade de instâncias do WordPress;
- tipo de cenário executado.

As métricas representadas nos gráficos são:

```text
P95
Taxa de erro
Tempo médio de resposta
```

Exemplo de organização dos arquivos:

```text
graficos/
├── p95_musuarioshibrido.png
├── taxa_falha_%usuarioshibrido.png
├── tempo_medio_musuarioshibrido.png
├── p95_minstanciasimagem_1mb.png
├── taxa_falha_%instanciasimagem_1mb.png
└── tempo_medio_minstanciasimagem_1mb.png
```

---

## Relatório

O relatório completo com a análise dos gráficos está disponível no repositório:

```text
relatorio_trabalho3_resultados_graficos.pdf
```

Nele são discutidos:

- comportamento do P95;
- taxa de erro em cada cenário;
- tempo médio de resposta;
- impacto do aumento de usuários;
- impacto da variação de instâncias;
- conclusão geral sobre o desempenho do WordPress no ambiente testado.

---


## Resumo dos Resultados

De forma geral, os testes mostraram que os cenários com imagens estáticas tiveram melhor estabilidade e menor tempo de resposta. Já os cenários com texto e principalmente o cenário híbrido exigiram mais da aplicação, apresentando aumento no P95 e pequenas taxas de erro em cargas maiores.

Mesmo nos cenários mais pesados, os resultados ficaram dentro do limite definido para o trabalho, mantendo a taxa de erro abaixo de **10%**.
