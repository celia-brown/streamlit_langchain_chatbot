# streamlit_langchain_chatbot

本项目为聊天与翻译机器人项目，利用Streamlit 构建 Web 应用，使用外部库，如 langchain_community、dashscope 等，用于调用特定的 AI 模型或处理数据。
看官若喜欢，请点个star哦~~~
展示页面如下：
![image](https://github.com/user-attachments/assets/59cef960-dec7-4df8-b686-bf56ff027729)

![image](https://github.com/user-attachments/assets/ab3749a9-5fa4-4845-a956-70a36ef647f8)

![image](https://github.com/user-attachments/assets/9592ac2c-10e1-48ab-a4f3-6eeba17f34d3)

# 版本情况
python==3.10
langchain==0.2.8
langchain-community==0.2.7
streamlit==1.36.0

# 注意！！！！
在app.py中，由于API-KEY值涉及个人信息和隐私，各位对API-KAY的值需要修改，如何获取API-KEY值，大家请看以下流程~~~

1. 进入阿里的通义官网https://tongyi.aliyun.com/

2. 选择“阿里云百炼”，进入阿里云百炼官网

![image](https://github.com/user-attachments/assets/ff6bd10c-eb80-4955-9187-9964d89e855d)

4. 在应用创建中，选择“立即创建”

![image](https://github.com/user-attachments/assets/25d6f17b-dce5-4ab8-9f08-28e1c5a9fa46)


5. 选择“新增应用”

![image](https://github.com/user-attachments/assets/744bcceb-d0e6-49bb-849a-9138666d66f3)

6. 选择“模型”，点击发布即可

 ![image](https://github.com/user-attachments/assets/f96002dd-1357-409d-9b11-bf2be6cf2903)

7. 在右上角“用户”，点开“API-KEY”

![image](https://github.com/user-attachments/assets/cd1b9b8c-3b1a-4c50-b49b-7e37767babe6)

8. 点击“查看”，可以知道完整的API-KEY，复制API-KEY

![image](https://github.com/user-attachments/assets/acddb11b-ef62-49c4-b5fa-ee4fd4329c01)

9. 打开环境变量，在系统变量中，创建-----变量名写DASHSCOPE_API_KEY，变量值写API-KEY

![image](https://github.com/user-attachments/assets/505277ea-8302-4ef0-9a52-f138f89ec598)

10. 最后，在app.py中修改一下API-KEY

![image](https://github.com/user-attachments/assets/b173abb6-fbcf-435c-96d5-6d72d9777a77)

各位就可以运行啦~~~~
如有问题，欢迎提问~~~
    

















