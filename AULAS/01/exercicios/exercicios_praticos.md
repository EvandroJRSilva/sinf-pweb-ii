# Exercícios Práticos - Programação Web Síncrona e Assíncrona

## 🎯 Objetivos de Aprendizagem

Ao completar estes exercícios, você será capaz de:
- Implementar requisições HTTP síncronas e assíncronas
- Comparar performance entre diferentes abordagens
- Utilizar callbacks, Promises e async/await
- Criar interfaces responsivas que não bloqueiam durante operações de rede
- Aplicar boas práticas de programação assíncrona

**Tempo estimado**: 90-120 minutos  
**Modalidade**: Individual ou em duplas  
**Pré-requisitos**: Conhecimentos básicos de JavaScript e Python

---

## 🌐 EXERCÍCIO 1: Comparando Requisições Síncronas e Assíncronas em JavaScript

### Objetivo
Criar uma página web que demonstre claramente a diferença entre requisições síncronas e assíncronas.

### Instruções

Crie um arquivo HTML chamado `comparacao_requisicoes.html` com as seguintes funcionalidades:

#### Parte A: Interface Base
1. Crie uma página com dois botões:
   - "Requisição Síncrona"
   - "Requisição Assíncrona"
2. Adicione um contador que incrementa a cada segundo
3. Inclua uma área para exibir os resultados das requisições

#### Parte B: Implementação Síncrona
```javascript
// Implemente uma função que faça uma requisição síncrona
// Use XMLHttpRequest com async = false
// API sugerida: https://jsonplaceholder.typicode.com/posts/1
```

#### Parte C: Implementação Assíncrona
```javascript
// Implemente uma função que faça uma requisição assíncrona
// Use fetch() com Promises ou async/await
// Use a mesma API da parte B
```

#### Parte D: Contador em Tempo Real
```javascript
// Implemente um contador que atualiza a cada segundo
// Deve mostrar claramente quando a interface está bloqueada
```

### Código Base para Começar

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparação: Síncrono vs Assíncrono</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        button { padding: 10px 20px; margin: 10px; font-size: 16px; }
        .counter { font-size: 24px; font-weight: bold; margin: 20px 0; }
        .result { background: #f0f0f0; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .sync { border-left: 5px solid #e74c3c; }
        .async { border-left: 5px solid #27ae60; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Comparação: Requisições Síncronas vs Assíncronas</h1>
        
        <div class="counter">
            Contador: <span id="contador">0</span>
        </div>
        
        <!-- SEU CÓDIGO AQUI -->
        
    </div>
    
    <script>
        // SEU JAVASCRIPT AQUI
    </script>
</body>
</html>
```

### Critérios de Avaliação
- [ ] Interface funcional com botões e contador
- [ ] Requisição síncrona implementada corretamente
- [ ] Requisição assíncrona implementada corretamente
- [ ] Contador demonstra claramente o bloqueio na versão síncrona
- [ ] Tratamento de erros implementado
- [ ] Código bem comentado

---

## 🐍 EXERCÍCIO 2: Sistema de Monitoramento de APIs em Python

### Objetivo
Criar um sistema que monitore múltiplas APIs e compare a performance entre abordagens síncronas e assíncronas.

### Instruções

Crie um arquivo Python chamado `monitor_apis.py` que:

#### Parte A: Configuração
```python
# Lista de APIs para monitorar
APIS = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/users/1',
    'https://jsonplaceholder.typicode.com/users/2'
]
```

#### Parte B: Implementação Síncrona
```python
def monitorar_apis_sincrono(apis):
    """
    Monitora as APIs de forma síncrona
    Retorna: lista de resultados e tempo total
    """
    # SEU CÓDIGO AQUI
    pass
```

#### Parte C: Implementação Assíncrona
```python
async def monitorar_apis_assincrono(apis):
    """
    Monitora as APIs de forma assíncrona
    Retorna: lista de resultados e tempo total
    """
    # SEU CÓDIGO AQUI
    pass
```

#### Parte D: Comparação e Relatório
```python
def gerar_relatorio(resultado_sincrono, resultado_assincrono):
    """
    Gera um relatório comparativo
    """
    # SEU CÓDIGO AQUI
    pass
```

### Código Base para Começar

```python
#!/usr/bin/env python3
import requests
import asyncio
import aiohttp
import time
from datetime import datetime

# Configuração
APIS = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/users/1',
    'https://jsonplaceholder.typicode.com/users/2'
]

