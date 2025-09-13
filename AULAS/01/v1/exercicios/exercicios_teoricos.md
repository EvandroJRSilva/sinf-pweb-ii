# Exercícios Teóricos - Arquitetura da Web e Comunicação Síncrona/Assíncrona

## 📚 Instruções Gerais

Estes exercícios foram elaborados para reforçar os conceitos apresentados na aula sobre Arquitetura da Web e Comunicação Síncrona/Assíncrona. Responda às questões de forma clara e completa, demonstrando sua compreensão dos conceitos fundamentais.

**Tempo estimado**: 45-60 minutos  
**Modalidade**: Individual ou em duplas  
**Material de apoio**: Slides da apresentação e exemplos práticos

---

## 🏗️ PARTE I: Arquitetura da Web (25 pontos)

### Questão 1 (5 pontos)
**Explique o modelo cliente-servidor e identifique os componentes principais desta arquitetura.**

Descreva em suas palavras como funciona a comunicação entre cliente e servidor na web. Inclua em sua resposta:
- O que é um cliente e quais são seus exemplos
- O que é um servidor e qual sua função
- Como ocorre a comunicação entre eles
- Pelo menos duas vantagens desta arquitetura

**Espaço para resposta:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

### Questão 2 (5 pontos)
**Descreva o processo que acontece quando você digita uma URL no navegador e pressiona Enter.**

Liste e explique brevemente cada etapa do processo, desde a digitação da URL até a exibição da página. Considere pelo menos 5 etapas principais.

**Espaço para resposta:**
```
1. ____________________________________________________________
   ____________________________________________________________

2. ____________________________________________________________
   ____________________________________________________________

3. ____________________________________________________________
   ____________________________________________________________

4. ____________________________________________________________
   ____________________________________________________________

5. ____________________________________________________________
   ____________________________________________________________
```

### Questão 3 (5 pontos)
**Compare Apache e Nginx, destacando suas principais diferenças arquiteturais.**

Complete a tabela comparativa abaixo:

| Aspecto | Apache | Nginx |
|---------|--------|-------|
| **Arquitetura de processamento** | ________________ | ________________ |
| **Consumo de memória** | ________________ | ________________ |
| **Melhor uso para** | ________________ | ________________ |
| **Configuração** | ________________ | ________________ |

### Questão 4 (5 pontos)
**Explique a diferença entre HTTP e HTTPS, incluindo aspectos de segurança.**

Sua resposta deve abordar:
- O que significa cada sigla
- Principais diferenças técnicas
- Quando usar cada um
- Importância da segurança na web

**Espaço para resposta:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

### Questão 5 (5 pontos)
**Identifique e explique os componentes de uma requisição HTTP.**

Liste e descreva brevemente os principais componentes que fazem parte de uma requisição HTTP:

**Espaço para resposta:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## ⚡ PARTE II: Comunicação Síncrona vs. Assíncrona (25 pontos)

### Questão 6 (8 pontos)
**Defina comunicação síncrona e assíncrona, destacando as principais diferenças.**

Complete o quadro comparativo:

| Característica | Comunicação Síncrona | Comunicação Assíncrona |
|----------------|---------------------|------------------------|
| **Bloqueio de execução** | ________________ | ________________ |
| **Ordem de execução** | ________________ | ________________ |
| **Performance** | ________________ | ________________ |
| **Complexidade de implementação** | ________________ | ________________ |
| **Experiência do usuário** | ________________ | ________________ |
| **Uso de recursos** | ________________ | ________________ |

### Questão 7 (5 pontos)
**Explique o problema da "espera" em aplicações síncronas.**

Descreva:
- O que acontece durante uma operação síncrona demorada
- Como isso afeta a experiência do usuário
- Por que isso é considerado um problema em aplicações web modernas

**Espaço para resposta:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

### Questão 8 (6 pontos)
**Analise os cenários abaixo e indique se seria melhor usar comunicação síncrona ou assíncrona. Justifique sua escolha.**

**Cenário A**: Um script que processa um arquivo CSV linha por linha e precisa garantir que cada linha seja processada na ordem correta.
```
Escolha: ________________
Justificativa: ___________________________________________
_______________________________________________________
```

