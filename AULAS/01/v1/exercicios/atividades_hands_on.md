# Atividades Hands-On - Arquitetura da Web e Comunicação Síncrona/Assíncrona

## 🎯 Visão Geral

Estas atividades foram projetadas para serem executadas **durante a aula**, proporcionando experiência prática imediata com os conceitos apresentados. Cada atividade tem duração específica e pode ser realizada individualmente ou em grupos pequenos.

**Duração total**: 60-80 minutos (distribuídos ao longo da aula de 2 horas)  
**Modalidade**: Individual, duplas ou grupos de 3-4 pessoas  
**Recursos necessários**: Computador com navegador e editor de texto

---

## 🚀 ATIVIDADE 1: Explorando o Ciclo de Requisição-Resposta (15 minutos)

### Objetivo
Visualizar e compreender o que acontece "por baixo dos panos" quando acessamos um site.

### Materiais Necessários
- Navegador web (Chrome, Firefox, Safari, Edge)
- Acesso à internet

### Passo a Passo

#### Parte A: Usando as Ferramentas de Desenvolvedor (8 minutos)

1. **Abra o navegador** e pressione `F12` (ou `Ctrl+Shift+I` no Windows/Linux, `Cmd+Option+I` no Mac)

2. **Vá para a aba "Network" (Rede)**

3. **Visite diferentes sites** e observe:
   ```
   Site 1: https://www.google.com
   Site 2: https://jsonplaceholder.typicode.com/posts/1
   Site 3: https://httpbin.org/get
   ```

4. **Para cada site, anote:**
   - Quantas requisições foram feitas?
   - Qual foi o tempo total de carregamento?
   - Quais tipos de arquivos foram baixados? (HTML, CSS, JS, imagens)
   - Qual o status code da requisição principal?

#### Parte B: Analisando Headers HTTP (7 minutos)

1. **Clique em uma requisição** na aba Network

2. **Examine os headers de requisição:**
   - User-Agent
   - Accept
   - Host

3. **Examine os headers de resposta:**
   - Content-Type
   - Server
   - Cache-Control

4. **Preencha a tabela:**

| Site | Tempo Total | Nº Requisições | Servidor | Content-Type |
|------|-------------|----------------|----------|--------------|
| Google | _____ ms | _____ | _____ | _____ |
| JSONPlaceholder | _____ ms | _____ | _____ | _____ |
| HTTPBin | _____ ms | _____ | _____ | _____ |

### Discussão em Grupo (5 minutos)
- Por que alguns sites fazem mais requisições que outros?
- O que significa cada status code observado?
- Como os headers influenciam o comportamento da requisição?

---

## ⚡ ATIVIDADE 2: Sentindo a Diferença - Síncrono vs Assíncrono (20 minutos)

### Objetivo
Experimentar na prática a diferença entre operações síncronas e assíncronas.

### Materiais Necessários
- Editor de texto ou IDE
- Navegador web

### Passo a Passo

#### Parte A: Criando o Experimento (10 minutos)

1. **Crie um arquivo HTML** chamado `experimento.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Experimento: Síncrono vs Assíncrono</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        button { padding: 10px 20px; margin: 10px; font-size: 16px; }
        .contador { font-size: 24px; margin: 20px 0; }
        .resultado { background: #f0f0f0; padding: 15px; margin: 10px 0; }
        .red { background: #ffebee; }
        .green { background: #e8f5e8; }
    </style>
</head>
<body>
    <h1>Experimento: Síncrono vs Assíncrono</h1>
    
    <div class="contador">
        Contador: <span id="contador">0</span>
    </div>
    
    <button onclick="testarSincrono()">Teste Síncrono</button>
    <button onclick="testarAssincrono()">Teste Assíncrono</button>
    <button onclick="incrementarContador()">Incrementar Contador</button>
    
    <div id="resultado" class="resultado">
        Clique nos botões acima para testar...
    </div>
    
    <script>
        let contador = 0;
        
        // Atualiza contador na tela
        function atualizarContador() {
            document.getElementById('contador').textContent = contador;
        }
        
        function incrementarContador() {
            contador++;
            atualizarContador();
        }
        
        // COMPLETE ESTAS FUNÇÕES:
        function testarSincrono() {
            // Dica: Use XMLHttpRequest com async = false
            // URL: https://httpbin.org/delay/3
        }
        
        function testarAssincrono() {
            // Dica: Use fetch()
            // URL: https://httpbin.org/delay/3
        }
    </script>
</body>
</html>
```

2. **Complete as funções JavaScript** seguindo as dicas nos comentários

