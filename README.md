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

- RESTful API for analysing raw log data
- Accepts multiline log text via HTTP POST
- Counts log levels (ERROR, WARNING, INFO)
- Detects and reports malformed log lines
- Returns structured JSON analysis results
- Core analysis logic separated from API layer
- Persistent storage of analysis results using SQLite
- Defensive database initialisation for serverless environments
- Publicly deployed API with interactive Swagger documentation


## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pytest
- Render (deployment)


## Running the API

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

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
  "text": "2026-01-12 14:33:01 ERROR Something failed\n2026-01-12 14:33:02 INFO All good\nINVALID LINE"
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

## Deployment

This API is deployed on Render (free tier).

- The service runs using Uvicorn and FastAPI
- The application binds to Render’s assigned `$PORT`
- SQLite is used for persistence with serverless-safe safeguards

The live API exposes interactive documentation via Swagger UI.

## Deployment Notes & Problem Solving

This project was deployed to Render (free tier) and required solving several real-world backend deployment issues. These challenges and solutions are intentionally documented to demonstrate practical debugging and production readiness.

### Key Challenges Encountered

- **Ephemeral filesystem on Render**
  - SQLite databases are not persistent across deploys on the free tier.
  - Solution: Store the database in `/tmp` and design the application to safely recreate state when needed.

- **Database table not existing at runtime**
  - On first requests, the SQLite table did not exist, causing insert failures.
  - Solution: Implement defensive table creation using `CREATE TABLE IF NOT EXISTS` immediately before inserts.
  - This approach is idempotent and safe for SQLite on serverless platforms.

- **ORM portability issues**
  - SQLAlchemy’s `JSON` column type caused runtime failures with SQLite in production.
  - Solution: Store JSON data as serialized `TEXT` and manually encode/decode using `json.dumps` / `json.loads`.

- **Application startup vs request lifecycle**
  - Relying solely on startup hooks was not sufficient on Render due to timing and filesystem behaviour.
  - Solution: Combine startup logic with request-level safeguards to guarantee correctness.

- **Render port binding**
  - Initial deployment failed with “no open ports detected”.
  - Solution: Configure Uvicorn to bind to Render’s injected `$PORT` environment variable.

- **Invalid client request formats**
  - Initial API tests failed due to invalid JSON request bodies.
  - Solution: Correct request structure and validate payloads via FastAPI’s request handling.

### Why This Matters

These issues mirror real production problems encountered when deploying backend services to cloud and serverless environments. Solving them required:

- Reading and interpreting production logs
- Understanding framework and platform lifecycles
- Applying defensive programming techniques
- Knowing when to drop below ORM abstractions safely

The final deployed service is stable, predictable, and demonstrably production-aware.

### Live Deployment

The API is deployed and publicly accessible:

- **Swagger UI**: `/docs`
- **POST** `/analyse`
- **GET** `/analyses`


============================================

# 日志分析 API

这是一个使用 FastAPI 构建的简单后端 API，用于分析应用程序日志数据，并以 JSON 格式返回结构化结果。

该项目旨在展示后端开发的基础能力、良好的代码结构以及单元测试实践。

## 项目目的

本项目用于展示真实世界后端开发所需的核心能力，包括：

- RESTful API 的设计与实现
- 将业务逻辑与框架代码清晰分离
- 使用关系型数据库进行数据持久化
- 编写可测试、模块化的 Python 代码
- 使用 Git 进行专业的软件版本管理

该项目模拟了一个后端服务：接收原始日志数据，对其进行分析，将结果存储到数据库中，并支持历史结果的查询。

## 功能特性

- 提供用于分析原始日志数据的 RESTful API
- 通过 HTTP POST 接收多行日志文本
- 统计日志级别（ERROR、WARNING、INFO）
- 自动识别并统计格式错误的日志行
- 返回结构化的 JSON 分析结果
- 将核心分析逻辑与 API 层清晰分离
- 使用 SQLite 对分析结果进行持久化存储
- 针对 serverless 环境实现防御式数据库初始化
- 已部署的公共 API，并提供可交互的 Swagger 文档

## 技术栈

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pytest
- Render（部署）

## 运行 API

创建并激活 Python 虚拟环境：

python3 -m venv venv
source venv/bin/activate

安装依赖：

pip install -r requirements.txt

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
  "text": "2026-01-12 14:33:01 ERROR Something failed\n2026-01-12 14:33:02 INFO All good\nINVALID LINE"
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

## 部署说明

本 API 已部署至 Render（免费层）。

- 服务使用 FastAPI 与 Uvicorn 运行
- 应用通过绑定 Render 提供的 `$PORT` 环境变量启动
- 使用 SQLite 进行数据持久化，并针对 serverless 环境进行了安全处理

部署后的服务提供 Swagger UI 作为交互式接口文档。

## 部署问题与设计决策

在将本项目部署至 Render 的过程中，遇到了多个真实生产环境中常见的问题。以下内容记录了问题及其解决方案，以展示实际的后端工程能力。

### 遇到的主要问题

- **Render 的临时文件系统**
  - 免费层环境中，SQLite 数据在重新部署后不会持久保存
  - 解决方案：将数据库存储在 `/tmp` 目录，并确保应用能够安全地重新创建所需状态

- **数据库表在运行时不存在**
  - 初次请求时，SQLite 表尚未创建，导致写入失败
  - 解决方案：在写入数据前显式执行 `CREATE TABLE IF NOT EXISTS`，确保表存在

- **ORM 可移植性问题**
  - SQLAlchemy 的 `JSON` 类型在 SQLite 生产环境中不稳定
  - 解决方案：将 JSON 数据序列化为 `TEXT` 存储，并使用 `json.dumps` / `json.loads` 手动转换

- **应用启动阶段与请求生命周期差异**
  - 仅依赖应用启动事件无法在 Render 环境中完全保证数据库状态正确
  - 解决方案：结合启动逻辑与请求级防御式检查

- **Render 端口绑定问题**
  - 初始部署出现 “no open ports detected” 错误
  - 解决方案：通过 `$PORT` 环境变量启动 Uvicorn

- **客户端请求格式错误**
  - 初期测试失败源于请求体 JSON 格式不正确
  - 解决方案：修正请求结构，并依赖 FastAPI 的请求验证机制

### 为什么这些问题很重要

上述问题均来自真实生产环境，而非教程示例。解决这些问题需要：

- 阅读并理解生产日志
- 理解框架与云平台的运行机制
- 编写防御式代码
- 在必要时安全地绕过 ORM 抽象层

最终部署的服务稳定、可预测，并具备明确的生产环境意识。
