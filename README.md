# Sistema de Vendas de Carros

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema de vendas de carros para uma loja de veículos, utilizando programação orientada a objetos em Python. O sistema visa organizar e automatizar o processo de venda, controle de estoque de veículos, cadastro de clientes e registros das transações de venda. Através da implementação de três entidades principais — **Veículo**, **Cliente** e **Venda** — o sistema visa melhorar a eficiência das operações e reduzir a ocorrência de erros manuais.

## Funcionalidades

- **Cadastro de Veículos**: Armazenamento de informações detalhadas sobre os carros (marca, modelo, ano, preço, cor, etc.).
- **Cadastro de Clientes**: Informações dos clientes, como nome, CPF, telefone e e-mail.
- **Registro de Vendas**: Realização de transações onde cada cliente pode comprar um carro por venda. O sistema atualizará automaticamente a disponibilidade dos veículos.
- **Controle de Estoque**: Após uma venda, a disponibilidade do veículo será alterada, evitando duplicação de vendas.

## Estrutura do Sistema

As principais entidades do sistema são:

1. **Veículo**: Armazena informações sobre o carro, como marca, modelo, preço e disponibilidade.
2. **Cliente**: Contém os dados do cliente, incluindo nome, CPF, telefone e e-mail.
3. **Venda**: Registra a transação de venda, associando um cliente a um veículo, com a data da venda e o valor total.

## Como Executar o Projeto

1. **Instalar dependências**:
   - Clone o repositório:  
     ```bash
     git clone https://github.com/usuario/repositorio.git
     ```
   - Navegue até o diretório do projeto:
     ```bash
     cd repositorio
     ```
   - Instale as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```

2. **Executar o programa**:
   - Para iniciar o sistema, execute o script principal:
     ```bash
     python main.py
     ```

## Arquivos de Documentação e Diagramas

Para melhor entendimento da estrutura e funcionamento do sistema, consulte os arquivos de documentação e diagramas abaixo:

- **Documentação do Sistema**: [documentacao.pdf](link-para-documentacao.pdf)
- **Diagramas do Sistema**: [Diagrama Draw.io](link-para-diagrama.drawio)

> **Nota**: Caso precise de mais informações ou detalhes sobre a arquitetura do sistema, consulte a documentação completa e os diagramas fornecidos.

## Contribuições

Se você deseja contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Faça as alterações necessárias e commit (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

