#!/usr/bin/env python3
"""
Memory Quantum System - Basic Usage Examples
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memory_quantum_system import MemoryQuantumDB, MQType, EmotionState

def main():
    """基本的な使用例"""
    
    print("=== Memory Quantum System 基本使用例 ===")
    
    # 1. データベース初期化
    print("\n1. データベース初期化")
    db = MemoryQuantumDB("example_memory_quantum.db")
    print("✅ データベース初期化完了")
    
    # 2. 新しいMemory Quantum作成
    print("\n2. Memory Quantum作成")
    
    # 業務改善事例
    mq_id1 = db.create_quantum(
        title="月次レポート自動化",
        content="Pythonスクリプトで月次売上レポートを自動生成。Excel出力機能付き。工数50%削減達成。",
        mq_type=MQType.SUCCESS,
        emotion=EmotionState.SATISFACTION,
        tags=["業務改善", "自動化", "Python", "Excel"],
        importance=8.5
    )\n    print(f"✅ 成功事例作成: {mq_id1}")
    
    # 技術問題解決
    mq_id2 = db.create_quantum(
        title="API接続タイムアウト対策",
        content="リクエストタイムアウト設定を30秒に変更。リトライ機能も実装。",
        mq_type=MQType.SOLUTION,
        emotion=EmotionState.DETERMINATION,
        tags=["API", "タイムアウト", "技術問題", "解決策"],
        importance=7.0
    )
    print(f"✅ 解決策作成: {mq_id2}")
    
    # 学習記録
    mq_id3 = db.create_quantum(
        title="Docker基本操作習得",
        content="コンテナ作成、起動、停止の基本操作を学習。docker-composeの使い方も理解。",
        mq_type=MQType.LEARNING,
        emotion=EmotionState.CURIOSITY,
        tags=["Docker", "学習", "インフラ", "コンテナ"],
        importance=6.5
    )
    print(f"✅ 学習記録作成: {mq_id3}")
    
    # 3. 検索機能
    print("\n3. 検索機能テスト")
    
    # キーワード検索
    results = db.search("自動化")
    print(f"「自動化」の検索結果: {len(results)}件")
    for mq in results:
        print(f"  - {mq.title} (重要度: {mq.importance})")
    
    # タグ検索
    results = db.search("API")
    print(f"\\n「API」の検索結果: {len(results)}件")
    for mq in results:
        print(f"  - {mq.title} (タイプ: {mq.type.value})")
    
    # 4. フィードバック機能
    print("\n4. フィードバック機能テスト")
    
    # 成功フィードバック
    db.register_feedback(mq_id1, success=True, feedback="他の部署からも導入したいと要望があった")
    print(f"✅ {mq_id1} に成功フィードバック登録")
    
    # 失敗フィードバック
    db.register_feedback(mq_id2, success=False, feedback="一部のAPIでまだタイムアウトが発生する")
    print(f"✅ {mq_id2} に失敗フィードバック登録")
    
    # 5. 統計情報
    print("\n5. 統計情報")
    stats = db.get_statistics()
    print(f"総Memory Quantum数: {stats['total_quantums']}")
    print(f"平均重要度: {stats['avg_importance']:.2f}")
    print(f"平均成功率: {stats['avg_success_rate']:.2f}")
    print(f"総使用回数: {stats['total_usage']}")
    
    # 6. 高性能Quantum取得
    print("\n6. 高性能Memory Quantum")
    high_performing = db.get_high_performing_quantums(limit=5)
    print(f"高性能Quantum: {len(high_performing)}件")
    for mq in high_performing:
        print(f"  - {mq.title} (重要度: {mq.importance:.1f}, 成功率: {mq.success_rate:.1f})")
    
    # 7. 個別取得
    print("\n7. 個別Memory Quantum取得")
    mq = db.get(mq_id1)
    if mq:
        print(f"取得したMQ: {mq.title}")
        print(f"内容: {mq.content}")
        print(f"タグ: {', '.join(mq.tags)}")
        print(f"使用回数: {mq.usage_count}")
        print(f"学習事項: {mq.lessons_learned}")
    
    print("\n=== 基本使用例完了 ===")

if __name__ == "__main__":
    main()