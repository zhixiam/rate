# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:00:02 2023

@author: mot66
"""

import requests
from bs4 import BeautifulSoup
import time

if __name__ == "__main__":
    
    headers = {
        'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        
    url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
    
    # 發送HTTP請求獲取網頁內容
    response = requests.get(url)

    # 檢查是否成功獲取網頁
    if response.status_code == 200:
            # 使用Beautiful Soup解析HTML內容
            soup = BeautifulSoup(response.text, 'html.parser')
    
    currency_rows = soup.find_all(class_="currency")
    #當前時間
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fp = open('.匯率.txt','w',encoding='utf-8')
    for row in currency_rows:
        # 提取貨幣名稱（例如，"美元"）
        currency_name = row.find(class_='col-auto px-3 col-lg-5 title-item').text
        currency_name = currency_name.strip()
        #貨幣縮寫(如:USD)
        currency_en = row.find(class_='title-en').text
        currency_en = currency_en.strip()
        #即期匯率
        buy_rate = row.find(class_="BBoardRate").text
        sell_rate = row.find(class_="SBoardRate").text
        #網銀/App優惠
        app_buy_rate = row.find(class_="BuyIncreaseRate").text
        app_sell_rate = row.find(class_="SellDecreaseRate").text
        #現金匯率
        cash_buy_rate = row.find(class_="CashBBoardRate").text
        cash_sell_rate = row.find(class_="CashSBoardRate").text
        cash = ''
        if cash_buy_rate != '':
            cash = '現金匯率:'
        if cash_sell_rate != '':
            cash = '現金匯率:'
            
        # 打印提取的數據或將其存儲在數據結構中（例如，列表、字典）
        print(f"貨幣：{currency_name} {currency_en}")
        print(f"買入:即期匯率：{buy_rate} 網銀/App優惠:{app_buy_rate} {cash}{cash_buy_rate}")
        print(f"賣出:即期匯率：{sell_rate} 網銀/App優惠:{app_sell_rate} {cash}{cash_sell_rate}")
        print("\n")
        fp.write(f'貨幣:{currency_name} {currency_en}\n')
        fp.write(f"買入:即期匯率：{buy_rate} 網銀/App優惠:{app_buy_rate} {cash}{cash_buy_rate}\n")
        fp.write(f"賣出:即期匯率：{sell_rate} 網銀/App優惠:{app_sell_rate} {cash}{cash_sell_rate}\n")
        fp.write(f'\n')
    print(time)
    fp.write(f'{time}\n')
    fp.close()
        
    
        
    
    
    
    