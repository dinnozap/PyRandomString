from random import choice as c
""" PyRandomString """

LIST_CH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
           '9', '0', '_', '-']


def rand_str(ch_nb):
    """:param ch_nb:
    :return: Random String of length ch_nb
    """
    rdm_str = ""
    for _ in range(ch_nb):
        rdm_str += c(LIST_CH)
    print(rdm_str)
