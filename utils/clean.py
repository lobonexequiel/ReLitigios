import re
import nltk
import spacy

stops = nltk.corpus.stopwords.words('spanish')


def general(txt):
    """
        elimina caracteres no deseados
        w = texto tipo string
    """
    txt = txt.translate(str.maketrans(
        'áéíóúýàèìòùÁÉÍÓÚÀÈÌÒÙÝ', 'aeiouyaeiouAEIOUAEIOUY'))
    txt = txt.lower()
    txt = txt.replace('\r', ' ').replace('\n', ' ').replace("\v", ' ').replace(
        "\t", ' ').replace("\f", ' ').replace("\a", ' ').replace("\b", ' ')
    txt = re.sub(r'[^\w\s]', ' ', txt)
    txt = re.sub(r'\d+', ' ', txt)
    txt = re.sub(' +', ' ', txt)
    txt = txt.strip()
    return txt


def deleteRepeated(row):
    row = row.split()
    i = 0
    while i < len(row) - 1:
        if row[i] == row[i + 1]:
            del row[i]
        i += 1
    return ' '.join(row)


def remove_stops(texto):
    texto = [
        i for i in texto.split() if i not in stops
    ]
    return ' '.join(texto)


def numtex2num(texto, index_final_word=-2, symbol='$'):
    """Función que recorre el texto reemplazando los números escritos

    :param texto: str, texto
    :param index_final_word: int, es el índice antes del cual será
    insertado el número
    :returns: str, texto limpio

    """
    texto = texto.lower().split()
    num = ''
    i = 0
    while i < len(texto):
        if texto[i] in Traductor().get_full_dic():
            num += texto[i] + ' '
            texto.remove(texto[i])
        else:
            i += 1

    texto.insert(index_final_word, ' '+symbol+str(utils.string2int(num))+' ')
    return ' '.join(texto)


def lemmatize(texto ,nlp):
    """Función que devuelve el texto lematizado

    Args:
        texto (str): texto a lematizar

    Returns:
        str: texto lematizado
    """    
    lem = nlp(texto)
    try:
        return ' '.join([i.lemma_ for i in lem])
    except NameError:
        nlp = spacy.load('es_core_news_md')
        return ' '.join([i.lemma_ for i in lem])

