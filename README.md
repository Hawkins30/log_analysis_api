# Log Analysis API

A simple backend API built with FastAPI that analyses application log data and returns structured results as JSON.

This project is designed to demonstrate backend development fundamentals, clean code structure, and basic testing.

## Why this project exists

This project was built to demonstrate real-world backend development skills, including:

- Designing RESTful APIs
- Separating business logic from framework code
- Persisting data using a relational database
- Writing testable, modular Python code
- Using Git professionally with clean commits

It simulates a backend service that ingests raw log data, analyses it, stores results, and allows historical retrieval.

## Features

- Health check endpoint
- Log analysis endpoint accepting raw log text
- Counts log levels (ERROR, WARNING, INFO)
- Detects malformed log lines
- Returns structured JSON responses
- Core analysis logic separated from API layer
- Unit-tested analysis logic

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pytest

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

## Project Structure

- main.py — API layer and HTTP endpoints
- analyser.py — Core log analysis logic (pure, testable)
- database.py — Database setup, models, and session handling
- tests/ — Unit tests for analysis and models

The API layer depends on the analysis and database layers, keeping responsibilities clearly separated.


## Tests

Basic unit tests are included for the core analysis logic.

Run tests with:

python -m pytest

============================================

# 日志分析 API

这是一个使用 FastAPI 构建的简单后端 API，用于分析应用程序日志数据，并以 JSON 格式返回结构化结果。

该项目旨在展示后端开发的基础能力、良好的代码结构以及基础的单元测试实践。

## 项目目的

本项目用于展示真实世界后端开发所需的核心能力，包括：

- RESTful API 的设计与实现
- 将业务逻辑与框架代码清晰分离
- 使用关系型数据库进行数据持久化
- 编写可测试、模块化的 Python 代码
- 使用 Git 进行专业的软件版本管理

该项目模拟了一个后端服务：接收原始日志数据，对其进行分析，将结果存储到数据库中，并支持历史结果的查询。

## 功能特性

- 健康检查接口
- 接收原始日志文本的日志分析接口
- 统计日志级别（ERROR、WARNING、INFO）
- 识别并统计格式错误的日志行
- 返回结构化的 JSON 数据
- 将核心分析逻辑与 API 层分离
- 核心分析逻辑包含单元测试

## 技术栈

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pytest

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

## 项目结构说明

- main.py —— API 层，负责 HTTP 接口与请求处理
- analyser.py —— 核心日志分析逻辑（纯函数，易于测试）
- database.py —— 数据库配置、数据模型与会话管理
- tests/ —— 单元测试，覆盖分析逻辑与数据模型

API 层依赖分析层与数据库层，从而实现职责清晰分离，便于维护与扩展。


## 测试

项目包含用于核心分析逻辑的基础单元测试。

运行测试：

python -m pytest