def monitorar_apis_sincrono(apis):
    """Implementação síncrona"""
    # SEU CÓDIGO AQUI
    pass

async def monitorar_apis_assincrono(apis):
    """Implementação assíncrona"""
    # SEU CÓDIGO AQUI
    pass

def gerar_relatorio(resultado_sincrono, resultado_assincrono):
    """Gera relatório comparativo"""
    # SEU CÓDIGO AQUI
    pass

if __name__ == "__main__":
    print("🔍 Sistema de Monitoramento de APIs")
    print("=" * 50)
    
    # Execute suas implementações aqui
    # SEU CÓDIGO AQUI
```

### Critérios de Avaliação
- [ ] Implementação síncrona funcional
- [ ] Implementação assíncrona funcional
- [ ] Medição precisa de tempo de execução
- [ ] Tratamento de erros e timeouts
- [ ] Relatório comparativo informativo
- [ ] Código bem estruturado e comentado

---

## 🎮 EXERCÍCIO 3: Jogo de Reação - Interface Responsiva

### Objetivo
Criar um jogo simples que demonstre a importância de interfaces não-bloqueantes.

### Instruções

Crie um jogo onde o usuário deve clicar em botões que aparecem aleatoriamente. O jogo deve:

#### Funcionalidades Principais
1. **Botões aleatórios**: Aparecem em posições aleatórias na tela
2. **Pontuação**: Sistema de pontos baseado na velocidade de reação
3. **Requisições em background**: Enviar pontuação para uma API sem bloquear o jogo
4. **Comparação**: Modo com requisições síncronas vs assíncronas

#### Estrutura do Arquivo `jogo_reacao.html`

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogo de Reação</title>
    <style>
        /* SEU CSS AQUI */
    </style>
</head>
<body>
    <div class="game-container">
        <h1>Jogo de Reação</h1>
        
        <div class="controls">
            <button id="iniciar">Iniciar Jogo</button>
            <button id="modo-sincrono">Modo Síncrono</button>
            <button id="modo-assincrono">Modo Assíncrono</button>
        </div>
        
        <div class="info">
            <div>Pontos: <span id="pontos">0</span></div>
            <div>Tempo: <span id="tempo">0</span>s</div>
            <div>Modo: <span id="modo">Assíncrono</span></div>
        </div>
        
        <div class="game-area" id="game-area">
            <!-- Botões do jogo aparecerão aqui -->
        </div>
        
        <div class="log" id="log">
            <!-- Log de requisições -->
        </div>
    </div>
    
    <script>
        // SEU JAVASCRIPT AQUI
    </script>
</body>
</html>
```

### Funcionalidades a Implementar

#### 1. Sistema de Jogo Base
```javascript
class JogoReacao {
    constructor() {
        this.pontos = 0;
        this.tempo = 0;
        this.ativo = false;
        this.modoSincrono = false;
    }
    
    iniciar() {
        // Inicializa o jogo
    }
    
    criarBotaoAleatorio() {
        // Cria botão em posição aleatória
    }
    
    enviarPontuacao(pontos) {
        // Envia pontuação para API (síncrono ou assíncrono)
    }
}
```

#### 2. Requisições para API
```javascript
// Função síncrona (bloqueia o jogo)
function enviarPontuacaoSincrono(pontos) {
    // Use XMLHttpRequest com async = false
    // API: https://httpbin.org/delay/2 (simula delay)
}

// Função assíncrona (não bloqueia o jogo)
async function enviarPontuacaoAssincrono(pontos) {
    // Use fetch() com async/await
    // API: https://httpbin.org/delay/2 (simula delay)
}
```

