#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo Prático: Requisições Assíncronas em Python

Este exemplo demonstra como fazer requisições HTTP assíncronas usando asyncio e aiohttp.
Em requisições assíncronas, o programa pode continuar executando outras tarefas
enquanto espera as respostas dos servidores.

Dependências necessárias:
    pip install aiohttp

Autor: Material Didático - Arquitetura da Web
"""

import asyncio
import aiohttp
import time
from datetime import datetime


async def exemplo_requisicao_assincrona():
    """
    Demonstra uma requisição HTTP assíncrona simples.
    O programa não bloqueia enquanto espera a resposta.
    """
    print("=" * 60)
    print("EXEMPLO 1: Requisição Assíncrona Simples")
    print("=" * 60)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando requisição assíncrona...")
    
    async with aiohttp.ClientSession() as session:
        try:
            # Esta linha NÃO bloqueia outras operações
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Fazendo requisição para JSONPlaceholder...")
            
            async with session.get('https://jsonplaceholder.typicode.com/posts/1') as resposta:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Resposta recebida!")
                
                if resposta.status == 200:
                    dados = await resposta.json()
                    print(f"✅ Sucesso! Status: {resposta.status}")
                    print(f"📄 Título: {dados['title']}")
                    print(f"📝 Conteúdo: {dados['body'][:100]}...")
                    print(f"👤 User ID: {dados['userId']}")
                else:
                    print(f"❌ Erro! Status: {resposta.status}")
                    
        except aiohttp.ClientError as e:
            print(f"❌ Erro na requisição: {e}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Requisição concluída.\n")


async def buscar_post(session, post_id):
    """
    Função auxiliar para buscar um post específico.
    """
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    
    try:
        async with session.get(url) as resposta:
            if resposta.status == 200:
                dados = await resposta.json()
                return {
                    'id': dados['id'],
                    'titulo': dados['title'][:50] + '...',
                    'sucesso': True
                }
            else:
                return {
                    'id': post_id,
                    'erro': f'Status {resposta.status}',
                    'sucesso': False
                }
    except aiohttp.ClientError as e:
        return {
            'id': post_id,
            'erro': str(e),
            'sucesso': False
        }


async def exemplo_multiplas_requisicoes_assincronas():
    """
    Demonstra múltiplas requisições assíncronas executadas em paralelo.
    Todas as requisições são iniciadas simultaneamente.
    """
    print("=" * 60)
    print("EXEMPLO 2: Múltiplas Requisições Assíncronas (Paralelas)")
    print("=" * 60)
    
    post_ids = [1, 2, 3, 4, 5]
    
    inicio = time.time()
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando {len(post_ids)} requisições assíncronas em paralelo...")
    
    async with aiohttp.ClientSession() as session:
        # Cria todas as tarefas assíncronas
        tarefas = [buscar_post(session, post_id) for post_id in post_ids]
        
        # Executa todas as tarefas em paralelo
        resultados = await asyncio.gather(*tarefas)
    
    fim = time.time()
    tempo_total = fim - inicio
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Todas as requisições concluídas!")
    
    print(f"\n📊 Resultados:")
    for resultado in resultados:
        if resultado['sucesso']:
            print(f"  ✅ Post {resultado['id']}: {resultado['titulo']}")
        else:
            print(f"  ❌ Post {resultado['id']}: {resultado['erro']}")
    
    print(f"\n⏱️  Tempo total: {tempo_total:.2f} segundos")
    print(f"📝 Observação: As requisições foram executadas em PARALELO!")
    print(f"   Se fossem síncronas, levariam aproximadamente {len(post_ids)} vezes mais tempo.")
    print()


async def exemplo_com_timeout():
    """
    Demonstra como usar timeout em requisições assíncronas.
    """
    print("=" * 60)
    print("EXEMPLO 3: Requisição Assíncrona com Timeout")
    print("=" * 60)
    
    timeout = aiohttp.ClientTimeout(total=5)  # 5 segundos
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fazendo requisição com timeout de 5 segundos...")
    
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.get('https://jsonplaceholder.typicode.com/posts/1') as resposta:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Resposta recebida dentro do timeout!")
                print(f"✅ Status: {resposta.status}")
                
                dados = await resposta.json()
                print(f"📄 Título: {dados['title']}")
                
        except asyncio.TimeoutError:
            print("❌ Timeout! A requisição demorou mais de 5 segundos.")
        except aiohttp.ClientError as e:
            print(f"❌ Erro na requisição: {e}")
    
    print()


async def exemplo_com_headers_personalizados():
    """
    Demonstra como enviar headers personalizados em requisições assíncronas.
    """
    print("=" * 60)
    print("EXEMPLO 4: Requisição Assíncrona com Headers Personalizados")
    print("=" * 60)
    
    headers = {
        'User-Agent': 'Exemplo-Python-Assincrono/1.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Enviando requisição com headers personalizados...")
    print("📋 Headers enviados:")
    for chave, valor in headers.items():
        print(f"  • {chave}: {valor}")
    
    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get('https://jsonplaceholder.typicode.com/posts/1') as resposta:
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Resposta recebida!")
                print(f"✅ Status: {resposta.status}")
                
                # Mostra alguns headers da resposta
                print("📋 Alguns headers da resposta:")
                headers_interessantes = ['content-type', 'server', 'date']
                for header in headers_interessantes:
                    if header in resposta.headers:
                        print(f"  • {header}: {resposta.headers[header]}")
                
        except aiohttp.ClientError as e:
            print(f"❌ Erro na requisição: {e}")
    
    print()


async def tarefa_em_background():
    """
    Simula uma tarefa que executa em background enquanto as requisições acontecem.
    """
    for i in range(10):
        print(f"  🔄 Tarefa em background executando... ({i+1}/10)")
        await asyncio.sleep(0.5)  # Simula trabalho
    print("  ✅ Tarefa em background concluída!")


async def exemplo_nao_bloqueante():
    """
    Demonstra como operações assíncronas não bloqueiam outras tarefas.
    """
    print("=" * 60)
    print("EXEMPLO 5: Demonstração de Operação Não-Bloqueante")
    print("=" * 60)
    
    print("🔄 Este exemplo mostra como operações assíncronas permitem que outras")
    print("   tarefas sejam executadas simultaneamente.\n")
    
    async with aiohttp.ClientSession() as session:
        # Inicia a requisição e a tarefa em background simultaneamente
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando requisição e tarefa em paralelo...")
        
        tarefa_requisicao = buscar_post(session, 1)
        tarefa_background = tarefa_em_background()
        
        # Executa ambas as tarefas em paralelo
        resultado_requisicao, _ = await asyncio.gather(tarefa_requisicao, tarefa_background)
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Ambas as tarefas concluídas!")
        
        if resultado_requisicao['sucesso']:
            print(f"📄 Post obtido: {resultado_requisicao['titulo']}")
        
    print("\n📝 Observação: A requisição e a tarefa em background executaram")
    print("   simultaneamente, demonstrando que operações assíncronas não bloqueiam!")
    print()


async def comparacao_performance():
    """
    Compara a performance entre requisições síncronas simuladas e assíncronas reais.
    """
    print("=" * 60)
    print("EXEMPLO 6: Comparação de Performance")
    print("=" * 60)
    
    post_ids = [1, 2, 3, 4, 5]
    
    # Simulação de requisições síncronas (sequenciais)
    print("🐌 Simulando requisições síncronas (sequenciais)...")
    inicio_sincrono = time.time()
    
    async with aiohttp.ClientSession() as session:
        for post_id in post_ids:
            resultado = await buscar_post(session, post_id)
            print(f"  • Post {post_id} processado")
    
    fim_sincrono = time.time()
    tempo_sincrono = fim_sincrono - inicio_sincrono
    
    # Requisições assíncronas (paralelas)
    print("\n🚀 Executando requisições assíncronas (paralelas)...")
    inicio_assincrono = time.time()
    
    async with aiohttp.ClientSession() as session:
        tarefas = [buscar_post(session, post_id) for post_id in post_ids]
        resultados = await asyncio.gather(*tarefas)
        
        for resultado in resultados:
            print(f"  • Post {resultado['id']} processado")
    
    fim_assincrono = time.time()
    tempo_assincrono = fim_assincrono - inicio_assincrono
    
    # Comparação
    print(f"\n📊 COMPARAÇÃO DE PERFORMANCE:")
    print(f"⏱️  Tempo síncrono (simulado):  {tempo_sincrono:.2f} segundos")
    print(f"⏱️  Tempo assíncrono:          {tempo_assincrono:.2f} segundos")
    print(f"🚀 Speedup: {tempo_sincrono/tempo_assincrono:.2f}x mais rápido!")
    print()


async def main():
    """
    Função principal que executa todos os exemplos assíncronos.
    """
    print("🌐 EXEMPLOS DE REQUISIÇÕES ASSÍNCRONAS EM PYTHON")
    print("=" * 60)
    print("Este script demonstra como funcionam as requisições HTTP assíncronas")
    print("usando asyncio e aiohttp do Python.")
    print("=" * 60)
    print()
    
    # Executa todos os exemplos
    await exemplo_requisicao_assincrona()
    await exemplo_multiplas_requisicoes_assincronas()
    await exemplo_com_timeout()
    await exemplo_com_headers_personalizados()
    await exemplo_nao_bloqueante()
    await comparacao_performance()
    
    print("=" * 60)
    print("🎓 RESUMO DOS CONCEITOS APRENDIDOS:")
    print("=" * 60)
    print("✅ Requisições assíncronas NÃO bloqueiam a execução do programa")
    print("✅ Permitem execução paralela de múltiplas operações")
    print("✅ Melhoram significativamente a performance")
    print("✅ Ideais para aplicações que fazem muitas requisições")
    print("✅ Mantêm interfaces de usuário responsivas")
    print("❌ Mais complexas de implementar que requisições síncronas")
    print("❌ Requerem compreensão de conceitos de programação assíncrona")
    print()
    print("💡 CONCEITOS IMPORTANTES:")
    print("   • async/await: Sintaxe para programação assíncrona")
    print("   • asyncio.gather(): Executa múltiplas tarefas em paralelo")
    print("   • ClientSession: Gerencia conexões HTTP de forma eficiente")
    print("   • Timeouts: Evitam que operações travem indefinidamente")
    print("=" * 60)


if __name__ == "__main__":
    # Verifica se aiohttp está instalado
    try:
        import aiohttp
    except ImportError:
        print("❌ Erro: A biblioteca 'aiohttp' não está instalada.")
        print("💡 Para instalar, execute: pip install aiohttp")
        exit(1)
    
    # Executa o programa principal
    asyncio.run(main())

