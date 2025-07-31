# Dashboard de Prestação de Contas - PNAB 📊

Este projeto apresenta um painel interativo construído com **Streamlit**, voltado para a gestão à vista de diversos projetos culturais.

## Funcionalidades

- Leitura automática de um arquivo Excel com múltiplas abas
- Menu interativo para acesso direto a cada projeto
- Indicadores (KPIs) como:
  - Valor Total Recebido
  - Valor Pago
  - Retenção IRPF
  - Restos a Pagar
  - Total de Contemplados
- Tabela com todos os dados detalhados
- Gráfico interativo de distribuição de valores por pessoa

## Como rodar localmente

1. Clone este repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute o dashboard:
   ```
   streamlit run dashboard_gestao_a_vista_pnab.py
   ```

## Deploy

Você pode hospedar esse projeto gratuitamente em [streamlit.io/cloud](https://streamlit.io/cloud).
