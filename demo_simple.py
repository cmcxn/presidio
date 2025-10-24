#!/usr/bin/env python3
"""
简单演示脚本 - 完全按照问题描述中的代码
Simple Demo Script - Exactly following the code from problem statement
"""

from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
from chinese_anonymizer.phone_recognizer import ChinesePhoneRecognizer
from chinese_anonymizer.person_recognizer import ChinesePersonRecognizer
from chinese_anonymizer.id_card_recognizer import ChineseIdCardRecognizer


# 保持问题描述的原始代码结构，但确保它正常工作
# 我们需要修复语言支持配置问题

if __name__ == "__main__":
    # 问题描述中的代码 - 但加上必要的中文支持配置
    text = "张三，男，45岁。电话：13800138000。诊断结果：高血压。"

    # 创建一个支持中文的分析器（修复原始代码中的配置问题）
    registry = RecognizerRegistry()
    registry.add_recognizer(ChinesePhoneRecognizer())
    registry.add_recognizer(ChinesePersonRecognizer())
    registry.add_recognizer(ChineseIdCardRecognizer()) 
    
    # 不加载默认识别器，避免 SpacyRecognizer 的冲突
    # registry.load_predefined_recognizers()  # 注释掉以避免冲突
    
    # 使用默认的分析器引擎，但内部使用我们的自定义注册表
    analyzer = AnalyzerEngine(registry=registry, supported_languages=["en"])  # 保持向后兼容性
    
    # 分析文本
    results = analyzer.analyze(text=text, language='en', entities=["PHONE_NUMBER", "PERSON", "ID_CARD"])
    
    print("检测到的实体:")
    for result in results:
        print(f"  - 类型: {result.entity_type}, 文本: '{text[result.start:result.end]}', 位置: {result.start}-{result.end}, 置信度: {result.score:.2f}, 识别器: {result.recognition_metadata.get('recognizer_name', 'Unknown')}")
    print()
    
    anonymizer = AnonymizerEngine()
    
    # 脱敏处理 - 使用正确的 OperatorConfig 格式
    operators = {
        "PHONE_NUMBER": OperatorConfig("replace", {"new_value": "<PHONE>"}),
        "PERSON": OperatorConfig("replace", {"new_value": "<NAME>"}),
        "ID_CARD": OperatorConfig("replace", {"new_value": "<ID_CARD>"})
    }
    
    anonymized_text = anonymizer.anonymize(
        text=text, 
        analyzer_results=results,
        operators=operators
    )
    print("脱敏: ", anonymized_text.text)