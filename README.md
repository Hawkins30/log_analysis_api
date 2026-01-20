# Log Analysis API

A simple backend API built with FastAPI that analyses application log data and returns structured results as JSON.

This project is designed to demonstrate backend development fundamentals, clean code structure, and basic testing.

## Features

- Health check endpoint
- Log analysis endpoint accepting raw log text
- Counts log levels (ERROR, WARNING, INFO)
- Detects malformed log lines
- Returns structured JSON responses
- Core analysis logic separated from API layer
- Unit-tested analysis logic

## Running the API

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install fastapi uvicorn

Run the development server:

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation (Swagger UI):

http://127.0.0.1:8000/docs

## Log Analysis Endpoint

Analyse log data by sending a POST request to:

POST /analyse

Request body example:

{
  "text": "2026-01-12 14:33:01 ERROR Something failed
2026-01-12 14:33:02 INFO All good
INVALID LINE"
}

Example response:

{
  "counts": {
    "ERROR": 1,
    "WARNING": 0,
    "INFO": 1
  },
  "total_lines": 3,
  "malformed_lines": 1
}

## Tests

Basic unit tests are included for the core analysis logic.

Run tests with:

python -m pytest

============================================

# 日志分析 API

这是一个使用 FastAPI 构建的简单后端 API，用于分析应用程序日志数据，并以 JSON 格式返回结构化结果。

该项目旨在展示后端开发的基础能力、良好的代码结构以及基础的单元测试实践。

## 功能特性

- 健康检查接口
- 接收原始日志文本的日志分析接口
- 统计日志级别（ERROR、WARNING、INFO）
- 识别并统计格式错误的日志行
- 返回结构化的 JSON 数据
- 将核心分析逻辑与 API 层分离
- 核心分析逻辑包含单元测试

## 运行 API

创建并激活 Python 虚拟环境：

python3 -m venv venv
source venv/bin/activate

安装依赖：

pip install fastapi uvicorn

启动开发服务器：

uvicorn main:app --reload

API 访问地址：

http://127.0.0.1:8000

交互式 API 文档（Swagger UI）：

http://127.0.0.1:8000/docs

## 日志分析接口

通过发送 POST 请求来分析日志数据：

POST /analyse

请求体示例：

{
  "text": "2026-01-12 14:33:01 ERROR Something failed
2026-01-12 14:33:02 INFO All good
INVALID LINE"
}

返回结果示例：

{
  "counts": {
    "ERROR": 1,
    "WARNING": 0,
    "INFO": 1
  },
  "total_lines": 3,
  "malformed_lines": 1
}

## 测试

项目包含用于核心分析逻辑的基础单元测试。

运行测试：

python -m pytest
