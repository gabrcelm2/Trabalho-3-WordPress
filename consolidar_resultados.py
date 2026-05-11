import os
import csv
import glob

# Caminhos das pastas
pasta_resultados = 'resultados/finais'
arquivo_saida = 'resultados/resumo_resultados.csv'

# Dicionários para mapear os nomes e valores corretamente
nomes_cenarios = {
    'imagem_1mb': 'Imagem 1 MB',
    'texto_400kb': 'Texto 400 KB',
    'imagem_300kb': 'Imagem 300 KB',
    'hibrido': 'Híbrido'
}
usuarios_carga = {'leve': 100, 'media': 200, 'pesada': 250}
ordem_carga = {'leve': 0, 'media': 1, 'pesada': 2}

# Cabeçalho idêntico ao modelo
cabecalho_saida = [
    'arquivo', 'cenario', 'cenario_nome', 'instancias', 'carga', 'usuarios', 
    'request_count', 'failure_count', 'taxa_falha_%', 'tempo_medio_ms', 
    'tempo_mediano_ms', 'p95_ms', 'min_ms', 'max_ms', 'rps', 'failures_s', 'ordem_carga'
]

linhas_saida = []

# Pega todos os arquivos _stats.csv gerados
arquivos_csv = glob.glob(f"{pasta_resultados}/*_stats.csv")

for arquivo in arquivos_csv:
    nome_arquivo = os.path.basename(arquivo)
    
    # Extrai informações do nome do arquivo (ex: i1_leve_imagem_1mb_stats.csv)
    nome_sem_extensao = nome_arquivo.replace('_stats.csv', '')
    partes = nome_sem_extensao.split('_')
    
    instancias = partes[0].replace('i', '')
    carga = partes[1]
    cenario = "_".join(partes[2:])
    
    cenario_nome = nomes_cenarios.get(cenario, cenario)
    usuarios = usuarios_carga.get(carga, 0)
    ordem = ordem_carga.get(carga, 0)
    
    # Abre o CSV bruto para pegar a linha "Aggregated"
    with open(arquivo, 'r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            if linha['Name'] == 'Aggregated' or linha['Type'] == '':
                req_count = float(linha['Request Count'])
                fail_count = float(linha['Failure Count'])
                taxa_falha = (fail_count / req_count * 100) if req_count > 0 else 0.0
                
                nova_linha = {
                    'arquivo': nome_arquivo,
                    'cenario': cenario,
                    'cenario_nome': cenario_nome,
                    'instancias': int(instancias),
                    'carga': carga,
                    'usuarios': usuarios,
                    'request_count': req_count,
                    'failure_count': fail_count,
                    'taxa_falha_%': taxa_falha,
                    'tempo_medio_ms': float(linha['Average Response Time']),
                    'tempo_mediano_ms': float(linha['Median Response Time']),
                    'p95_ms': float(linha['95%']),
                    'min_ms': float(linha['Min Response Time']),
                    'max_ms': float(linha['Max Response Time']),
                    'rps': float(linha['Requests/s']),
                    'failures_s': float(linha['Failures/s']),
                    'ordem_carga': ordem
                }
                linhas_saida.append(nova_linha)

# Escreve o arquivo consolidado final
with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f:
    escritor = csv.DictWriter(f, fieldnames=cabecalho_saida)
    escritor.writeheader()
    for linha in sorted(linhas_saida, key=lambda x: (x['cenario'], x['instancias'], x['ordem_carga'])):
        escritor.writerow(linha)

print(f"Sucesso! O arquivo {arquivo_saida} foi gerado com os dados consolidados.")