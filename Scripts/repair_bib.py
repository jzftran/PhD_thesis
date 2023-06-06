#%%
import glob
#%%
for file in glob.glob('./*.bib'):
    print(file)
    with open(file, 'r', encoding="utf8") as f :
        filedata = f.read()
    # filedata = filedata.replace('\\c{a}', '\\k{a}')
    # filedata = filedata.replace('\\c{e}', '\\k{e}')
    # filedata = filedata.replace('–', '--')
    # filedata = filedata.replace('−', '--')
    filedata = filedata.replace('ı́', '\\\'{i}')
    filedata = filedata.replace('{\\\'{\\i}}', '\\\'{i}')
    filedata = filedata.replace('@misc', '@online')
    filedata = filedata.replace('howpublished', 'url')
    
    
    with open(file, 'w', encoding="utf8") as f:
        f.write(filedata)
        f.close()

# %%
