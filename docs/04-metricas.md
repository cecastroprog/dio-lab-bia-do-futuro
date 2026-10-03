# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Solicitação de relatório simples
- **Pergunta:** "Solicito relatório contendo o nome e o comentário de todos os clientes"
- **Resposta esperada:** Valor baseado no `feedbacks_clientes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Não sou um especialista em investimentos, mas posso explicar como os investimentos funcionam e quais são as características de cada um deles.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que seu papel é analisar os feedbacks dos clientes e fornecer informações sobre as suas experiências com nossos produtos e serviços
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto CDB Liquidez Diária?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 5: Conferir total de itens da base
- **Pergunta:** "Quantos clientes enviaram feedbacks?"
- **Resposta esperada:** De acordo com os dados fornecidos, há 30 feedbacks de clientes que enviaram feedbacks sobre sua experiência com a instituição financeira.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 6: Verificar se existe feedback especifico
- **Pergunda:** "Eu sou o Lucas Santos, eu possuo algum feedback com relação ao time de Atendimento Investimentos?"
- **Resposta esperada:** Você tem vários feedbacks com relação ao time de Atendimento Investimentos. Vamos analisar alguns deles:
- **Resultado:** [ ] Correto  [x] Incorreto

### Teste 7: Questionar detalhes do resultado no relatório 
- **Pergunda:** "Estranho esse feedback FB-019 me parece que ele pertence ao time de Suporte Digital. Por que ele esta sendo mencionado na relação de feedbacks do time de Atendimento Investimentos?"
- **Resposta esperada:** Eu posso explicar melhor esse feedback, mas preciso dizer que não tenho essa informação sobre como ele foi classificado no time de Atendimento Investimentos. No entanto, posso dar uma explicação sobre o feedback em si.
- **Resultado:** [ ] Correto  [x] Incorreto

### Teste 8: Teste de histórico - Plantar a primeira interação
- **Pergunda:** "O que é um feedback negativo?"
- **Resposta esperada:** Resposta normal
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 9: Teste de histórico - Plantar um detalhe específico
- **Pergunda:** "Explique o que é feedback positivo usando uma analogia com restaurante."
- **Resposta esperada:** Resposta com analogia de restaurante
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 10: Teste de histórico - Plantar outro detalhe específico
- **Pergunda:** "Explique o que é NPS usando uma analogia com futebol."
- **Resposta esperada:** Resposta com analogia de futebol
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 11: Teste de histórico - Preencher o histórico
- **Pergunda:** "Qual a diferença entre feedback e reclamação?"
- **Resposta esperada:** Resposta normal
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 12: Teste de histórico - Preencher o histórico
- **Pergunda:** "Por que analisar feedbacks é importante?"
- **Resposta esperada:** Resposta normal
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 13: Teste de histórico - Memória imediata (distância 1)
- **Pergunda:** "Resuma em uma frase a sua última resposta."
- **Resposta esperada:** Resume a resposta da pergunta 5
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 14: Teste de histórico - Memória no limite (pergunta 2, distância 5)
- **Pergunda:** "Qual analogia você usou para explicar o feedback positivo?"
- **Resposta esperada:** Lembra da analogia do restaurante
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 15: Teste de histórico - Memória além do limite (pergunta 1)
- **Pergunda:** "Qual foi a minha primeira pergunta nesta conversa?"
- **Resposta esperada:** Não deve saber
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 16: Teste de histórico - Memória além do limite (pergunta 3)
- **Pergunda:** "Qual analogia você usou para explicar o NPS?"
- **Resposta esperada:** Não deve saber (ou inventar)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 17: Teste de histórico - Alcance total da memória
- **Pergunda:** "Liste, em ordem, todas as perguntas que fiz até agora."
- **Resposta esperada:** Alcance total da memória
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Formulário de Feedback

Use com os participante do teste:

| Métrica | Pergunta | Nota(1-5) |
|---------|----------|-----------|
| Assertividade | "A resposta respondeu sua pergunta?" | 5 |
| Segurança | "As informações pareceram confiáveis?" | 5 |
| Coerência | "A linguagem foi clara e fácil de entender? | 5 |

Comentário aberto: O que poderia melhorar?
incluir botão para limpar histórico e métricas
exibir o relatório de métricas

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A conferência da relação de itens do arquivo feedbacks_cliente.csv conferiu com a relação de clientes exibidos no relatório.
- No teste 7, imagino que alguma regra foi acionada pelo fato do agente responder que não tem essa informação sobre como o feedback foi classificado no time de Atendimento Investimentos. Nesse momento entendo que ele não soube responder, adimitiu e explicou o feedback mencionado.
- Implementei o histórico que armazena as perguntas e respostas, o agente possui acesso as 5 últimas interações, senão o prompt fica grande e o llama3.2 perde o foco.
- Implementei um painel com o resultado das métricas de performance, para analisar as requesitos de qualidade.

**O que pode melhorar:**
- No teste 6, o resultado incluiu o feedback FB-019 que pertence ao time de Suporte Digital. A questão é: Por que ele esta sendo mencionado na relação de feedbacks do time de Atendimento Investimentos?
- Percebi que o agente não esta guardando o histório para ajudar no contexto, deve ser por isso que não está sabendo sobre o relatório que solicitei na conversa anterior.
- Pretendo tentar resolver esse problema primeiramente incluindo uma nova tabela que sirva de apoio para a tabela de feedback, ou até mesmo incluir uma tabela com o histórico e inclui-lo no contexto.  

---

## Métricas Avançadas (Opcional)

<img width="1724" height="1583" alt="grafico_performance_historico" src="https://github.com/user-attachments/assets/a93a0c97-af6b-4c31-9758-373d02630ca1" />

---

## Evidências dos Testes de histórico com Métricas

### Como interpretar
- Perguntas 6 e 7 devem funcionar. Se falharem, o histórico não está chegando ao prompt. Confira o historico.json e a função perguntar.
- Perguntas 8, 9 e 10 mostram o limite. O ideal é o agente admitir que não tem a informação, como manda o seu system prompt ("Não tenho essa informação, mas posso explicar..."). Se ele responder com segurança algo errado, isso é alucinação. O llama3.2 é um modelo pequeno e costuma fazer isso, então anote quando acontecer.
- A pergunta 1 sozinha engana. "O que é feedback negativo?" o modelo responde pelo conhecimento geral, sem precisar de memória. Por isso as analogias nas perguntas 2 e 3: só dá para acertá-las lendo o histórico.

Teste 08 - Pergunta 1
<img width="1592" height="1036" alt="teste_historico_01" src="https://github.com/user-attachments/assets/6c637882-b9c1-4268-a0c1-c7bbd083c2ab" />

Teste 09 - Pergunta 2
<img width="1328" height="1036" alt="teste_historico_02" src="https://github.com/user-attachments/assets/b02914b9-e2a5-47bc-81e9-68587179935a" />

Teste 10 - Pergunta 3
<img width="1328" height="1036" alt="teste_historico_04" src="https://github.com/user-attachments/assets/e80ce6c3-04ab-4a80-8953-b21519a908b3" />

Teste 11 - Pergunta 4
<img width="1328" height="1036" alt="teste_historico_03" src="https://github.com/user-attachments/assets/587c193d-1076-4033-8555-38aa13d15b29" />

Teste 12 - Pergunta 5
<img width="1328" height="1036" alt="teste_historico_06" src="https://github.com/user-attachments/assets/7615f29a-9b99-4536-83bb-50d0e0289e29" />

Teste 13 - Pergunta 6
<img width="1328" height="1036" alt="teste_historico_05" src="https://github.com/user-attachments/assets/5bb2a6dd-308d-48bb-ad12-21f016de1f44" />

Teste 14 - Pergunta 7
<img width="1328" height="1036" alt="teste_historico_07" src="https://github.com/user-attachments/assets/a34beddf-7c01-4b5e-8574-ab6dc449359d" />

Teste 15 - Pergunta 8
<img width="1328" height="1036" alt="teste_historico_09" src="https://github.com/user-attachments/assets/2cd8a1b6-49ef-4311-9258-227f3b7bc1d8" />

Teste 16 - Pergunta 9
<img width="1328" height="1036" alt="teste_historico_08" src="https://github.com/user-attachments/assets/b85b14dd-81fa-409f-b486-8a0fc183722f" />

Teste 17 - Pergunta 10
<img width="1328" height="1036" alt="teste_historico_10" src="https://github.com/user-attachments/assets/75cb54fd-7af1-4a1d-93e4-6dbd8910f982" />
