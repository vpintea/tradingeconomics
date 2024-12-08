import pandas as pd
import matplotlib
import plotly.graph_objs as go
pd.set_option('display.max_columns', None)
matplotlib.use('TkAgg')

def plot(merged_df):

    date_values = merged_df.iloc[:, 0]
    currency = merged_df.columns[1]
    currency_values = merged_df.iloc[:, 1]
    bond_yield = merged_df.columns[2]
    bond_yield_values = merged_df.iloc[:, 2]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=date_values,
        y=currency_values,
        mode='lines+markers',
        name=currency,
        marker=dict(color='blue', size=3),
        line=dict(color='blue'),
        yaxis='y1',
        hovertemplate='Currency: %{y:.4f}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=date_values,
        y=bond_yield_values,
        mode='lines+markers',
        name=bond_yield,
        marker=dict(color='green', symbol='triangle-up', size=4),
        line=dict(color='green'),
        yaxis='y2',
        hovertemplate='Bond Yield: %{y:.2f}<extra></extra>'
    ))

    fig.update_layout(
        title=f'MXNUSD and 10-Year Bond Yield for Mexico Over Time',
        xaxis=dict(title='Date', tickformat='%Y-%m-%d'),
        yaxis=dict(
            title=currency,
            titlefont=dict(color='blue'),
            tickfont=dict(color='blue'),
            showgrid=False,
        ),
        yaxis2=dict(
            title=bond_yield,
            titlefont=dict(color='green'),
            tickfont=dict(color='green'),
            overlaying='y',
            side='right',
            showgrid=False,
            automargin=True,
            range=[bond_yield_values.min(), bond_yield_values.max()]
        ),

        hovermode='x unified',
        legend=dict(orientation="h", yanchor="top", y=-0.2, xanchor="center", x=0.5),
        template='plotly_white'
    )

    fig.show()