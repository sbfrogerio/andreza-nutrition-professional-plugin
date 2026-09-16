---
name: nutri-auditar-suplementos
description: Auditar suplemento, medicamento informado e rótulo quanto a identidade, dose, sinônimos, alegações, interações, certificação e risco antidopagem em fontes oficiais atuais. Use explicitamente para produto, ingrediente ou protocolo. Nunca declare segurança absoluta, prescreva medicamento ou substitua ABCD/WADA/médico/farmacêutico.
---

# Auditar suplementos e antidopagem

Esta é uma verificação documentada de risco, não um certificado de segurança. Exija invocação explícita.

## Gate de dados

1. Leia [references/protocolo.md](references/protocolo.md).
2. Confirme atleta/código, modalidade, país, competição/data, produto, fabricante, apresentação, lote, validade e fotografias legíveis de todas as faces.
3. Sem rótulo/lote ou sem acesso à lista oficial vigente, limite o estado a `NÃO AVALIÁVEL`.

## Fluxo

1. Transcreva literalmente ingredientes, doses, porção e advertências; preserve erros do rótulo como observação.
2. Normalize sinônimos em coluna separada e marque blend/quantidade oculta.
3. Consulte ABCD e WADA vigentes, registrando URL, versão e data/hora.
4. Se disponível, use `supplement-drug-interactions` apenas como triagem; confirme alegações materiais em fonte primária/oficial.
5. Diferencie: ingrediente declarado, medicamento, interação potencial, substância proibida/condicional, certificação e risco de contaminação.
6. Verifique se a certificação se aplica ao lote específico; não confunda selo geral com garantia.
7. Produza [assets/modelo-auditoria-suplemento.md](assets/modelo-auditoria-suplemento.md) usando os estados do protocolo.

## Regras críticas

- Nunca use “100% seguro”, “liberado” ou equivalentes.
- Não inferir fórmula pelo nome comercial e não completar blend proprietário.
- Não orientar suspensão/ajuste de medicamento; encaminhar interação e AUT ao profissional habilitado.
- Sinais de farmacovigilância não provam causalidade nem incidência.
- Se a fonte vigente não puder ser aberta e verificada, pare a conclusão.

## Controle de qualidade

Confira identidade do produto, lote, país, data, legibilidade, correspondência exata dos sinônimos, escopo da proibição e linguagem proporcional ao risco residual.

