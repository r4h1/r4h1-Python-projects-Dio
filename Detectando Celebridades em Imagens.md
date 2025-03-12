Reconhecimento de Celebridades em Imagens com Python

Este projeto utiliza a biblioteca `face_recognition` para identificar celebridades em imagens. Ele carrega um conjunto de imagens de celebridades conhecidas, codifica seus rostos e, em seguida, compara esses códigos com os rostos detectados em uma imagem de teste.

## Funcionalidades

* **Detecção de Rostos:** Identifica rostos em imagens usando a biblioteca `face_recognition`.
* **Reconhecimento de Celebridades:** Compara rostos detectados com um banco de dados de rostos conhecidos para identificar celebridades.
* **Desenho de Caixas Delimitadoras:** Desenha caixas delimitadoras ao redor dos rostos detectados e exibe os nomes das celebridades identificadas.
* **Fácil de Usar no Google Colab:** O código foi otimizado para ser executado no Google Colab, com instruções claras para upload de arquivos e visualização de resultados.

## Como Usar

1.  **Pré-requisitos:**
    * Python 3
    * Bibliotecas: `face_recognition`, `opencv-python`, `Pillow` (instaladas automaticamente no Google Colab).
2.  **Preparação:**
    * Crie uma pasta chamada `known_faces` no seu computador.
    * Adicione imagens de celebridades que você deseja reconhecer dentro desta pasta. Nomeie os arquivos de imagem com o nome da celebridade (por exemplo, `Tom_Cruise.jpg`).
    * Compacte a pasta `known_faces` em um arquivo ZIP chamado `known_faces.zip`.
    * Prepare uma imagem de teste que contenha rostos de celebridades e salve-a como `test_image.jpg`.
3.  **Executando no Google Colab:**
    * Abra um novo notebook do Google Colab.
    * Faça o upload dos arquivos `known_faces.zip` e `test_image.jpg` para o Colab.
    * Cole o código Python fornecido neste repositório em uma célula de código no Colab.
    * Execute a célula de código. O script irá instalar as bibliotecas necessárias, descompactar `known_faces.zip`, executar o reconhecimento facial e exibir a imagem resultante com as caixas delimitadoras e nomes das celebridades.
4.  **Visualizando os Resultados:**
    * A imagem com os rostos reconhecidos será exibida diretamente no notebook do Colab.

## Estrutura do Projeto

├── known_faces/        # Pasta contendo imagens de celebridades conhecidas
│   ├── Celebrity1.jpg
│   ├── Celebrity2.jpg
│   └── ...
├── known_faces.zip     # Arquivo zipado da pasta known_faces
├── test_image.jpg      # Imagem de teste para reconhecimento
└── reconhecimento_celebridades.ipynb # O notebook do Colab com o código.


## Dependências

* `face_recognition`
* `opencv-python`
* `Pillow`
* `numpy`

## Observações

* A precisão do reconhecimento facial depende da qualidade e variedade das imagens na pasta `known_faces`.
* O reconhecimento facial pode ser computacionalmente intensivo, especialmente com grandes conjuntos de dados de rostos conhecidos.
* Este projeto foi desenvolvido para fins educacionais e de demonstração. Para aplicações do mundo real, considere usar serviços ou bibliotecas de reconhecimento facial mais robustas.
* Esteja atento às questões de privacidade ao usar a tecnologia de reconhecimento facial.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.
