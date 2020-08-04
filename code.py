import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'svg' 
plt.style.use('fivethirtyeight')


dec6 = pd.read_csv(r'coinmarketcap_06122017.csv')
market_cap_raw = dec6[['id','market_cap_usd']]
#selecting only the market capitalization
print(market_cap_raw.count())

#there are some cryptocurrencies listed in coinmarketcap.com have no known market capitalization,
#these need to be removed for proper analysis

cap = market_cap_raw[market_cap_raw['market_cap_usd']> 0]

#exploring the market share of Bitcoins
TOP_CAP_YLABEL = '% of total cap'
total=cap['market_cap_usd'].sum()
# Selecting the first 10 rows and setting the index
cap10 = cap.head(10).set_index('id')
fig, ax = plt.subplots(figsize =(15, 7)) 
# Calculating market_cap_perc
cap10=cap10.assign(market_cap_perc=cap10['market_cap_usd']/total*100)
ax.bar(cap10.index,cap10['market_cap_perc']) 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
# Plotting the barplot with the title defined above 
plt.savefig('Top-10-market-capitalization.png', dpi=300, bbox_inches='tight')
plt.show()

volatility = dec6[['id', 'percent_change_24h','percent_change_7d']]
v_24h = volatility.query('percent_change_24h != \'NaN\'')

TOP_CAP_TITLE = 'Top 10 highly volatile cryptocurrencies in a day'
TOP_CAP_YLABEL = '% change in 24 hrs'
v_24h_top_10=v_24.head(10)
v_24h_top_10.plot.bar(x='id',y='percent_change_24h') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('Top-10-highly-volatile-cryptocurrencies-in-a-day.png', dpi=300, bbox_inches='tight')
plt.show()

TOP_CAP_TITLE = '24 hours top losers'
TOP_CAP_YLABEL = '% change in 24 hrs'
v_24h_top_10=v_24.tail(10)
v_24h_top_10.plot.bar(x='id',y='percent_change_24h') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('24-hours-top-losers.png', dpi=300, bbox_inches='tight')
plt.show()

v_w=volatility.query('percent_change_7d != \'NaN\'')
v_w=v_w.sort_values(by='percent_change_7d',ascending=False)

TOP_CAP_TITLE = '1 week top winners'
TOP_CAP_YLABEL = '% change in a week'
v_w_top_10=v_w.head(10)
v_w_top_10.plot.bar(x='id',y='percent_change_7d') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('1-week-top-winners.png', dpi=300, bbox_inches='tight')
plt.show()

TOP_CAP_TITLE = '1 week top losers'
TOP_CAP_YLABEL = '% change in a week'
v_w_top_10=v_w.tail(10)
v_w_top_10.plot.bar(x='id',y='percent_change_7d') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('1-week-top-losers.png', dpi=300, bbox_inches='tight')
plt.show()

top_cap=dec6.sort_values(by='market_cap_usd',ascending=False)

TOP_CAP_TITLE = '24 hour change for top cryptocurencies'
TOP_CAP_YLABEL = '% change in a day'
v_w_top_10=top_cap.head(10)
v_w_top_10.plot.bar(x='id',y='percent_change_24h') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('24-hour-change-for-top-cryptocurencies.png', dpi=300, bbox_inches='tight')
plt.show()

TOP_CAP_TITLE = '24 hour change for top cryptocurencies'
TOP_CAP_YLABEL = '% change in a day'
v_w_top_10=top_cap.head(10)
v_w_top_10.plot.bar(x='id',y='percent_change_24h') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('24-hour-change-for-top-cryptocurencies.png', dpi=300, bbox_inches='tight')
plt.show()

TOP_CAP_TITLE = '1 week change for top cryptocurencies'
TOP_CAP_YLABEL = '% change in a day'
v_w_top_10=top_cap.head(10)
v_w_top_10.plot.bar(x='id',y='percent_change_7d') 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 2)
plt.ylabel(TOP_CAP_YLABEL)
plt.title(TOP_CAP_TITLE)
# Plotting the barplot with the title defined above 
plt.savefig('1-week-change-for-top-cryptocurencies.png', dpi=300, bbox_inches='tight')
plt.show()