#### Parte B: Testando e Observando (10 minutos)

1. **Abra o arquivo no navegador**

2. **Teste a requisição síncrona:**
   - Clique em "Teste Síncrono"
   - Imediatamente tente clicar em "Incrementar Contador"
   - O que acontece?

3. **Teste a requisição assíncrona:**
   - Clique em "Teste Assíncrono"
   - Imediatamente tente clicar em "Incrementar Contador"
   - O que acontece?

4. **Anote suas observações:**
   ```
   Requisição Síncrona:
   - O contador conseguiu ser incrementado durante a requisição? ______
   - A interface ficou responsiva? ______
   - Quanto tempo demorou? ______
   
   Requisição Assíncrona:
   - O contador conseguiu ser incrementado durante a requisição? ______
   - A interface ficou responsiva? ______
   - Quanto tempo demorou? ______
   ```

### Reflexão
- Por que a interface se comportou diferente em cada caso?
- Qual abordagem oferece melhor experiência ao usuário?

---

## 🔄 ATIVIDADE 3: Construindo um Sistema de Callbacks (25 minutos)

### Objetivo
Implementar um sistema simples que demonstre o uso de callbacks na prática.

### Cenário
Você vai criar um simulador de pedido de pizza que usa callbacks para cada etapa do processo.

### Passo a Passo

#### Parte A: Estrutura Base (5 minutos)

1. **Crie um arquivo** `simulador_pizza.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Simulador de Pedido de Pizza</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; max-width: 800px; margin: 0 auto; }
        .etapa { background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .ativa { background: #fff3cd; border-left: 4px solid #ffc107; }
        .concluida { background: #d4edda; border-left: 4px solid #28a745; }
        button { padding: 10px 20px; font-size: 16px; margin: 10px 0; }
        .log { background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: monospace; }
    </style>
</head>
<body>
    <h1>🍕 Simulador de Pedido de Pizza</h1>
    
    <button onclick="fazerPedido()">Fazer Pedido</button>
    <button onclick="limparLog()">Limpar Log</button>
    
    <div id="etapas">
        <div class="etapa" id="etapa-pedido">1. Receber Pedido</div>
        <div class="etapa" id="etapa-preparo">2. Preparar Pizza</div>
        <div class="etapa" id="etapa-assar">3. Assar Pizza</div>
        <div class="etapa" id="etapa-embalar">4. Embalar Pizza</div>
        <div class="etapa" id="etapa-entregar">5. Entregar Pizza</div>
    </div>
    
    <div class="log" id="log">
        Log do pedido aparecerá aqui...
    </div>
    
    <script>
        // SEU CÓDIGO AQUI
    </script>
</body>
</html>
```

#### Parte B: Implementando as Funções com Callbacks (15 minutos)

2. **Implemente as funções do processo:**

```javascript
function receberPedido(callback) {
    log("📝 Recebendo pedido...");
    marcarEtapaAtiva("etapa-pedido");
    
    setTimeout(() => {
        log("✅ Pedido recebido: Pizza Margherita");
        marcarEtapaConcluida("etapa-pedido");
        callback(null, "Pizza Margherita");
    }, 1000);
}

function prepararPizza(tipoPizza, callback) {
    // IMPLEMENTE ESTA FUNÇÃO
    // Deve demorar 3 segundos
    // Deve atualizar o log e as etapas visuais
}

function assarPizza(pizzaPreparada, callback) {
    // IMPLEMENTE ESTA FUNÇÃO
    // Deve demorar 5 segundos
}

function embalarPizza(pizzaAssada, callback) {
    // IMPLEMENTE ESTA FUNÇÃO
    // Deve demorar 1 segundo
}

function entregarPizza(pizzaEmbalada, callback) {
    // IMPLEMENTE ESTA FUNÇÃO
    // Deve demorar 2 segundos
}

// Funções auxiliares
function log(mensagem) {
    const logElement = document.getElementById('log');
    const timestamp = new Date().toLocaleTimeString();
    logElement.innerHTML += `[${timestamp}] ${mensagem}\n`;
    logElement.scrollTop = logElement.scrollHeight;
}

function marcarEtapaAtiva(etapaId) {
    document.getElementById(etapaId).className = 'etapa ativa';
}

function marcarEtapaConcluida(etapaId) {
    document.getElementById(etapaId).className = 'etapa concluida';
}

function limparLog() {
    document.getElementById('log').innerHTML = 'Log do pedido aparecerá aqui...';
    // Resetar todas as etapas
    const etapas = document.querySelectorAll('.etapa');
    etapas.forEach(etapa => etapa.className = 'etapa');
}
```

