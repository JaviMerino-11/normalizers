from typing import List


def lower_case_normalizer(phrase_list: List[str]) -> List[str]:
    phrase_list = [lower_case.lower() for lower_case in phrase_list]
    return phrase_list