---
name: nutri-planejar-hidratacao-prova
description: Criar estratégia individualizada de hidratação e alimentação para treino-chave ou competição usando taxa de sudorese medida, clima, duração, abastecimento, tolerância gastrointestinal e produtos testados. Não estime sudorese sem dados, prometa prevenção de hiponatremia/desidratação ou substitua avaliação médica.
---

# Planejar hidratação e prova

Use medições contextualizadas e parâmetros aprovados para construir um roteiro testável, logístico e contingencial.

## Gate de entrada

1. Leia [references/protocolo.md](references/protocolo.md).
2. Confirme evento, modalidade, data/local, duração esperada, intensidade informada, clima com fonte/horário, altitude, postos e regras.
3. Confirme pesos pré/pós, fluidos, urina, duração e condições do teste de sudorese.
4. Sem medições válidas, não invente taxa: produza protocolo de coleta e lista de dados faltantes.

## Fluxo

1. Execute `python3 scripts/sweat_rate.py entrada.json`; preserve entradas, fórmula, unidade e condições.
2. Compare o teste apenas com situações suficientemente semelhantes, explicitando diferenças de ambiente, equipamento e aclimatação.
3. Integre histórico gastrointestinal, preferências, alergias e produtos já testados.
4. Monte roteiro cronológico pré/durante/pós sem exceder parâmetros aprovados pela nutricionista.
5. Inclua contingências para calor/frio, atraso, posto ausente, produto perdido e sintomas.
6. Use [assets/modelo-hidratacao-prova.md](assets/modelo-hidratacao-prova.md).

## Segurança

- Não experimente produto novo no evento-alvo.
- Não prometa reposição integral de perdas nem “hidratação perfeita”.
- Não defina sódio/eletrólitos sem parâmetros e revisão profissional.
- Separe taxa observada de meta de ingestão.
- Inclua critérios claros para interromper a estratégia e acionar suporte médico.

## Controle de qualidade

Valide fórmula, unidades, duração, plausibilidade das medições, condições do teste, disponibilidade real, abastecimento, tolerância e plano alternativo.