3. **Implemente a função principal:**

```javascript
function fazerPedido() {
    limparLog();
    log("🚀 Iniciando processo de pedido...");
    
    receberPedido((erro, tipoPizza) => {
        if (erro) return log("❌ Erro: " + erro);
        
        prepararPizza(tipoPizza, (erro, pizzaPreparada) => {
            if (erro) return log("❌ Erro: " + erro);
            
            // CONTINUE O CALLBACK HELL AQUI...
            // assarPizza -> embalarPizza -> entregarPizza
        });
    });
}
```

#### Parte C: Testando e Melhorando (5 minutos)

4. **Teste o sistema:**
   - Clique em "Fazer Pedido"
   - Observe as etapas sendo executadas
   - Verifique se o log está sendo atualizado

5. **Identifique problemas:**
   - O código está ficando difícil de ler?
   - Como você melhoraria esta implementação?
   - O que acontece se uma etapa falhar?

### Discussão
- Como o "Callback Hell" afeta a legibilidade do código?
- Que alternativas existem para resolver este problema?

---

## 🐍 ATIVIDADE 4: Python Síncrono vs Assíncrono na Prática (20 minutos)

### Objetivo
Comparar performance entre requisições síncronas e assíncronas em Python.

### Pré-requisitos
- Python 3.7+
- Bibliotecas: `requests`, `aiohttp` (instalar se necessário)

### Passo a Passo

#### Parte A: Preparação do Ambiente (5 minutos)

1. **Instale as dependências:**
```bash
pip install requests aiohttp
```

2. **Crie um arquivo** `comparacao_python.py`:

```python
#!/usr/bin/env python3
import requests
import asyncio
import aiohttp
import time
from datetime import datetime

# URLs para testar
URLS = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1'
]

def log(mensagem):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {mensagem}")

# COMPLETE ESTAS FUNÇÕES:

def requisicoes_sincronas(urls):
    """Faz requisições síncronas sequenciais"""
    log("🐌 Iniciando requisições síncronas...")
    inicio = time.time()
    
    # SEU CÓDIGO AQUI
    
    fim = time.time()
    tempo_total = fim - inicio
    log(f"⏱️  Tempo total (síncrono): {tempo_total:.2f} segundos")
    return tempo_total

async def requisicoes_assincronas(urls):
    """Faz requisições assíncronas paralelas"""
    log("🚀 Iniciando requisições assíncronas...")
    inicio = time.time()
    
    # SEU CÓDIGO AQUI
    
    fim = time.time()
    tempo_total = fim - inicio
    log(f"⏱️  Tempo total (assíncrono): {tempo_total:.2f} segundos")
    return tempo_total

if __name__ == "__main__":
    print("🔬 Comparação: Síncrono vs Assíncrono em Python")
    print("=" * 50)
    
    # Teste síncrono
    tempo_sincrono = requisicoes_sincronas(URLS)
    
    print()
    
    # Teste assíncrono
    tempo_assincrono = asyncio.run(requisicoes_assincronas(URLS))
    
    print()
    print("📊 RESULTADOS:")
    print(f"Síncrono:   {tempo_sincrono:.2f}s")
    print(f"Assíncrono: {tempo_assincrono:.2f}s")
    print(f"Speedup:    {tempo_sincrono/tempo_assincrono:.2f}x")
```

#### Parte B: Implementação (10 minutos)

3. **Complete a função síncrona:**
```python
def requisicoes_sincronas(urls):
    log("🐌 Iniciando requisições síncronas...")
    inicio = time.time()
    
    resultados = []
    for i, url in enumerate(urls, 1):
        log(f"  Requisição {i}...")
        try:
            resposta = requests.get(url)
            resultados.append(resposta.status_code)
            log(f"  ✅ Requisição {i} concluída")
        except Exception as e:
            log(f"  ❌ Erro na requisição {i}: {e}")
    
    fim = time.time()
    tempo_total = fim - inicio
    log(f"⏱️  Tempo total (síncrono): {tempo_total:.2f} segundos")
    return tempo_total
```

