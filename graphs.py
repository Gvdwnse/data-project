python3
import ipywidgets as widgets
def plot_wb(wb_fosl, country): 
    I = wb_fosl['country'] == country
    ax=wb_fosl.loc[I,:].plot(x='year', y='fosl', style='-o', legend=False)
    ax.set_ylabel('% of total')
    ax.set_title('Energy production from fossil fuels 1975-2015')