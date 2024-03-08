def obter_recomendacao_vestimenta(temperatura, clima):
    if clima.lower() == 'céu limpo':
        if temperatura > 30:
            return "Hoje o dia está bem quente! Recomendamos roupas leves, como shorts, camisetas e chapéu para se proteger do sol."
        elif 20 <= temperatura <= 30:
            return "Dia ensolarado! Um look confortável com camiseta, calça ou bermuda seria ideal."
        else:
            return "Dia de sol, mas um pouco mais fresco. Considere uma jaqueta leve ou suéter."
        
    elif clima.lower() == 'nublado':
        return "O céu está nublado. Opte por roupas mais leves, mas tenha algum recurso extra para caso esfrie."
    
    elif clima.lower() == 'chuva':
        return "Hoje pode chover. Recomendamos uma capa de chuva ou guarda-chuva, além de roupas impermeáveis."
    
    elif clima.lower() == 'neve':
        return "Está nevando! Vista-se com roupas térmicas, casaco quente, e não se esqueça das botas."
    
    elif clima.lower() == 'tempestade':
        return "Há previsão de tempestade! Use roupas impermeáveis e evite tecidos metálicos."
    
    elif clima.lower() == 'neblina':
        return "Névoa no ar. Escolha roupas que proporcionem boa visibilidade e mantenha-se aquecido."


    return "Recomendação de vestimenta não disponível para este clima."