**Cenário B**: Uma aplicação web que precisa carregar dados de múltiplas APIs diferentes para exibir um dashboard.
```
Escolha: ________________
Justificativa: ___________________________________________
_______________________________________________________
```

**Cenário C**: Um sistema de backup que precisa copiar arquivos de um servidor para outro, onde a ordem não importa.
```
Escolha: ________________
Justificativa: ___________________________________________
_______________________________________________________
```

### Questão 9 (6 pontos)
**Explique o conceito de callbacks e sua importância na programação assíncrona.**

Sua resposta deve incluir:
- Definição de callback
- Como os callbacks resolvem problemas de programação assíncrona
- Um exemplo simples de uso
- Pelo menos uma desvantagem dos callbacks

**Espaço para resposta:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## 🧠 PARTE III: Análise e Aplicação (25 pontos)

### Questão 10 (8 pontos)
**Analise o código JavaScript abaixo e responda às perguntas:**

```javascript
function buscarDados() {
    console.log("Iniciando busca...");
    
    fetch('https://api.exemplo.com/dados')
        .then(response => response.json())
        .then(dados => {
            console.log("Dados recebidos:", dados);
            processarDados(dados);
        })
        .catch(erro => {
            console.error("Erro:", erro);
        });
    
    console.log("Função buscarDados concluída");
}

function processarDados(dados) {
    console.log("Processando dados...");
}
```

**a) Este código usa comunicação síncrona ou assíncrona? Justifique.**
```
_________________________________________________________________
_________________________________________________________________
```

**b) Qual será a ordem de execução das mensagens no console? Explique por quê.**
```
1. ____________________________________________________________
2. ____________________________________________________________
3. ____________________________________________________________
4. ____________________________________________________________
```

**c) O que aconteceria se a API demorar 5 segundos para responder?**
```
_________________________________________________________________
_________________________________________________________________
```

### Questão 11 (8 pontos)
**Compare os dois códigos Python abaixo e explique as diferenças:**

**Código A (Síncrono):**
```python
import requests

def buscar_multiplos_dados():
    urls = ['api1.com', 'api2.com', 'api3.com']
    resultados = []
    
    for url in urls:
        resposta = requests.get(url)
        resultados.append(resposta.json())
    
    return resultados
```

**Código B (Assíncrono):**
```python
import asyncio
import aiohttp

async def buscar_multiplos_dados():
    urls = ['api1.com', 'api2.com', 'api3.com']
    
    async with aiohttp.ClientSession() as session:
        tarefas = [session.get(url) for url in urls]
        respostas = await asyncio.gather(*tarefas)
        resultados = [await r.json() for r in respostas]
    
    return resultados
```

**Análise:**
```
Diferenças principais:
1. ____________________________________________________________
2. ____________________________________________________________
3. ____________________________________________________________

Vantagens do Código A:
_________________________________________________________________

Vantagens do Código B:
_________________________________________________________________

Qual seria mais rápido e por quê?
_________________________________________________________________
_________________________________________________________________
```

### Questão 12 (9 pontos)
**Projeto de Solução: Você foi contratado para melhorar a performance de um site de notícias que está muito lento.**

**Situação atual:**
- O site carrega notícias de 5 fontes diferentes
- Cada fonte demora 2 segundos para responder
- As requisições são feitas sequencialmente
- Os usuários reclamam que o site demora 10+ segundos para carregar

**Sua tarefa:**
Proponha uma solução técnica detalhada para resolver este problema, considerando os conceitos aprendidos na aula.

**Espaço para resposta:**
```
Problema identificado:
_________________________________________________________________
_________________________________________________________________

Solução proposta:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

Tecnologias/técnicas a utilizar:
_________________________________________________________________
_________________________________________________________________

Benefícios esperados:
_________________________________________________________________
_________________________________________________________________

Tempo de carregamento estimado após a melhoria:
_________________________________________________________________
```

---

## 🎯 PARTE IV: Questões de Múltipla Escolha (25 pontos)

**Instruções**: Marque a alternativa correta para cada questão.

### Questão 13 (3 pontos)
**Qual é a principal característica da arquitetura cliente-servidor?**

a) ( ) O cliente sempre processa mais dados que o servidor  
b) ( ) A comunicação acontece apenas em uma direção  
c) ( ) Os recursos são centralizados no servidor e acessados pelos clientes  
d) ( ) Não é possível ter múltiplos clientes conectados simultaneamente  

