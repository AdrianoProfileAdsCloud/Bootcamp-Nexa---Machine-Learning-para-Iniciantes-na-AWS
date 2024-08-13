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

<br>

### 3. Selecionar Dataset

- Seguindo nossos Objetivos.O próximo passo e selecionar nosso Dataset.Neste ponto é muito interessante, porque ele já nós traz uma serie de Dataset pre estabelecidos pronto para treinar e testar nossos modelo de ML.Como  mostra a imagem abaixo. Para este projeto como já dito anteriormente utilizarei um criado por mim com auxilio de IA(ChatGPT).

<br>

## :keyboard: Segue o prompt utilizado para gerar os dados para treinar o Modelo.

>ChatGPT/Copilot：

|   Ação   |                                     Prompt                                                                                                                                                                                                                                                                         |
| :------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conteúdo | Atue como um cientista de dados e crie um dataset para treinar um modelo de Machine Learning de pelo menos 1000 registros de produtos de carácter alimentícios como arroaz, 
|          | feijão, macarrão, leite, açúcar conforme as regras abaixo para um Sistema de Gerenciamento Inteligente de estoque:
|          | > Crie uma coluna identificadora ID_PRODUTO, número incremental
|          | > ID_PRODUTO 10 diferentes por dia
|          | > Crie uma coluna NOME_DO_PRODUTO
|          | > Crie uma coluna PRECO_PODUTO
|          | >  Crie uma coluna QTD_EM_ESTOQUE
|          | >  Crie uma coluna QTD_PRODUTO_VENDIDO
|          | > Crie uma coluna PRODUTO_EM_PROMOCAO
|          | > Crie uma coluna QTD_DIAS_EM_PROMOCAO
|  Regras  | > Crie uma coluna DATA_COMPRA inicando por 2022 até 2024
|          | > Gere dados de forma consistente, de tal modo que tenha uma boa variação de dados nas colunas QTD_PRODUTO_VENDIDO e QTD_DIAS_EM_PROMOCAO 
|          | > Garantir que cada produto tenha uma quantidade inicial em estoque e o mesmo vá decrescendo de maneira variavel dia a dia em relação a QTD_PRODUTO_VENDIDO
|          | > Marcar PRODUTO_EM_PROMOCAO como SIM e NÃO 
|          | > Exportar para um arquivo csv |
<br> 

- Observação:
  Pode ser que o ChatGPT não gere o arquivo diretamente, fiz algumas vezes ele gerou o arquivo para download em outras vezes foi necessário executar alguns passos no VSCode para poder gerar o arquivo.O código abaixo assim como as instruções de como gerar o arquivo é fornecido pelo próprio ChatGPT quando ele não gera o arquivo automaticamente para download.

 ```python

 import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações
num_registros = 1000
produtos = [
    "Arroz", "Feijão", "Óleo", "Leite", "Farinha de Trigo",
    "Açúcar", "Sal", "Macarrão", "Café", "Manteiga",
    "Queijo", "Presunto", "Molho de Tomate", "Aveia", "Farinha de Mandioca"
]

# Função para gerar dados aleatórios
def gerar_dados():
    dados = []
    hoje = datetime.today()
    for i in range(num_registros):
        id_produto = i + 1
        nome_do_produto = random.choice(produtos)
        preco_produto = round(random.uniform(1.0, 20.0), 2)
        qtd_em_estoque = random.randint(0, 200)
        qtd_produto_vendido = random.randint(0, qtd_em_estoque)
        produto_em_promocao = random.choice(["SIM", "NÃO"])
        qtd_dias_em_promocao = random.randint(0, 30) if produto_em_promocao == "SIM" else 0
        data_compra = hoje - timedelta(days=random.randint(0, 365))
        dados.append([
            id_produto, nome_do_produto, preco_produto, qtd_em_estoque, qtd_produto_vendido,
            produto_em_promocao, qtd_dias_em_promocao, data_compra.strftime("%Y-%m-%d")
        ])
    return dados

# Gerar dados e criar DataFrame
dados = gerar_dados()
df = pd.DataFrame(dados, columns=[
    "ID_PRODUTO", "NOME_DO_PRODUTO", "PRECO_PRODUTO", "QTD_EM_ESTOQUE",
    "QTD_PRODUTO_VENDIDO", "PRODUTO_EM_PROMOCAO", "QTD_DIAS_EM_PROMOCAO", "DATA_COMPRA"
])

# Exportar para CSV
df.to_csv("produtos_dados.csv", index=False)

print("Arquivo CSV gerado com sucesso!")

```
<br>

## Como Executar.

 - Instale as Bibliotecas Necessárias:
Certifique-se de que as bibliotecas pandas e numpy estão instaladas. Você pode instalar usando pip:
<br>

```python
pip install pandas
```
<br>

- Execute o Código:
Copie o código acima para um arquivo Python (por exemplo, gerar_dados.py) e execute-o:

