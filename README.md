 📊 Previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

> **_NOTE:_**  Desafio de projeto "Previsão de Estoque Inteligente na AWS com SageMaker Canvas. 
Tem como objetivo, demostrar os conhecimentos adquiridos ao longo do Bootcamp "Nexa - Machine Learning para Iniciantes na AWS". 
Como abordado nas ulas farei uso do SageMaker Canvas para criar previsões de estoque baseadas em Machine Learning (ML).
 Guiado pelos passos abaixo:

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter uma conta na AWS. Se precisar de ajuda para criar sua conta, confira o repositório da DIO com um passo a passo de como criar.<br>
 [AWS Cloud Quickstart](https://github.com/digitalinnovationone/aws-cloud-quickstart).


## 🎯 Objetivos Deste Desafio de Projeto.
- Criar previsões de estoque baseadas em Machine Learning (ML) com o serviço da AWS SageMaker Canvas.Guiado pelos processos demostrado na imagem no SageMaker.

  ![image](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque/assets/730492/72f5c21f-5562-491e-aa42-2885a3184650)


## 🚀 Passo a Passo

### 1. Criar um dominio.

-   Após ter criado a conta na AWS. Busque pelo Serviço do SageMaker.

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/Busca%20por%20Servi%C3%A7o%20-%20SageMaker.png)

<br>

- O próximo passo é criar um Dominiio  no qual ficarão centralizadas todas configurações e projetos futuros. Servindo também para outras aplicaçoes que compoem o ecosistema SageMaker.

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/CriarDominioSageCanvas.png)

<br>
- Após ter realizado a criação do dominio, quando clicamos em canvas o dominio automaticamente é reconhecido.Então clicamos em "Open Canvas".

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/DominioReconhecido.png)

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/TelaDoSageMakerCanvas.png)

### 2. Construir/Treinar

- Na Home do SageMaker Canvas quando entramos existem alguns cards com algumas opções: "Create a Model", "ExploreGenerativa IA" e "Explore ready-to-use-Models".
 Para nosso proposito iremos selecionar o primeiro card "Create a Model".Para criarmos um modelo customizado.
<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/CriandoUmModeloCustomizado.png)


### 3. Selecionar Dataset

- Seguindo nossos Objetivos.O próximo passo e selecionar nosso Dataset.Neste ponto é muito interessante, porque ele já nós traz uma serie de Dataset pre estabelecidos pronto para treinar e testar nossos modelo de ML.Como  mostra a imagem abaixo. Para este projeto como já dito anteriormente utilizarei um criado por mim com auxilio de IA(ChatGPT).Clicando no botão <<Create Dataset>>

<br>

![image]( https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/SelecionandoDataSet.png)
 
<br>

-   No SageMaker Canvas, importe o dataset que foi criado com o auxilio do ChatGPT.
<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/Selecionando%20o%20Dataset.png)

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/Criando%20o%20dataset.png)

<br>

- Selecione e faça a importação dos dados desejados.

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/Importar%20os%20dados%20para%20o%20Dataset.png)

<br>

- Após a selecionar o dataset e realizar o upload do arquivo csv esta tela deverá ser mostrada.

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/AposSelecaoDoDataset.png)

  
-   Na guia Buid, devemos selecionar a coluna do que será previsto.

 <br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/EscolaDaColunaDePrevisao.png)

 <br>

 - Podemo alterar outras configurações aqui.

   <br>

![image]( https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/ConfDaGuiaBuid.png)
  
 
-   Inicie o treinamento do modelo. Isso pode levar algum tempo, dependendo do tamanho do dataset.

>## :keyboard: Segue o prompt utilizado para gerar os dados para treinar o Modelo.
>
>ChatGPT/Copilot：

|   Ação   |                                     Prompt                                                                                                                                                                                                                                                                         |
| :------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conteúdo | Crie uma massa de dados para machine learning de pelo menos 1000 registros de produtos de caracter alimentícios 
|          | de consumo básico diário como Arroz, Feijão, Óleo, Leite,  Farinha de Trigo etc , conforme as regras abaixo:
|          | > Crie uma coluna identificadora ID_PRODUTO
|          | > Crie uma coluna NOME_DO_PRODUTO
|          | > Crie uma coluna PRECO_PODUTO
|          | >  Crie uma coluna QTD_EM_ESTOQUE
|          | >  Crie uma coluna QTD_PRODUTO_VENDIDO
|          | > Crie uma coluna PRODUTO_EM_PROMOCAO
|          | > Crie uma coluna QTD_DIAS_EM_PROMOCAO
|  Regras  | > Crie uma coluna DATA_COMPRA
|          | > Gere uma massa de dados para Machine learning de forma consistente, de forma que tenha uma boa variação de dados nas colunas QTD_PRODUTO_VENDIDO e QTD_DIAS_EM_PROMOCAO ,  |          |    com base no estoque 
|          | > Marcar PRODUTO_EM_PROMOCAO como SIM e NÃO 
|          | > Distribuir uniformente as datas de compra
|          | > Distribuír os dados  mensalmente, não ultrapassar 12 meses.
|          | > Exportar para um arquivo csv |
<br> 
-   Com o csv criado apartir do prompt acima então agora de vemos selecionar o o dataset que será usado para treinar o modelo de previsão de estoque.
-   Faça o upload do dataset no SageMaker Canvas.


### 3. Analisar

-   Após o treinamento, examine as métricas de performance do modelo.
-   Verifique as principais características que influenciam as previsões.
-   Faça ajustes no modelo se necessário e re-treine até obter um desempenho satisfatório.

### 4. Prever

-   Use o modelo treinado para fazer previsões de estoque.
-   Exporte os resultados e analise as previsões geradas.
-   Documente suas conclusões e qualquer insight obtido a partir das previsões.

## 🤔 Dúvidas?

Esperamos que esta experiência tenha sido enriquecedora e que você tenha aprendido mais sobre Machine Learning aplicado a problemas reais. Se tiver alguma dúvida, não hesite em abrir uma issue neste repositório ou entrar em contato com a equipe da DIO.
