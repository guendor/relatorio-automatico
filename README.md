<h1 align="center" id='titulo-e-imagem-de-capa'>

**Automatizador de Relatórios**

</h1>

<p align="center">
<img src="assets/%C3%ADcone-autom%C3%A1tico-da-resposta-da-resposta-do-email-o-auto-envia-78256838.jpg" alt="Carta aberta com seta circular ao fundo, indicando renovação" width="200">
</p>

<p align='center' id='badges'>
<img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Badge em Desenvolvimento">
<img src='https://img.shields.io/badge/Version-V1.0-blue' alt='Badge Versão'>
<img src='https://img.shields.io/github/stars/guendor?style=social' alt='Badge Stars'>
</p>

<p id='descriçao-do-projeto'>

É um Script para a automatização de rotinas através de instruções dadas aos periféricos da máquina, com auxílio de bibliotecas como [Pyautogui](https://pyautogui.readthedocs.io/en/latest/) e [Pandas](https://pandas.pydata.org/docs/), caso necessário.

</p>

<h2 align='left' id='indice'>

* [Título e imagem de capa](#titulo-e-imagem-de-capa)
* [Badges](#badges)
* [Descrição do Projeto](#descriçao-do-projeto)
* [Índice](#indice)
* [Funcionalidades e Instruções](#funcionalidade)
* [Acesso ao Projeto](#acesso)
* [Tecnologias Utilizadas](#tecnologias)
* [Pessoas Desenvolvedoras](#devs)

</h2>

<h2 id='funcionalidade'>

**Funcionalidades do projeto**

</h2>

---

* `Funcionalidade 1`: Ferramenta para identificar o posicionamento do mouse na máquina: Abra a ferramenta e rode o script. Por padrão o programa aguarda 3 segundos e retorna a posição do mouse em coordenadas x, y. Caso precise de mais tempo altere o parâmetro da função sleep() na celula.

* `Funcionalidade 2`: Automação dos periféricos mouse e teclado: Utilizando os comandos do [Pyautogui](https://pyautogui.readthedocs.io/en/latest/), instrua o passo a passo que a máquina deverá cumprir para completar a rotina. Faça uso da `Funcionalidade 1` para localizar com precisão onde serão dados os clicks.

* `Funcionalidade 3`: Leitura e análise de banco de dados: Através da biblioteca [Pandas](https://pandas.pydata.org/docs/), faça a leitura da base de dados baixada, separe as informações e índices relevantes para sua rotina em variáveis para serem chamadas na `Funcionalidade 4`.

* `Funcionalidade 4`: Abertura do provedor de Mailing e envio de relatório: Prepare o corpo do texto do seu relatório que será enviado (passo 6), insíra as variáveis com as informações relevantes nele. Use as `Funcionalidades` anteriores para indicar corretamente a sequência de ações e enviar o informativo.

<h2 id='acesso'>

*📁* Acesso ao projeto

</h2>

---

Você [pode acessar o código fonte do projeto inicial](https://github.com/guendor/relatorio-automatico) ou [baixá-lo](https://github.com/guendor/relatorio-automatico/archive/refs/heads/master.zip).

## 🛠️ Abrir e rodar o projeto

---

Após baixar o projeto, você pode abrir com qualquer interpretador de python. Para isso, na tela de launcher clique em:

* **Abrir Pasta** (ou opção similar)
* Procure o local onde o projeto está e o selecione (Caso o projeto esteja zipado, é necessário extraí-lo antes de procurá-lo)
* Clique em OK

O interpretador deve executar algumas tasks para configurar o projeto, aguarde até finalizar. Ajuste o programa as necessidades da rotina que você deseja automatizar, utilizando as `Funcionalidades` disponíveis. Execute o programa.

<h2 id='tecnologias'>

Técnicas e tecnologias utilizadas

</h2>

---

* `Python`

<h2 id='devs'>

Autor

</h2>

---

[<img src='assets/octacat1.png' width=180><br><sub>Raphael "Guendor" Izidio</sub>](https://github.com/guendor)
