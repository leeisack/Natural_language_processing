#크롤링한 네이버 영화 csv파일 불러오기
import pandas as pd
data = pd.read_csv('movie.csv', low_memory=False)
data.head()

data['join']=data['genre']+' '+data['story']
movie=data['join']

#정규표현식 특수문자 제거
import re
movie_data=[]
for n in movie:
    n=str(n)
    n=n.replace("\r",' ').replace("\xa0",' ')
    nr=re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>'\'…》]", '', n)
    movie_data.append(nr)

#movie_data를 list가 DataFrame으로
movie_data=pd.DataFrame(movie_data)

data['join']=movie_data

#data['join']에서 Null 값을 가진 경우에는 값 제거
data['join'] = data['join'].fillna('')

# data['join']에 대해서 tf-idf 수행
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['join'])

print(tfidf_matrix.shape)

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim)

indices = pd.Series(data.index, index=data['title']).drop_duplicates()
print(indices.head())

def get_recommendations(title, cosine_sim=cosine_sim):
    # 선택한 영화의 타이틀로부터 해당되는 인덱스를 받아온다.
    idx = indices[title]

    # 모든 영화에 대해서 해당 영화와의 유사도를 구한다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 영화들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화를 받는다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 영화의 인덱스를 받는다.
    movie_indices = [i[0] for i in sim_scores]

    # 가장 유사한 10개의 영화의 제목을 리턴한다.
    return data['title'].iloc[movie_indices]

get_recommendations('토이 스토리')