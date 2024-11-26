## Design Pattern Creational Singleton

O padrão de projeto Singleton é usado para garantir que uma classe tenha apenas uma única instância durante toda a execução do programa e fornecer um ponto global de acesso a essa instância. Ele é útil em situações onde é necessário gerenciar recursos compartilhados, como conexões com banco de dados ou configurações globais. Isso ajuda a manter a consistência e evita problemas que podem surgir com múltiplas instâncias desnecessárias.

Na implementação de exemplo, utilizei uma metaclass (`SingletonMeta`) para controlar a criação da instância, armazenando-a em um dicionário interno. Assim, sempre que a classe Singleton for chamada, a mesma instância será retornada.
