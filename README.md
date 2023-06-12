# p3-ES-FastApi
[![NPM](https://img.shields.io/npm/l/react)]() 

# Sobre o projeto
Este projeto foi desenvolvido com o objetivo de criar  CRUD usando a linguagem de programação Python a fim de praticar a utilização de testes e de frameworks no processo de desenvolvimento de software,usando para isso as técnicas de TDD. A implementação seguiu uma abordagem passo a passo, começando com a criação de testes, seguida pela codificação das funções, a adição de um banco de dados e, por fim, a utilização do framework FastAPI.



# Casos de uso

### ------Adicionar Produto------

Caso de Uso: Adicionar Produto

Objetivo: Adicionar um novo produto ao estoque

Atores: Estoquista

Pré-Condição: Ao menos um produtos está cadastrado no estoque

Pós-Condição: Produto cadastrado

Fluxo Principal de Eventos:
- O Estoquista insere nome, tipo e quantidade do produto.
- O sistema emite uma confirmação de sucesso da ação realizada.
- O caso de uso termina.

Fluxo Alternativos:
- Bloqueio: O produto já está adicionado ao estoque. O sistema emite uma mensagem e a ação não pode ser realizada
- Bloqueio Estoque Lotado: Se o estoque estiver cheio. O sistema emite uma mensagem informando que o estoque está cheio e a ação não pode ser realizada.

Cenário Principal: Inserção de um novo produto.

Cenário Secundário: Bloqueio, Bloqueio Estoque Lotado



### ------Listar Produtos------ 

Caso de Uso: Listar Produtos

Objetivo: Listar todos os produtos cadastrados no estoque

Atores: Estoquista

Pré-Condição: Pelo menos um produto está cadastrado no estoque

Pós-Condição: Nenhum

Fluxo Principal de Eventos:
- O Estoquista solicita a listagem dos produtos.
- O sistema exibe a lista de produtos cadastrados no estoque..
- O caso de uso termina.

Fluxo Alternativos:
- Lista Vazia: Caso não haja nenhum produto cadastrado, a lista estará vazia.
- Erro de Conexão: Caso o sistema não consiga acessar o banco de dados com os produtos.

Cenário Principal: Listar produtos cadastrados.

Cenário Secundário: Lista Vazia,Erro de Conexão.



### ------Deletar Produtos------ 

Caso de Uso: Deletar Produtos

Objetivo: Remover um produto do estoque

Atores: Estoquista

Pré-Condição: Pelo menos um produto está cadastrado no estoque

Pós-Condição: Produto removido do estoque

Fluxo Principal de Eventos:
- O Estoquista solicita a remoção de um produto.
- O sistema exibe a lista de produtos cadastrados no estoque.
- O Estoquista seleciona o produto a ser removido.
- O sistema confirma a remoção do produto e o remove do estoque.
- O sistema emite uma confirmação de sucesso da ação realizada.
- O caso de uso termina.

Fluxo Alternativos:
- Bloqueio: Se a lista de produtos estiver vazia, o sistema emite uma mensagem informando que não há produtos cadastrados e a ação não pode ser realizada.
- Produto não encontrado: Caso um produto não seja encontrado para deletar, o sistema emite uma mensagem informando que o produto não está no estoque.

Cenário Principal: Remoção de um produto.

Cenário Secundário: Bloqueio,Produto não encontrado.



### ------Atualizar Produto------

Caso de Uso: Atualizar Produto

Objetivo: Atualizar informações de um produto no estoque

Atores: Estoquista

Pré-Condição: Ao menos um produtos está cadastrado no estoque

Pós-Condição: Informações do produto atualizadas no estoque

Fluxo Principal de Eventos:
- O Estoquista solicita a atualização de um produto.
- O sistema exibe a lista de produtos cadastrados no estoque.
- O Estoquista seleciona o produto a ser atualizado.
- O sistema exibe as informações atuais do produto selecionado.
- O Estoquista insere as novas informações do produto (nome, tipo e quantidade).
- O sistema confirma a atualização das informações e atualiza o produto no estoque.
- O sistema emite uma confirmação de sucesso da ação realizada.
- O caso de uso termina.


Fluxo Alternativos:
- Bloqueio:Se a lista de produtos estiver vazia, o sistema emite uma mensagem informando que não há produtos cadastrados e a ação não pode ser realizada.
- Produto não encontrado: Caso um produto não seja encontrado para atualizar, o sistema emite uma mensagem informando que o produto não está no estoque.

Cenário Principal: Atualização de informações de um produto.

Cenário Secundário: Bloqueio, Produto não encontrado.



### ------Listar 1 Produto------

Caso de Uso: Listar 1 Produto

Objetivo: Listar as informações de um único produto no estoque

Atores: Estoquista

Pré-Condição: Ao menos um produto está cadastrado no estoque

Pós-Condição: Nenhuma

Fluxo Principal de Eventos:
- O Estoquista solicita a listagem de um produto específico.
- O sistema exibe um campo de pesquisa para que o Estoquista possa inserir informações sobre o produto .
- O Estoquista insere as informações do produto que deseja listar.
- O sistema exibe as informações detalhadas do produto.
- O caso de uso termina.

Fluxo Alternativos:
- Bloqueio Lista Vazia: Se a lista de produtos estiver vazia, o sistema emite uma mensagem informando que não há produtos cadastrados e a ação não pode ser realizada.
- Produto não encontrado: Caso um produto não seja encontrado para atualizar, o sistema emite uma mensagem informando que o produto não está no estoque.

Cenário Principal: Exibir informações de um produto específico..

Cenário Secundário: Bloqueio Lista Vazia, Produto não encontrado.

# Competencias
- Test Driven Development (TDD)

# Tecnologias utilizadas

## Back end
- Python
##Banco de dados
-MySQL

# Autores
- Fernando Costa:
https://github.com/fercostard
- Guilherme Aquino:
https://github.com/guilhermeaquinop
- Victor Coelho:
https://github.com/VictorCoelho957
