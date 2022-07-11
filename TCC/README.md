INSTITUTO FEDERAL CATARINENSE

Curso Técnico em Informática

Projeto Integrador

Nome do Projeto: E-plays

Equipe: Gustavo Almeida da Silva

Araquari, maio, 2021




#	Descrição Geral do Produto

### ⦁	Visão Geral:

 O site terá como tema os esportes eletrônicos, e possuirá notícias, informações do cenário competitivo, criação de campeonatos próprios, rankings, estatísticas e etc.
 Contará com vídeos, links, imagens, textos.
 Será feito uma parte voltada pro cenário nacional, e outra pro cenário das demais regiões.
 Terá produtos envolvendo o tema, mas não próprio e sim de outros sites já existentes, ou seja, funcionará mais como divulgação e indicação.
 Produziremos também conteúdos para ajudar no desenvolvimento dos internautas em jogos específicos, para ajudá-los a melhorarem. Além de dicas de jogos que estão em alta e que podem vir a ser divertidos.




#	Especificação de Requisitos

### ⦁	Requisitos Funcionais:

RF001 - O sistema deve permitir que o usuário se cadastre no site.

RF002 - O sistema deve permitir que o usuário tenha acesso ao portal de notícias.

RF003 - O sistema deve divulgar criações e organizações de campeonatos.

RF004 - O sistema deve permitir que o usuário se inscreva no campeonato.

RF005 - O sistema deve permitir que o usuário tenha acesso aos gráficos e às estatísticas.

RF006 - O sistema deve fornecer rankings dos cenários competitivos.

RF007 - O sistema deve dar dicas de jogos que estão em alta, postadas no portal de notícias em formato de notícia.

RF008 - O sistema deve apresentar produtos e redirecionar o usuário ao site responsável pela venda do mesmo.

RF009 - O sistema deve permitir que o usuário tenha acesso à conteúdos que ajude-o a melhorar em algum jogo específico de seu interesse.


### ⦁	Requisitos Não Funcionais:

RNF001 - O sistema deve funcionar em qualquer plataforma.

RNF002 - O sistema não deve apresentar a usuários quaisquer dados de cunho privado.

RNF003 - O sistema deve ficar no ar por pelo menos 20 horas diárias.

RNF004 - O sistema deve ter um tempo de resposta menor do que 5 segundos.

RNF005 - O sistema deve atender às leis, normas e padrões impostos.

RNF006 - O sistema deve utilizar o Sistema de Gerenciamento de Banco de Dados Microsoft SQL Server.


### ⦁	Regras de Negócio

RN001 - O apelido de usuário deve conter no máximo 15 caracteres.

RN002 - A senha do usuário deve conter pelo menos 3 caracteres, e no máximo 15.

RN003 - Para que o usuário possa se inscrever em um campeonato, ele deve estar cadastrado no site.


# Detalhamento de Casos de Uso

## Cadastrar-se

Fluxo principal
1) Usuário fornece seu nome completo. 
2) Usuário fornece o e-mail. 
3) Usuário fornece a senha.
4) Sistema verifica se a senha respeita as exigências do site (conforme RN002). 
5) Usuário fornece sua data de nascimento. 
6) Usuário fornece seu apelido. 
7) Sistema verifica se o apelido respeita as exigências do site (conforme RN003).
8) Sistema efetua o cadastro e redireciona o usuário para a página principal (portal de notícias).

Fluxo alternativo(3): Usuário digita uma senha com menos de 3 ou mais de 15 caracteres (contrariando RN002)
- Sistema pede para que o usuário registre uma outra senha, respeitando os critérios previstos. 
Fluxo alternativo(5): Usuário digita um apelido com mais de 15 caracteres (contrariando RN001)
- Sistema pede para que o usuário registre um outro apelido, respeitando os critérios previstos. 


## Fazer login 

Fluxo principal
1) Usuário fornece o apelido já cadastrado. 
2) Usuário fornece a senha já cadastrada. 
3) Sistema verifica se os dados informados constam no banco de dados.
4) Sistema efetua o login e redireciona o usuário para a página principal (portal de notícias). 

Fluxo alternativo(1): Usuário fornece apelido ou senha que não constam no banco de dados 
- Sistema pede para que o usuário revise os dados informados. 


## Inscrever-se em um campeonato 
Fluxo principal
1) Usuário se direciona à página de inscrição. 
2) Sistema verifica se o usuário é cadastrado no site. 
3) Usuário lê as informações .
4) Usuário clica em “inscrever-se”.
5) Sistema registra o participante. 

Fluxo alternativo(2): Usuário não é cadastrado no site (contrariando RN003)
- Sistema exibe uma mensagem indagando se o usuário deseja cadastrar-se para participar.
- Caso o usuário concorde, o sistema irá direcioná-lo à página de cadastro.
- Usuário efetua seu cadastro.
- Sistema redireciona o usuário para a página de inscrição.


## Cadastrar  um campeonato 

Fluxo principal
1) Administrador se direciona à página de campeonato. 
2) Administrador vai em “Criar campeonato”. 
3) Administrador coloca um título.
4) Administrador coloca uma imagem.
5) Administrador coloca um texto.
6) Administrador coloca um valor de premiação.
7) Administrador efetua o cadastro do campeonato e abre as inscrições.


## Acessar uma notícia

Fluxo principal
1) Usuário se direciona à página de notícias. 
2) Usuário clica na notícia que desejar.

## Cadastrar  uma notícia

Fluxo principal
1) Administrador se direciona à página de notícias. 
2) Administrador vai em “Criar notícia”. 
3) Administrador coloca um título.
4) Administrador coloca uma imagem.
5) Administrador coloca um texto.
6) Administrador coloca um vídeo.
7) Administrador coloca um link.
8) Administrador coloca a data da notícia.
9) Administrador efetua o cadastro da notícia e a disponibiliza aos internautas.


## Acessar um produto

Fluxo principal
1) Usuário se direciona à página de produtos. 
2) Usuário clica no produto que desejar.


## Cadastrar  um produto

Fluxo principal
1) Administrador se direciona à página de produtos. 
2) Administrador vai em “Adicionar produto”. 
3) Administrador coloca um título.
4) Administrador coloca uma imagem.
5) Administrador coloca um texto.
6) Administrador coloca um link.
7) Administrador coloca o preço..
8) Administrador efetua o cadastro do produto e o disponibiliza aos internautas.




## Acessar uma notícia

Fluxo principal
1) Usuário se direciona à página do ranking. 
Atualizar o ranking

Fluxo principal
1) Administrador se direciona à página do ranking. 
2) Administrador vai em “Atualizar ranking”. 
3) O sistema faz uma consulta no banco de dados (entidade time e entidade jogador) .
4) Administrador coloca a data da atualização.
5) Administrador efetua a atualização do ranking e o disponibiliza aos internautas.