### Critérios de Avaliação
- [ ] Jogo funcional com botões aleatórios
- [ ] Sistema de pontuação implementado
- [ ] Modo síncrono bloqueia visivelmente o jogo
- [ ] Modo assíncrono mantém o jogo fluido
- [ ] Interface clara mostrando a diferença entre modos
- [ ] Tratamento de erros nas requisições
- [ ] Design responsivo e atrativo

---

## 🔄 EXERCÍCIO 4: Sistema de Callbacks Avançado

### Objetivo
Implementar um sistema de processamento de dados que demonstre o uso de callbacks, Promises e async/await.

### Instruções

Crie um arquivo `processamento_dados.js` que simule um pipeline de processamento de dados:

#### Pipeline de Processamento
1. **Buscar dados** de uma API
2. **Validar dados** recebidos
3. **Transformar dados** (ex: converter para maiúsculas)
4. **Salvar dados** processados
5. **Enviar notificação** de conclusão

#### Implementação com Callbacks

```javascript
// Implementação usando callbacks (pode gerar callback hell)
function processarDadosComCallbacks(callback) {
    buscarDados((erro, dados) => {
        if (erro) return callback(erro);
        
        validarDados(dados, (erro, dadosValidos) => {
            if (erro) return callback(erro);
            
            transformarDados(dadosValidos, (erro, dadosTransformados) => {
                if (erro) return callback(erro);
                
                salvarDados(dadosTransformados, (erro, resultado) => {
                    if (erro) return callback(erro);
                    
                    enviarNotificacao(resultado, (erro, notificacao) => {
                        if (erro) return callback(erro);
                        
                        callback(null, notificacao);
                    });
                });
            });
        });
    });
}
```

#### Implementação com Promises

```javascript
// Implementação usando Promises (mais limpa)
function processarDadosComPromises() {
    return buscarDadosPromise()
        .then(dados => validarDadosPromise(dados))
        .then(dadosValidos => transformarDadosPromise(dadosValidos))
        .then(dadosTransformados => salvarDadosPromise(dadosTransformados))
        .then(resultado => enviarNotificacaoPromise(resultado))
        .catch(erro => {
            console.error('Erro no processamento:', erro);
            throw erro;
        });
}
```

#### Implementação com Async/Await

```javascript
// Implementação usando async/await (mais legível)
async function processarDadosComAsyncAwait() {
    try {
        const dados = await buscarDadosAsync();
        const dadosValidos = await validarDadosAsync(dados);
        const dadosTransformados = await transformarDadosAsync(dadosValidos);
        const resultado = await salvarDadosAsync(dadosTransformados);
        const notificacao = await enviarNotificacaoAsync(resultado);
        
        return notificacao;
    } catch (erro) {
        console.error('Erro no processamento:', erro);
        throw erro;
    }
}
```

### Código Base para Começar

```javascript
// Simulação de operações assíncronas
function buscarDados(callback) {
    setTimeout(() => {
        const dados = { id: 1, nome: 'joão silva', email: 'joao@email.com' };
        callback(null, dados);
    }, 1000);
}

function validarDados(dados, callback) {
    setTimeout(() => {
        if (!dados.nome || !dados.email) {
            return callback(new Error('Dados inválidos'));
        }
        callback(null, dados);
    }, 500);
}

// Implemente as outras funções...
// transformarDados, salvarDados, enviarNotificacao

// Versões Promise
function buscarDadosPromise() {
    return new Promise((resolve, reject) => {
        // SEU CÓDIGO AQUI
    });
}

// Versões Async (retornam Promises)
async function buscarDadosAsync() {
    // SEU CÓDIGO AQUI
}

// Função de teste
async function testarImplementacoes() {
    console.log('Testando implementações...');
    
    // Teste com callbacks
    console.log('\n1. Testando com callbacks:');
    // SEU CÓDIGO AQUI
    
    // Teste com Promises
    console.log('\n2. Testando com Promises:');
    // SEU CÓDIGO AQUI
    
    // Teste com async/await
    console.log('\n3. Testando com async/await:');
    // SEU CÓDIGO AQUI
}

testarImplementacoes();
```

