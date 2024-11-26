## Design Pattern Behavioral Command

O padrão de projeto Command é usado para encapsular uma solicitação como um objeto, permitindo que comandos sejam parametrizados, armazenados em fila ou históricos e suportem operações de desfazer/refazer. Esse padrão é útil para implementar funcionalidades como botões configuráveis ou automações complexas. Amplamente utilizado em jogos ou editores de texto. Seu ponto negativo é a verbosidade e o aumento da complexidade do código.

Na implementação de exemplo, criei uma interface `Command` com os métodos `execute()` e `undo()`, que são implementados pelos comandos concretos. Cada comando encapsula uma ação específica de um receptor (como uma luz, TV ou persiana). Um invocador (como um controle remoto) gerencia os comandos, permitindo executá-los, desfazê-los ou refazê-los.