4. **Complete a função assíncrona:**
```python
async def requisicoes_assincronas(urls):
    log("🚀 Iniciando requisições assíncronas...")
    inicio = time.time()
    
    async def fazer_requisicao(session, url, numero):
        log(f"  Requisição {numero}...")
        try:
            async with session.get(url) as resposta:
                log(f"  ✅ Requisição {numero} concluída")
                return resposta.status
        except Exception as e:
            log(f"  ❌ Erro na requisição {numero}: {e}")
            return None
    
    async with aiohttp.ClientSession() as session:
        tarefas = [
            fazer_requisicao(session, url, i+1) 
            for i, url in enumerate(urls)
        ]
        resultados = await asyncio.gather(*tarefas)
    
    fim = time.time()
    tempo_total = fim - inicio
    log(f"⏱️  Tempo total (assíncrono): {tempo_total:.2f} segundos")
    return tempo_total
```

#### Parte C: Execução e Análise (5 minutos)

5. **Execute o script:**
```bash
python comparacao_python.py
```

6. **Anote os resultados:**
```
Tempo Síncrono: _____ segundos
Tempo Assíncrono: _____ segundos
Speedup: _____ x
```

7. **Experimente com diferentes números de URLs:**
   - Teste com 2 URLs
   - Teste com 10 URLs
   - Como o speedup muda?

### Reflexão
- Por que o speedup aumenta com mais requisições?
- Em que situações você usaria cada abordagem?

---

## 🎨 ATIVIDADE BÔNUS: Criando um Mini Dashboard (Tempo restante)

### Objetivo
Aplicar todos os conceitos aprendidos em um projeto integrado.

### Descrição Rápida
Criar uma página web simples que:
1. Monitore o status de 3 APIs diferentes
2. Atualize as informações a cada 10 segundos
3. Mostre se cada API está online/offline
4. Permita alternar entre modo síncrono e assíncrono

### Estrutura Mínima

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Mini Dashboard</title>
    <style>
        .api-card { 
            border: 1px solid #ddd; 
            padding: 15px; 
            margin: 10px; 
            border-radius: 5px; 
        }
        .online { border-left: 4px solid #28a745; }
        .offline { border-left: 4px solid #dc3545; }
    </style>
</head>
<body>
    <h1>📊 Mini Dashboard de APIs</h1>
    
    <button onclick="alternarModo()">
        Modo: <span id="modo">Assíncrono</span>
    </button>
    
    <div id="apis">
        <!-- Cards das APIs serão inseridos aqui -->
    </div>
    
    <script>
        const APIS = [
            { nome: 'JSONPlaceholder', url: 'https://jsonplaceholder.typicode.com/posts/1' },
            { nome: 'HTTPBin', url: 'https://httpbin.org/get' },
            { nome: 'ReqRes', url: 'https://reqres.in/api/users/1' }
        ];
        
        let modoAssincrono = true;
        
        // IMPLEMENTE AS FUNÇÕES AQUI
    </script>
</body>
</html>
```

### Implementação Livre
- Use sua criatividade para implementar as funcionalidades
- Aplique os conceitos aprendidos na aula
- Foque na diferença entre os modos síncrono e assíncrono

---

## 📝 Relatório de Atividades

### Para Cada Atividade, Anote:

#### Atividade 1: Ciclo de Requisição-Resposta
- **Maior descoberta**: ________________________________
- **Dificuldade encontrada**: ___________________________
- **Conceito mais claro agora**: ________________________

#### Atividade 2: Síncrono vs Assíncrono
- **Diferença mais notável**: ____________________________
- **Impacto na experiência do usuário**: __________________
- **Aplicação prática**: _________________________________

#### Atividade 3: Sistema de Callbacks
- **Complexidade do Callback Hell**: _____________________
- **Alternativas pensadas**: ______________________________
- **Lição aprendida**: ___________________________________

#### Atividade 4: Python Comparativo
- **Speedup obtido**: ____________________________________
- **Situação ideal para cada abordagem**: __________________
- **Surpresa na implementação**: __________________________

### Reflexão Final
**O que você aplicaria em seus projetos futuros?**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Qual conceito precisa de mais estudo?**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 🎯 Objetivos de Aprendizagem Alcançados

Ao completar estas atividades, você deve ser capaz de:

- [ ] **Visualizar** o ciclo de requisição-resposta HTTP
- [ ] **Sentir** a diferença entre operações síncronas e assíncronas
- [ ] **Implementar** callbacks em JavaScript
- [ ] **Comparar** performance entre abordagens síncronas e assíncronas
- [ ] **Aplicar** conceitos em projetos práticos
- [ ] **Identificar** quando usar cada abordagem
- [ ] **Explicar** os trade-offs entre simplicidade e performance

---

**Parabéns por completar as atividades hands-on! 🎉**

Estes exercícios práticos complementam perfeitamente a teoria apresentada nos slides e preparam você para os exercícios mais avançados que virão a seguir.

