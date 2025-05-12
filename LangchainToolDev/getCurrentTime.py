from langchain_core.tools import tool
import cloudpickle
import datetime

class GetTime():

    def create_tools(self):

        @tool
        def get_current_time() -> str:
            """获取当前时间的函数
            :return: 当前的时间
            """
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return current_time

        tools = [get_current_time]

        return tools


langChainName = "常用工具"
serialized_langchain = GetTime()
with open(f"{langChainName}.pkl", "wb") as f:
    cloudpickle.dump(serialized_langchain, f)