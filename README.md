# 《CodeWeaver》：AI系統紡織機

![image](https://github.com/hank1224/CodeWeaver/blob/main/.github/workflows/A08Poster.png)

## 設計架構圖

![image](https://github.com/hank1224/CodeWeaver/blob/main/.github/workflows/Architecture%20Diagram.jpg)

![image](https://github.com/hank1224/CodeWeaver/blob/main/.github/workflows/Functions.jpg)

## 需設置環境變數

創建.env檔案輸入key，可參考.env.example檔案
```env
DJANGO_SECRET_KEY='django-insecure-^2^0qd(@mq-p03et2tp)6qyh(qj6-$i!mdka$dpi5x*$**f#36'
DJANGO_DEBUG=True

# 官方的key
OPENAI_API_KEY=sk-*************
```

[0.0.0.0:8000/webpages/test_index](http://0.0.0.0:8000/webpages/test_index) - 測試圖片庫讀取 和 OpenAI API key讀取

[0.0.0.0:8000/gpt_handler](http://0.0.0.0:8000/gpt_handler) - 測試OpenAI API
