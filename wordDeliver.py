from jieba import analyse
# 引入TF-IDF关键词抽取接口

class deliver:
    data=[]

    def __init__(self,text):
        self.textAnalyse(text)

    def textAnalyse(self,text):
        tfidf = analyse.extract_tags

        # 基于TF-IDF算法进行关键词抽取
        keywords = tfidf(text)
        # print ("keywords by tfidf:")
        # 输出抽取出的关键词
        array=[]
        for keyword in keywords:
            print (keyword)
            array.append(keyword)
        self.data=array