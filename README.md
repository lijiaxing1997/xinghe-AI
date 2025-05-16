<picture>
  <source media="(prefers-color-scheme: light)" srcset="标题.png">
  <img alt="" src="标题.png"  width="full">
</picture>
<h1 align="center">LangChain & MCP 统一调用的 AI 🤖</h1>



# 简介

兴河 AI Assistant 是一个通用型Agent，旨在完成用户交代的各种任务，可以根据需求连接不同的大模型、MCP工具、Langchain工具、提示词，组建可编排的特定场景下的Agent，它还具有图片多模态的解析和生成功能、Computer Use、Browser Use、Phone Use可以接管你的电脑、浏览器、手机。
    
Agent的开发离不开外部工具的支持，兴河 AI Assistant 统一了工具调用的兼容性，使得外部MCP和Langchain工具可以统一接入LLM，目前正在积极的适配和接入外部工具，使得大模型可以快速拥有操纵外部的手脚。
    
我也会积极听取大家的意见，制作最贴合大家需求的Langchain或MCP工具，希望可以在内测期间和大家多多交流。


# 预览

<picture>
  <source media="(prefers-color-scheme: light)" srcset="组合.png">
  <img alt="" src="组合.png"  width="full">
</picture>

# 安装
## 客户端安装
选择自己合适的平台进行安装即可。
## 服务端安装
准备：
服务端使用了`LibreOffice`的一些功能，请先安装`LibreOffice`：https://zh-tw.libreoffice.org/download/download-libreoffice/

服务端使用了ollama中的bge-m3:latest，请先安装ollama，然后`ollama pull bge-m3:latest`
```shell
1、解压下载好的xinghe.assistant-server-v1.0.0.zip
2、cd xinghe.assistant-server-v1.0.0
3、conda create --name xinghe python=3.11 //遇到选择选y就行
4、conda activate xinghe
5、pip install -r requirements.txt //有的版本我忘记放了，github首页我传了一个，放到和main.py平级目录即可
6、cd ExternalTools/mcp-sse-client-python/
7、python setup.py install
8、cd ../../
9、playwright install
10、python main.py --workers=5 #使用gemini等国外模型记得要先设置命令行代理
```

服务端目录下有`.env`文件，请运行前打开编辑，填入`api key`，才可以调用模型

没有授权文件请联系作者获取，获取到授权文件放在`main.py`同级目录即可。

关于身份验证，本程序仅使用随机数生成`token`，无会话有效时间，在正常进入程序前，请使用
```
python create_token.py
```
来创建`token`文件，如果`token`泄漏或想更换`token`，请再次执行上述命令。


# 授权码获取

一、转发集赞

用户身份是公众号主：联系我转推公众号文章。

用户身份是普通用户：转发公众号文章到朋友圈，集赞38个。



二、关注找我进群

关注bilibili “**兴河弟弟**”，在首页置顶视频一键三连+评论区留言，然后在b站私信我带上集赞截图或者转推文章截图会将大家拉到内测群中。（在一已经完成的基础上）


三、本次内测时间**2025年5月7日-2025年6月7日**，时间之内，均可申请内测。（自申请之日起一个月）


四、内测时间内，根据大家提出的意见和bug（可在交流群和github提出），会继续完善兴河AI的功能，可以在群里和大家一起讨论AI的发展之路，也邀请拥有开发能力的开发者，共建langchain和mcp生态，让AGI更早到来！**对社区有贡献的开发者，将持续免费**！


如果您感觉对您有帮助，希望您可以成为我b站的原始粉丝（**突破1000粉之前**），后续有活动原始粉丝优先。


内测期间，兴河AI助手**完全免费**，有向您付费出售的，请喷他拉黑举报三连。



# 联系我

<picture>
  <source media="(prefers-color-scheme: light)" srcset="二维码.jpg">
  <img alt="" src="二维码.jpg"  width="20%">
</picture>
