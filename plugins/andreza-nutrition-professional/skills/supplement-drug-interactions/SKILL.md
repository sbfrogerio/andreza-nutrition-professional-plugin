---
name: supplement-drug-interactions
description: Triage possible supplement–medicine interactions using current authoritative sources, mechanism, dose, formulation, timing, and patient context. Use only when the user explicitly asks to check an interaction; never change medicines or present a database signal as proof of causation.
license: MIT
metadata:
  version: "1.0.0-public-safe"
  skill-author: Open Medical Skills contributors; public safety adaptation by Andreza Agra Nutrition
---

# Supplement–Medicine Interaction Triage

Produza triagem informacional conservadora para apoiar revisão por nutricionista, médico ou farmacêutico. Não diagnostique, não prescreva e não recomende iniciar, suspender ou alterar medicamento.

## Dados mínimos

Solicite, quando relevantes:

- medicamento, princípio ativo, dose, via, frequência e indicação;
- suplemento, composição integral, concentração, dose, forma, marca/lote e frequência;
- horário relativo entre produtos;
- idade/faixa etária, gestação/lactação e condições relevantes;
- função renal/hepática quando informada;
- sintomas ou evento adverso atual;
- finalidade da análise e data.

Se a composição ou dose do suplemento não estiver disponível, limite a conclusão e peça o rótulo. Não infira formulação apenas pelo nome comercial.

## Método

1. Normalize princípios ativos e ingredientes sem perder a formulação original.
2. Pesquise fontes atuais e rastreáveis: bula/agência reguladora, bases farmacológicas reconhecidas, revisões sistemáticas e literatura primária.
3. Classifique o tipo de evidência: estudo clínico, farmacocinética humana, estudo observacional, relato de caso, mecanismo pré-clínico ou sinal de farmacovigilância.
4. Diferencie interação demonstrada, possível por mecanismo, relato isolado e ausência de evidência localizada.
5. Avalie mecanismo plausível: absorção, quelagem, enzimas/transportadores, coagulação, pressão, glicemia, sedação, serotonina ou outro efeito farmacodinâmico.
6. Considere dose, formulação, duração, janela temporal e vulnerabilidades do caso.
7. Defina urgência e encaminhamento sem alterar a terapêutica.

## Saída

Para cada combinação, apresente:

- combinação analisada;
- evidência encontrada e data da busca;
- mecanismo e grau de confiança;
- relevância clínica potencial;
- fatores que aumentam ou reduzem preocupação;
- sinais de alerta;
- informação que falta;
- ação segura: discutir com prescritor/farmacêutico, monitorar conforme profissional responsável ou buscar atendimento urgente quando indicado;
- referências verificadas.

Não use “seguro”, “sem interação” ou percentuais de risco absolutos quando a evidência só indicar ausência de relatos ou mecanismo incerto. Sinais de farmacovigilância geram hipótese, não causalidade.

## Encaminhamento imediato

Oriente avaliação urgente diante de sangramento importante, síncope, dispneia, reação alérgica, confusão, convulsão, dor torácica, arritmia percebida, ideação suicida ou outros sinais graves. Não instrua o usuário a compensar doses ou suspender tratamento por conta própria.

## Privacidade

Use apenas dados mínimos e desidentificados em consultas externas. Nunca transmita prontuário, nome, contato ou documentos.

## Atribuição

Esta skill é uma adaptação de `supplement-drug-interactions`, do projeto Open Medical Skills, sob licença MIT. A licença original e o commit de origem constam em `THIRD_PARTY_NOTICES.md`.
