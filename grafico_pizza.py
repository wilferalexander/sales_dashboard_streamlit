import pandas as pd
import plotly.express as px

def crear_grafico(df):
	df_review = df.groupby('review_score').agg(
		total_ventas= ('cantidad_itens', 'sum')
	).reset_index()

	colors = ['#0077b6','#1a4d83','#063970','#2f567D','#4B6A92']
	fig = px.pie(df_review,
		values = 'total_ventas',
		names = 'review_score',
		title = 'Clasificacion de las ventas',
		color_discrete_sequence = colors
	)

	fig.update_layout(yaxis_title = 'Clasificacion', xaxis_title ='Ventas', showlegend= False)
	fig.update_traces(textposition = 'inside', textinfo='percent+label', insidetextfont=dict(size=16))

	return fig


