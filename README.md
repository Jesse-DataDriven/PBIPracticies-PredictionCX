# PBIPracticies-PredictionCX
Here my projects in Pbix front end to prective and statistic CX
# Predição de Experiência do Cliente (CX) | Metodologia Lean Six Sigma

![Demonstração do Dashboard](https://i.postimg.cc/gkGWL3QK/01-Algoritmo-de-Predicao-de-NPS.gif)

## 📌 Visão Geral
Este projeto foi desenvolvido utilizando a metodologia **DMAIC** para identificar os principais drivers de satisfação do cliente. Através de modelos de regressão, foi possível prever o impacto de variáveis operacionais no NPS (Net Promoter Score), permitindo uma tomada de decisão proativa e baseada em dados.

> **Nota de Confidencialidade:** Devido a políticas de LGPD, dados sensíveis e nomes de colunas reais foram omitidos ou mascarados. O foco deste repositório é demonstrar a arquitetura da solução e os resultados de negócio obtidos.

## 🚀 Resultados Alcançados (Ciclo Improve)
A implementação do algoritmo de predição e o ajuste nos processos internos geraram resultados expressivos entre Junho e Novembro de 2025:

* **NPS (Net Promoter Score):** Saltou de **35,77%** (Início do DMAIC) para **57,50%** (Pós-Improve).
* **Monitoramento (Aderência ao Processo):** Evoluiu de **87,04%** para **96,50%**.
* **Impacto:** A predição permitiu identificar exatamente em quais alavancas de monitoramento atuar para maximizar a percepção de valor do cliente.

## 🛠️ Ferramentas Utilizadas
* **Estatística:** Minitab (Modelagem de Regressão e Validação de Hipóteses). Utilizei regressão logística para identificar padrões de comportamento do usuário que correlacionam com notas baixas. O dashboard permite filtrar por risco de churn.
* **Business Intelligence:** Power BI (Visualização de dados e Dashboards interativos).
* **Lógica de Dados:** DAX (Métricas calculadas para simulação de cenários).
* **Metodologia:** Lean Six Sigma (Foco em redução de variabilidade e melhoria de processos).

## 📈 Modelagem Estatística
Nesta seção, detalho como cheguei aos coeficientes de predição:
* **Variáveis analisadas:** [% de aderência processos internos, Reclamações públicas, reclamaç~eos internas, Tempo de resposta, Nota esforço].
* **Saída:** Probabilidade de [Churn/Satisfação NPS].

## 📂 Estrutura do Repositório
* `/visuals`: GIF de navegação e prints das análises estatísticas no Minitab.
* `/metrics`: Documentação das fórmulas DAX e lógica de predição.
* `/documentation`: Case Study completo detalhando as etapas de Define, Measure, Analyze, Improve e Control.
* `/results`: Tabelas de coeficientes e resultados consolidados.

## 👤 Autor
**Jessé DataDriven** - https://www.linkedin.com/in/jesse-oliveira-de-castro-88421536/
