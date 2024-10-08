# Especifica o nome do arquivo CSV
nome_arquivo = 'veiculos.tsv'

# Abre o arquivo para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Cria o objeto writer com delimitador de tabulação
    writer = csv.DictWriter(arquivo_csv, fieldnames=["Codigo","Fabricante","Modelo","Ano","Cor","Motor","Preço"], delimiter='\t',)
    
    # Escreve os cabeçalhos
    writer.writeheader()