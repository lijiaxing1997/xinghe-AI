# PDF OCR MCP Server

一个基于 FastMCP 和 PaddleOCR 构建的 PDF 文字识别 MCP 服务器，支持将 PDF 文件转换为图片并进行 OCR 文字识别。

## 功能特性

### 📄 PDF 处理
- **PDF 转图片** - 使用 PyMuPDF 将 PDF 页面高质量转换为图片
- **OCR 文字识别** - 使用 PaddleOCR 识别图片中的文字
- **中文支持** - 优化的中文识别配置
- **自动清理** - 处理完成后自动清理临时图片文件

### 🎯 技术特点
- 高分辨率转换（5倍缩放因子）
- 优化的 OCR 参数配置
- 本地模型存储，无需每次下载
- 支持多页 PDF 批量处理

## 系统要求

- Python 3.8+
- 足够的磁盘空间用于存储 PaddleOCR 模型（约 100MB）

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 准备 PaddleOCR 模型

项目已包含 `model` 目录结构：
```
pdf_ocr/
├── model/
│   ├── det/    # 文字检测模型
│   ├── cls/    # 文字方向分类模型
│   └── rec/    # 文字识别模型
```

**首次运行时，PaddleOCR 会自动下载模型到这些目录。** 如果已有模型文件，请将它们放置在对应目录中。

### 3. 创建临时图片目录

```bash
mkdir imgs
```

## 运行服务器

```bash
cd pdf_ocr
python pdf_ocr.py
```

服务器将在 `http://localhost:2223` 上运行，使用 SSE (Server-Sent Events) 传输协议。

## MCP 客户端配置

### Claude Desktop 配置

在 Claude Desktop 的配置文件中添加：

**macOS/Linux**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "pdf-ocr": {
      "command": "python",
      "args": ["/Users/你的用户名/PycharmProjects/MCP/pdf_ocr/pdf_ocr.py"]
    }
  }
}
```

**注意**：请将路径替换为实际的绝对路径。

### 其他 MCP 客户端

如果使用其他 MCP 客户端，配置 SSE 连接到：
```
http://localhost:2223/sse
```

## 工具使用说明

### ocr_pdf_tool - PDF OCR 识别

将 PDF 文件转换为图片并进行 OCR 文字识别，返回识别出的文本内容。

**参数：**
- `pdf_file` (string): PDF 文件的路径（支持相对路径和绝对路径）

**返回：**
- 识别出的文本内容（字符串）

**示例：**
```python
# 使用相对路径
ocr_pdf_tool(pdf_file="document.pdf")

# 使用绝对路径
ocr_pdf_tool(pdf_file="/Users/username/Documents/report.pdf")
```

**处理流程：**
1. 将 PDF 的每一页转换为高分辨率 PNG 图片（5倍缩放）
2. 对每张图片进行 OCR 识别
3. 合并所有页面的识别结果
4. 自动清理临时图片文件
5. 返回完整文本

## OCR 参数配置

当前使用的 PaddleOCR 参数：

```python
{
    'use_angle_cls': True,      # 使用角度分类器，自动纠正文字方向
    'lang': 'ch',               # 中文识别模式
    'use_gpu': False,           # CPU 模式（如需 GPU 加速可改为 True）
    'show_log': False,          # 不显示详细日志
    'det_db_thresh': 0.2,       # 检测阈值（降低以检测更多区域）
    'det_db_box_thresh': 0.3,   # 框阈值
    'det_db_unclip_ratio': 1.8, # 扩大检测区域
    'det_model_dir': './model/det',
    'cls_model_dir': './model/cls',
    'rec_model_dir': './model/rec'
}
```

## 目录结构

```
pdf_ocr/
├── pdf_ocr.py          # 主程序文件
├── README.md           # 本文档
├── requirements.txt    # Python 依赖
├── imgs/               # 临时图片存储目录（自动清理）
└── model/              # PaddleOCR 模型目录
    ├── det/            # 检测模型
    ├── cls/            # 分类模型
    └── rec/            # 识别模型
```

## 技术栈

- **FastMCP** - MCP 服务器框架
- **PaddleOCR** - 百度开源的 OCR 引擎
- **PyMuPDF (fitz)** - PDF 处理库
- **Pillow (PIL)** - Python 图像处理库
- **ReportLab** (可选) - 用于创建示例 PDF

## 性能优化建议

### 1. 启用 GPU 加速

如果有 NVIDIA GPU 和 CUDA 环境：

```python
# 修改 pdf_ocr.py 中的参数
'use_gpu': True
```

需要安装 GPU 版本的 PaddlePaddle：
```bash
pip install paddlepaddle-gpu
```

### 2. 调整缩放因子

根据 PDF 质量调整 `zoom_factor`（在 `toimages` 函数中）：
- 高质量 PDF：`zoom_factor=3`
- 普通质量：`zoom_factor=5`（默认）
- 低质量扫描件：`zoom_factor=7`

### 3. 批量处理

对于大量 PDF 文件，建议：
- 增加系统内存
- 使用 SSD 存储临时图片
- 考虑分批处理

## 注意事项

1. **文件路径**：确保 PDF 文件路径正确，支持中文路径
2. **磁盘空间**：处理大型 PDF 时需要足够的临时存储空间
3. **模型下载**：首次运行会下载模型，需要网络连接
4. **权限问题**：确保程序有读取 PDF 和写入 `imgs` 目录的权限
5. **自动清理**：每次 OCR 完成后会自动删除 `imgs` 目录中的临时文件

## 故障排除

### 模型下载失败

如果自动下载失败，可以手动下载 PaddleOCR 模型：

1. 访问 [PaddleOCR 模型库](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/models_list.md)
2. 下载中文检测、分类、识别模型
3. 解压到对应的 `model/det`、`model/cls`、`model/rec` 目录

### OCR 识别率低

- 检查 PDF 质量，扫描件建议提高 `zoom_factor`
- 调整 OCR 参数（`det_db_thresh`、`det_db_box_thresh`）
- 确保使用了正确的语言模型（`lang='ch'` 为中文）

### 内存不足

- 降低 `zoom_factor` 减少图片大小
- 分批处理大型 PDF
- 关闭其他占用内存的程序

### 临时文件未清理

如果程序异常退出，临时文件可能残留：
```bash
rm -rf ./imgs/*
```

## 使用示例

### 在 Claude Desktop 中使用

```
用户：请帮我识别这个 PDF 文件的内容：/Users/username/Documents/contract.pdf

Claude：我来帮您识别这个 PDF 文件...
[调用 ocr_pdf_tool]

识别结果：
[返回 PDF 中的文字内容]
```

### 通过 API 调用

```python
import requests

response = requests.post(
    "http://localhost:2223/tools/ocr_pdf_tool",
    json={"pdf_file": "document.pdf"}
)
print(response.json())
```

## 许可证

本项目为开源项目，仅供学习和个人使用。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 相关资源

- [PaddleOCR 官方文档](https://github.com/PaddlePaddle/PaddleOCR)
- [PyMuPDF 文档](https://pymupdf.readthedocs.io/)
- [FastMCP 文档](https://github.com/jlowin/fastmcp)

