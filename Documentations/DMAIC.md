# 📘 Ciclo DMAIC — Projeto PredictionCX

O projeto **PredictionCX** aplica rigorosamente a metodologia **DMAIC (Define, Measure, Analyze, Improve, Control)** para estruturar, validar e implementar um modelo preditivo de Qualidade, NPS e Menções Negativas, integrando ciência de dados, estatística e visualização analítica no Power BI.

Este documento descreve cada fase do ciclo, as entregas, os insights e os resultados alcançados.

---

# 🟦 1. DEFINE — Definir

## 🎯 Objetivo do Projeto
Desenvolver um modelo preditivo capaz de:
- Antecipar o NPS com base em variáveis operacionais.
- Prever evolução da Qualidade e impacto no bônus da equipe.
- Identificar alavancas que reduzem menções negativas na jornada.
- Automatizar relatórios e análises recorrentes.

## 🧩 Problema de Negócio
A operação apresentava:
- Variabilidade elevada nos indicadores.
- Baixa previsibilidade de NPS.
- Dificuldade em identificar causas raiz.
- Ações reativas e pouco orientadas por dados.

## 👥 Stakeholders
- Operações  
- Qualidade  
- CX  
- Analytics  
- Liderança executiva  

---

# 🟧 2. MEASURE — Medir

## 📊 Coleta de Dados
Foram utilizados:
- Bases históricas de Qualidade  
- NPS por jornada  
- Menções categorizadas  
- Indicadores operacionais  
- Logs de monitoramento  

## 📏 Tratamento e Padronização
- Remoção de outliers  
- Normalização de variáveis  
- Criação de variáveis derivadas  
- Correlação entre indicadores  

## 📈 Métricas de Referência
- Qualidade inicial: **87,04% (Jun/25)**  
- NPS médio histórico  
- Menções negativas por categoria  
- Projeção de atingimento de meta: **85% (Jun/25)**  

---

# 🟨 3. ANALYZE — Analisar

## 🔬 Modelos Estatísticos Aplicados
- Regressão Linear  
- Regressão Lasso (modelo final)  
- Testes de significância  
- Análise de sensibilidade  
- Intervalos de confiança  

## 📌 Resultados Científicos
| Métrica | Resultado |
|--------|-----------|
| **R² Lasso** | 0,84 |
| **R² Linear** | 0,70 |
| **Significância** | 95% (α = 0,05) |
| **Margem de erro** | 0,015 |
| **Acuracidade média** | 96% |

## 🧠 Principais Insights
- Qualidade é a variável mais influente no NPS.  
- Pequenas variações de monitoramento geram impacto direto no indicador.  
- Menções negativas têm comportamento preditivo por categoria.  
- A operação possui espaço claro para otimização.

---

# 🟩 4. IMPROVE — Melhorar

## 🚀 Ações Implementadas
- Criação de algoritmo preditivo no Power BI com parâmetro dinâmico.  
- Simulações de cenários (85% → 100% de monitoramento).  
- Storytelling das alavancas de impacto.  
- Automação de relatórios operacionais.  

## 📈 Resultados Obtidos
### Qualidade
- Evolução: **87,04% → 92,53% (Jun/25 → Out/25)**  
- Crescimento absoluto: **+5,49 p.p.**

### Bônus da Equipe
- Projeção Junho: **85%**  
- Projeção Dezembro: **100%**  
- Ganho previsto: **+15 p.p.**

### NPS
- Aumento consistente conforme simulações e ações priorizadas.

---

# 🟫 5. CONTROL — Controlar

## 🛡️ Mecanismos de Controle
- Dashboard preditivo no Power BI.  
- Parâmetros dinâmicos para simulação contínua.  
- Monitoramento mensal de Qualidade e NPS.  
- Revisão trimestral dos coeficientes do modelo.  

## 📘 Documentação
- Notebook com camadas do modelo.  
- Métricas e simulações.  
- Resultados científicos.  
- Storytelling e visuais.  
- PPT DMAIC (anexado no repositório).  

---

# 🏁 Conclusão

O ciclo DMAIC aplicado ao PredictionCX permitiu:
- Estruturar o problema com clareza.  
- Medir e analisar com rigor estatístico.  
- Implementar melhorias com impacto real.  
- Criar mecanismos de controle sustentáveis.  

O resultado é um modelo preditivo robusto, replicável e integrado ao fluxo de decisão da operação.

---

# 🎖️ Badges do Projeto

![DMAIC](https://img.shields.io/badge/DMAIC-Lean%20Six%20Sigma-28a745?style=for-the-badge&logo=leanpub&logoColor=white)
![Minitab](https://img.shields.io/badge/Minitab-Statistical%20Validation-1f77b4?style=for-the-badge&logo=google-analytics&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Predictive%20Analytics-f2c811?style=for-the-badge&logo=powerbi&logoColor=black)

