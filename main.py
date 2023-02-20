import csv


INPUT_FILENAME = "./data/input.txt"
OUTPUT_FILENAME = "./data/output.csv"


def getInput() -> dict:
    """
    Returns:
        dictionary of sources and their rankings (e.g. {
            "sourceA": ["B", "C", "D"],
            "sourceB": ["C", "D", "A"],
            "sourceC": ["D", "A", "B"],
            "sourceD": ["A", "B", "C"]
        })
    """
    input = {}
    source = None
    with open(INPUT_FILENAME, "r") as file:
        for line in file:
            line = line.strip()

            if source is None:
                source = input[line] = []
                continue

            if line == "":
                source = None
                continue

            source.append(line)

    return input

def getRanking(input: dict) -> list:
    """
    Parameters:
        dictionary of sources and their rankings (e.g. {
            "sourceA": ["B", "C", "D"],
            "sourceB": ["C", "D", "A"],
            "sourceC": ["D", "A", "B"],
            "sourceD": ["A", "B", "C"]
        })

    Returns:
        list of dictionaries of subjects (e.g. [
            {
                "name": "A",
                "sourceA": 1,
                "sourceB": 3,
                "sourceC": 4,
                "sourceD": 1,
                "rank": 1.8
            },
            {
                "name": "B",
                "sourceA": 2,
                "sourceB": 1,
                "sourceC": 2,
                "sourceD": 2,
                "rank": 1.8
            }
        ])
    """

    # gather list of rankings
    rankings = {}
    for sourceKey, sourceValue in input.items():

        for i in range(len(sourceValue) - 1, -1, -1):
            sourceSubject = sourceValue[i]

            if sourceSubject not in rankings:
                rankings[sourceSubject] = {}
            

            rankings[sourceSubject][sourceKey] = i + 1


    # add estimated ranks from asbsences
    for _, subjectValue in rankings.items():
        for sourceKey, sourceValue in input.items():

            if sourceKey not in subjectValue:
                subjectValue[sourceKey] = (len(rankings) + len(sourceValue) + 1) / 2

    # calculate mean rank
    for _, subjectValue in rankings.items():
        subjectValue["rank"] = round(sum(subjectValue.values()) / len(subjectValue), 1)

    # add subject names
    for subjectKey, subjectValue in rankings.items():
        subjectValue["subject"] = subjectKey

    # sort by mean rank
    return [ value for _, value in sorted(rankings.items(), key=lambda item: item[1]["rank"]) ]

if __name__ == "__main__":
    rankings = getRanking(getInput())
    with open(OUTPUT_FILENAME, "w", newline="") as file:
        writer = csv.writer(file)

        # my God there must be a better way to do this
        mostKeys = list(rankings[0].keys())
        mostKeys.remove("subject")
        keys = ["subject"]
        keys.extend(mostKeys)

        writer.writerow(keys)
        for subject in rankings:
            writer.writerow([ subject[key] for key in keys ])
