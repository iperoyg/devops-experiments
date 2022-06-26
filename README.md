# devops-experiments
Este é um projeto de teste para fazer experimentações de DevOps no GitHub


*Author:* [Arthur Iperoyg](mailto:iperoyg@gmail.com)


## Basic instructions
- Utilize o arquivo de [ambiente conda](env.yml) para replicar o ambiente
    - `conda env create -n devops-experiments-env -f env.yml`
- *Prefira* modificar os arquivos de [ambiente conda](env.yml) ou de [requerimentos do pip](requirements.txt) para modificar/adicionar/remover bibliotecas ao **invés de operar diretamente nos ambientes**.
    - `conda env update -n devops-experiments-env -f env.yml`
- Para executar os testes, use *pytest*
    - `pytest`
- Para executar a verificação de lint, use o *flake*
    - `flake8 . --count --statistics`
    - `flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics`
- Para atualizar a documentação gerada automaticamente (dentro da pasta de [documentação](docs/)) utilize o pdoc
    - `pdoc src\complexoperations -o docs`
## Para contribuir
- Use sua imaginação
