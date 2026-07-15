# Engenharia de Software II — Introdução ao pytest e Projeto Cards

Este repositório contém a implementação prática dos conceitos apresentados na disciplina de **Engenharia de Software II** (ministrada pelo Prof. Vinicius H. S. Durelli na UFSCar). O foco deste laboratório é a introdução ao framework de testes `pytest` e a exploração de testes práticos na biblioteca e CLI `cards`.

---

## 📂 Estrutura do Projeto

O projeto está organizado com os seguintes arquivos e diretórios principais:

* **[cards_proj/](file:///d:/GitHub/ES2/PC1/cards_proj)**: Diretório contendo a aplicação `cards` (empacotada com `pyproject.toml` e seu próprio código fonte em `src/`).
  * **CLI (Command Line Interface)**: Interface de terminal para interação direta com os cards.
  * **API (Application Programming Interface)**: A lógica principal da aplicação e a definição da estrutura de dados `Card`.
  * **DB (Database)**: Camada de banco de dados para a persistência local dos cards.
* **[test_card.py](file:///d:/GitHub/ES2/PC1/test_card.py)**: Suíte de testes unitários para a classe de dados `Card` (valores padrão, igualdade de atributos ignorando o ID, desigualdade e conversões de/para dicionários).
* **[test_exceptions.py](file:///d:/GitHub/ES2/PC1/test_exceptions.py)**: Testes para demonstrar o comportamento de exceções esperadas via `pytest.raises()`, falhas forçadas explicitamente com `pytest.fail()`, e tracebacks de erro gerados pelo `pytest`.
* **[test_exercicios.py](file:///d:/GitHub/ES2/PC1/test_exercicios.py)**: Resoluções das atividades propostas nos slides (utilizando operadores como `in`, `<` e filtros de busca com `-k`).
* **[teste-cards-1.py](file:///d:/GitHub/ES2/PC1/teste-cards-1.py)**: Suíte alternativa de testes cobrindo variações na criação e verificação da entidade `Card`.
* **[test1.py](file:///d:/GitHub/ES2/PC1/test1.py)**: Arquivo inicial introduzindo a escrita de testes simples com asserts.

---

## 🛠️ Configuração do Ambiente

Siga os passos abaixo para preparar o ambiente virtual e instalar as dependências necessárias:

### 1. Criar o Ambiente Virtual (venv)

No diretório raiz do projeto, execute o comando correspondente ao seu sistema operacional para criar o ambiente virtual:

```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

* **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **Windows (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
* **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

*(Uma vez ativado, você notará a indicação `(venv)` no prefixo da linha de comando do seu terminal).*

### 3. Instalar o pytest

Com o ambiente virtual ativo, instale a biblioteca `pytest`:

```bash
pip install pytest
```

### 4. Instalar o Pacote `cards` Localmente

Instale o código-fonte da aplicação `cards` diretamente do diretório `cards_proj` em modo de instalação local:

```bash
pip install ./cards_proj/
```

---

## 💻 Interagindo com a CLI da Aplicação Cards

A aplicação permite manipular tarefas diretamente pelo terminal usando comandos CLI. Veja alguns exemplos:

```bash
# Adicionar tarefas
cards add "Estudar pytest para Engenharia de Software II" --owner "Maylon"
cards add "Resolver os exercicios propostos"

# Listar todas as tarefas ativas
cards

# Atualizar o proprietário ou detalhes de uma tarefa (ex: ID 2)
cards update 2 --owner "Durelli"

# Alterar o progresso dos cards (todo -> in prog -> done)
cards start 1
cards finish 1
cards start 2

# Excluir um card
cards delete 1
```

---

## 🧪 Executando os Testes com o pytest

O `pytest` busca automaticamente por arquivos iniciados em `test_` ou terminados em `_test` e executa funções declaradas com o prefixo `test_`.

### Executar toda a suíte de testes:

```bash
pytest
```

### Executar em modo verboso (mostra o nome completo das funções e o status `PASSED` / `FAILED` de forma detalhada):

```bash
pytest -v
```

### Executar ocultando o Traceback detalhado de erros:

```bash
pytest --tb=no
```

### Filtrar execução por nome do teste usando a opção `-k`:

```bash
# Executa apenas testes que possuem "laranja" no nome da função
pytest -k laranja
```

---

## 📖 Principais Conceitos Abordados

1. **Anatomia de um Teste**:
   * **Preparação (Setup)**: Configuração do ambiente e inicialização de variáveis.
   * **Execução (Action)**: Rodar a lógica/método a ser testado.
   * **Verificação (Assert)**: Checagem dos resultados comparando o resultado obtido com o esperado.
2. **Knowledge-building Tests**:
   * Utilizar a escrita de testes unitários no início de um desenvolvimento para explorar o comportamento de novas estruturas de dados ou componentes (como a classe `@dataclass Card`), compreendendo na prática seus valores padrões e restrições.
3. **Simplicidade do assert**:
   * O `pytest` permite usar a instrução nativa `assert` do Python com qualquer operador ou expressão (`==`, `!=`, `in`, `is None`), sem a necessidade de importar métodos auxiliares complexos das classes do `unittest`.
4. **Testando Exceções**:
   * O uso do gerenciador de contexto `with pytest.raises(TypeError):` para garantir que o código lance a exceção esperada sob determinadas condições (ex: inicializar o `CardsDB` sem fornecer o caminho do banco de dados).
