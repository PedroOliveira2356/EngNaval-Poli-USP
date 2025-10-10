Para o fucionamento do código é necessário apenas ter o arquivo "Tabela_de_cotas.xlsx" no mesmo diretório, para que seja possível que o programa o acesse e faça alterações nos dados.

Não é necessária nenhuma outra ação para que o programa faça os cálculos das propriedades e plote os gráficos, mas é possível alterar o calado inicial, o passo para cada calado e o calado final nos dados que serão plotados, apenas alterando os valores no techo de "prints e resultados" como no exemplo:

 inputs = np.arange(3, 19, 1) #(calado incial, valor de parada, passo)
