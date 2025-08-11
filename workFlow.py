"""
可拓创新方法工作流系统
实现「建模 → 拓展 → 变换 → 选优」四步流程
"""

from openai import OpenAI
from prompts_config import prompt_templates


class ExtensicsInnovationWorkflow:
    """可拓创新方法工作流系统"""
    
    def __init__(self):
        """初始化系统，配置LLM客户端"""

        self.YOUR_API_KEY = "your-api-key"
        self.YOUR_CUSTOM_BASE_URL = "your-base-url"
        self.client = OpenAI(
            api_key=self.YOUR_API_KEY,
            base_url=self.YOUR_CUSTOM_BASE_URL,
        )
        self.model_name = "deepseek-v3-250324"
        
        # 存储各步骤的结果
        self.step_results = {}
        
        # 引用prompt模板
        self.prompts = prompt_templates
    
    
    def _call_llm(self, system_prompt, user_prompt, model_name = "deepseek-v3-250324",temperature=1.0):
        """调用大语言模型"""
        try:

            client = self.client


            response = client.chat.completions.create(
                model = model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                # response_format={'type': 'json_object'},
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM调用错误: {e}")
            return None
    
    def _call_llm_with_model(self, system_prompt, user_prompt, model_name, temperature=0.7, response_format=False):
        """调用指定模型的大语言模型"""
        try:
          
            client = self.client

            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                # 增加参数控制是否要按照json格式输出
                response_format={'type': 'json_object'} if response_format else None,
                temperature = temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM调用错误 (模型: {model_name}): {e}")
            return None
    
    def step1_modeling(self, background_description):
        """
        步骤1：建模 (Model)
        用"三元组"形式给出焦点事元，指出主要限制条件
        """
        system_prompt, user_template = self.prompts.get_both_prompts('step1_modeling')
        user_prompt = user_template.format(background_description=background_description)
        
        response = self._call_llm(system_prompt, user_prompt, temperature=0.2)
        if response:
            print(response)
            return response
        return None
    
    def step2_extend(self, background_description, modeling_result):
        """
        步骤2：拓展 (Extend)
        在三个维度上发散列举可能的拓展
        """
        if not modeling_result:
            print("错误：需要先完成建模步骤")
            return None
        
        system_prompt, user_template = self.prompts.get_both_prompts('step2_extend')
        user_prompt = user_template.format(
            background_description=background_description,
            modeling_result=modeling_result
        )
        
        response = self._call_llm(system_prompt, user_prompt, temperature=1.0)
        if response:
            print(response)
            return response
        return None
    
    def step3_transform(self, background_description, modeling_result, extend_result):
        """
        步骤3：变换 (Transform)
        对拓展结果进行对换、压缩、放大、升维、析维等操作
        """
        if not modeling_result or not extend_result:
            print("错误：需要先完成建模和拓展步骤")
            return None
        
        system_prompt, user_template = self.prompts.get_both_prompts('step3_transform')
        user_prompt = user_template.format(
            background_description=background_description,
            modeling_result=modeling_result,
            extend_result=extend_result
        )
        
        response = self._call_llm(system_prompt, user_prompt, temperature=1.0)
        if response:
            print(response)
            return response
        return None
    
    def run_complete_workflow(self, background_description):
        """
        运行完整的可拓创新方法工作流程
        实现「建模 → 拓展 → 变换」三步流程
        """
        print("=== 可拓创新方法工作流开始 ===\n")
        
        # 步骤1：建模
        print("步骤1：建模中...")
        modeling_result = self.step1_modeling(background_description)
        if not modeling_result:
            print("建模步骤失败，工作流终止")
            return None
        
        # 步骤2：拓展
        print("\n步骤2：拓展中...")
        extend_result = self.step2_extend(background_description, modeling_result)
        if not extend_result:
            print("拓展步骤失败，工作流终止")
            return None
        
        # 步骤3：变换
        print("\n步骤3：变换中...")
        transform_result = self.step3_transform(background_description, modeling_result, extend_result)
        if not transform_result:
            print("变换步骤失败，工作流终止")
            return None
        
        # 处理变换结果，提取<answer>标签中的内容
        if "<answer>" in transform_result and "</answer>" in transform_result:
            transform_result = transform_result.split("<answer>")[1].split("</answer>")[0]
        
        print("\n=== 可拓创新方法工作流完成 ===")
        
        # 返回完整结果
        complete_result = {
            'modeling': modeling_result,
            'extend': extend_result,
            'transform': transform_result
        }
        
        return complete_result


def main():
    """主函数示例"""
    # 创建工作流实例
    workflow = ExtensicsInnovationWorkflow()
    
    # 示例背景描述
    background = """
    现有某款红光激光笔是长方体、黑色的，价格 210 元，电源类型为一节 7 号电池，无电源开关， 红色激光指示，有点、直线、圆圈三种指示图形， 可翻页，可黑屏，可直接返回编辑状态，在激光笔 背面底部设计了 USB 卡插槽。通过用户调查可知 该产品的缺点为：形状不美观、颜色单调、无图案、 用电量高、价格高。
    """
    
    print("=== 可拓创新方法工作流系统 ===")
    print("本系统实现「建模 → 拓展 → 变换」三步可拓创新流程")
    print("\n请选择运行模式：")
    print("1. 运行完整可拓工作流")
    print("2. 使用示例问题")
    
    choice = input("\n请输入选择 (1-2): ").strip()
    
    if choice == "1":
        # 运行完整工作流
        print("\n=== 运行完整可拓创新工作流 ===")
        background = input("请输入问题背景描述: ").strip()
        if not background:
            background = """
            现有某款红光激光笔是长方体、黑色的，价格 210 元，电源类型为一节 7 号电池，无电源开关， 红色激光指示，有点、直线、圆圈三种指示图形， 可翻页，可黑屏，可直接返回编辑状态，在激光笔 背面底部设计了 USB 卡插槽。通过用户调查可知 该产品的缺点为：形状不美观、颜色单调、无图案、 用电量高、价格高。
            """
        workflow.run_complete_workflow(background)
    elif choice == "2":
        # 使用示例问题
        print("\n=== 使用示例问题运行可拓工作流 ===")
        results = workflow.run_complete_workflow(background)
    else:
        print("无效选择，默认使用示例问题")
        results = workflow.run_complete_workflow(background)


if __name__ == "__main__":
    main() 