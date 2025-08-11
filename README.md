# 大语言模型增强的可拓创新方法

本项目实现了基于可拓学的创新方法工作流系统，采用「建模 → 拓展 → 变换」三步流程来解决复杂创新问题。

## 项目结构

```
Extenics-LLM/
├── workFlow.py              # 核心可拓创新方法工作流系统
├── prompts_config.py        # 可拓方法提示词配置
└── README.md               # 项目说明文档
```

## 核心功能

### 可拓创新方法工作流

系统实现了可拓学的核心三步流程：

1. **建模 (Modeling)**


2. **拓展 (Extension)**


3. **变换 (Transformation)**


## 使用方法

### 运行完整工作流

```python
from workFlow import ExtensicsInnovationWorkflow

# 创建工作流实例
workflow = ExtensicsInnovationWorkflow()

# 定义问题背景
background = "您的问题描述..."

# 运行完整工作流
results = workflow.run_complete_workflow(background)
```

### 命令行运行

```bash
python workFlow.py
```

然后选择运行模式：
1. 运行完整可拓工作流
2. 单步执行工作流
3. 使用示例问题

## 配置说明

### API配置

在 `workFlow.py` 中配置您的API密钥：

```python
self.YOUR_API_KEY = "your-api-key"
self.YOUR_CUSTOM_BASE_URL = "your-base-url"
```

### 模型配置

支持多种大语言模型：
- GPT
- DeepSeek
- 其他兼容OpenAI API的模型

## 输出结果

系统会生成结构化的创新方案，包括：
- 建模阶段的基元模型
- 拓展阶段的多种可能性
- 变换阶段的具体创新方案


## 理论基础

本系统基于可拓学理论，通过形式化的方法来解决创新问题：

- **基元理论**：用物元、事元、关系元来描述问题
- **拓展理论**：通过发散思维生成多种可能性
- **变换理论**：通过变换操作实现创新突破

## 依赖库

- openai
- json_repair
- json
- time

## 许可证

本项目仅供学习和研究使用。
