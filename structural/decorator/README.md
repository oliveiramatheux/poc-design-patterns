## Design Pattern Structural Decorator

O padrão de projeto Decorator é usado para adicionar funcionalidades a um objeto de forma dinâmica, sem alterar sua estrutura original. Ele permite criar uma cadeia de decoradores, onde cada um adiciona uma nova responsabilidade ao objeto, promovendo flexibilidade e reutilização de código.

Na implementação, criei uma classe base `Converter` e decoradores como `JsonDecorator` e `XMLDecorator`, que recebem um conversor base `BaseConverter` (ou outro decorador) e adicionam novos comportamentos, como a conversão de dados para JSON ou XML. Isso torna o sistema modular e facilita a extensão de funcionalidades sem modificar as classes existentes.

1 - O objetivo do Decorator é adicionar funcionalidades extras a um objeto sem alterar sua estrutura básica;

2 - Você sempre terá:
    - Interface Comum para definir o comportamento geral;
    - Objeto Original (Componente Concreto) que será decorado;
    - Decoradores que encapsulam o objeto original e acrescentam novos comportamentos.

3 - Os decoradores podem ser combinados em cadeia, ou seja, você pode empilhar funcionalidades extras.
