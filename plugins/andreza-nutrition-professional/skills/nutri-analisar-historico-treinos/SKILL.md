---
name: nutri-analisar-historico-treinos
description: Analisar semanas, meses e ciclos de treino por modalidade, duração, intensidade, carga, competições, interrupções e resposta do atleta para contextualizar decisões nutricionais. Não use para prescrever treino, diagnosticar lesão/overtraining ou inferir intensidade não registrada.
---

# Analisar histórico de treinos

Descreva a evolução do treinamento e suas relações temporais com nutrição e recuperação, preservando limites entre carga externa, carga interna e percepção subjetiva.

## Preparação

1. Leia [references/protocolo.md](references/protocolo.md).
2. Defina período, modalidade, fuso, fontes, dispositivos, unidades e proporção de sessões cobertas.
3. Diferencie planejado de realizado e semana completa de parcial.
4. Identifique duplicatas, troca de dispositivo/método, competições, viagens, doença, lesão e pausas somente quando documentadas.

## Fluxo

1. Estruture cada sessão com data, modalidade, tipo, duração, distância, intensidade disponível, RPE, potência/FC e eventos contextuais.
2. Calcule sessão-RPE somente quando duração e RPE forem válidos.
3. Execute `python3 scripts/training_history.py entrada.json` para agregação por semana ISO quando possível.
4. Compare semanas e blocos sem aplicar limiares automáticos de risco.
5. Relacione ingestão, peso, sintomas, recuperação e desempenho somente como coincidências temporais ou hipóteses a investigar.
6. Produza [assets/modelo-historico-treinos.md](assets/modelo-historico-treinos.md).

## Limites

- Não misture volume, carga interna, carga externa e desempenho.
- Não determine prontidão, lesão, overreaching ou overtraining.
- Não recomende aumentar/reduzir carga; formule perguntas para treinador/equipe.
- Para janela diária/semanal de recuperação, encaminhe para `nutri-monitorar-recuperacao`.

## Controle de qualidade

Confira cobertura, duplicatas, semanas parciais, cálculo de carga, mudança de fonte, eventos competitivos e explicações alternativas.

