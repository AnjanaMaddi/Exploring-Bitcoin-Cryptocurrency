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


#volatile natute of Bitcoins
#change in 24 hours
