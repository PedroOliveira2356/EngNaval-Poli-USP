Passo 1: Instalar Python, numpy e matplotlib

Passo 2: Abrir o arquivo parametrizacao.pdf.
Nesse arquivo, constam as referencias de cada ponto (numeros de 0 a 14) e cada distância significativa (B1, H3) para parametrizar o problema.
B -> Boca; distância lateral
H -> altura

Passo 3: abrir inputs.csv
Será a partir dos pontos e distâncias da figura que você deverá editar o arquivo inputs.csv. Toda a geometria da plataforma depende desses parâmetros. Vale destacar que os segmentos serão espelhados (a parametrização ocorre apenas para uma metade da seção mestra, mas o código espelha as linhas e cria a seção inteira)

- R_cantos: o raio do quarto de círculo nos cantos da seção
- H_fundo: a altura da quilha
- H1, H2, H3, H4: as alturas das 4 seções laterais
- B1, B2: comprimento lateral das 2 seções centrais
- B_costas: o comprimento da porção lateral onde constam os reforçadores do costado
- Comprimento SM: comprimento da seção mestra (valor a ser extrudado a partir do sketch)
- Ref-T, Ref-L: dimensões dos reforçadores em T e L; o primeiro valor corresponde à altura do reforçador, o segundo corresponde ao comprimento da parcela horizontal. Em caso de duvidas, comparar os valores com a foto do arquivo reforcadores.jpeg

- Número de reforçadores por seção: aqui, cada codigo "x-y" representa um par de pontos, como ilustrado na figura parametrizacao.pdf, e o número ao lado corresponde ao número de reforçadores daquele segmento de linha entre os dois pontos.

- Calado, carga: definidos conforme a ficha do professor para o Suezmax de Minimo custo
- Mesh seed: a seed que define o mesh; para a parametrizacao atual, esse valor cria ~190 mil elementos

Pode mudar os valores acima, respeitando que todos os valores numericos devem ser colocados em formato "float", com separador decimal de ponto '.', exceto o número de reforçadores, que deverá ser inteiro.

IMPORTANTE: foi estabelecido que a espessura de todo o chapeamento será de 12mm. Pode alterar a outro valor, mas todo o chapeamento sempre terá esse mesmo valor. Eu vi que os reforçadores em T eram de 15 na sua parte superior/horizontal, mas não consegui selecionar apenas eles para esse valor, então tudo está como 12. Duvido enormemente que isso vai fazer tanta diferença e, principalmente, que o professor vai se importar com isso.

Passo 4: rodar script make_abaqus_file.py
Umas vez alterados os parametros acima, sempre salve o arquivo inputs.csv. Depois disso, rode o arquivo make_abaqus_file.py. Não é necessário alterar nada.

Como está configurado, ele cria o arquivo Model.py e um desenho esquemático com as linhas do sketch. Caso queira desabiliar esse desenho, basta abrir o arquivo e comentar a penultima linha, "draw_segments(composed_segments)". A ultima linha, "make_file()" efetivamente escreve o arquivo que será usado no Abaqus.

Dica: antes de rodar esse script, convem renomear o arquivo Model.py que foi criado anteriormente, pois o script vai apagá-lo e escrever um novo arquivo.

Passo 5: Rodar no Abaqus

- 5.1: Verifique o diretorio em uso em File -> Set work directory, pois é nesse local que o Abaqus vai escrever os arquivos de saída das simulacoes
- 5.2: Vá em File -> Run script, navegue até a pasta atual e selecione o arquivo Model.py. O Abaqus vai receber todos os dados, criar o mesh e o job.

MUITO IMPORTANTE: você deverá averiguar a direção das forças atuantes no modelo. Eu não consegui deixar todas com a mesma orientação, então, em alguns casos, as forças estão opostas ao que deveria. Para corrigir isso, vá em Loads -> load manager e clique-duplo em cada uma das forças criadas. Você verá que a região onde a força é aplicada pode ser selecionada e o Abaqus dá a opção de girar a superfície (flip surface). Faça as alterações apropriadas para cada caso. VOCÊ DEVERÁ REPETIR ESSE PASSO A CADA VEZ QUE CRIAR UMA SEÇÃO NOVA (ou seja, cada vez que rodar o script do Model.py no Abaqus)

IMPORTANTE: perceba que eu já criei uma interação entre os vértices laterais do navio e os Reference Points correspondentes, e já criei também as condições de contorno dessa região. Caso haja outros contornos, precisa ser feito manualmente (e refazer sempre que criar um modelo novo)

IMPORTANTE: não foi possível criar os Paths, isso também terá que ser feito manualmente

Passo 6: rodar o Job
Após verificar as forças, Paths e criar as demais condições da simulação, submeter o Job e coletar todos os gráficos
