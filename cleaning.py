# import pandas as pd
# import nltk
# from nltk.stem import PorterStemmer
# import re
# from nltk.corpus import stopwords


# df = pd.read_csv("DataNeuron_Text_Similarity.csv")

# all_stopwords = stopwords.words("english")
# all_stopwords.remove("not")
# all_stopwords.remove("nor")
# all_stopwords.remove("no")

# ps = PorterStemmer()

# corpus1 = []
# for i in range(df["text1"].shape[0]):
#     rev = re.sub("[^a-zA-Z]"," " ,df["text1"][i])
#     rev = rev.lower()
#     rev = rev.split()
#     rev = [ps.stem(word) for word in rev if not word in set(all_stopwords) ]
#     rev = " ".join(rev)
#     corpus1.append(rev)

# corpus2 = []
# for i in range(df["text2"].shape[0]):
#     rev = re.sub("[^a-zA-Z]"," " ,df["text2"][i])
#     rev = rev.lower()
#     rev = rev.split()
#     rev = [ps.stem(word) for word in rev if not word in set(all_stopwords) ]
#     rev = " ".join(rev)
#     corpus2.append(rev)
    
# data = pd.DataFrame([corpus1,corpus2]).T
# data = data.rename({0:"text1", 1:"text2"}, axis= 1)

