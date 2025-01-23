# def cryptography(word: str, encode=True) -> str:
#     results = ""

#     for letter in word:
#         current_idx = word.index(letter) + 1
#         alpha_idx = alphabet.index(letter)
#         try:
#             if encode:
#                 results += alphabet[alpha_idx + current_idx]
#             else:
#                 results += alphabet[alpha_idx - current_idx]
#         except:
#             results += alphabet[alpha_idx - (26 - current_idx)]
#     return results


# if __name__ == "__main__":
#     alphabet = "abcdefghijklmnopqrstuvwxyz"

#     word = "cryptography"
#     encoded_word = cryptography(word)
#     decoded_word = cryptography(encoded_word, encode=False)
# print(encoded_word, decoded_word)


######### Recommended Changes
"""
Turns out .index() only gets the index of the first occurrence so it a letter shows up more than once it is an issue so we switched to enumerate.

Ord() makes sense too because it removes the dependency on the alphabet string!
"""


def revised_cryptography(word: str, encode=True) -> str:
    results = ""

    for idx, letter in enumerate(word):
        current_idx = idx + 1
        alpha_idx = ord(letter) - ord("a")

        # This actually handles the wrap around piece for us by returning the remainder if/when
        # we go beyond the 26 values
        # Example y = position 25 and let's say the current idx is 4 and we're encoding
        # (25 + 4) = 29 % 26 = 3 -- so it would shift forward 4 positions landing on C after the rap around
        if encode:
            new_idx = (alpha_idx + current_idx) % 26
        else:
            new_idx = (alpha_idx - current_idx) % 26

        results += chr(new_idx + ord("a"))

    return results


if __name__ == "__main__":
    word = "cryptography"
    encoded_word = revised_cryptography(word)
    decoded_word = revised_cryptography(encoded_word, encode=False)
    print(encoded_word, decoded_word)
