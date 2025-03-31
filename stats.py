def number_of_words(file_contents) -> int:
    return len(file_contents.split())

def character_count(file_contents) -> dict:
    norm = file_contents.lower()
    characterMap = {}
    for char in norm:
        if char not in characterMap:
            characterMap[char] = 1
        else:
            characterMap[char] += 1

    return characterMap


def sort_on(dict):
    return dict["count"]

def list_of_dicts(counts):
    unsortedList = []
    for count in counts:
        unsortedList.append({"char":count, "count":counts[count]})

    unsortedList.sort(reverse=True, key=sort_on)
    return unsortedList