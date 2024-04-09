#!/usr/bin/python3
"""
module that contain -
function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""
def text_indentation(text):
    """
    Print the text with 2 new lines after each '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    start_of_line = True
    for char in text:
        if char == ' ' and start_of_line:
            continue
        print(char, end='')
        if char in punctuation_marks:
            print('\n\n', end='')
            start_of_line = True
        elif char == '\n':
            start_of_line = True
        else:
            start_of_line = False

if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
