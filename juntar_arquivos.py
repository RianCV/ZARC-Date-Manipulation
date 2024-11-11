import pandas as pd
import glob

#creates pandas series with the paths of the csv files for each seed
urls_trigo = pd.Series(glob.glob('./trigo/*.csv'))
urls_cafe = pd.Series(glob.glob('./cafe/*.csv'))
urls_cana = pd.Series(glob.glob('./cana/*.csv'))
urls_feijao = pd.Series(glob.glob('./feijao/*.csv'))
urls_milho = pd.Series(glob.glob('./milho/*.csv'))
urls_soja = pd.Series(glob.glob('./soja/*.csv'))
urls_trigo = pd.Series(glob.glob('./trigo/*.csv'))
urls_arroz = pd.Series(glob.glob('./arroz/*.csv'))


def junta_arquivos(nome_arquivo, *urls): #function that will concatenate different CSVs into one
    urls_list = []
    for url in (urls):
        df = pd.read_csv(url)
        urls_list.append(df)
    cultura_total = pd.concat(urls_list,ignore_index=True)
    cultura_total.to_csv(nome_arquivo, index=False)

#runs the function for each seed forming csv files ending with '_TOTAL'
junta_arquivos("./arroz/arroz_TOTAL.csv", *urls_arroz.tolist())
junta_arquivos("./cafe/cafe_TOTAL.csv", *urls_cafe.tolist())
junta_arquivos("./cana/cana_TOTAL.csv", *urls_cana.tolist())
junta_arquivos("./feijao/feijao_TOTAL.csv", *urls_feijao.tolist())
junta_arquivos("./milho/milho_TOTAL.csv", *urls_milho.tolist())
#junta_arquivos("./soja/soja_TOTAL.csv", *urls_soja.tolist()) #not necessary (there is only one file)
junta_arquivos("./trigo/trigo_TOTAL.csv", *urls_trigo.tolist())



#merges all the FINAL files into one (final part of the task)
urls_arquivos_finais = pd.Series(glob.glob('./arquivos_finais/*.csv'))
junta_arquivos("./arquivos_finais/all_cultures_final.csv", *urls_arquivos_finais.tolist())

