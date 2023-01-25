#%%
import urllib.request
from bs4 import BeautifulSoup
import matplotlib as plt
import pandas as pd

def pubs_by_year(link):
    """Fetches count of publications published in Pubmed in each year based on search query."""
    page = urllib.request.urlopen(link)
    htmlSource = BeautifulSoup(page, "html.parser")
    counts = {"counts":{}}
    yeartable = htmlSource.select('#timeline-table')[0]
    yeartable_body = yeartable.find('tbody')
    for row in yeartable_body.find_all("tr"):
        cells = row.find_all("td")
        year = cells[0].find(text=True).strip()
        count = cells[1].find(text=True).strip()
        counts['counts'][year] = count
    return counts



Ag_toxicity_query = 'https://pubmed.ncbi.nlm.nih.gov/?term="silver+toxicity"'
Hg_toxicity_query = 'https://pubmed.ncbi.nlm.nih.gov/?term="mercury+toxicity"'
ag = pubs_by_year(Ag_toxicity_query)
hg = pubs_by_year(Hg_toxicity_query)
#%%
ag = pd.DataFrame(ag).rename({'counts':'Search query: "silver toxicity"'},axis=1)
hg = pd.DataFrame(hg).rename({'counts':'Search query: "mercury toxicity"'},axis=1)
ag_hg = pd.concat([ag,hg], axis=1)
ag_hg = ag_hg.iloc[1: , :].fillna(0)
ag_hg = ag_hg.astype('int')
#%%
ag_hg.sort_index(inplace=True)
ax = ag_hg.plot(style=('o-'), markersize=4)
ax.set_xlabel("Year")
ax.set_ylabel("Number of results")
ax.axvline(x=64, linestyle='--', color='black')
# %%
fig = ax.get_figure()
fig.savefig('./gfx/ag_hg_count.png',transparent=True, dpi=300)
