# Trabalho 3 — Wordpress, Locust e Nginx

Este repositório contém o projeto desenvolvido para o **Trabalho 3 da disciplina de Computação Distribuída**, com foco na realização de testes de carga em uma aplicação **WordPress** executada em contêineres Docker.

O objetivo do trabalho é analisar o comportamento da aplicação sob diferentes níveis de carga, utilizando o **Locust** para simular usuários virtuais e o **Nginx** como balanceador de carga entre múltiplas instâncias do WordPress.

---

## Relatório do Trabalho

O relatório completo com a análise dos resultados, gráficos e conclusões está disponível no arquivo:

```text
relatorio_trabalho3_resultados_graficos.pdf
```

O relatório apresenta a análise das principais métricas coletadas durante os testes:

- P95 do tempo de resposta;
- taxa de erro;
- tempo médio de resposta;
- comparação por número de usuários;
- comparação por número de instâncias do WordPress.

---

## Alunos

- Gabriel Costa — 2314515
- Lívia Catarina — 2315085
- Alanis Bitencourt — 2315059

---

## Tecnologias Utilizadas

- Docker
- Docker Compose
- WordPress
- MySQL
- Nginx
- Locust
- Python
- PowerShell
- Matplotlib
- Pandas

---

## Arquitetura do Projeto

A arquitetura utilizada nos testes segue o seguinte fluxo:

```text
Locust → Nginx → WordPress → MySQL
```

| Serviço | Função |
|---|---|
| Locust | Simula usuários virtuais e gera carga na aplicação |
| Nginx | Atua como proxy reverso e balanceador de carga |
| WordPress | Aplicação web utilizada nos testes |
| MySQL | Banco de dados utilizado pelo WordPress |
| Python | Usado para consolidar os resultados e gerar gráficos |

---

## Estrutura do Repositório

```text
TRABALHO3_WORDPRESS/
│
├── __pycache__/
│
├── graficos/
│   ├── p95_msinstanciashibrido.png
│   ├── p95_msinstanciasimagem_1mb.png
│   ├── p95_msinstanciasimagem_300kb.png
│   ├── p95_msinstanciastexto_400kb.png
│   ├── p95_msusuarioshibrido.png
│   ├── p95_msusuariosimagem_1mb.png
│   ├── p95_msusuariosimagem_300kb.png
│   ├── p95_msusuariostexto_400kb.png
│   ├── taxa_falha_%instanciashibrido.png
│   ├── taxa_falha_%instanciasimagem_1mb.png
│   ├── taxa_falha_%instanciasimagem_300kb.png
│   ├── taxa_falha_%instanciastexto_400kb.png
│   ├── taxa_falha_%usuarioshibrido.png
│   ├── taxa_falha_%usuariosimagem_1mb.png
│   ├── taxa_falha_%usuariosimagem_300kb.png
│   ├── taxa_falha_%usuariostexto_400kb.png
│   ├── tempo_medio_msinstanciashibrido.png
│   ├── tempo_medio_msinstanciasimagem_1mb.png
│   ├── tempo_medio_msinstanciasimagem_300kb.png
│   ├── tempo_medio_msinstanciastexto_400kb.png
│   ├── tempo_medio_msusuarioshibrido.png
│   ├── tempo_medio_msusuariosimagem_1mb.png
│   ├── tempo_medio_msusuariosimagem_300kb.png
│   └── tempo_medio_msusuariostexto_400kb.png
│
├── locust_scripts/
│
├── resultados/
│
├── consolidar_resultados.py
├── csv_novo.csv
├── docker-compose.yml
├── gerar_graficos.py
├── locustfile.py
├── nginx.conf
├── resumo_resultados.csv
├── testes.ps1
├── relatorio_trabalho3_resultados_graficos.pdf
└── README.md
```

---

## Descrição dos Arquivos Principais

| Arquivo/Pasta | Descrição |
|---|---|
| `docker-compose.yml` | Define os serviços utilizados no ambiente, como WordPress, MySQL, Nginx e Locust |
| `nginx.conf` | Configuração do Nginx como balanceador de carga entre as instâncias do WordPress |
| `locustfile.py` | Arquivo principal do Locust com os cenários de teste |
| `locust_scripts/` | Pasta destinada aos scripts relacionados ao Locust |
| `testes.ps1` | Script PowerShell utilizado para automatizar a execução dos testes |
| `consolidar_resultados.py` | Script responsável por consolidar os resultados brutos dos testes |
| `gerar_graficos.py` | Script responsável por gerar os gráficos finais a partir dos resultados consolidados |
| `resumo_resultados.csv` | Arquivo consolidado com os dados finais dos testes |
| `csv_novo.csv` | Arquivo CSV auxiliar utilizado no tratamento dos resultados |
| `graficos/` | Pasta contendo os gráficos gerados para análise |
| `resultados/` | Pasta com os arquivos de saída produzidos durante os testes |
| `relatorio_trabalho3_resultados_graficos.pdf` | Relatório final do trabalho com a análise completa |

