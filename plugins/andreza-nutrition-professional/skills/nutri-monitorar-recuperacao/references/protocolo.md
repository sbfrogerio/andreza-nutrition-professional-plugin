# Protocolo de monitoramento recente

## Dados e fontes

Aceitar dados de planilha, wearable, aplicativo e relato. Identificar fonte por campo. Não presumir equivalência entre dispositivos.

Campos úteis:

- data;
- duração e sRPE;
- sono;
- HRV e FC de repouso;
- peso;
- ingestão estimada;
- adesão;
- fadiga e dor;
- sintomas gastrointestinais;
- observação de viagem, prova, doença ou ciclo menstrual quando autorizado.

## Cálculos descritivos

Executar:

`python3 scripts/summarize_monitoring.py entrada.json`

O script calcula apenas cobertura, média, mediana, extremos, variação primeiro-último e carga sessão-RPE quando os campos existem. Não usar limites automáticos de risco.

## Alertas

Um alerta deve conter:

1. dado e período;
2. mudança observada;
3. qualidade/cobertura;
4. explicações alternativas;
5. pergunta ou revisão humana necessária.

Nunca emitir diagnóstico ou ajuste de treino.

