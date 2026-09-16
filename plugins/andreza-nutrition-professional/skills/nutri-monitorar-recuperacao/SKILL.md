---
name: nutri-monitorar-recuperacao
description: Consolidar dados diários ou semanais de treino, sono, HRV, frequência cardíaca de repouso, peso, ingestão, sintomas, fadiga e adesão. Use para tendências recentes, mudanças de padrão e perguntas de acompanhamento. Não use para diagnóstico, prontidão automática, prescrição de redução de treino ou alteração autônoma do plano.
---

# Monitorar treino e recuperação

Transforme dados recentes em um resumo descritivo para decisão humana da equipe.

## Preparação

1. Leia [references/protocolo.md](references/protocolo.md).
2. Confirme período, fontes, dispositivos, unidades, frequência de coleta e campos faltantes.
3. Diferencie `MEDIDO`, `ESTIMADO PELO DISPOSITIVO` e `AUTORRELATADO`.
4. Não compare diretamente métricas produzidas por dispositivos/protocolos diferentes.

## Fluxo

1. Padronize datas e identifique duplicatas, dias sem dados e mudança de dispositivo.
2. Execute `python3 scripts/summarize_monitoring.py entrada.json` quando houver JSON estruturado.
3. Descreva cobertura, tendência, variabilidade e coincidências temporais; não atribua causa.
4. Compare o atleta consigo mesmo no período disponível, sem faixas populacionais não fornecidas.
5. Para cada sinal relevante, apresente dado, janela, cobertura, explicações alternativas e pergunta para revisão humana.
6. Produza [assets/modelo-monitoramento.md](assets/modelo-monitoramento.md).

## Limites

- Nenhuma métrica isolada determina recuperação, RED-S, doença ou prontidão.
- Não prescreva afastamento, ajuste de treino ou intervenção médica.
- Sintomas importantes devem ser destacados para avaliação humana imediata conforme o contexto.
- Para ciclos históricos longos, use `nutri-analisar-historico-treinos`.

## Controle de qualidade

Confira período, cobertura, duplicatas, unidades, cálculo, mudança de fonte e distinção entre correlação, hipótese e decisão.