---

## Cenários de Teste

Foram utilizados quatro cenários principais para avaliar o comportamento do WordPress sob carga:

| Cenário | Descrição |
|---|---|
| `imagem_1mb` | Acesso a uma imagem de aproximadamente 1 MB |
| `imagem_300kb` | Acesso a uma imagem de aproximadamente 300 KB |
| `texto_400kb` | Acesso a uma página/post com aproximadamente 400 KB de texto |
| `hibrido` | Fluxo combinando imagem de 1 MB, texto de 400 KB e imagem de 300 KB |

O cenário híbrido representa uma navegação mais próxima de um uso real, pois combina diferentes tipos de conteúdo em uma mesma execução.

---

## Cargas Utilizadas

Os testes foram realizados com diferentes níveis de carga, simulando usuários virtuais no Locust.

| Carga | Usuários simulados |
|---|---:|
| Leve | 100 usuários |
| Média | 200 usuários |
| Pesada | 250 usuários |

Essas cargas foram utilizadas para observar o comportamento da aplicação conforme o número de usuários simultâneos aumentava.

---

## Métricas Analisadas

As principais métricas analisadas foram:

| Métrica | Descrição |
|---|---|
| Tempo médio de resposta | Média do tempo gasto para responder às requisições |
| P95 | Tempo abaixo do qual 95% das requisições foram respondidas |
| Taxa de erro | Percentual de requisições que falharam durante o teste |

A taxa de erro foi calculada pela fórmula:

```text
taxa de erro = failure_count / request_count × 100
```

---

## Gráficos Gerados

A pasta `graficos/` contém os gráficos finais usados na análise do trabalho. Eles foram divididos por métrica e por tipo de comparação.

### Gráficos de P95

- P95 por usuários;
- P95 por instâncias;
- análise por cenário: `hibrido`, `imagem_1mb`, `imagem_300kb` e `texto_400kb`.

### Gráficos de Taxa de Erro

- taxa de erro por usuários;
- taxa de erro por instâncias;
- comparação entre cenários e cargas.

### Gráficos de Tempo Médio

- tempo médio por usuários;
- tempo médio por instâncias;
- análise da latência média em cada cenário.

---

## Resumo dos Resultados

De forma geral, os testes mostraram que os cenários com arquivos estáticos, como `imagem_300kb` e `imagem_1mb`, apresentaram maior estabilidade e menor taxa de erro.

Os cenários `texto_400kb` e `hibrido` tiveram maior impacto no desempenho, principalmente em cargas mais altas, pois exigem maior processamento do WordPress e maior uso de recursos compartilhados, como banco de dados e ambiente local.

Mesmo nos cenários mais pesados, a taxa de erro permaneceu abaixo do limite definido no trabalho, indicando que o ambiente conseguiu suportar a carga simulada com estabilidade aceitável.

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <link-do-repositorio>
cd TRABALHO3_WORDPRESS
```

### 2. Subir os contêineres

```bash
docker compose up -d
```

### 3. Verificar se os serviços estão em execução

```bash
docker ps
```

### 4. Acessar o WordPress

```text
http://localhost:8080
```

### 5. Acessar o painel do WordPress

```text
http://localhost:8080/wp-admin
```

### 6. Executar os testes com Locust

```bash
locust -f locustfile.py --host=http://localhost:8080
```

Depois, acesse a interface do Locust pelo navegador:

```text
http://localhost:8089
```

### 7. Gerar ou atualizar os gráficos

```bash
python gerar_graficos.py
```

---

## Conclusão

O trabalho permitiu avaliar o comportamento de uma aplicação WordPress submetida a diferentes cargas e quantidades de instâncias. A análise mostrou que o aumento de usuários afeta diretamente métricas como P95 e tempo médio de resposta, principalmente nos cenários que exigem mais processamento.

Também foi possível observar que adicionar mais instâncias do WordPress não garante ganho linear de desempenho, pois ainda existem gargalos compartilhados, como banco de dados, armazenamento e limitações físicas da máquina local.

Assim, o projeto demonstra na prática conceitos importantes de Computação Distribuída, balanceamento de carga, testes de desempenho, escalabilidade e análise de métricas em sistemas web.
