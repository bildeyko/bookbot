def get_num_words(str) -> int:
    return len(str.split())

def get_num_chars(str: str) -> dict:
    chars = {}
    for c in str:
        low = c.lower()
        if low in chars:
            chars[low] += 1
        else:
            chars[low] = 1
    return chars

def get_chars_sorted_list(chars: dict) -> list:
    new_chars = []
    for c in chars:
        new_chars.append({"char": c, "num": chars[c]})
    new_chars.sort(reverse=True, key=sort_on)
    return new_chars

def sort_on(items):
    return items["num"]