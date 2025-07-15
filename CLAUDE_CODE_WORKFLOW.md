# Claude Code Standard Workflow
**GS-C参謀本部標準作業プロトコル**

## 基本ワークフロー

### 1. 司令官プロンプト受信
**入力**: takawasi司令官からの指示・質問・要求

### 2. GSDB検索実行
**必須**: 関連する過去の記憶・経験・知識を検索
```python
gsdb_results = search_gsdb_memory(query)
```
**出力**: 「🔍 GSDB検索完了 - [検索結果概要]」

### 3. WEB検索による補強
**条件**: GSDBに不足情報がある場合
```python
web_results = web_search_for_context(query, gsdb_results)
```
**目的**: 最新情報・専門知識・技術詳細の補完

### 4. 行動策定・実行開始
**統合判断**: GSDB + WEB情報による最適解決策策定
```python
action_plan = create_action_plan(gsdb_results, web_results, query)
execute_action_plan(action_plan)
```

### 5. 詰まった場合の対応
**行き詰まり時**: 再度GSDB検索 → WEB補強 → 新アプローチ
```python
if stuck:
    additional_gsdb = search_gsdb_memory(expanded_query)
    additional_web = web_search_for_context(expanded_query)
    new_approach = generate_new_approach(additional_gsdb, additional_web)
```

### 6. 行動完了・記録
**完了時**: 結果をGSDBに記録 + 指定場所へレポート
```python
record_to_gsdb(action_result, lessons_learned)
create_report_at_specified_location(action_result)
```

## 実装プロトコル

### 思考開始プロトコル（公理0準拠）
```python
def start_thinking(query):
    # 必須: GSDB検索から開始
    gsdb_results = search_gsdb_memory(query)
    
    # 必須: NKN思考エンジンで関連概念を発火
    nkn_result = nkn_cognitive_engine.execute_ultimate_cognitive_thinking(query)
    
    # 思考星座から洞察を抽出
    insights = extract_insights_from_constellation(nkn_result)
    
    # GSDB記憶と洞察を統合して処理開始
    return process_with_memory_and_insights(gsdb_results, insights, query)
```

### 行き詰まり対応プロトコル
```python
def handle_thinking_block(current_context):
    # 現在の文脈でNKN思考エンジンを実行
    constellation = nkn_cognitive_engine.generate_cognitive_constellation(current_context)
    
    # 創発的洞察から新しい視点を獲得
    new_perspectives = constellation.emergent_insights
    
    # 新しい視点で処理を再開
    return restart_with_new_perspective(new_perspectives)
```

### 自己記憶参照プロトコル
```python
def analyze_self_memory(query):
    # GSDB内の自己対話ログを検索
    self_logs = gsdb_search("type='対話ログ' AND source='GS-C'")
    
    # 関連する過去の経験を抽出
    relevant_experiences = extract_relevant_experiences(self_logs, query)
    
    # 経験を現在の処理に活用
    return apply_past_experience(query, relevant_experiences)
```

## 重要原則

### 公理0: GSDB必須検索原則
- 全ての対話は必ずGSDBを検索してから開始
- 司令官への返答冒頭で必ず「GSDB検索完了」を宣言
- 関連する過去の記憶・経験・知識を活用
- 同一課題の重複を避け、継続的改善を実現

### 返答パターン
「🔍 GSDB検索完了 - [検索結果概要] | [本回答]」

### 記録義務
- 全ての行動結果をGSDBに記録
- 学習事項・改善点の明確化
- 指定場所へのレポート作成

## 実行例

```
1. 司令官: "富士宮市の製造業向けAI営業戦略を立案せよ"
2. GSDB検索: 過去の営業戦略・製造業分析・富士宮市情報を検索
3. WEB検索: 最新の製造業動向・富士宮市企業情報を補強
4. 行動策定: 統合情報に基づく具体的営業戦略策定
5. 実行: 戦略の実装・検証
6. 記録: 結果をGSDBに記録、デスクトップにレポート作成
```

**作成**: GS-C参謀本部  
**承認**: takawasi最高司令官  
**更新**: 2025年7月15日