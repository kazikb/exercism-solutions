def can_chain(dominoes):
    if len(dominoes) == 1:
        return dominoes if dominoes[0][0] == dominoes[0][1] else None

    stack =[([], dominoes)]
    while stack:
        domino_chain, domino_left = stack.pop()
        if not domino_left and (not domino_chain or domino_chain[0][0] == domino_chain[-1][1]):
            return domino_chain

        for domino in domino_left:
            if not domino_chain or domino[0] == domino_chain[-1][1]:
                next_domino = (domino_chain + [domino], domino_left.copy())
                next_domino[1].remove(domino)
                stack.append(next_domino)
            if not domino_chain or domino[1] == domino_chain[-1][1]:
                next_domino = (domino_chain + [(domino[1], domino[0])], domino_left.copy())
                next_domino[1].remove(domino)
                stack.append(next_domino)
                