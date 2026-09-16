---
name: nutri-analisar-exames
description: Analisar longitudinalmente exames laboratoriais e histórico clínico fornecido, preservando datas, unidades, métodos, referências do próprio laboratório e contexto esportivo. Use explicitamente para séries de resultados, tendências e perguntas para nutricionista ou médico. Não diagnostique, prescreva ou aplique faixas universais.
---

# Analisar exames e histórico clínico

Esta skill é apoio técnico de alta cautela e deve ser invocada explicitamente. Transforme laudos em uma linha do tempo verificável sem automatizar diagnóstico ou conduta.

## Requisitos de entrada

1. Leia [references/protocolo.md](references/protocolo.md).
2. Prefira laudo original legível. Para dado apenas relatado, marque `RELATO`, não `RESULTADO DOCUMENTADO`.
3. Registre laboratório, data/hora da coleta, marcador textual, valor textual e numérico, unidade, material, método, intervalo do próprio laudo e observações.
4. Se identificação do paciente ou origem estiver ambígua, interrompa a consolidação até confirmar.

## Fluxo

1. Transcreva os valores críticos com dupla conferência contra o original.
2. Preserve sinais `<`, `>`, “não detectável”, hemólise, jejum e observações.
3. Agrupe apenas resultados comparáveis. Mudança de unidade, método, laboratório ou referência deve ficar visível.
4. Converta unidade somente com fator inequívoco, mostrando valor original, fórmula e resultado.
5. Execute `python3 scripts/lab_trends.py entrada.json` quando houver dados estruturados. Sem execução, faça análise descritiva e declare que o cálculo não foi automatizado.
6. Integre sintomas, medicamentos, suplementos, ciclo menstrual, treino e alimentação apenas como contexto temporal, sem causalidade.
7. Produza [assets/modelo-exames.md](assets/modelo-exames.md).

## Limites e escalonamento

- “Abaixo/acima” significa apenas fora da referência impressa no laudo.
- Não conclua deficiência, doença, RED-S, efeito de suplemento ou aptidão esportiva.
- Não recomende iniciar, suspender ou ajustar medicamento/suplemento.
- Destaque resultados potencialmente urgentes como necessidade de avaliação humana; não faça triagem médica automática.
- Minimize identificadores e não misture dados de pessoas diferentes.

## Controle de qualidade

Valide paciente/código, fonte, datas, unidades, método, referência, duplicatas, comparabilidade, transcrição e separação entre fato, tendência, hipótese e pergunta clínica.

