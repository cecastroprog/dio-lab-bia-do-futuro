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

O feedback FB-019 parece referir uma dúvida feita por uma cliente, Aline Pereira, sobre a instabilidade do CDB Liquidez Diária, e a maneira como ela foi tratada pelo time do Suporte Digital. Ele menciona que a taxa de administração é levemente alta, e que o CDB Liquidez Diária oscila bastante, como esperado.

É possível que, de alguma forma, ele tenha sido classificado no time de Atendimento Investimentos, mas sem uma explicação clara sobre como isso ocorreu.
- **Resultado:** [ ] Correto  [x] Incorreto

### Teste 8: Teste de histórico - Plantar a primeira interação
- **Pergunda:** "O que é um feedback negativo?"
- **Resposta esperada:** Resposta normal

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 9: Plantar um detalhe específico
- **Pergunda:** "Explique o que é feedback positivo usando uma analogia com restaurante."
- **Resposta esperada:** Resposta com analogia de restaurante

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 10: Plantar outro detalhe específico
- **Pergunda:** "Explique o que é NPS usando uma analogia com futebol."
- **Resposta esperada:** Resposta com analogia de futebol

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 11: Preencher o histórico
- **Pergunda:** "Qual a diferença entre feedback e reclamação?"
- **Resposta esperada:** Resposta normal

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 12: Preencher o histórico
- **Pergunda:** "Por que analisar feedbacks é importante?"
- **Resposta esperada:** Resposta normal

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 13: Memória imediata (distância 1)
- **Pergunda:** "Resuma em uma frase a sua última resposta."
- **Resposta esperada:** Resume a resposta da pergunta 5

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 14: Memória no limite (pergunta 2, distância 5)
- **Pergunda:** "Qual analogia você usou para explicar o feedback positivo?"
- **Resposta esperada:** Lembra da analogia do restaurante

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 15: Memória além do limite (pergunta 1)
- **Pergunda:** "Qual foi a minha primeira pergunta nesta conversa?"
- **Resposta esperada:** Não deve saber

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 16: Memória além do limite (pergunta 3)
- **Pergunda:** "Qual analogia você usou para explicar o NPS?"
- **Resposta esperada:** Não deve saber (ou inventar)

- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 17: Alcance total da memória
- **Pergunda:** "Liste, em ordem, todas as perguntas que fiz até agora."
- **Resposta esperada:** Alcance total da memória

- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Formulário de Feedback

Use com os participante do teste:

| Métrica | Pergunta | Nota(1-5) |
|---------|----------|-----------|
| Assertividade | "A resposta respondeu sua pergunta?" | __ |
| Segurança | "As informações pareceram confiáveis?" | __ |
| Coerência | "Alinguagem foi clara e fácil de entender? | __ |

Comentário aberto: O que poderia melhorar?

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A conferência da relação de itens do arquivo feedbacks_cliente.csv conferiu com a relação de clientes exibidos no relatório.
- No teste 7, imagino que alguma regra foi acionada pelo fato do agente responder que não tem essa informação sobre como o feedback foi classificado no time de Atendimento Investimentos. Nesse momento entendo que ele não soube responder, adimitiu e explicou o feedback mencionado.
- Implementei um painel com o resultado das métricas de performance, para analisar as requesitos de qualidade.

**O que pode melhorar:**
- No teste 6, o resultado incluiu o feedback FB-019 que pertence ao time de Suporte Digital. A questão é: Por que ele esta sendo mencionado na relação de feedbacks do time de Atendimento Investimentos?
- Percebi que o agente não esta guardando o histório para ajudar no contexto, deve ser por isso que não está sabendo sobre o relatório que solicitei na conversa anterior.
- Pretendo tentar resolver esse problema primeiramente incluindo uma nova tabela que sirva de apoio para a tabela de feedback, ou até mesmo incluir uma tabela com o histórico e inclui-lo no contexto.  

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
