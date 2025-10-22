# macOS System MCP Server

一个基于 FastMCP 构建的 macOS 系统控制 MCP 服务器，提供应用程序管理、系统控制和键盘自动化功能。

## 功能特性

### 🚀 应用程序管理
- **启动应用** (`launch_app`) - 通过 Spotlight 搜索并启动应用程序
- **关闭应用** (`close_app`) - 优雅地退出指定应用程序

### 🎛️ 系统控制
- **音量控制** (`set_volume`) - 设置系统音量（0-100）
- **锁屏** (`lock_screen`) - 快速锁定屏幕
- **弹窗提醒** (`alert_dialog`) - 显示系统提醒对话框

### ⌨️ 窗口和空间管理
- **全屏切换** (`full_screen`) - 切换当前窗口的全屏模式
- **空间切换** (`swipe_space`) - 在 macOS 虚拟桌面（Spaces）之间切换

## 系统要求

- macOS 操作系统
- Python 3.8+
- 辅助功能权限（用于键盘控制）

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 macOS 权限

为了使键盘自动化功能正常工作，需要授予终端或 Python 辅助功能权限：

1. 打开 **系统设置** > **隐私与安全性** > **辅助功能**
2. 添加你使用的终端应用（如 Terminal.app、iTerm.app）或 Python 解释器
3. 确保开关已启用

## 运行服务器

```bash
python macos_system_mcp.py
```

服务器将在 `http://localhost:1234` 上运行，使用 SSE (Server-Sent Events) 传输协议。

## MCP 客户端配置

### Claude Desktop 配置

在 Claude Desktop 的配置文件中添加：

**macOS/Linux**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "macos-system": {
      "command": "python",
      "args": ["/Users/你的用户名/PycharmProjects/MCP/macos_system_mcp/macos_system_mcp.py"]
    }
  }
}
```

### 其他 MCP 客户端

如果使用其他 MCP 客户端，配置 SSE 连接到：
```
http://localhost:1234/sse
```

## 工具使用说明

### launch_app - 启动应用程序

通过 Spotlight 搜索并启动应用。

**参数：**
- `app_name` (string): 应用程序名称（如 "Safari"、"微信"、"Chrome"）

**示例：**
```python
launch_app(app_name="Safari")
```

### close_app - 关闭应用程序

优雅地退出指定应用程序。

**参数：**
- `app_name` (string): 应用程序名称

**示例：**
```python
close_app(app_name="Safari")
```

### set_volume - 设置音量

设置系统输出音量。

**参数：**
- `volume` (int): 音量值，范围 0-100

**示例：**
```python
set_volume(volume=50)
```

### full_screen - 全屏切换

模拟 Control + Command + F 快捷键，切换当前窗口全屏模式。

**参数：**
- `placeholder` (string, 可选): 占位参数，可不填

**示例：**
```python
full_screen()
```

### swipe_space - 切换虚拟桌面

在 macOS Spaces（虚拟桌面）之间切换。

**参数：**
- `direction` (string): 切换方向，"left" 或 "right"

**示例：**
```python
swipe_space(direction="left")   # 向左切换
swipe_space(direction="right")  # 向右切换
```

### lock_screen - 锁定屏幕

立即锁定 macOS 屏幕。

**参数：**
- `placeholder` (string, 可选): 占位参数，可不填

**示例：**
```python
lock_screen()
```

### alert_dialog - 显示提醒对话框

显示系统级提醒对话框。

**参数：**
- `message` (string): 要显示的消息内容

**示例：**
```python
alert_dialog(message="任务已完成！")
```

## 注意事项

1. **权限要求**：首次运行时，macOS 可能会提示授予辅助功能权限，请按照提示操作
2. **Spotlight 延迟**：`launch_app` 功能依赖 Spotlight 响应速度，如果启动失败，可能需要调整代码中的延迟时间
3. **应用名称**：使用应用的显示名称（如 "Safari"），而不是包名
4. **安全性**：此工具具有系统控制能力，请谨慎使用，避免在不受信任的环境中运行

## 技术栈

- **FastMCP** - MCP 服务器框架
- **pynput** - 键盘控制库
- **subprocess** - 执行 AppleScript 命令

## 故障排除

### 应用启动失败
- 检查辅助功能权限是否已授予
- 确认应用名称拼写正确
- 尝试增加代码中的 `time.sleep()` 延迟值

### 键盘快捷键不工作
- 确认终端或 Python 已添加到辅助功能权限列表
- 重启终端或 Python 进程

### AppleScript 错误
- 确认在 macOS 系统上运行
- 检查应用程序是否支持 AppleScript 控制

## 许可证

本项目为开源项目，仅供学习和个人使用。

## 贡献

欢迎提交 Issue 和 Pull Request！

