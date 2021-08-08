# Aprendendo Python 3.0

Curso python - Curso em video do professor Gustavo Guanabara

## Comando uteis

## Montando ambiente de desenvolvimento

Ao executar o projeto a primeira vez:

1. Clonar projeto no github

2. Instalar Python 3.6

3. Instalar ou Atualizar o Anaconda

    - Caso tenha o Anaconda instalado,
atualize o Anaconda.

    ```shell
    conda update
    ```

    - Este comando atualiza o anaconda, indicando a pasta que ele está instalado.

    ```shell
    conda update --prefix D:\Anaconda anaconda
    ```

4. Criar e ativar ambiente virtual

    - É muito importante que o ambiente virtual seja salvo em uma pasta com um nome DIFERENTE de .env. Uma sugestção é .venv.

    ```shell
    conda create  -p .venv python
    ```

    - Ativando o ambiente virtual.

    ```shell
    conda activate ./.venv
    ```