### Questão 14 (3 pontos)
**Em uma requisição HTTP síncrona:**

a) ( ) A interface do usuário permanece sempre responsiva  
b) ( ) É possível executar outras operações simultaneamente  
c) ( ) O programa espera a resposta antes de continuar a execução  
d) ( ) Múltiplas requisições são sempre executadas em paralelo  

### Questão 15 (3 pontos)
**Qual das seguintes NÃO é uma vantagem das requisições assíncronas?**

a) ( ) Melhor experiência do usuário  
b) ( ) Possibilidade de execução paralela  
c) ( ) Simplicidade de implementação  
d) ( ) Interface não-bloqueante  

### Questão 16 (3 pontos)
**O "Callback Hell" refere-se a:**

a) ( ) Erro que acontece quando callbacks não são executados  
b) ( ) Problema de performance em operações assíncronas  
c) ( ) Aninhamento excessivo de callbacks tornando o código difícil de ler  
d) ( ) Impossibilidade de usar callbacks em JavaScript  

### Questão 17 (3 pontos)
**Qual protocolo é mais seguro para transmissão de dados sensíveis?**

a) ( ) HTTP, pois é mais rápido  
b) ( ) HTTPS, pois utiliza criptografia  
c) ( ) FTP, pois é específico para arquivos  
d) ( ) TCP, pois garante a entrega dos dados  

### Questão 18 (3 pontos)
**Em JavaScript, a função `fetch()` retorna:**

a) ( ) Diretamente os dados da API  
b) ( ) Uma Promise que resolve com a resposta  
c) ( ) Um callback que deve ser executado  
d) ( ) Um erro se a requisição falhar  

### Questão 19 (3 pontos)
**Qual é a principal diferença entre Apache e Nginx?**

a) ( ) Apache é gratuito, Nginx é pago  
b) ( ) Apache usa threads, Nginx usa eventos  
c) ( ) Apache é mais rápido que Nginx  
d) ( ) Nginx não suporta HTTPS  

### Questão 20 (4 pontos)
**Em Python, para fazer requisições assíncronas, você precisa usar:**

a) ( ) Apenas a biblioteca `requests`  
b) ( ) `asyncio` junto com `aiohttp`  
c) ( ) Apenas `urllib`  
d) ( ) `threading` com `requests`  

---

## ✅ Gabarito e Critérios de Avaliação

### Distribuição de Pontos:
- **Parte I (Arquitetura da Web)**: 25 pontos
- **Parte II (Comunicação Síncrona/Assíncrona)**: 25 pontos  
- **Parte III (Análise e Aplicação)**: 25 pontos
- **Parte IV (Múltipla Escolha)**: 25 pontos
- **Total**: 100 pontos

### Critérios de Avaliação:
- **Excelente (90-100 pontos)**: Demonstra compreensão completa dos conceitos
- **Bom (80-89 pontos)**: Compreende a maioria dos conceitos com pequenas lacunas
- **Satisfatório (70-79 pontos)**: Compreensão básica dos conceitos principais
- **Necessita Melhoria (60-69 pontos)**: Compreensão limitada, necessita revisão
- **Insatisfatório (<60 pontos)**: Compreensão insuficiente, necessita reestudo

---

## 📝 Observações para o Professor

### Tempo de Aplicação:
- **Explicação das instruções**: 5 minutos
- **Realização dos exercícios**: 45-50 minutos
- **Discussão das respostas**: 15-20 minutos

### Dicas de Correção:
1. **Questões abertas**: Valorize a demonstração de compreensão dos conceitos, mesmo que a linguagem técnica não seja perfeita
2. **Questões práticas**: Considere soluções criativas que demonstrem entendimento dos princípios
3. **Análise de código**: Foque na capacidade de identificar padrões síncronos/assíncronos
4. **Múltipla escolha**: Use como indicador rápido de compreensão dos conceitos básicos

### Recursos de Apoio:
- Permita consulta aos slides durante a primeira aplicação
- Considere realizar em duplas para estimular discussão
- Use as questões como base para discussão em classe

---

**Boa sorte com os exercícios! 🚀**