### Critérios de Avaliação
- [ ] Implementação com callbacks funcional
- [ ] Implementação com Promises funcional
- [ ] Implementação com async/await funcional
- [ ] Tratamento de erros em todas as versões
- [ ] Comparação clara entre as abordagens
- [ ] Código bem comentado explicando as diferenças

---

## 🏆 EXERCÍCIO DESAFIO: Dashboard de Monitoramento em Tempo Real

### Objetivo
Criar um dashboard completo que monitore múltiplas APIs e exiba informações em tempo real, demonstrando todos os conceitos aprendidos.

### Funcionalidades Principais

1. **Monitoramento de APIs**: Verificar status de múltiplas APIs
2. **Atualizações em tempo real**: Atualizar dados sem bloquear a interface
3. **Gráficos de performance**: Mostrar tempo de resposta ao longo do tempo
4. **Alertas**: Notificar quando uma API estiver fora do ar
5. **Comparação de métodos**: Permitir alternar entre síncrono e assíncrono

### Estrutura de Arquivos

```
dashboard/
├── index.html
├── css/
│   └── style.css
├── js/
│   ├── dashboard.js
│   ├── api-monitor.js
│   └── charts.js
└── README.md
```

### Especificações Técnicas

#### APIs para Monitorar
```javascript
const APIS = [
    { nome: 'JSONPlaceholder', url: 'https://jsonplaceholder.typicode.com/posts/1' },
    { nome: 'HTTPBin', url: 'https://httpbin.org/get' },
    { nome: 'ReqRes', url: 'https://reqres.in/api/users/1' },
    // Adicione mais APIs conforme necessário
];
```

#### Funcionalidades Obrigatórias

1. **Status Cards**: Cards mostrando status de cada API
2. **Gráfico de Tempo de Resposta**: Linha temporal com tempos de resposta
3. **Log de Eventos**: Lista de eventos com timestamps
4. **Controles**: Botões para iniciar/parar monitoramento
5. **Modo de Operação**: Toggle entre síncrono/assíncrono

#### Tecnologias Sugeridas
- **HTML/CSS/JavaScript** (vanilla ou com bibliotecas)
- **Chart.js** para gráficos
- **Fetch API** para requisições
- **WebSockets** (opcional, para atualizações em tempo real)

### Critérios de Avaliação Final
- [ ] Interface profissional e responsiva
- [ ] Monitoramento funcional de múltiplas APIs
- [ ] Gráficos atualizando em tempo real
- [ ] Diferença clara entre modos síncrono/assíncrono
- [ ] Tratamento robusto de erros
- [ ] Código bem estruturado e documentado
- [ ] Performance otimizada
- [ ] Funcionalidades extras criativas

---

## 📚 Recursos de Apoio

### APIs Públicas para Teste
- **JSONPlaceholder**: https://jsonplaceholder.typicode.com/
- **HTTPBin**: https://httpbin.org/
- **ReqRes**: https://reqres.in/
- **Random User**: https://randomuser.me/api/

### Bibliotecas Úteis
- **Chart.js**: Para gráficos
- **Axios**: Cliente HTTP alternativo ao fetch
- **Lodash**: Utilitários JavaScript
- **Moment.js**: Manipulação de datas

### Documentação Recomendada
- [MDN - Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN - Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [aiohttp Documentation](https://docs.aiohttp.org/)

---

## ✅ Entrega dos Exercícios

### Formato de Entrega
1. **Código fonte** de todos os exercícios
2. **Screenshots** das aplicações funcionando
3. **Relatório** comparando performance (Exercício 2)
4. **README** explicando como executar cada exercício

### Prazo
- **Exercícios 1-3**: 1 semana após a aula
- **Exercício Desafio**: 2 semanas após a aula

### Critérios de Avaliação Geral
- **Funcionalidade** (40%): O código funciona conforme especificado
- **Qualidade** (30%): Código limpo, bem estruturado e comentado
- **Criatividade** (20%): Soluções criativas e funcionalidades extras
- **Documentação** (10%): README claro e explicações adequadas

---

**Boa sorte com os exercícios práticos! 💪**

