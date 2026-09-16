# Protocolo de diário, fotos e rótulos

## Confiança da quantidade

- **Alta:** alimento pesado ou porção declarada com rótulo/receita.
- **Moderada:** medida caseira reconhecível e preparação simples.
- **Baixa:** fotografia sem escala, preparação mista, óleo/molho desconhecido.

## Campos

Registrar data, horário, refeição, contexto, item, quantidade, unidade, fonte da quantidade, fonte nutricional e confiança.

## Imagens

Não inferir ingrediente oculto. Perguntar sobre óleo, molhos, recheios, marca, tamanho do recipiente e repetição. Usar intervalo quando necessário.

## Cálculo

Executar:

`python3 scripts/sum_nutrients.py entrada.json`

O script soma apenas valores informados. Registros sem nutrientes continuam no denominador de cobertura e não viram zero.

## Comparação

Comparar com meta somente se a meta e o período forem fornecidos. Separar dias completos, parciais e atípicos.

