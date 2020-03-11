# 코드 작성전 어떤 그림이 그려질지 상상하자 

# import 
import re, glob, json, os
from string import ascii_lowercase

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt 
%matplotlib inline


# 파일 목록 보기 =>  파일명 전부 확득  
try:
    path = './input/train/*.txt'
    file_list = glob.glob(path)
    print('정상작동\n',file_list)
    
except Exception as e :
    print('에러발생', e)


# -----------
# 변수
file_path_input  = './input/'
file_path_output = './output/'
file_name        = 'labels_freqs_data'
full_path_input  = file_path_input  + file_name
full_path_output = file_path_output + file_name
# -----------


# get_data() 함수 
def get_data(file_path):

    base_name = os.path.basename(file_path)
    p = re.compile('^[a-z]{2}')
    lng_code = p.match(base_name).group()

    try:
        with open( file_path, encoding='utf-8') as f :
            text = f.read().lower() 
            p    = re.compile('[^a-z]*')
            text = p.sub('', text)

        print('정상작동', f,'\n','='*70 )

    except Exception as e:

        print('에러발생', e)


    counts = [0] * 26 # counts = [0 for n in range(26)]
    ASCII_A = ord('a')
    for i in text:
        counts[(ord(i)-ASCII_A)] += 1
    
    total_counts = sum(counts)  
    frequences = list(map(lambda x:x/total_counts, counts)) 

    return lng_code, frequences


# get_data() # 함수 확인 


# load_data()함수
# defult = path = 'train' (지금은 생략 )
def load_data(path):

    file_path_input  = './input/'
    file_boxs = glob.glob(file_path_input + '{}/*txt'.format(path))

    labels = list()
    freqs  = list()

    for box in file_boxs:
        lng,freq = get_data(box)
        labels.append( lng )
        freqs.append( freq )

    return {'labels ':labels , 'freqs': freqs } #  {'labels':['en','fr'], 'freqs': [[],[]] } 


# try_load()함수
def try_load( name, option, encoding='utf-8'):
    file_path_input  = './input/'
    file_path = file_path_input + '{}.json'.format(name)
    
    try:
        with open( file_path , option) as f:
            if option == 'w' :
                train_data = load_data('train')
                test_data  = load_data('test')
                data = [train_data, test_data]
                # print(type(data))
                json.dump(data,f)

            elif option == 'r' :  
                tmp = json.load(f)
                # print(tmp)
                print('\n길이 =', len(tmp)) 
                return tmp

        print('정상동작')

    except Exception as e:
        print('에러발생', e )

    return  


# sklearn
from sklearn import svm, metrics
from sklearn.externals import joblib

try_load('test_data', 'w')
freq = try_load('test_data', 'r')

print(len(freq[0]['labels']),len(freq[0]['freqs']))
print(len(freq[1]['labels']),len(freq[1]['freqs']))


clf = svm.SVC( gamma = 'auto' )
clf.fit(freq[0]['freqs'],freq[0]['labels'])
predict = clf.predict(freq[1]['freqs'])
# print(predict)
metrics.classification_report(freq[1]['labels'], predict )

try:
    joblib.dump(clf,'./output/clf_lang_20200310.model')
except Exception as e:
    print('에러발생', e )

label_dic = {
    'en':'영어',
    'fr':'프랑스어',
    'tl':'타갈리아어',
    'id':'인도네시아어'
}

try:
    with open('clf_labels.json', 'w', encoding='utf-8' ) as f:
    json.dump(label_dic, f)
    print('정상동작')

except Exception as e:
    print('에러발생', e )

