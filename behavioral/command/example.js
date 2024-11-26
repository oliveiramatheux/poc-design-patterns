// Interface Command
class Command {
    execute() {
      throw new Error('Este método deve ser implementado');
    }
    
    undo() {
      throw new Error('Este método deve ser implementado');
    }
  }
  
  // Receptores
  class Luz {
    ligar() {
      console.log('A luz foi ligada.');
    }
  
    desligar() {
      console.log('A luz foi desligada.');
    }
  
    diminuir() {
      console.log('A intensidade da luz foi diminuída.');
    }
  
    aumentar() {
      console.log('A intensidade da luz foi aumentada.');
    }
  }
  
  class Persiana {
    abaixar() {
      console.log('A persiana foi abaixada.');
    }
  
    levantar() {
      console.log('A persiana foi levantada.');
    }
  }
  
  class TV {
    ligar() {
      console.log('A TV foi ligada.');
    }
  
    desligar() {
      console.log('A TV foi desligada.');
    }
  }
  
  // Comandos Concretos com métodos undo()
  class ComandoLigarLuz extends Command {
    constructor(luz) {
      super();
      this.luz = luz;
    }
  
    execute() {
      this.luz.ligar();
    }
  
    undo() {
      this.luz.desligar();
    }
  }
  
  class ComandoDesligarLuz extends Command {
    constructor(luz) {
      super();
      this.luz = luz;
    }
  
    execute() {
      this.luz.desligar();
    }
  
    undo() {
      this.luz.ligar();
    }
  }
  
  class ComandoDiminuirLuz extends Command {
    constructor(luz) {
      super();
      this.luz = luz;
    }
  
    execute() {
      this.luz.diminuir();
    }
  
    undo() {
      this.luz.aumentar();
    }
  }
  
  class ComandoAbaixarPersiana extends Command {
    constructor(persiana) {
      super();
      this.persiana = persiana;
    }
  
    execute() {
      this.persiana.abaixar();
    }
  
    undo() {
      this.persiana.levantar();
    }
  }
  
  class ComandoLevantarPersiana extends Command {
    constructor(persiana) {
      super();
      this.persiana = persiana;
    }
  
    execute() {
      this.persiana.levantar();
    }
  
    undo() {
      this.persiana.abaixar();
    }
  }
  
  class ComandoLigarTV extends Command {
    constructor(tv) {
      super();
      this.tv = tv;
    }
  
    execute() {
      this.tv.ligar();
    }
  
    undo() {
      this.tv.desligar();
    }
  }
  
  class ComandoDesligarTV extends Command {
    constructor(tv) {
      super();
      this.tv = tv;
    }
  
    execute() {
      this.tv.desligar();
    }
  
    undo() {
      this.tv.ligar();
    }
  }
  
  // Invocador com funcionalidade de Desfazer/Refazer
  class ControleRemoto {
    constructor() {
      this.comandos = {};
      this.historico = [];
      this.desfeitos = [];
    }
  
    setComando(nome, comando) {
      this.comandos[nome] = comando;
    }
  
    apertarBotao(nome) {
      if (this.comandos[nome]) {
        const comando = this.comandos[nome];
        comando.execute();
        this.historico.push(comando);
        // Limpa a pilha de comandos desfeitos quando um novo comando é executado
        this.desfeitos = [];
      } else {
        console.log(`Nenhum comando definido para o botão: ${nome}`);
      }
    }
  
    desfazer() {
      if (this.historico.length > 0) {
        const comando = this.historico.pop();
        comando.undo();
        this.desfeitos.push(comando);
      } else {
        console.log('Nada para desfazer.');
      }
    }
  
    refazer() {
      if (this.desfeitos.length > 0) {
        const comando = this.desfeitos.pop();
        comando.execute();
        this.historico.push(comando);
      } else {
        console.log('Nada para refazer.');
      }
    }
  }
  
  // Cliente
  // Configurando o sistema
  const luzSala = new Luz();
  const persianaSala = new Persiana();
  const tvSala = new TV();
  
  const comandoLigarLuz = new ComandoLigarLuz(luzSala);
  const comandoDiminuirLuz = new ComandoDiminuirLuz(luzSala);
  const comandoAbaixarPersiana = new ComandoAbaixarPersiana(persianaSala);
  const comandoLigarTV = new ComandoLigarTV(tvSala);
  
  const controleRemoto = new ControleRemoto();
  
  // Configurando o "Modo Filme"
  controleRemoto.setComando('modoFilme', {
    execute: function() {
      comandoDiminuirLuz.execute();
      comandoAbaixarPersiana.execute();
      comandoLigarTV.execute();
    },
    undo: function() {
      // Desfaz os comandos em ordem reversa
      comandoLigarTV.undo();
      comandoAbaixarPersiana.undo();
      comandoDiminuirLuz.undo();
    }
  });
  
  // Usando o controle remoto
  controleRemoto.apertarBotao('modoFilme');
  
  // Desfazendo a última ação (Modo Filme)
  console.log('\nDesfazendo a ação:');
  controleRemoto.desfazer();
  
  // Refazendo a última ação
  console.log('\nRefazendo a ação:');
  controleRemoto.refazer();
  