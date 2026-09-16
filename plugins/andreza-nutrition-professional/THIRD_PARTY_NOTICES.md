# Avisos de terceiros e proveniência

Este pacote combina skills privadas revisadas com materiais externos preservados sob suas licenças originais. A inclusão não implica endosso clínico pelos autores externos. Antes de atualizações, revise código, permissões, dependências e mudanças de licença.

| Projeto | Skills incluídas | Commit fixado | Origem | Licença |
|---|---|---|---|---|
| K-Dense Scientific Agent Skills | `literature-review` | `330c8e764435a731eff571e3efdda70b363d0792` | https://github.com/K-Dense-AI/scientific-agent-skills | ver `third_party/licenses/k-dense-LICENSE.md` |
| Open Medical Skills | `pubmed-literature-search`, `evidence-synthesis-ai`, `systematic-review-assistant`, `supplement-drug-interactions`, `clinical-guideline-navigator` | `0275541192e5875baa17085483586dd76b26c84e` | https://github.com/Open-Medica/open-medical-skills | ver `third_party/licenses/open-medica-LICENSE` |
| DeerFlow | `academic-paper-review` | `a022be195a1aaca47aafe0583c8a14b8b3f4b4e4` | https://github.com/bytedance/deer-flow | ver `third_party/licenses/deer-flow-LICENSE` |

## Adaptações da edição pública

As skills `literature-review` e `supplement-drug-interactions` foram adaptadas para reduzir risco clínico, coleta desnecessária e dependências externas. As alterações removem instalação automática de software, geração obrigatória por API de terceiros, alegações excessivamente categóricas e orientação que pudesse ser interpretada como modificação medicamentosa. As atribuições e licenças MIT foram preservadas.

## Observações de segurança

- As skills externas foram selecionadas por utilidade profissional, preservadas em diretórios próprios e validadas estruturalmente.
- Scripts externos podem acessar a internet e serviços de terceiros. `literature-review` inclui verificação DOI/Crossref, geração opcional de PDF com Pandoc/LaTeX e geração opcional de esquemas por OpenRouter. Não envie dados de pacientes a esses serviços.
- Dependências, APIs e custos externos não são instalados nem ativados automaticamente.
- A skill externa `supplement-drug-interactions` serve para triagem informacional; decisões clínicas continuam sob responsabilidade profissional e, quando necessário, médica/farmacêutica.
- Conteúdo externo deve ser reavaliado antes de cada atualização; o arquivo `SOURCE-LOCK.json` fixa a versão auditada neste pacote.
