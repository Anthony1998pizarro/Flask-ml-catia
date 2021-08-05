from controllers.nlp_controller import stemmerBolsaPalabras, lowercase, deleteChars, tokenizertext, stemmer, stopWords
from controllers.read_text_controller import readTxt
from controllers.jaccard_controller import vectores
from controllers.coseno_controller import coseno
import numpy as np
import json


def predict_text(text):
    data_A = []
    data_B = []
    data_C = []
    text_1=[]
    text_2=[]
    text_3=[]
    text_4=[]
    text_5=[]
    text_1.append(lowercase([text]))
    text_2.append(deleteChars(text_1[0]))
    text_3.append(tokenizertext(text_2[0]))
    text_4.append(stemmer(text_3[0]))
    text_5.append(stopWords(text_4[0],1))
    data_A.append(stemmerBolsaPalabras(readTxt('models/data/dic_epc.txt')))
    data_B.append(stemmerBolsaPalabras(readTxt('models/data/dic_mbm.txt')))
    data_C.append(stemmerBolsaPalabras(readTxt('models/data/dic_ec.txt')))

    jacc_epc= vectores(text_5[0],data_A[0])
    jacc_mbm = vectores(text_5[0],data_B[0])
    jacc_ec = vectores(text_5[0],data_C[0])
    cos_epc = coseno(text_5[0],data_A[0])
    cos_mbm = coseno(text_5[0],data_B[0])
    cos_ec = coseno(text_5[0],data_C[0])

    return json.dumps({"jacc_epc":jacc_epc[0],"jacc_mbm":jacc_mbm[0],"jacc_ec":jacc_ec[0],"cos_epc":cos_epc,"cos_mbm":cos_mbm,"cos_ec":cos_ec
})













