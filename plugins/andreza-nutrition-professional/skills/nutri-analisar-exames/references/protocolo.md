# Protocolo de exames e histórico clínico

## Unidade de registro

Para cada resultado, preservar:

- marcador exatamente como no laudo;
- data e hora da coleta;
- valor textual e valor numérico quando possível;
- unidade;
- intervalo de referência do próprio laudo;
- método, material e observação;
- laboratório e documento-fonte;
- jejum e contexto quando informados.

## Comparabilidade

Agrupar apenas marcador e unidade compatíveis. Informar mudança de método, laboratório ou referência. Não converter unidade sem fator inequívoco e registro da conversão.

## Estados

- dentro/abaixo/acima apenas segundo o intervalo do laudo;
- indeterminado quando não houver referência ou o valor não for comparável;
- tendência descritiva como aumento, redução, estabilidade aproximada ou dados insuficientes.

## Contexto

Relacionar medicamentos, suplementos, sintomas, fase do treino e alimentação pela data. Não afirmar causa.

## Script

`python3 scripts/lab_trends.py entrada.json`

O script não contém faixas clínicas universais e não emite diagnóstico.

