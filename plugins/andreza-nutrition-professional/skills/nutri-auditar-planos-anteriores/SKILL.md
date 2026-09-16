---
name: nutri-auditar-planos-anteriores
description: Comparar planos alimentares anteriores, metas, substituições, adesão, tolerância, desempenho e desfechos para recuperar aprendizados antes de nova conduta. Não trate prescrição como ingestão real, julgue profissional anterior, atribua causalidade ou crie um novo plano completo.
---

# Auditar planos alimentares anteriores

Reconstrua o histórico de estratégias de modo neutro, rastreável e útil para decisão profissional.

## Fluxo

1. Leia [references/protocolo.md](references/protocolo.md).
2. Ordene os planos por período, objetivo, fase esportiva, peso de referência e fonte/autoria disponível.
3. Separe quatro camadas: `PRESCRITO`, `RELATADO COMO EXECUTADO`, `OBSERVADO/MEDIDO` e `NÃO AVALIADO`.
4. Extraia energia, macronutrientes, horários, substituições, suplementos, flexibilidade, adesão, sintomas, tolerância, praticidade e desfechos com data.
5. Compare números somente com unidade, conceito e peso de referência compatíveis.
6. Execute `python3 scripts/compare_plans.py entrada.json` quando houver dados estruturados.
7. Classifique aprendizados como mantido, modificado, bem tolerado, baixa viabilidade, contraditório ou evidência insuficiente.
8. Produza [assets/modelo-historico-planos.md](assets/modelo-historico-planos.md).

## Regras de interpretação

- Não assuma adesão nem chame plano de sucesso/fracasso sem critérios prévios.
- Associação temporal não estabelece causa.
- Não replique automaticamente restrição, suplemento ou erro de plano anterior.
- Preserve tom técnico e não depreciativo sobre outros profissionais.
- Qualquer hipótese de nova conduta fica para validação da nutricionista.

## Controle de qualidade

Verifique completude temporal, equivalência de unidades, contexto de treino, adesão, desfechos, fonte e incerteza.

