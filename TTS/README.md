# Minimax & Edge TTS

### 概述

OpenAI Edge TTS 是一个文本转语音（TTS）服务，使用 Microsoft Edge TTS 作为后端引擎，提供与 OpenAI 兼容的 API 接口。它同时支持 REST API 和 WebSocket 流式传输，支持多个 TTS 提供商，包括 Edge TTS 和 Minimax TTS。

### 特性

- ✅ **OpenAI API 兼容** - 可直接替代 OpenAI 的 TTS API
- 🎙️ **多 TTS 提供商** - 支持 Edge TTS 和 Minimax TTS
- 🔄 **WebSocket 流式传输** - 实时流式 TTS，支持句子级处理
- 🎵 **多种音频格式** - 支持 MP3、WAV、OPUS、AAC、FLAC（通过 FFmpeg）
- 🗣️ **语音映射** - 将 OpenAI 语音名称映射到 Edge TTS 语音
- ⚡ **速度控制** - 可调节语速（0.25x - 4.0x）
- 📝 **文本处理** - 自动清理 Markdown 和表情符号
- 🌐 **CORS 支持** - 可用于 Web 应用

### 安装

#### 前置要求

- Python 3.7+
- FFmpeg（可选，用于音频格式转换）

#### 安装 FFmpeg（可选）

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载

#### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置

在项目根目录创建 `.env` 文件：

```env
# API 配置
API_KEY=your_api_key_here
REQUIRE_API_KEY=true

# 服务器配置
PORT=5050

# TTS 配置
DEFAULT_VOICE=zh-CN-XiaoxiaoNeural
DEFAULT_RESPONSE_FORMAT=wav
DEFAULT_SPEED=1.0
DEFAULT_LANGUAGE=zh-CN

# 功能开关
REMOVE_FILTER=false
EXPAND_API=true
```

### 使用方法

#### 启动服务器

```bash
python app/websocket_edge_tts.py
```

服务器将在 `http://0.0.0.0:5050` 启动

#### WebSocket API

##### 连接 WebSocket

```javascript
const ws = new WebSocket('ws://localhost:5050/genVoice');

// 配置 TTS 设置
ws.send(JSON.stringify({
    type: "edge",           // "edge" 或 "minimax"
    voice_id: "zh-CN-XiaoxiaoNeural",
    speed: 1.0,
    vol: 2
}));

// 发送文本进行 TTS
ws.send("你好，这是一个测试。");

// 接收音频数据
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('序列号:', data.seq);
    console.log('文本:', data.text);
    console.log('音频 Base64:', data.wav_base64);
    console.log('时长:', data.duration);
};

// 刷新剩余缓冲区
ws.send(JSON.stringify({ command: "__FLUSH__" }));

// 结束会话
ws.send(JSON.stringify({ command: "__END__" }));
```

##### Minimax TTS 的 WebSocket 配置

```javascript
ws.send(JSON.stringify({
    type: "minimax",
    api_key: "your_minimax_api_key",
    group_id: "your_group_id",
    voice_id: "female-shaonv",
    speed: 1.0,
    vol: 2
}));
```

#### REST API

##### 测试 Edge TTS

```bash
curl -X POST http://localhost:5050/test-edge-tts \
  -H "Content-Type: application/json" \
  -d '{
    "text": "你好，这是一个测试。",
    "voice_id": "zh-CN-XiaoxiaoNeural",
    "speed": 1.0
  }'
```

响应：
```json
{
  "seq": 1,
  "text": "你好，这是一个测试。",
  "wav_base64": "UklGRiQAAABXQVZFZm10...",
  "duration": "2.50"
}
```

### 可用语音

#### OpenAI 语音映射

| OpenAI 语音 | Edge TTS 语音 |
|-------------|---------------|
| alloy       | en-US-AvaNeural |
| echo        | en-US-AndrewNeural |
| fable       | en-GB-SoniaNeural |
| onyx        | en-US-EricNeural |
| nova        | en-US-SteffanNeural |
| shimmer     | en-US-EmmaNeural |

您也可以直接使用任何 Edge TTS 语音，只需指定语音名称（例如，中文使用 `zh-CN-XiaoxiaoNeural`）。

### 音频格式

支持的格式：`mp3`、`wav`、`opus`、`aac`、`flac`

**注意：** 除 MP3 外的其他格式需要安装 FFmpeg。

### 特殊功能

#### 句子级流式传输

WebSocket API 会自动按句子标点符号（`。`、`？`、`！`、`；`、`\n`）分割文本，并独立处理每个句子，以获得更快的响应时间。

#### 文本预处理

- 移除 Markdown 格式
- 移除表情符号
- 移除特殊标签，如 `<表情>...</表情>` 和 `<动作>...</动作>`
- 将标题转换为口语化上下文（例如，"标题 — 标题文本"）

### 项目结构

```
openai-edge-tts/
├── app/
│   ├── websocket_edge_tts.py  # 主 WebSocket 服务器（入口点）
│   ├── server.py              # Flask REST API 服务器
│   ├── tts_handler.py         # TTS 生成逻辑
│   ├── handle_text.py         # 文本预处理
│   └── utils.py               # 工具函数
├── requirements.txt           # Python 依赖
├── .env                       # 配置文件
└── README.md                  # 本文件
```

### 依赖项

- `fastapi` - 现代 Web 框架，用于 WebSocket API
- `uvicorn` - ASGI 服务器
- `flask` - Web 框架，用于 REST API
- `edge-tts` - Microsoft Edge TTS 引擎
- `librosa` - 音频分析
- `soundfile` - 音频文件 I/O
- `requests` - HTTP 库，用于 Minimax API
- `python-dotenv` - 环境变量管理
- `emoji` - 表情符号处理

### 许可证

本项目是开源的，采用 MIT 许可证。

