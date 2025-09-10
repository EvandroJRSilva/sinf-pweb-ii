# Exemplos Práticos - Arquitetura da Web

Este diretório contém exemplos práticos que complementam a apresentação sobre **Arquitetura da Web e Comunicação Síncrona/Assíncrona**.

## 📁 Estrutura dos Arquivos

### Exemplos em JavaScript
- **`exemplo_sincrono_js.html`** - Demonstra requisições síncronas em JavaScript (XMLHttpRequest)
- **`exemplo_assincrono_js.html`** - Demonstra requisições assíncronas em JavaScript (fetch, Promises)
- **`exemplo_callbacks_js.html`** - Explora o conceito de callbacks com exemplos interativos

### Exemplos em Python
- **`exemplo_sincrono_python.py`** - Demonstra requisições síncronas em Python (requests)
- **`exemplo_assincrono_python.py`** - Demonstra requisições assíncronas em Python (asyncio + aiohttp)

## 🚀 Como Executar os Exemplos

### Exemplos JavaScript
1. Abra os arquivos `.html` diretamente no navegador
2. Clique nos botões para executar os exemplos
3. Observe o comportamento da interface durante as requisições

### Exemplos Python

#### Requisições Síncronas
```bash
# Não requer instalação adicional (usa requests, que geralmente já vem instalado)
python3 exemplo_sincrono_python.py
```

#### Requisições Assíncronas
```bash
# Instale a dependência necessária
pip install aiohttp

# Execute o exemplo
python3 exemplo_assincrono_python.py
```

## 📚 Conceitos Demonstrados

### 1. Comunicação Síncrona
- **Bloqueio da execução** durante requisições
- **Execução sequencial** de múltiplas operações
- **Simplicidade** de implementação
- **Problemas de performance** e experiência do usuário

### 2. Comunicação Assíncrona
- **Execução não-bloqueante** de requisições
- **Paralelização** de múltiplas operações
- **Melhor performance** e responsividade
- **Complexidade adicional** na implementação

### 3. Callbacks
- **Funções como parâmetros** para outras funções
- **Execução condicional** baseada em eventos
- **Callback Hell** e seus problemas
- **Evolução para Promises** e async/await

## 🎯 Objetivos de Aprendizagem

Após executar estes exemplos, você deve ser capaz de:

1. **Identificar** a diferença entre operações síncronas e assíncronas
2. **Explicar** por que requisições síncronas podem prejudicar a experiência do usuário
3. **Implementar** requisições assíncronas em JavaScript e Python
4. **Utilizar** callbacks para lidar com operações assíncronas
5. **Comparar** a performance entre abordagens síncronas e assíncronas

## 🔍 Detalhes dos Exemplos

### JavaScript - Requisições Síncronas
- Usa `XMLHttpRequest` com terceiro parâmetro `false`
- Demonstra como a interface fica "travada"
- Mostra o impacto negativo na experiência do usuário
- **⚠️ Importante**: Não use em produção!

### JavaScript - Requisições Assíncronas
- Usa `fetch()` API moderna
- Demonstra Promises e async/await
- Interface permanece responsiva
- Múltiplas requisições em paralelo

### JavaScript - Callbacks
- Callbacks simples e com operações assíncronas
- Demonstra o problema do "Callback Hell"
- Mostra a evolução para Promises
- Exemplos interativos no navegador

### Python - Requisições Síncronas
- Usa biblioteca `requests` padrão
- Demonstra bloqueio da execução
- Múltiplas requisições sequenciais
- Medição de tempo de execução

### Python - Requisições Assíncronas
- Usa `asyncio` e `aiohttp`
- Demonstra execução paralela
- Comparação de performance
- Tarefas em background simultâneas

## 📊 Comparação de Performance

Os exemplos incluem medições de tempo que demonstram:

- **Requisições Síncronas**: Tempo total = soma de todas as requisições
- **Requisições Assíncronas**: Tempo total ≈ tempo da requisição mais lenta
- **Speedup típico**: 3-5x mais rápido para múltiplas requisições

## 🛠️ Tecnologias Utilizadas

### JavaScript
- **XMLHttpRequest**: API mais antiga para requisições HTTP
- **Fetch API**: API moderna para requisições HTTP
- **Promises**: Padrão para lidar com operações assíncronas
- **Async/Await**: Sintaxe moderna para código assíncrono

### Python
- **requests**: Biblioteca popular para requisições HTTP síncronas
- **asyncio**: Biblioteca padrão para programação assíncrona
- **aiohttp**: Biblioteca para requisições HTTP assíncronas

## 🎓 Exercícios Sugeridos

1. **Modifique** os exemplos para usar diferentes APIs públicas
2. **Implemente** tratamento de erro mais robusto
3. **Crie** uma versão que compare tempos de execução
4. **Experimente** com diferentes números de requisições simultâneas
5. **Adicione** indicadores visuais de progresso

## 📖 Recursos Adicionais

- [MDN - Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [aiohttp Documentation](https://docs.aiohttp.org/)
- [JavaScript Promises Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)

## ❓ Dúvidas Frequentes

**Q: Por que não devo usar requisições síncronas em JavaScript?**
A: Elas bloqueiam a thread principal do navegador, tornando a interface não responsiva.

**Q: Quando usar requisições síncronas em Python?**
A: Em scripts simples, ferramentas de linha de comando, ou quando a simplicidade é mais importante que a performance.

**Q: O que é "Callback Hell"?**
A: É quando você tem muitos callbacks aninhados, tornando o código difícil de ler e manter.

**Q: Async/await substitui completamente os callbacks?**
A: Não completamente, mas oferece uma sintaxe mais limpa para a maioria dos casos de uso.

---

**💡 Dica**: Execute os exemplos lado a lado para ver claramente a diferença entre abordagens síncronas e assíncronas!

