# Aula 14

## CI/CD

*Continuous Integration*/*Continuous Delivery* (Integração Contínua/Implantação Contínua) pode ser entendido como um fluxo de trabalho automatizado que substitui etapas manuais, do `commit` à produção, por *pipelines* que compilam, testam e implantam software de forma confiável.

Com um *pipeline* de CI/CD, as equipes de desenvolvimento podem fazer alterações no código que são então testadas e enviadas automaticamente para entrega e implantação. Ao implementar o CI/CD corretamente, o tempo de inatividade é minimizado e as versões de código são lançadas mais rapidamente.

### CI

A Integração Contínua é uma prática de software que exige `commits` **frequentes** de códigos para um repositório compartilhado. A partir disso é possível detectar erros com mais antecedência, se reduz a quantidade de código necessária para depuração, e o `merge` das alterações também fica mais fácil de ser conduzido.

Após o `commit` do código no repositório, ele pode ser compilado e testado de maneira automática e contínua para garantir que o `commit` não introduza erros. Esses testes podem incluir *linters*, verificações de segurança, cobertura de código, testes funcionais, etc.

A compilação e teste podem ser feitos localmente antes de fazer o `push`, ou podem ser feitos em algum servidor de CI.

### CD

A Implantação Contínua é o processo de preparar automaticamente o código testado de forma que ele esteja sempre preparado para implantação em qualquer ambiente. É uma prática de desenvolvimento de software que trabalha em conjunto com a CI para automatizar o provisionamento de infraestrutura e processo de lançamento da aplicação.

### Elementos fundamentais

- **Um único repositório fonte**: onde estarão armazenados todos os arquivos e scripts necessários para criar *builds*, o que inclui o código fonte, estrutura do banco de dados, bibliotecas, arquivos de configuração, controle de versionamento e scripts de teste e compilação.
- ***Commits* frequentes na *branch* principal**: deve-se evitar *sub-branches*, pois o foco está na *branch* principal. Os *commits* devem ser pequenos para facilitar o *merge* com a maior frequência possível. Não se deve fazer o *merge* de mais de uma alteração por vez.
- **Scripts de compilação automatizada**: devem incluir todo o necessário para a compilação do código a partir de um único comando. Isso inclui arquivos de servidor web, scripts de banco de dados e software de aplicação. Os processos de CI devem empacotar e compilar o código automaticamente em uma aplicação utilizável.
- **Compilações (*builds*) autotestáveis**: os scripts de teste devem garantir que a falha de um teste resulte em uma falha na compilação. Recomenda-se o uso de scripts de pré-compilação para verificar a integridade, qualidade e conformidade de segurança do código
- **Iterações frequentes**: Vários *commits* no repositório resultam em menos lugares onde conflitos podem se esconder. Deve-se fazer iterações pequenas e frequentes em vez de grandes alterações. Dessa forma, é possível reverter as alterações facilmente caso haja algum problema ou conflito.
- **Ambientes de teste estáveis**: o ambiente de teste deve ser um clone o mais próximo possível do ambiente real. Scripts de teste rigorosos devem ser usados para capturar quaisquer bugs que tenham passado despercebidos durante os testes de pré-compilação.
- **Máxima visibilidade**: todo desenvolvedor deve ser capaz de acessar os últimos executáveis e ver quaisquer mudanças no repositório. Todos devem ser capazes de monitorar o progresso e identificar possíveis problemas.
- **Implantações previsíveis a qualquer momento**: as implantações devem ser tão rotineiras e de baixo risco que a equipe se sinta confortável em realizá-las a qualquer momento. Os processos de teste e verificação de CI/CD devem ser rigorosos e confiáveis, dando à equipe a segurança necessária para implantar atualizações a qualquer momento. Implantações frequentes com alterações limitadas também apresentam riscos menores e podem ser revertidas facilmente.

### Dados

- [Pesquisa sobre CI/CD](https://blog.jetbrains.com/teamcity/2026/03/best-ci-tools/)
- Plataforma mais conhecida/utilizada: GitHub Actions.
- [Alternativas](https://northflank.com/blog/github-actions-alternatives).
- [CI/CD Local](https://medium.com/@deepakkr35/building-a-devops-ci-cd-pipeline-locally-github-jenkins-maven-sonarqube-docker-dockerhub-ba5cf7d58074)

## Testes

- https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing
- https://www.guru99.com/software-testing.html
- Teste de unidade
  - https://github.com/goldbergyoni/javascript-testing-best-practices
  - https://www.guru99.com/unit-testing-guide.html
- Teste de integração
  - https://www.guru99.com/integration-testing.html
- Teste funcional
  - https://www.guru99.com/functional-testing.html

<!--
CI/CD
    - https://thenewstack.io/ci-cd/
    - https://about.gitlab.com/topics/ci-cd/
    - https://docs.github.com/pt/actions
      - https://docs.github.com/en/actions/tutorials/build-and-test-code

Testing
    - Overall concepts
      - https://www.geeksforgeeks.org/software-testing/levels-of-software-testing/
      - https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing
      - https://dev.to/campkathleen3/what-are-the-4-levels-of-software-testing-41kk
    - Unit test
      - https://github.com/goldbergyoni/javascript-testing-best-practices
      - https://en.wikipedia.org/wiki/Unit_testing
      - https://www.guru99.com/unit-testing-guide.html
    - Integration test
      - https://www.guru99.com/integration-testing.html
      - https://www.testim.io/blog/unit-test-vs-integration-test/
      - https://thenewstack.io/how-to-integrate-and-test-your-tech-stack/
    - Functional test
      - https://www.guru99.com/functional-testing.html
      - https://www.atlassian.com/continuous-delivery/software-testing/functional-testing
-->