```python
python gerar_dados.py
```
<br>
 Isso criará um arquivo produtos_dados.csv no mesmo diretório onde o script foi executado, contendo os dados gerados.
 <br>

  
-   Com o csv criado apartir do prompt acima então agora de vemos selecionar o o dataset que será usado para treinar o modelo de previsão de estoque.
-   Faça o upload do dataset no SageMaker Canvas.

- Clicando no botão Importar --> Tabular.

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/ImportandoODataSet.png)
 
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

 - Podemos alterar outras configurações aqui.

   <br>

![image]( https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/ConfDaGuiaBuid.png)

<br>

- Inclusivel entre essas configurações se encontra uma opção muito útil para o que estamos tentando prever que e a programação de feriados.

 <br>

  ![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/FeriadosParaPrecisaodaPrevisao.png)
  
 
-  Antes iniciar o treinamento do modelo. O pode levar algum tempo, dependendo do tamanho do dataset. Devemos ter em mente entre qual processo devemos escolher.
   Entre: Standart Build ou Quick Build, sendo que:
   Ao escolher Standart Build o processo será mais lento para criação, no entanto teremos um modelo mais consistente, mais preciso.
   Entretanto ao ecolher Quick Build o processo de criação será mais rápido, o que resultará em um modelo menos consistente,portanto menos preciso.
<br>

  ![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/TiposDeBuild.png)

  <br>

  - É importante avisar que enquanto houver incosistência no dataset importado, seremos avisados para corrigir antes de prosseguir! Na verdade nem segue enquando não estiver tudo ok.

<br>

 ![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/ErrosNoBuild.png)



### 3. Analisar
<br>

 ![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/Predi%C3%A7%C3%A3o.png
)

<br>

# Entendendo um pouco as Métricas.

  **wQLA** Average Weighted Quantile Loss (wQL) é uma métrica usada para avaliar a precisão de previsões probabilísticas. Aqui está uma análise do conceito:
  <br>
  **MAPE** É uma métrica direta e amplamente usada para avaliar a precisão da previsão, com sua principal força sendo sua interpretabilidade como uma porcentagem de erro. No entanto, deve-se tomar cuidado em situações em que os valores reais podem ser próximos de zero, pois isso pode levar a valores de erro enganosamente altos.
  <br>
 **WAPE** Fornece uma medida mais robusta e realista da precisão da previsão em comparação ao MAPE, particularmente em casos com grande variabilidade nos valores reais. Ele pondera os erros de acordo com o tamanho dos valores reais, oferecendo um melhor reflexo do desempenho geral da previsão.
 <br>
 **RMSE** É uma métrica valiosa para avaliar a precisão da previsão, particularmente quando erros maiores são mais críticos e devem ser penalizados mais pesadamente. Sua sensibilidade a erros grandes e interpretação direta o tornam útil para
 <br>
 **MASE** Fornece uma medida normalizada de precisão de previsão ao comparar um modelo de previsão a um modelo de benchmark ingênuo. Sua independência de escala e capacidade de lidar com dados sazonais tornam o MASE uma ferramenta valiosa para avaliar a precisão de modelos de previsão, especialmente em cenários com variação significativa de escala ou padrões sazonais.
 <br>
 Em geral é considerado satisfatório um modelo preciso quando os valores detas métricas estiverem próximas de ZERO.
 <br>

-   Com o modelo já treinado podemos examinar as métricas de performance do modelo.
-   Verificar as principais características que influenciam as previsões.
-   Podemos e devemos realizar ajustes no modelo e re-treina-lo até obter um desempenho satisfatório de acordo com as métricas exlicadas acima.

### 4. Prever
<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/AnaliseDePredi%C3%A7%C3%A3o.png)

<br>

![image](https://github.com/AdrianoProfileAdsCloud/Bootcamp-Nexa-Machine-Learning-para-Iniciantes-na-AWS/blob/main/imagens/AnaliseDaPreci%C3%A7%C3%A3oEseusPesos.png)

<br>

-   Este modelo treinado ajudará fazer previsões de estoque.Para sabermos a um determinado prazo o que devemos ter em estoque ou não. Pois de acordo com a analise das métricas podemos ver os produtos de maior procura e os que menos são procurados. Inclusivé saber quando ocorre esta procura se são em dias de semana, finais de semana ou em feriados.
-   Exporte os resultados e analise as previsões geradas.
-   Documente suas conclusões e qualquer insight obtido a partir das previsões.

  # Entendendo os percentis (P10,P50 e P90)
  <br>
  Esses percentis representam as previsões, em que:
  <br>

  **P10** Siginificado uma previsão pessimista
  <br>
  **P50** Significado uma previsão normal
  <br>
  **P10** Significa uma previsão otimista
  <br>
  Desta forma conseguir analisar a demanda por determinado produto seja ela pessimista, normal ou otmista.Com base nessa alalise podemos ter um estoque mais coerente,no que diz respeito a compra de produtos certos de acordo com sua procura.
  <br>
  Ao final podemos exortar a predição em dois formatos: CSV ou IMAGEN.


