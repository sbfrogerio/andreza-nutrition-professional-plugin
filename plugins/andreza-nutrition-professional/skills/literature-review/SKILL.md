---
name: literature-review
description: Conduct reproducible multi-database literature reviews, scoping reviews, evidence maps, or broad scientific syntheses. Use when a question requires searches beyond one database, documented screening, critical appraisal, thematic synthesis, or PRISMA-style reporting.
license: MIT
metadata:
  version: "1.8-public-safe"
  skill-author: K-Dense Inc.; public safety adaptation by Andreza Agra Nutrition
---

# Literature Review

Conduza revisões amplas e reproduzíveis sem fabricar referências, resultados ou acesso a bases. Esta edição pública preserva a metodologia do projeto K-Dense e remove dependências obrigatórias de APIs, instaladores externos e geração de imagens por terceiros.

## Antes de começar

Defina e registre:

1. objetivo e tipo de revisão;
2. pergunta estruturada (PICO, PECO, SPIDER ou equivalente);
3. população, exposição/intervenção, comparador e desfechos;
4. critérios de inclusão e exclusão;
5. idiomas, período e bases;
6. data-limite da busca;
7. plano de extração, avaliação crítica e síntese.

Não chame uma busca de “sistemática” quando não houver protocolo, rastreabilidade e seleção documentada.

## Fluxo

### 1. Planejar

- Execute busca-piloto para ajustar termos.
- Combine vocabulário controlado e texto livre.
- Registre sinônimos, grafias, operadores, filtros e campos.
- Evite filtros injustificados que possam excluir evidência relevante.

### 2. Buscar em múltiplas fontes

Escolha fontes coerentes com a pergunta. Em saúde, considere PubMed/MEDLINE, Cochrane, Embase quando disponível, Scopus/Web of Science quando disponíveis e registros de estudos. Preprints devem ser identificados como não revisados por pares.

Para cada fonte, registre consulta exata, data, filtros e número de resultados. Se uma base não estiver acessível, declare isso; não simule resultados.

### 3. Deduplicar e selecionar

- Preserve identificadores DOI, PMID, registro e URL.
- Documente critérios antes da seleção.
- Separe triagem de título/resumo e texto completo.
- Registre motivo de exclusão na fase de texto completo.
- Recomende dupla revisão independente quando o uso exigir padrão de revisão sistemática.

### 4. Extrair e avaliar

Extraia desenho, população, contexto, intervenção/exposição, comparador, desfechos, medidas de efeito, precisão, perdas, financiamento e conflitos. Use ferramenta de risco de viés compatível com o desenho. Não converta qualidade metodológica em uma nota genérica sem justificativa.

### 5. Sintetizar

- Organize por pergunta, mecanismo, população ou desfecho; evite uma lista estudo por estudo.
- Separe resultados dos estudos, interpretação e aplicação clínica.
- Discuta heterogeneidade, inconsistência, indireção, imprecisão e viés de publicação.
- Não combine quantitativamente estudos incompatíveis.
- Quando houver certeza da evidência, explicite o método usado.

### 6. Verificar referências

Abra cada fonte citada ou valide seus metadados em índice confiável. Confirme título, autores, periódico, ano e DOI/PMID. Uma referência não verificada deve ser marcada como tal ou removida. Nunca gere DOI plausível por padrão textual.

### 7. Relatar

Entregue:

1. resumo executivo;
2. pergunta e protocolo;
3. estratégia completa por base;
4. fluxo de seleção e motivos de exclusão;
5. tabela de estudos e risco de viés;
6. síntese dos achados;
7. certeza, limitações e lacunas;
8. implicações práticas com limites de extrapolação;
9. referências verificadas;
10. data de atualização recomendada.

Use `assets/review_template.md` quando um relatório completo for solicitado. Consulte as referências internas somente quando necessárias ao caso.

## Segurança e privacidade

- Pesquisas externas devem usar termos científicos, não dados identificáveis de pacientes.
- Não envie prontuários, exames identificáveis ou histórico clínico a serviços externos.
- Não instale ferramentas ou dependências automaticamente.
- Geração de PDF, figuras e diagramas é opcional e nunca condição para concluir a revisão.
- Declare bases indisponíveis, paywalls e limitações de acesso.

## Atribuição

Esta skill é uma adaptação de `literature-review`, do projeto K-Dense Scientific Agent Skills, sob licença MIT. A licença original e o commit de origem constam em `THIRD_PARTY_NOTICES.md`.
