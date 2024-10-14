# Custom Logging Library
### Descrição
Esta é uma biblioteca simples e customizável para registro de logs (logging) em aplicações Python. Ela oferece funcionalidades básicas para logar informações, avisos, erros e mensagens customizadas de forma thread-safe, garantindo que múltiplas threads possam escrever nos arquivos de log simultaneamente sem causar conflitos.

Além disso, a biblioteca utiliza a colorama para adicionar cores diferenciadas às mensagens no console, facilitando a identificação de diferentes níveis de log (INFO, WARNING, ERROR, etc.).

### Funcionalidades
- Log de Informações: Registra mensagens informativas no log.
- Log de Avisos: Registra avisos que podem exigir atenção.
- Log de Erros: Registra mensagens de erro juntamente com o traceback.
- Log Customizado: Registro de mensagens de um "robô" ou outro tipo personalizado.
- Gravação Thread-safe: Garantia de que múltiplas threads podem logar simultaneamente sem conflitos.
- Suporte a Cores no Console: Diferentes cores para cada nível de log usando colorama.
## Instalação
### Via GitHub
Para instalar diretamente do repositório GitHub, você pode usar o seguinte comando:

```
pip install git+https://github.com/seuusuario/custom_logging.git
```

### Dependências
A biblioteca requer o pacote colorama para colorir as saídas no terminal. Ele será automaticamente instalado junto com a biblioteca.

```
pip install colorama
```

## Como Usar
Aqui está um exemplo básico de como utilizar a biblioteca em sua aplicação:

```
from logging import Log

log = Log()

log.info("Esta é uma mensagem de informação.")
log.warning("Este é um aviso!")
log.error("Este é um erro que ocorreu.")
log.robot("Mensagem de log customizada para um robô.")
```

Por padrão, a biblioteca criará um arquivo de log chamado log.txt dentro de uma pasta log no diretório raiz da aplicação, onde todas as mensagens serão registradas.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no GitHub.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.