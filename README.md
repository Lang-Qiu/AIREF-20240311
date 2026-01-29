# AIREF-20240311 - 人工智能模型鲁棒性评估平台

本项目包含前端和后端两个部分，分别位于 `frontend` 和 `backend` 目录下。

## 目录结构

*   `backend/`: Django 后端项目代码
*   `frontend/`: Vue 前端项目代码
*   `artifacts/`: 项目设计文档与接口定义
*   `requirements.yaml`: 项目需求规格说明

## 环境要求

*   **Python**: 3.8+
*   **Node.js**: 14+ (建议使用 LTS 版本)
*   **npm** 或 **yarn**

---

## 快速启动

### 1. 后端启动 (Backend)

后端基于 Django 框架开发。

1.  进入后端目录：
    ```bash
    cd backend
    ```

2.  (可选) 创建并激活虚拟环境：
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

4.  执行数据库迁移：
    ```bash
    python manage.py migrate
    ```

5.  启动开发服务器：
    ```bash
    python manage.py runserver
    ```
    后端服务默认运行在 `http://127.0.0.1:8000`。

### 2. 前端启动 (Frontend)

前端基于 Vue 2 开发。

1.  进入前端目录：
    ```bash
    cd frontend
    ```

2.  安装依赖：
    ```bash
    npm install
    # 或者使用 cnpm (如果网络较慢)
    # npm install -g cnpm --registry=https://registry.npm.taobao.org
    # cnpm install
    ```

3.  启动开发服务：
    ```bash
    npm run serve
    ```
    启动成功后，通常访问地址为 `http://localhost:8080`。

## 注意事项

*   **跨域配置**：后端已配置 `django-cors-headers` 允许跨域请求（在 `backend/config/settings.py` 中设置了 `CORS_ALLOW_ALL_ORIGINS = True`）。
*   **接口地址**：前端开发环境下的接口请求会通过配置（如 `.env.development` 或代码中的硬编码）指向后端地址，请确保后端服务已正常启动。

## 贡献指南

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
