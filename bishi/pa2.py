#由于xpath提取的都是空值一直没试出正确的数据xpath路径，所以爬取失败
import requests
from lxml import html
import pandas as pd
data = pd.DataFrame(columns=['isin','Bond_Code', ' Issuer', 'Bond_Type','Issue_Date', ' Latest_Rating'])
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
pageList = []
isin_list =  []
Bond_Code_list = []
Issuer_list =[]
Bond_Type_list = []
Issue_Date_list=[]
Latest_Rating_list=[]
for i in range(1,8):
        formdata = {'pageNo':i,'pageSize':15,'bondType':100001,'issueYear':2023}

        etree=html.etree
        headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

        r = requests.post(url, timeout=30, headers=headers,params=formdata)
        print(r.status_code)
        r.encoding = r.apparent_encoding
        selector = etree.HTML(r.text)
        isin = selector.xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tr/td/span/a/text()')
        isin_list+=isin
        Bond_Code= selector.xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/table/tr/td[2]/span/a/text()')
        Bond_Code_list+=Bond_Code
        Issuer = selector.xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/table/tr/td[3]/span/text()')
        Issuer_list+=Issuer
        Bond_Type = selector.xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/table/tr/td[4]/span/text()')
        Bond_Type_list+=Bond_Type
        Issue_Date  = selector.xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/table/tr/td[5]/span/text()')
        Issue_Date_list+=Issue_Date
        Latest_Rating = selector.xpath('/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/table/tr/td[6]/span/text()')
        Latest_Rating_list+=Latest_Rating
data['isin']=isin_list
data['Bond_Code']=Bond_Code_list
data['Issuer']=Issuer_list
data['Bond_Type']=Bond_Type_list
data['Issue_Date']=Issue_Date_list
data['Latest_Rating']=Latest_Rating_list
data.to_csv(r'D:\pycharmproject\pachong\yichuanren.csv')