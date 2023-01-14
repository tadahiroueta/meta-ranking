def getRanking() -> list:
    """Returns a list from user input with new lines as dividers"""
    ranking = []
    while True:
        option = input("Option: ")
        if option == "":
            print("<end of ranking>")
            return ranking
        ranking.append(option)


def getRankingMatrix() -> list:
    """
    Returns:
        list of descending, ranked lists of options (e.g. [
            ["A", "B", "C", "D"],
            ["B", "C", "D", "A"],
            ["C", "D", "A", "B"],
            ["D", "A", "B", "C"]
        ])
    """
    rankingMatrix = []
    while True:
        ranking = getRanking()
        if ranking == []:
            print("<end of matrix>")
            return rankingMatrix
        rankingMatrix.append(ranking)

def getRankedDictionary(rankingMatrix: list) -> dict:
    """
    Parameters:
        rankingMatrix: list of descending, ranked lists of options (e.g. [
            ["A", "B", "C", "D"],
            ["B", "C", "D", "A"],
            ["C", "D", "A", "B"],
            ["D", "A", "B", "C"]
        ])

    Returns:
        dictionary of descending ranked options with a tuple including their mean rank and a list of their rankings (e.g. {
            "A": (2.5, [1, 2, 3, 4]),
            "B": (2.5, [2, 3, 4, 1]),
            "C": (2.5, [3, 4, 1, 2]),
            "D": (2.5, [4, 1, 2, 3])
        })
    """

    # gather list of rankings
    rankingDictionary = {}
    for ranking in rankingMatrix:
        for i in range(len(ranking)):
            if ranking[i] not in rankingDictionary:
                rankingDictionary[ranking[i]] = [i + 1]

            else:
                rankingDictionary[ranking[i]].append(i + 1)

    # add estimated ranks from absences
    for ranking in rankingMatrix:
        estimatedAbsentRank = int((len(rankingDictionary) + len(ranking) + 1) / 2)
        for option in rankingDictionary:
            if option not in ranking:
                rankingDictionary[option].append(estimatedAbsentRank)

    # calculate mean rank
    for option in rankingDictionary:
        rankingDictionary[option] = (round(sum(rankingDictionary[option]) / len(rankingDictionary[option]), 1), rankingDictionary[option])

    # sort by mean rank
    return sorted(rankingDictionary.items(), key=lambda x: x[1][0])

def excelPrint(rankedDictionary: dict):
    """Prints the dictionary in an excel-like format"""
    for subject in rankedDictionary:
        print(subject[0])

    print()

    for subject in rankedDictionary:
        print(subject[1][0])

if __name__ == "__main__":
    excelPrint(getRankedDictionary(getRankingMatrix()))
    
    input() # keep console open
