---
name: nutri-planejar-periodizacao
description: Elaborar ou revisar planejamento nutricional periodizado conforme microciclo, sessões, descanso, competição, composição corporal, horários, tolerância e disponibilidade. Use para distribuir metas aprovadas, refeições e substituições com conferência matemática. Não decida metas clínicas, diagnostique ou interprete exames isoladamente.
---

# Planejar periodização nutricional

Produza proposta individualizada e auditável para aprovação da nutricionista — nunca dieta genérica derivada apenas de calorias.

## Gate de entrada

1. Leia [references/protocolo.md](references/protocolo.md).
2. Confirme peso de referência/data, objetivo, modalidade, fase, calendário, microciclo, horários, restrições, preferências e metas já aprovadas.
3. Se metas ainda não foram aprovadas, apresente cenários com premissas e perguntas; não escolha automaticamente energia ou g/kg.

## Fluxo

1. Classifique dias/sessões apenas com intensidade, duração e objetivo informados.
2. Execute `python3 scripts/calculate_targets.py entrada.json` para transformar taxas aprovadas em gramas e conferir energia derivada.
3. Distribua ingestão no tempo considerando sessão, tolerância gastrointestinal, rotina, acesso, preparo e produtos testados.
4. Use base alimentar brasileira indicada pela profissional; registre fonte/versão e estado cru/preparado.
5. Some refeições, compare com metas e exponha diferenças e arredondamentos.
6. Inclua substituições equivalentes, contingências e condição/data de reavaliação.
7. Produza [assets/modelo-plano-periodizado.md](assets/modelo-plano-periodizado.md).

## Segurança

- Wearable estima gasto; não mede necessidade energética individual.
- Não altere conduta por exame, sintoma ou suspeita de RED-S sem revisão.
- Não crie precisão incompatível com composição/porção incerta.
- Toda saída é minuta; destaque premissas ainda não aprovadas.

## Controle de qualidade

Valide unidades, peso/data, energia derivada, somas, compatibilidade sessão-horário, alergias, tolerância, disponibilidade e divergências entre meta e proposta.

