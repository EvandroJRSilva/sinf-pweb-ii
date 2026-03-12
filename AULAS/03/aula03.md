# Aula 03

## Arquitetura de Software

A **Arquitetura de Software** é uma estrutura de alto nível de um sistema de software, a qual inclui um conjunto de regras, padrões e diretrizes para a organização, interações e relações entre os componentes do software. Ela serve como um projeto para garantir que o sistema alcançe seus requisitos e que seja sustentável e escalável.

Um **Padrão de Arquitetura** é um modelo de arquitetura que serve como uma solução comprovada e reutilizável para algum problema recorrente na Arquitetura de Software, e aborda temas estruturais como o desempenho, escalabilidade, modularidade e manutenibilidade. Ele expressa um esquema fundamental de organização estrutural para sistemas de software, fornecendo um conjunto de subsistemas predefinidos e especificando suas responsabilidades.

### Padrões de Arquitetura vs. Padrões de Design

Os Padrões de Arquitetura e os Padrões de Design compartilham similaridades fundamentais uma vez que são abstrações reusáveis para a abordagem de problemas recorrentes na Engenharia de Software. Entretanto eles diferem entre si no **escopo** e **granularidade**.

Os Padrões de Design têm como alvo interações que ocorrem em nível de classe ou módulo, oferecendo soluções para problemas específicos como a criação de objetos (padrões criacionais/*creational patterns*), composição (padrões estruturais/*structural patterns*), ou comunicação (padrões de comportamento/*behavioral patterns*) dentro de subsistemas.

Em contraste, os Padrões de Arquitetura, ou Padrões Arquiteturais, focam na organização do sistema como um todo, definindo componentes de alto nível, suas resposabilidades e interconexões de forma a satisfazer os já citados atributos de qualidade (desempenho, escalabilidade, modularidade e manutenibilidade).

| **Características** | **Software Architecture Pattern** | **Design Pattern** |
|---|---|---|
| **Definição** | Consiste uma estrutura de alto nível do sistema, por completo. | Consiste em soluções de baixo nível para problemas comuns de design dentro de componentes. |
| **Escopo** | Amplo, cobre o sistema inteiro. | Estreito, foca em componentes individuais. |
| **Objetivo** | Estabelecer um layout para o sistema inteiro. | Fornecer soluções reutilizávels para problemas recorrentes na implementação de um sistema. |
| **Foco** | Estabilidade do sistema, organização estrutural. | Aspectos comportamentais e estruturas dentro de componentes. |
| **Documentação** | Envolve diagramas arquiteturais e documentos de design de alto nível. | Inclui doagramas UML e especificações de design detalhadas. |
| **Exemplos** | Arquitetura em Camadas, Microserviços, Cliente-Servidor. | Singleton, Factory, Strategy, Observer. |

## Padrões de Arquitetura mais comuns

### **MVC** (*Model-View-Controller*)

Talvez o mais conhecido. Ele separa uma aplicação em três camadas/componentes interconectados: 

- **Model**: representa os dados e lógica/regras de negócios, encapsulando o estado da aplicação e operações sem o conhecimento direto da interface de usuário.
- **View**: renderiza os dados vindos do *Model* em um formato amigável ao usuário; seu foco é inteiramente sobre a visualização, sem a manipulação dos dados.
- **Controller**: age como um intermediário, processando entradas vindas da *View*, interpretando-as, e coordenando atualizações entre *Model* e *View*, de forma a garantir consistência.

**Vantagens**

- *Reusabilidade*: as mesmas regras de negócio (*Model*) podem ser utilizadas em diferentes *Views*.
- *Flexibilidade*: componentes na camada *Model* podem ser testados em separado dos componentes na camada *View*, e também dos componentes na camada *Controller*.

**Desvantagens**

- *Complexidade*: em aplicações pequenas o MVC pode introduzir complexidade desnecessária; além disso, se não houver implementação cuidadosa pode ocorrer de o *Controller* lidar com lógica excessiva.
- *Sobrecarga*: em cenários complexos, uma forte dependência do lado do cliente pode gerar sobrecarga de implementação.

### **Padrão em Camadas** (*Layered Pattern*)

Também conhecido como Arquitetura *n-tier* ("n-níveis"), organiza uma aplicação em uma série de camadas, cada uma responsável por um aspecto ou funcionalidade distinta. As camadas são dipostas de forma hierárquica e, por consequência, as dependências fluem estritamente em uma direção, tipicamente das camadas mais altas para as mais baixas. Isso faz com que modificações nas camadas mais baixas não sejam propagadas para as camadas superiores, o que facilita o desenvolvimento independente e o teste de cada camada.

As camadas costuma ser as seguintes:

- **Apresentação**: a camada de interface de usuário onde dados são visualizados e inseridos na aplicação.
- **Lógica de Negócio**: é responsável por executar as regras/lógicas de negócio.
- **Aplicação**: funciona como um meio de comunicação entre a Camada de Apresentação e a Camada de Dados.
- **Dados**: camada para o gerenciamento dos dados.

**Vantagens**

- *Escalabilidade*: camadas individuais podem ser escaladas de forma independente se houver necessidade de melhora de desempenho.
- *Flexibilidade*: diferentes tecnologias podem ser usadas dentro de cada camada, sem que as demais sejam afetadas.
- *Manutenibilidade*: mudanças em uma camada não necessariamente impactam das demais, o que simplifica a manutenção.

**Desvantagens**

- *Complexidade*: a adição de mais camadas à arquitetura pode resultar em um sistema mais completo e difícil de gerenciar.
- *Sobrecarga de desempenho*: múltiplas camadas podem introduzir latência devido à comunicação adicional entre as camadas.
- *Separação estrita entre camadas*: pode levar a ineficiências e aumentar o esforço no desenvolvimento.

### **Microserviços** (*Microservices*)

Consiste em uma coleção de pequenos serviços que são combinados para formar a aplicação, ou seja, em vez de uma aplicação grande, programas menores e independentes são desenvolvidos para cada serviço. A adição de novas funcionalidades ou a modificação de alguma existente deixa de ser um desafio, uma vez que os módulos possuem pouca ou nenhuma influência uns sobre os outros.

**Vantagens**

- *Escalabilidade*: cada serviço pode ser escalado independentemente, baseado em demanda.
- *Entrega mais rápida*: serviços independentes permitem aos times desenvolverem, testaram e implantarem funcionalidades mais rapidamente.
- *Manutenção mais fácil*: serviços podem ser atualizados e mantidos independentemente.

**Desvantagens**

- *Gerenciamento complexo*: gerenciar mútliplos serviços requer monitoramento robusto e ferramentas de gerenciamento.
- *Congestionamento de rede*: o aumento do tráfego de dados entre os serviços pode levar ao congestionamento e sobrecarga.
- *Segurança*: a necessidade de implementar a segurança para múltiplos serviços e suas comunicações pode aumentar a probabilidade de erros, vulnerabilidades e ataques.

### Monolítico

Abordagem antiga, onde os componentes são estreitamente integrados como um único serviço.

Uma vantagem é a simplificação do desenvolvimento.

**Desvantagens**

- *Escalabilidade*: limitada, pois toda a aplicação precisa ser escalada.
- *Manutenibilidade*: complexa devido à estreita integração entre os componentes.
- *Entrega*: a implantação de atualizações pode ter mais riscos.

### *Service-Oriented Architecture* (SOA)

Os serviços consistem em unidades auto-contidas com uma interface bem definida, e funcionam como "caixas pretas", onde sua implementação é escondida dos usuários e são expostas somente as informações e comportamentos necessários.

Esses serviços são tipicamente definidos por contrato como os que usam *Web Services Description Language* (WSDL) com *Simple Object Access Protocol* (SOAP) ou APIs REST, o que garante interações padronizadas. A orquestração entre os serviços é frequentemente mediada por um *Enterprise Service Bus* (ESB), o que facilita o roteamento, transformação e composição de serviços através de ambientes heterogêneos.

**Vantagens**

- *Escalabilidade* e *adaptabilidade*: serviços podem ser invocados independentemente sem a dependência de implementações específicas.
- *Interoperabilidade*: serviços podem ser suportados por diversos sistemas através de descrições de serviço consistentes e semântica compartilhada, permitindo a integração perfeita de componentes de diferentes fornecedores.

**Desvantagens**

- *Complexidade*: torna-se difícil o planejamento e gerenciamento de serviços.
- *Sobrecarga*: o tráfego da comunicação em rede entre os serviços pode gerar congestionamento.
- *Segurança*: serviços de diferentes fornecedores pode aumentar o risco de segurança.

### Cliente-Servidor

A aplicação é dividida entre clientes e servidores. Os clientes fazem requisições e os servidores recebem e processam as requisições.

**Vantagens**

- *Gerenciamento centralizado*: servidores podem gerenciar recursos, dados, e políticas de segurança, simplifcando o gerenciamento e manutenção.
- *Escalabilidade*: servidores podem ser escalados para lidar com requisições crescentes dos clientes.
- *Segurança*: medidas de segurança como controle de acesso e criptografia dos dados podem ser implementadas de uma melhor forma, dado a centralização do controle.

**Desvantagens**

- *Falha em ponto único*: devido à centralização no servidor, se ele falha os clientes perdem acesso aos serviços, o que leva à perda de produtividade.
- *Custo*: configurar e manter servidores costuma ser caro.
- *Complexidade*: projetar e manter uma arquitetura cliente-servidor pode ser complexo.

### Outros padrões existentes

1. *Pipe-and-Filter*
2. *Event-Driven*
3. *Publish-Subscribe*
4. *Peer-to-Peer*
5. *Blackboard*
6. *Microkernel*
7. *Serverless*
8. *Broker*
9. *Circuit breaker*
10. *Command query responsibility segregation (CQRS)*
11. *Component-Based*
12. *Controller-Responder*
13. *Event-Bus*
14. *Hybrid*
15. *Master-Slave*
16. *Saga*
17. *Sharding*
18. *Space-Based*