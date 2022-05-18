from typing import List
from normalizer_functions.lower_case_normalizer import lower_case_normalizer
from normalizer_functions.no_accents_nor_specialcharac import no_accents_nor_specialcharac
from normalizer_functions.remove_double_white_spaces import remove_double_white_spaces


def normalizer(phrase_list: List[str], result: List[str] = None) -> List[str]:
    phrase_list_lower_case = lower_case_normalizer(phrase_list)
    phrase_list_unaccented_no_special_characters = no_accents_nor_specialcharac(phrase_list_lower_case)
    phrase_list_without_white_spaces = remove_double_white_spaces(phrase_list_unaccented_no_special_characters)
    normalized_phrase_list = phrase_list_without_white_spaces

    print('INPUT: %s' % phrase_list)
    print('OUTPUT: %s' % normalized_phrase_list)
    return normalized_phrase_list


def main() -> None:
    phrase_list = ['Hola', 'múndó', 'ñoño', 'cosas  que haCer']
    normalizer(phrase_list)


if __name__ == '__main__':
    main()
