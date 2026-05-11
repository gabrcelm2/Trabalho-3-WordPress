# variaveis
$cenarios = @("imagem_1mb", "texto_400kb", "imagem_300kb", "hibrido")

$cargas = @(
    @{nome="leve"; usuarios=100; Spawn=20},
    @{nome="media"; usuarios=200; Spawn=40},
    @{nome="pesada"; usuarios=250; Spawn=50}
)

$instancias = @(1, 2, 3)

New-Item -ItemType Directory -Force -Path "resultados/finais" | Out-Null

Write-Host "Iniciando bateria de testes..." -ForegroundColor Green

foreach ($instancia in $instancias) {

    Write-Host "`n=======================================================" -ForegroundColor Cyan
    Write-Host "CONFIGURANDO AMBIENTE COM $instancia INSTÂNCIA(S) DO WORDPRESS" -ForegroundColor Yellow
    Write-Host "=======================================================" -ForegroundColor Cyan

    docker compose down
    docker compose up -d --scale wordpress=$instancia

    Write-Host "Aguardando WordPress/Nginx estabilizar..." -ForegroundColor Yellow
    Start-Sleep -Seconds 20

    foreach ($carga in $cargas) {
        foreach ($cenario in $cenarios) {

            $usuarios = $carga.usuarios
            $spawn = $carga.Spawn
            $nome_carga = $carga.nome

            $nome_arquivo = "resultados/finais/i${instancia}_${nome_carga}_${cenario}"

            Write-Host "-> Executando: [$instancia Instância(s)] | Carga: $nome_carga ($usuarios users) | Spawn: $spawn | Cenário: $cenario" -ForegroundColor White

            $env:CENARIO = $cenario

            locust -f locustfile.py `
                --headless `
                -u $usuarios `
                -r $spawn `
                --run-time 1m `
                --host=http://localhost:8080 `
                --csv=$nome_arquivo

            Remove-Item "${nome_arquivo}_failures.csv" -ErrorAction SilentlyContinue
            Remove-Item "${nome_arquivo}_exceptions.csv" -ErrorAction SilentlyContinue
            Remove-Item "${nome_arquivo}_stats_history.csv" -ErrorAction SilentlyContinue
        }
    }
}

Write-Host "`nTodos os 36 testes foram concluídos!" -ForegroundColor Green