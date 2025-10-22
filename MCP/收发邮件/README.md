# Email MCP Server

一个基于 FastMCP 构建的邮件收发 MCP 服务器，支持通过 IMAP 协议获取未读邮件和通过 SMTP 协议发送邮件。

## 功能特性

### 📧 邮件接收
- **获取未读邮件** (`fetch_unread_emails`) - 通过 IMAP 协议获取未读邮件
  - 返回发件人信息
  - 返回邮件主题
  - 返回邮件时间
  - 返回邮件正文内容
  - 支持中文编码解析
  - 自动处理多部分邮件（multipart）

### 📤 邮件发送
- **发送邮件** (`send_email`) - 通过 SMTP 协议发送邮件
  - 支持设置收件人
  - 支持设置邮件主题
  - 支持设置邮件正文
  - 支持抄送（CC）功能
  - 自动使用 UTF-8 编码

## 系统要求

- Python 3.8+
- 126 邮箱账号（或其他支持 IMAP/SMTP 的邮箱）
- 邮箱授权码（不是登录密码）

## 安装

### 1. 安装依赖

```bash
cd 收发邮件
pip install -r requirements.txt
```

### 2. 配置邮箱账户

编辑 `config.ini` 文件，填写您的邮箱账户信息：

```ini
[ACCOUNT]
email = your_email@126.com
password = your_authorization_code
```

**重要提示：**
- `password` 字段应填写**授权码**，而不是邮箱登录密码
- 126 邮箱授权码获取方法：
  1. 登录 126 邮箱网页版
  2. 进入"设置" -> "POP3/SMTP/IMAP"
  3. 开启 IMAP/SMTP 服务
  4. 获取授权码（通常需要手机验证）

### 3. 其他邮箱配置

如果您使用的不是 126 邮箱，可以修改 `config.ini` 中的服务器配置：

#### QQ 邮箱配置示例
```ini
[IMAP]
server = imap.qq.com
port = 993
use_ssl = true

[SMTP]
server = smtp.qq.com
port = 465
use_ssl = true
```

#### Gmail 配置示例
```ini
[IMAP]
server = imap.gmail.com
port = 993
use_ssl = true

[SMTP]
server = smtp.gmail.com
port = 465
use_ssl = true
```

#### 163 邮箱配置示例
```ini
[IMAP]
server = imap.163.com
port = 993
use_ssl = true

[SMTP]
server = smtp.163.com
port = 465
use_ssl = true
```

## 运行服务器

```bash
cd 收发邮件
python email_mcp.py
```

服务器将在 `http://localhost:3456` 上运行，使用 SSE (Server-Sent Events) 传输协议。

## MCP 客户端配置

### Claude Desktop 配置

在 Claude Desktop 的配置文件中添加：

**macOS/Linux**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "email": {
      "command": "python",
      "args": ["/Users/你的用户名/PycharmProjects/MCP/收发邮件/email_mcp.py"]
    }
  }
}
```

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "email": {
      "command": "python",
      "args": ["C:\\Users\\你的用户名\\PycharmProjects\\MCP\\收发邮件\\email_mcp.py"]
    }
  }
}
```

## 工具使用说明

### 1. 获取未读邮件 (fetch_unread_emails)

**参数：**
- `max_count` (可选): 最多获取的未读邮件数量，默认 10 封

**返回信息：**
- 邮件主题
- 发件人地址
- 发送时间
- 邮件正文（超过 1000 字符会自动截断）

**使用示例：**
```
请帮我查看未读邮件
```

AI 会自动调用 `fetch_unread_emails` 工具，返回未读邮件列表，包含完整的上下文信息，可以直接基于这些信息回复邮件。

### 2. 发送邮件 (send_email)

**参数：**
- `to_addr` (必填): 收件人邮箱地址
- `subject` (必填): 邮件主题
- `body` (必填): 邮件正文
- `cc` (可选): 抄送地址，多个地址用逗号分隔

**使用示例：**
```
请给 zhangsan@example.com 发送一封邮件，主题是"会议通知"，内容是"明天下午3点开会"
```

AI 会自动调用 `send_email` 工具发送邮件。

### 3. 智能回复邮件

由于 `fetch_unread_emails` 返回了完整的邮件上下文（发件人、主题、内容），AI 可以直接基于这些信息帮您回复邮件：

**使用示例：**
```
用户: 请查看我的未读邮件
AI: [调用 fetch_unread_emails，显示未读邮件列表]

用户: 请回复第一封邮件，告诉他我同意这个方案
AI: [自动提取发件人地址和主题，调用 send_email 发送回复]
```

## 技术特点

- ✅ 支持 IMAP 和 SMTP 协议
- ✅ 自动处理中文编码（UTF-8、GBK 等）
- ✅ 支持多部分邮件（multipart）解析
- ✅ 自动提取纯文本和 HTML 邮件正文
- ✅ SSL/TLS 加密连接
- ✅ 完整的错误处理机制
- ✅ 支持邮件抄送功能

## 常见问题

### 1. 登录失败

**错误信息**: `authentication failed` 或 `login failed`

**解决方法**:
- 确认使用的是**授权码**而不是登录密码
- 确认已在邮箱设置中开启 IMAP/SMTP 服务
- 检查邮箱地址和授权码是否正确

### 2. 连接超时

**错误信息**: `Connection timed out`

**解决方法**:
- 检查网络连接
- 确认防火墙没有阻止 993 (IMAP) 和 465 (SMTP) 端口
- 尝试使用其他网络环境

### 3. 中文乱码

本服务器已自动处理常见的中文编码问题（UTF-8、GBK 等），如果仍然出现乱码，请提交 issue。

### 4. 邮件正文为空

某些邮件可能只包含 HTML 内容，服务器会尝试提取 HTML 正文。如果仍然为空，可能是邮件格式特殊，建议直接在邮箱客户端查看。

## 安全建议

1. **不要将 `config.ini` 文件提交到版本控制系统**（已添加到 `.gitignore`）
2. **定期更换授权码**
3. **不要在公共场合分享配置文件**
4. **建议为 MCP 服务器单独创建一个邮箱账号**

## 开发说明

### 项目结构

```
收发邮件/
├── email_mcp.py      # 主程序文件
├── config.ini        # 配置文件（需要手动配置）
├── requirements.txt  # Python 依赖
└── README.md         # 说明文档
```

### 扩展功能

您可以基于此项目扩展更多功能：
- 标记邮件为已读/未读
- 删除邮件
- 搜索邮件
- 发送带附件的邮件
- 邮件分类和过滤
- 自动回复规则

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v1.0.0 (2025-10-22)
- ✨ 初始版本发布
- ✅ 支持获取未读邮件
- ✅ 支持发送邮件
- ✅ 支持中文编码
- ✅ 完整的配置文件支持

