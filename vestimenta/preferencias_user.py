
def obter_preferencias_usuario():
    print("\nVamos escolher a roupa ideal para você se vestir hoje!\n")


    try:
        orçamento = float(input("Qual é o seu orçamento total para as peças de roupa? R$: "))
        if orçamento < 0:
            raise ValueError("O orçamento não pode ser negativo.")
        
        genero = input("\nVocê é homem ou mulher? (h/m): ").lower()
        if genero not in ['h', 'm']:
            raise ValueError("Por favor, escolha 'h' para homem ou 'm' para mulher.")
        
        print("\nEscolha o estilo desejado:")
        print("1. Casual ")
        print("2. Social ")
        print("3. Minimalista ")
        print("4. Preppy (Old Money)")
        print("5. Country")
        print("6. Glam")
        print("7. Streetwear")
        print("8. Skate")
        print("9. Hip Hop")
        print("10. Gótico")
        print("11. Grunge")
        print("12. Punk")
        print("13. Boho (Boêmio Contemporâneo)")        
        

        estilo_opcao = input("\nDigite o número correspondente ao estilo desejado: ")
        estilo_info = None

        if estilo_opcao in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
            if estilo_opcao == '1':
                estilo = 'Casual'   
                estilo_info = "\nSurgiu na classe operária britânica dos anos 1970 um desejo de se distinguir"\
                    "por seu jeito de vestir. Isso se manifestou através do uso de marcas esportivas estrangeiras: "\
                        "os jovens fãs de futebol toda semana transformavam os estádios em passarelas. O estilo casual "\
                            "foi o primeiro a dar tanta importância para os logotipos. Eles não só estavam na moda, como"\
                                "também ajudavam a identificar para qual time cada um torcia."
                
            elif estilo_opcao == '2':
                estilo = 'Social'
                estilo_info = "\nAs roupas sociais têm que vestir o corpo com caimento perfeito, é isso que garante o estilo"\
                    "elegante do seu visual. Os homens, por exemplo, devem optar por calças de corte reto, blazers que não fiquem"\
                        "muito justos ou muito largos. É importante que as mangas terminem na altura dos ossinhos dos punhos."

            elif estilo_opcao == '3':
                estilo = 'Minimalista'
                estilo_info = "\nA princípio, o movimento minimalista nasceu como um braço da arte do início do século XX. Esse estilo começou"\
                    "a decolar nos anos 1990 e foi o antagonista reservado, tranquilo e modesto do glamour ostentoso da moda da década de 1980. "\
                        "Hoje, estamos vendo a segunda onda de popularidade do minimalismo, por conta da ideologia anticonsumismo, que está se tornando um estilo de vida."
                
            elif estilo_opcao == '4':
                estilo = '\nPreppy (Old Money)'
                estilo_info = "O desejo de imitar as classes mais abastadas deram origem ao estilo preppy depois da Segunda Guerra Mundial. "\
                    "Esse estilo era inspirado pelo uniforme de universidades e escolas de elite nos Estados Unidos, que preparavam seus alunos "\
                        "para ocuparem os cargos mais influentes do país. Hoje em dia, o preppy continua a ser um símbolo de privilégio e da estética old money."
                
            elif estilo_opcao == '5':
                estilo = 'Country'
                estilo_info = "\nNa década de 1920, surgiu o gênero western no cinema. Hollywood romantizou a figura do caubói, "\
                    "o colonizador da segunda metade do século XIX, e o transformou em um personagem nômade, solitário, valente e digno, "\
                        "com seu estilo único. Mais tarde, nos anos 1970, Ralph Lauren retornou à moda country, buscando resgatar um estilo nacional estadounidense."
                
            elif estilo_opcao == '6':
                estilo = 'Glam'
                estilo_info = "\nA história do estilo glamouroso representa a evolução dos padrões de beleza e a libertação das mulheres"\
                    "das obrigações e restrições sociais do passado. Ao deixar os espartilhos nos anos 1920, as mulheres conscientes de "\
                        "sua sexualidade começaram a ressaltá-la. As divas de Hollywood dos anos 1930 e 1940 criaram uma imagem de mulher sensual, "\
                            "poderosa e sofisticada, um ideal que muitas imitam até hoje."

            elif estilo_opcao == '7':
                estilo = 'Streetwear'
                estilo_info = "\nInspirado principalmente pelo hip hop, skateboard e surf nos anos 1980, o streetwear mudou completamente o modelo de moda tradicional."\
                    "Se antes os estilistas, varejos e editoriais de moda determinavam as tendências, agora quem passou a fazer isso foram os consumidores."\
                        "O streetwear depende das redes sociais onde esse mesmo público determina o que vai estar em alta na próxima temporada."
                
            elif estilo_opcao == '8':
                estilo = 'Skate'
                estilo_info = "\nNos anos 1960, o skate tomou conta da Califórnia e se tornou um estilo de vida, influenciando a moda, o gosto musical e simbolizando o espírito de rebeldia jovem."

            elif estilo_opcao == '9':
                estilo = 'Hip Hop'
                estilo_info = "\nO gênero musical mais popular do mundo não apenas definiu uma geração inteira nos anos 1980, como também moldou a muda urbana da época."\
                    "O paradoxo do hip hop é que os jovens afro-americanos imitavam o estilo da classe média, enquanto a classe média de zonas suburbanas se sentiam"\
                        "atraídos pela imagem romantizada da vida nos guetos e imitavam seu estilo."
                
            elif estilo_opcao == '10':
                estilo = 'Gótico'
                estilo_info = "\nA cultura gótica, com sua obsessão por morte, temáticas obscuras e um estilo de vestir inspirado na literatura e cinema de terror contrastava"\
                    "muito com a moda alegre dos anos 1980. Os jovens com seu cabelo tingido de preto e pele pálida pareciam personagens das histórias de Edgar Allan Poe, "\
                        "Mary Shelley ou H.P. Lovecraft. Hoje, a geração Z segue experimentando com esse estilo, graças à popularidade de séries como Vandinha da Netflix."
                
            elif estilo_opcao == '11':
                estilo = 'Grunge'
                estilo_info = "\nO estilo de moda mais antimoda que existe foi popularizado por bandas como Nirvana, Sonic Youth e Pearl Jam, no final dos anos 1980 e "\
                    "comecinho dos anos 1990. Os adeptos desse estilo expressavam seus niilismo e anticonsumismo no seu modo de vestir."
                
            elif estilo_opcao == '12':
                estilo = 'Punk'
                estilo_info = "\nCom o seu manifesto “Não há futuro” os punks rechaçavam as tradições culturais e convenções sociais, adaptando uma postura antissistema"\
                    "e comportamento provocador. Vivienne Westwood e seu marido Malcolm McLaren são ícones desse estilo e capturaram o espírito de rebeldia da época,"\
                        "refletindo-o em sua loja, Let It Rock, em Londres em 1974."
                
            elif estilo_opcao == '13':
                estilo = 'Boho (Boêmio Contemporâneo)'
                estilo_info = "\nO movimento boêmio recebeu esse nome por conta dos ciganos que chegaram à Europa pela região da Boêmia. "\
                    "Esse estilo geralmente expressa um interesse por poesia, arte, literatura e por um estilo de vida alternativo."
                
            if estilo_info:
                informacao_sobre_estilo = input(f"\nDeseja obter mais informações sobre o estilo '{estilo}'? (s/n): ").lower()
                if informacao_sobre_estilo == 's':
                    print(estilo_info)
                
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 13.")
            return None

    
        #ocasiao = input("Para qual ocasião você está procurando roupas? (Trabalho, esportes, praia, etc.): ").lower()
        
        #cores = input("informe uma paleta de 2 a 3 cores que deseja montar sua vestimenta").lower()

        tamanho = input("Qual é o seu tamanho de roupa? (pp,p,m,g,gg) ")

        tipo_roupas = int(input("Você está procurando por roupas inferiores (1), superiores(2) ou calcados(3)? "))

        #material = input("Algum material de roupa que você prefere ou evita? ").lower()
        #marcas_favoritas = input("Você tem alguma marca favorita ou prefere opções mais acessíveis? ").lower()

        return {
            "orçamento": orçamento,
            "genero": genero,
            "estilo": estilo,
            #"ocasiao": ocasiao,
            #"cores": cores,
            "tamanho": tamanho,
            "tipo_roupas": tipo_roupas,
            #"material": material,
            #"marcas_favoritas": marcas_favoritas,
        }
    
    except ValueError as e:
        print(f"Erro de entrada: {e}")
        return None  
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return None
    
