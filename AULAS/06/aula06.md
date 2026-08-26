<style>
  h1{font-size: 2.5em;}
  h2{font-size: 2.25em;}
  h3{font-size: 2em;}
  h4{font-size: 1.75em;}
  h5{font-size: 1.5em;}
  h6{font-size: 1.25em;}
</style>

# Aula 06

**Sumário**

- [Aula 06](#aula-06)
- [RFC 9110: STD 97: HTTP Semantics](#rfc-9110-std-97-http-semantics)
  - [Identifiers in HTTP](#identifiers-in-http)
    - [RFC 3986](#rfc-3986)
      - [Esquema](#esquema)
      - [Autoridade](#autoridade)
      - [Caminho](#caminho)
      - [Consulta](#consulta)
      - [Fragmento](#fragmento)
      - [Uso do URI](#uso-do-uri)
        - [Referência URI](#referência-uri)
        - [Referência relativa](#referência-relativa)
        - [URI Absoluto](#uri-absoluto)
        - [Referência no mesmo documento](#referência-no-mesmo-documento)
        - [Referência de sufixo (*Suffix Reference*)](#referência-de-sufixo-suffix-reference)
      - [FUTURAMENTE](#futuramente)
    - [URI x URL x URN](#uri-x-url-x-urn)
  - [Trabalho da semana](#trabalho-da-semana)


# [RFC 9110: STD 97: HTTP Semantics](www.rfc-editor.org/info/rfc9110/#section-4)

## [Identifiers in HTTP](https://www.rfc-editor.org/info/rfc9110/#section-4)

A quarta seção fala sobre as referências URI.

### [RFC 3986](https://www.rfc-editor.org/info/rfc3986/)

É o RFC que define a sintaxe genéria do URI (*Uniform Resource Identifier*). Padrões para a especificação da subestrutura do URI são fornecidos no [RFC 8820](https://www.rfc-editor.org/info/rfc8820/).

Essa sintaxe consiste de uma sequência hierárquica de componentes referidos como **esquema** (*scheme*), **autoridade** (*authority*), **caminho** (*path*), **consulta** (*query*) e **fragmento** (*fragment*):

```
URI         = scheme ":" hier-part ["?" query] ["#" fragment]

hier-part   = "//" authority path-abempty*
            / path-absolute
            / path-rootless
            / path-empty
```

> \* = **ab**[solute or]**empty**

O **esquema** e os componentes de **caminho** são exigidos, mas o **caminho** pode estar vazio (sem caracteres). Quando a **autoridade** está presente, o **caminho** precisa estar vazio ou começar com `/`. Quando a **autoridade** não está presente, o **caminho** não pode começar com `//`. Essas restrições resultam em 5 diferentes regras para um **caminho**, as quais podem ser consultadas no RFC.

Exemplo:

```
  foo://example.com:8042/over/there?name=ferret#nose
  \_/   \______________/\_________/ \_________/ \__/
   |           |            |            |        |
scheme     authority       path        query   fragment
   |   _____________________|__
  / \ /                        \
  urn:example:animal:ferret:nose
```

#### Esquema

Cada URI começa com o nome de um esquema que se refere a uma especificação para a atribuição de identificadores dentro desse esquema. Dessa forma, a sintaxe URI é um sistema de nomenclatura federado e extensível, no qual a especificação de cada esquema pode restringir ainda mais a sintaxe e a semântica dos identificadores que utilizam esse esquema.

```
scheme = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
```

Canonicamente, os nomes dos esquemas devem estar sempre escritos em minúsculo.

[Lista de esquemas](https://www.iana.org/assignments/uri-schemes) mantido pela IANA.

#### Autoridade

Esse componente é precedido por uma barra dupla `//` e é encerrado pela próxima barra `/`, ponto de interrogração `?`, cerquilha `#`, ou o fim do URI.

```
authority = [ userinfo "@" ] host [ ":" port ]
```

- O subcomponente `userinfo` pode consistir em um nome de usuário e, opcionalmente, informações específicas do esquema sobre como obter autorização para acessar o recurso.
- O subcomponente `host` é identificado por um IP literal encapsulado dentro de colchetes, endereço IP ou um nome registrado (DNS).
- O subcomponente `port` consiste em um número decimal. Um esquema pode definir uma porta padrão, por exemplo o esquema "http" define a porta padrão 80.

#### Caminho

Esse componente contém dados geralmente organizados de forma hierárquica, seguidos de dados de consulta não-hieráquicos. Serve para identificar um recurso dentro do escopo de um esquema de URI e autoridade de nomeação. O caminho é encerrado pelo primeiro ponto de interrogaçãp `?`, cerquilha `#`, ou pelo fim do URI.

Um caminho consiste em uma sequência de segmentos de caminho separados por uma barra `/`.

Os segmentos de caminho `.` e `..`, também conhecidos como *dot-segments* (segmentos de ponto), são definidos para referência relativa dentro da hierarquia de nome do caminho. Eles são destinados ao uso no início de uma referência de caminho relativo.

#### Consulta

Esse componente contém dados não-hieráquicos, os quais, junto com os dados no componente de caminho, servem para identificar um recurso dentro do escopo de um esquema de URI e autoridade de nomeação.

É indicado pelo caractere `?` e encerrado com `#`.

#### Fragmento

Esse componente permite identificação indireta de um recurso secundário por referência ao recurso primário e informações de identificação adicionais.

É indicado pela presença do caractere `#`.

#### Uso do URI

Para economizar espaço e aproveitar da localidade hierárquica, muitos elementos de protocolo e formatos de tipo de mídia da Internet permitem abreviações a um URI, enquanto outros restringem a sintaxe para uma forma particular de URI.

Nesse RFC são definidas as formas mais comuns de referência de sintaxe.

##### Referência URI

É usado para denotar o uso mais comum de um identificador de recurso.

```
URI-reference = URI / ref-relativa
```

Um URI-reference pode ser tanto um URI quanto uma referência relativa. Normalmente, uma referência URI é analisada primeiro e decomposta nos cinco componentes de URIs, para determinar quais componentes estão presentes e se a referência é relativa.

##### Referência relativa

Aproveita a vantagem da sintaxe hierárquica para expressar uma referência de URI relativa ao espaço de nome de outra URI hierárquica.

```
relative-ref  = relative-part [ "?" query ] [ "#" fragment ]

relative-part = "//" authority path-abempty
              / path-absolute
              / path-noscheme
              / path-empty
```

O URI referenciado por uma referência relativa, também conhecido como URI de destino (*target URI*), é obtido aplicando-se o algoritmo de resolução de referência.

- Uma referência relativa que inicia com `//` é denominada referência de caminho de rede (*network-path reference*);
- Uma referência relativa que inicia com `/` é denominada referência de caminho absoluto (*absolute-path reference*);
- Uma referência relativa que não inicia com uma barra é denominada referência de caminho relativo (*relative-path reference*).

##### URI Absoluto

Alguns elementos de protocolo permitem apenas a forma absoluta de um URI sem um identificador de fragmento.

```
absolute-URI = scheme ":" hier-part [ "?" query ]
```

##### Referência no mesmo documento

Quando uma referência URI se refere a um URI que é idêntido ao URI básico, exceto pelo componente de fragmento, essa referência é chamada de "*same-document reference*".

Essas referências iniciam com `#`. Exemplo: sumário deste arquivo.

##### Referência de sufixo (*Suffix Reference*)

Consiste nas referências que possuem somente os componentes de autoridade e partes do caminho. Por exemplo: "www.w3.org/Addressing/". E ainda: "ufpi.br".

#### FUTURAMENTE

- [Resolução de Referência](https://www.rfc-editor.org/info/rfc3986/#section-5)
- [Normalização e Comparação](https://www.rfc-editor.org/info/rfc3986/#section-6)

### URI x URL x URN

O URI serve como o conjunto maior que engloba tanto URL quanto URN. Por si só, ele somente fornece identificação. O acesso ao recurso não é garantido nem implícito pela presença de um URI. Exemplos de URIs:

```
ftp://ftp.is.co.za/rfc/rfc1808.txt

http://www.ietf.org/rfc/rfc2396.txt

ldap://[2001:db8::7]/c=GB?objectClass?one

mailto:John.Doe@example.com

news:comp.infosystems.www.servers.unix

tel:+1-816-555-1212

telnet://192.0.2.16:80/

urn:oasis:names:specification:docbook:dtd:xml:4.1.2
```

O URL (*Uniform Resource Locator*) é um **subconjunto** do URI, e consiste em um localizador de recursos na web.

O URN (*Uniform Resource Names*) - [RFC 81410](https://www.rfc-editor.org/info/rfc8141/) é **outro subconjunto** do URI, que nomeia um recurso de forma única e persistente (para sempre).

```
  ┌────────────────────────────────────────┐
  │                   URI                  │
  │     (Uniform Resource Identifier)      │
  │                                        │
  │   ┌────────────────┐  ┌────────────┐   │
  │   │      URL       │  │    URN     │   │
  │   │  (Localiza)    │  │  (Nomeia)  │   │
  │   └────────────────┘  └────────────┘   │
  └────────────────────────────────────────┘
```

## Trabalho da semana

Cada dupla deverá criar um documento fazendo a comparação entre o RFC 3986 e a Seção 4 do RFC 9110. Em outras palavras, as duplas devem mostrar como os esquemas **http** e **https** foram definidos à luz do RFC 3986, ou seja, quais conceitos e regras foram definidos (com os detalhes das definições - seção 4) e/ou descontinuados.