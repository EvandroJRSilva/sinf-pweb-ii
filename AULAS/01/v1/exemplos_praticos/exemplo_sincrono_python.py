#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo Prático: Requisição Síncrona em Python

Este exemplo demonstra como fazer requisições HTTP síncronas usando a biblioteca requests.
Em requisições síncronas, o programa espera (bloqueia) até receber a resposta do servidor
antes de continuar a execução.

Autor: Material Didático - Arquitetura da Web
"""

import requests
import time
from datetime import datetime


def exemplo_requisicao_sincrona():
    """
    Demonstra uma requisição HTTP síncrona simples.
    O programa bloqueia até receber a resposta.
    """
    print("=" * 60)
    print("EXEMPLO 1: Requisição Síncrona Simples")
    print("=" * 60)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando requisição síncrona...")
    
    try:
        # Esta linha BLOQUEIA a execução até receber resposta
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Fazendo requisição para JSONPlaceholder...")
        resposta = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Resposta recebida!")
        
        if resposta.status_code == 200:
            dados = resposta.json()
            print(f"✅ Sucesso! Status: {resposta.status_code}")
            print(f"📄 Título: {dados['title']}")
            print(f"📝 Conteúdo: {dados['body'][:100]}...")
            print(f"👤 User ID: {dados['userId']}")
        else:
            print(f"❌ Erro! Status: {resposta.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Requisição concluída.\n")


def exemplo_multiplas_requisicoes_sincronas():
    """
    Demonstra o problema de fazer múltiplas requisições síncronas.
    Cada requisição espera a anterior terminar antes de começar.
    """
    print("=" * 60)
    print("EXEMPLO 2: Múltiplas Requisições Síncronas (Sequenciais)")
    print("=" * 60)
    
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    
    inicio = time.time()
    resultados = []
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando {len(urls)} requisições síncronas...")
    
    for i, url in enumerate(urls, 1):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Requisição {i}...")
        
        try:
            # Cada requisição bloqueia até terminar
            resposta = requests.get(url)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                resultados.append({
                    'id': dados['id'],
                    'titulo': dados['title'][:50] + '...'
                })
                print(f"  ✅ Requisição {i} concluída")
            else:
                print(f"  ❌ Requisição {i} falhou: {resposta.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"  ❌ Erro na requisição {i}: {e}")
    
    fim = time.time()
    tempo_total = fim - inicio
    
    print(f"\n📊 Resultados:")
    for resultado in resultados:
        print(f"  • Post {resultado['id']}: {resultado['titulo']}")
    
    print(f"\n⏱️  Tempo total: {tempo_total:.2f} segundos")
    print(f"📝 Observação: As requisições foram executadas sequencialmente (uma após a outra)")
    print()


def exemplo_com_timeout():
    """
    Demonstra como usar timeout em requisições síncronas.
    """
    print("=" * 60)
    print("EXEMPLO 3: Requisição Síncrona com Timeout")
    print("=" * 60)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fazendo requisição com timeout de 5 segundos...")
    
    try:
        # Timeout de 5 segundos - se demorar mais, levanta exceção
        resposta = requests.get(
            'https://jsonplaceholder.typicode.com/posts/1',
            timeout=5  # timeout em segundos
        )
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Resposta recebida dentro do timeout!")
        print(f"✅ Status: {resposta.status_code}")
        print(f"⏱️  Tempo de resposta: {resposta.elapsed.total_seconds():.2f} segundos")
        
    except requests.exceptions.Timeout:
        print("❌ Timeout! A requisição demorou mais de 5 segundos.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    
    print()


def exemplo_com_headers_personalizados():
    """
    Demonstra como enviar headers personalizados em requisições síncronas.
    """
    print("=" * 60)
    print("EXEMPLO 4: Requisição Síncrona com Headers Personalizados")
    print("=" * 60)
    
    headers = {
        'User-Agent': 'Exemplo-Python-Sincrono/1.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Enviando requisição com headers personalizados...")
    print("📋 Headers enviados:")
    for chave, valor in headers.items():
        print(f"  • {chave}: {valor}")
    
    try:
        resposta = requests.get(
            'https://jsonplaceholder.typicode.com/posts/1',
            headers=headers
        )
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Resposta recebida!")
        print(f"✅ Status: {resposta.status_code}")
        
        # Mostra alguns headers da resposta
        print("📋 Alguns headers da resposta:")
        headers_interessantes = ['content-type', 'server', 'date']
        for header in headers_interessantes:
            if header in resposta.headers:
                print(f"  • {header}: {resposta.headers[header]}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    
    print()


def demonstrar_bloqueio():
    """
    Demonstra como as requisições síncronas bloqueiam a execução.
    """
    print("=" * 60)
    print("EXEMPLO 5: Demonstração do Bloqueio")
    print("=" * 60)
    
    print("🔄 Este exemplo mostra como o programa fica 'parado' durante requisições síncronas.")
    print("   Observe que não há nenhuma saída entre o início e o fim de cada requisição.\n")
    
    for i in range(3):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando requisição {i+1}...")
        
        # Durante esta linha, o programa fica completamente bloqueado
        resposta = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Requisição {i+1} concluída (Status: {resposta.status_code})")
        print("  ⏸️  O programa ficou bloqueado durante toda a requisição!")
        print()
    
    print("📝 Observação: Em aplicações reais, isso significa que:")
    print("   • A interface do usuário ficaria 'travada'")
    print("   • Outras operações não poderiam ser executadas")
    print("   • A experiência do usuário seria prejudicada")
    print()


def main():
    """
    Função principal que executa todos os exemplos.
    """
    print("🌐 EXEMPLOS DE REQUISIÇÕES SÍNCRONAS EM PYTHON")
    print("=" * 60)
    print("Este script demonstra como funcionam as requisições HTTP síncronas")
    print("usando a biblioteca 'requests' do Python.")
    print("=" * 60)
    print()
    
    # Executa todos os exemplos
    exemplo_requisicao_sincrona()
    exemplo_multiplas_requisicoes_sincronas()
    exemplo_com_timeout()
    exemplo_com_headers_personalizados()
    demonstrar_bloqueio()
    
    print("=" * 60)
    print("🎓 RESUMO DOS CONCEITOS APRENDIDOS:")
    print("=" * 60)
    print("✅ Requisições síncronas bloqueiam a execução do programa")
    print("✅ São mais simples de implementar e entender")
    print("✅ Adequadas para scripts simples e operações sequenciais")
    print("❌ Podem tornar aplicações lentas e não responsivas")
    print("❌ Não aproveitam bem recursos computacionais")
    print("❌ Inadequadas para interfaces de usuário")
    print()
    print("💡 PRÓXIMO PASSO: Aprenda sobre requisições assíncronas!")
    print("   • Use asyncio + aiohttp para requisições não-bloqueantes")
    print("   • Melhore a performance com operações paralelas")
    print("   • Crie aplicações mais responsivas")
    print("=" * 60)


if __name__ == "__main__":
    main()

