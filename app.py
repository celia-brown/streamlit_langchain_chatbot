import streamlit as st
from langchain_community.llms import Tongyi
from streamlit_option_menu import option_menu
from dashscope import Generation
import datetime
import base64
from langchain.prompts import ChatPromptTemplate

API_KEY = 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

menu0 = "首页"
menu1 = "聊天机器人"
menu2 = "翻译机器人"

st.sidebar.title("🌼 Tools 🌼")

with st.sidebar:
    menu = option_menu("功能分类", [menu0, menu1, menu2],
                       icons=['house', "list-task", "translate", ],
                       # menu_icon="cast",
                       default_index=0)


def main():
    if menu == menu0:
        showmenu0()

    if menu == menu1:
        showLLMChatbot()

    if menu == menu2:
        showmenu2()


def get_image_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def showmenu0():
    image_path = "E:/pycharm/shengchanshixi/huahui/pictures/flowe.jpg"
    base64_image = get_image_as_base64(image_path)

    # 使用 CSS 设置图片圆角
    st.markdown(
        f"""
        <style>
        .round-corner-image {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
            border-radius: 15px;
        }}
        </style>
        <img src="data:image/jpg;base64,{base64_image}" class="round-corner-image" />
        """,
        unsafe_allow_html=True
    )
    st.title(" 欢迎观看骰子🎲队的作品~~~~")
    st.caption("🚀 A Streamlit Chatbot Simulation")
    st.balloons()
    st.write()


def save_chat_history():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_history_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for message in st.session_state.messages:
            f.write(f"{message['role']}: {message['content']}\n\n")
    st.success(f"聊天记录已保存到 {filename}")


def showLLMChatbot():
    st.title("(๑́•∀•๑̀)ฅ  LLM聊天机器人")

    st.markdown("""
    欢迎使用我们的LLM聊天机器人！ta支持多轮对话哦~~~
    """)

    # 初始化聊天历史
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 添加清除聊天记录的按钮
    col1, col2 = st.columns(2)
    with col1:
        if st.button("新建对话"):
            st.session_state.messages = []
            st.experimental_rerun()

    # 添加保存聊天记录的按钮
    with col2:
        if st.button("保存对话"):
            save_chat_history()

    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 获取用户输入
    if prompt := st.chat_input("在这里输入你的问题..."):
        # 将用户输入添加到聊天历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 显示"正在思考"的消息
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("正在思考...")

            # 准备完整的对话历史
            full_conversation = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])

            try:
                # 调用通义千问 API
                gen = Generation()
                response = gen.call(
                    model='qwen-turbo',
                    prompt=full_conversation,
                    api_key=API_KEY
                )

                # 将 AI 回复添加到聊天历史
                assistant_response = response["output"]["text"]
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                message_placeholder.markdown(assistant_response)

            except Exception as e:
                error_message = f"抱歉，发生了一个错误：{str(e)}"
                st.session_state.messages.append({"role": "assistant", "content": error_message})
                message_placeholder.markdown(error_message)


def showmenu2():
    st.title("🤖翻译机器人")
    st.markdown("""
        ( つ•̀ω•́)つ  帮助你实现不同语言之间的翻译
    """)
    # 创建语言选择器
    input_language = st.selectbox("选择输入语言:", ["英语", "汉语", "法语", "德语", "西班牙语"])
    output_language = st.selectbox("选择输出语言:", ["汉语", "英语", "法语", "德语", "西班牙语"])
    chat_input = st.chat_input("请输入要翻译的文本：")
    if chat_input:
        st.chat_message("user").write(chat_input)

        # 创建prompt模板
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system",
                 f"你是一位专业的翻译，能够将{{input_language}}翻译成{{output_language}}，并且输出文本会根据用户要求的任何语言风格进行调整。请只输出翻译后的文本，不要有任何其它内容。"),
                ("human", f"文本：{chat_input}")
            ]
        )

        # 准备prompt值
        prompt_value = prompt_template.format_messages(input_language=input_language,
                                                       output_language=output_language,
                                                       text=chat_input)

        # 设置翻译模型并生成翻译结果
        model = Tongyi(model_name='qwen-max')
        result = model.invoke(prompt_value)

        st.chat_message("assistant").write(f"{result}")


if __name__ == "__main__":
    main()
