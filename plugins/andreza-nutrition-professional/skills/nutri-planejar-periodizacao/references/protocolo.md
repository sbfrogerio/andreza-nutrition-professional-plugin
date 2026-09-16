# Protocolo de planejamento periodizado

## Dados mínimos

- Peso de referência com data.
- Metas aprovadas ou método a validar.
- Microciclo com data, sessão, modalidade, duração, intensidade informada e horário.
- Objetivo, fase esportiva e competição-alvo.
- Rotina, acesso, orçamento, preparo e horários.
- Alergias, restrições, preferências e tolerância gastrointestinal.
- Alimentos e produtos já testados.

## Cálculo

Usar o script para transformar metas aprovadas em gramas e conferir energia derivada:

`python3 scripts/calculate_targets.py entrada.json`

O script não decide meta clínica. Registrar peso usado, taxa g/kg, arredondamento e diferença entre energia-alvo e energia derivada dos macros.

## Fontes alimentares

Priorizar tabela brasileira indicada pelo profissional. Usar USDA ou rótulo apenas para item não disponível ou produto específico, registrando origem. Não misturar valores de alimento cru e preparado.

## Saída

Entregar:

1. Premissas e dados faltantes.
2. Quadro do microciclo.
3. Metas por tipo de dia.
4. Distribuição por sessão/refeição.
5. Substituições.
6. Conferência matemática.
7. Tolerância, logística e contingências.
8. Pontos para validação.

