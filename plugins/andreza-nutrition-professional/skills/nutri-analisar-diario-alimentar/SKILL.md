---
name: nutri-analisar-diario-alimentar
description: Analisar recordatórios, diários alimentares, fotos, receitas, rótulos e exportações de aplicativos, separando consumo documentado de estimativas e comparando a ingestão com metas fornecidas. Use para avaliar cobertura, padrões, distribuição e lacunas. Não use fotografia para inferir ingredientes ocultos nem um único dia para representar ingestão habitual.
---

# Analisar diário alimentar

Produza uma análise nutricional auditável. Preserve a diferença entre alimento registrado, quantidade declarada, medida caseira e estimativa visual.

## Antes de analisar

1. Leia [references/protocolo.md](references/protocolo.md).
2. Identifique período, fuso, dias completos/parciais, fonte de cada entrada, contexto de treino e metas de comparação.
3. Se faltar quantidade, receita, marca, óleo, molho ou escala da imagem, registre a lacuna. Pergunte somente o que puder alterar materialmente a conclusão.
4. Não transforme ausência de registro em consumo zero.

## Fluxo

1. Estruture cada item por data/hora, refeição, alimento, quantidade, unidade, fonte da quantidade, fonte nutricional e confiança.
2. Classifique confiança como alta, moderada ou baixa segundo o protocolo.
3. Para preparações mistas, separe componentes confirmados de componentes possíveis. Nunca complete a receita por plausibilidade.
4. Use a base alimentar indicada pela nutricionista e registre nome/versão. Não misture alimento cru, cozido e preparado.
5. Quando houver JSON estruturado e execução disponível, rode `python3 scripts/sum_nutrients.py entrada.json`. No ChatGPT Work sem execução, mostre a fórmula e marque os totais como cálculo manual a conferir.
6. Compare somente com metas explicitamente fornecidas e no mesmo período/unidade.
7. Use [assets/modelo-diario.md](assets/modelo-diario.md) como formato de saída.

## Segurança e interpretação

- Use faixas para porções incertas; não crie falsa precisão.
- Não rotule alimentos como bons/ruins nem moralize adesão.
- Não conclua deficiência, excesso crônico ou transtorno alimentar a partir do diário isolado.
- Diferencie padrão observado, hipótese e pergunta de acompanhamento.
- Saída clínica é minuta para revisão da nutricionista.

## Controle de qualidade

Confira datas, duplicatas, cobertura, unidades, fonte de composição, confiança, itens não contabilizados e diferença entre ingestão confirmada, estimada e meta.

