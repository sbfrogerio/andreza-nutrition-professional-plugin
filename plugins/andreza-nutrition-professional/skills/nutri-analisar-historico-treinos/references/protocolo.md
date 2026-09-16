# Protocolo de histórico de treinos

## Dados por sessão

- data/hora e fuso;
- modalidade e tipo;
- planejado ou realizado;
- duração, distância e intensidade disponível;
- RPE e carga sessão-RPE quando calculável;
- potência, frequência cardíaca ou outras métricas com unidade;
- competição, viagem, doença, lesão e observações.

## Agregação

Usar semanas ISO. Informar semanas parciais. Calcular carga sessão-RPE como duração em minutos multiplicada pelo RPE quando ambos forem válidos.

O script pode calcular carga semanal, média diária, desvio-padrão, monotonia descritiva e strain. Não aplicar limiar automático de lesão ou prontidão.

`python3 scripts/training_history.py entrada.json`

## Comparação

Não comparar dispositivos ou métricas diferentes sem avisar. Separar carga interna, carga externa, volume e desempenho.

