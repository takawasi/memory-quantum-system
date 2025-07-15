#!/usr/bin/env python3
"""
Memory Quantum System - Advanced Usage Examples
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memory_quantum_system import MemoryQuantumDB, MQType, EmotionState, MQStatus
from datetime import datetime, timedelta

def main():
    """高度な使用例"""
    
    print("=== Memory Quantum System 高度使用例 ===")
    
    # データベース初期化
    db = MemoryQuantumDB("advanced_memory_quantum.db")
    
    # 1. 複数のMemory Quantumを系統的に作成
    print("\n1. 系統的なMemory Quantum作成")
    
    # プロジェクト管理系
    project_mqs = []
    
    # 失敗体験
    failure_id = db.create_quantum(
        title="新機能リリース遅延",
        content="要件定義が不十分で開発途中で大幅な仕様変更が発生。リリースが2週間遅延。",
        mq_type=MQType.FAILURE,
        emotion=EmotionState.FRUSTRATION,
        tags=["プロジェクト管理", "要件定義", "遅延", "失敗"],
        importance=9.0
    )
    project_mqs.append(failure_id)
    
    # その失敗からの学習
    learning_id = db.create_quantum(
        title="要件定義プロセス改善",
        content="詳細な要件定義フェーズを設定。ステークホルダーとの認識合わせを週次で実施。",
        mq_type=MQType.LEARNING,
        emotion=EmotionState.DETERMINATION,
        tags=["プロジェクト管理", "要件定義", "改善", "プロセス"],
        importance=8.5
    )
    project_mqs.append(learning_id)
    
    # 成功体験
    success_id = db.create_quantum(
        title="次期プロジェクト成功",
        content="改善した要件定義プロセスを適用。予定通りリリース完了。品質も向上。",
        mq_type=MQType.SUCCESS,
        emotion=EmotionState.JOY,
        tags=["プロジェクト管理", "成功", "改善効果", "品質向上"],
        importance=9.5
    )
    project_mqs.append(success_id)
    
    print(f"✅ プロジェクト管理系Memory Quantum作成: {len(project_mqs)}件")
    
    # 2. 関連性の構築
    print("\n2. Memory Quantum間の関連性構築")
    
    # 失敗 → 学習 → 成功の流れを関連付け
    failure_mq = db.get(failure_id)
    learning_mq = db.get(learning_id)
    success_mq = db.get(success_id)
    
    if failure_mq and learning_mq and success_mq:
        # 関連IDを設定
        failure_mq.related_ids = [learning_id]
        learning_mq.related_ids = [failure_id, success_id]
        success_mq.related_ids = [learning_id]
        
        # データベース更新
        db._save_to_db(failure_mq)
        db._save_to_db(learning_mq)
        db._save_to_db(success_mq)
        
        print("✅ Memory Quantum間の関連性構築完了")
    
    # 3. 段階的フィードバック
    print("\n3. 段階的フィードバック・学習サイクル")
    
    # 複数回の利用とフィードバック
    for i in range(5):
        # 成功フィードバック
        db.register_feedback(learning_id, success=True, 
                           feedback=f"改善プロセス適用第{i+1}回目 - 効果確認")
        
        # 重要度と成功率の変化を確認
        mq = db.get(learning_id)
        print(f"  {i+1}回目: 重要度={mq.importance:.2f}, 成功率={mq.success_rate:.2f}")
    
    # 4. 高度な検索・分析
    print("\n4. 高度な検索・分析")
    
    # タイプ別検索
    success_quantums = [mq for mq in [db.get(pid) for pid in project_mqs] if mq and mq.type == MQType.SUCCESS]
    failure_quantums = [mq for mq in [db.get(pid) for pid in project_mqs] if mq and mq.type == MQType.FAILURE]
    
    print(f"成功体験: {len(success_quantums)}件")
    print(f"失敗体験: {len(failure_quantums)}件")
    
    # 重要度分析
    all_quantums = [db.get(pid) for pid in project_mqs]
    avg_importance = sum(mq.importance for mq in all_quantums if mq) / len(all_quantums)
    print(f"平均重要度: {avg_importance:.2f}")
    
    # 5. パフォーマンス分析
    print("\n5. パフォーマンス分析")
    
    # 高性能Quantum
    high_performers = db.get_high_performing_quantums(limit=3)
    print(f"高性能Memory Quantum: {len(high_performers)}件")
    for mq in high_performers:
        print(f"  - {mq.title}")
        print(f"    重要度: {mq.importance:.1f}, 成功率: {mq.success_rate:.1f}, 使用回数: {mq.usage_count}")
    
    # 6. 学習パターンの抽出
    print("\n6. 学習パターンの抽出")
    
    # 失敗→学習→成功のパターン検出
    pattern_analysis = analyze_learning_patterns(db, project_mqs)
    print(f"学習パターン分析:")
    print(f"  - 失敗体験数: {pattern_analysis['failure_count']}")
    print(f"  - 学習記録数: {pattern_analysis['learning_count']}")
    print(f"  - 成功体験数: {pattern_analysis['success_count']}")
    print(f"  - 失敗→成功変換率: {pattern_analysis['conversion_rate']:.1f}%")
    
    # 7. 時系列分析
    print("\n7. 時系列分析")
    
    # 作成日時による分析
    quantums = [db.get(pid) for pid in project_mqs]
    quantums.sort(key=lambda mq: mq.created_at if mq else "")
    
    print("時系列順Memory Quantum:")
    for i, mq in enumerate(quantums):
        if mq:
            print(f"  {i+1}. {mq.title} ({mq.type.value}) - {mq.created_at[:10]}")
    
    # 8. 最終統計
    print("\n8. 最終統計")
    stats = db.get_statistics()
    print(f"総Memory Quantum数: {stats['total_quantums']}")
    print(f"平均重要度: {stats['avg_importance']:.2f}")
    print(f"平均成功率: {stats['avg_success_rate']:.2f}")
    print(f"総使用回数: {stats['total_usage']}")
    
    print("\n=== 高度使用例完了 ===")

def analyze_learning_patterns(db: MemoryQuantumDB, quantum_ids: list) -> dict:
    """学習パターン分析"""
    
    quantums = [db.get(qid) for qid in quantum_ids]
    
    failure_count = sum(1 for mq in quantums if mq and mq.type == MQType.FAILURE)
    learning_count = sum(1 for mq in quantums if mq and mq.type == MQType.LEARNING)
    success_count = sum(1 for mq in quantums if mq and mq.type == MQType.SUCCESS)
    
    conversion_rate = (success_count / failure_count * 100) if failure_count > 0 else 0
    
    return {
        'failure_count': failure_count,
        'learning_count': learning_count,
        'success_count': success_count,
        'conversion_rate': conversion_rate
    }

if __name__ == "__main__":
    main()