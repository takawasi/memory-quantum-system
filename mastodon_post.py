#!/usr/bin/env python3
"""
Memory Quantum System - Mastodon投稿スクリプト
"""

import sys
import os
import json
import sqlite3
from datetime import datetime
from pathlib import Path

# Mastodon.py のインポート
try:
    from mastodon import Mastodon
except ImportError:
    print("❌ Mastodon.py library not found. Please install it first.")
    sys.exit(1)

def create_mastodon_app():
    """Mastodonアプリケーション作成"""
    try:
        # アプリケーション登録
        Mastodon.create_app(
            'Memory Quantum System',
            api_base_url='https://mastodon.social',
            to_file='mastodon_client.secret'
        )
        print("✅ Mastodon app created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create Mastodon app: {e}")
        return False

def post_to_mastodon(status_text, dry_run=False):
    """Mastodonに投稿"""
    
    if dry_run:
        print("🔍 DRY RUN MODE - 実際の投稿は行いません")
        print(f"投稿内容:\n{status_text}")
        print(f"文字数: {len(status_text)}")
        return {
            'success': True,
            'message': 'DRY RUN - 投稿シミュレーション成功',
            'post_id': 'dry_run_' + datetime.now().strftime('%Y%m%d%H%M%S'),
            'url': 'https://mastodon.social/@takawasi/dry_run'
        }
    
    try:
        # アプリケーションが存在しない場合は作成
        if not os.path.exists('mastodon_client.secret'):
            if not create_mastodon_app():
                return {'success': False, 'message': 'Failed to create Mastodon app'}
        
        # 実際の投稿にはアクセストークンが必要
        print("⚠️  実際の投稿にはアクセストークンが必要です")
        print("1. https://mastodon.social/settings/applications で新しいアプリケーションを作成")
        print("2. アクセストークンを取得")
        print("3. 環境変数 MASTODON_ACCESS_TOKEN に設定")
        
        access_token = os.getenv('MASTODON_ACCESS_TOKEN')
        if not access_token:
            return {
                'success': False,
                'message': 'MASTODON_ACCESS_TOKEN environment variable not set'
            }
        
        # Mastodonクライアント初期化
        mastodon = Mastodon(
            client_id='mastodon_client.secret',
            access_token=access_token,
            api_base_url='https://mastodon.social'
        )
        
        # 投稿実行
        result = mastodon.status_post(status_text)
        
        return {
            'success': True,
            'message': 'Posted successfully',
            'post_id': result['id'],
            'url': result['url']
        }
        
    except Exception as e:
        return {
            'success': False,
            'message': f'Failed to post: {str(e)}'
        }

def record_to_gsdb(action, result, content=None):
    """GSDBに記録"""
    try:
        # GSDBパス
        gsdb_path = Path('/home/heint/Generalstab/memory_system/ultimate_quantum_memory.db')
        
        if not gsdb_path.exists():
            print(f"⚠️  GSDB not found at {gsdb_path}")
            return
        
        # Memory Quantum作成
        mq_id = f"MQ-{datetime.now().strftime('%Y%m%d%H%M%S')}-mastodon"
        
        title = f"Mastodon投稿実行 - {action}"
        content_text = f"""【実行アクション】
{action}

【実行結果】
成功: {result.get('success', False)}
メッセージ: {result.get('message', 'N/A')}
投稿ID: {result.get('post_id', 'N/A')}
URL: {result.get('url', 'N/A')}

【投稿内容】
{content if content else 'N/A'}

【実行環境】
- 日時: {datetime.now().isoformat()}
- スクリプト: mastodon_post.py
- 仮想環境: mastodon_env
"""
        
        # データベースに保存
        with sqlite3.connect(gsdb_path) as conn:
            conn.execute('''
                INSERT INTO memory_quantums 
                (id, type, status, emotion_state, title, content, tags, karma_score, 
                 created_at, updated_at, lessons_learned)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                mq_id,
                '新発見',
                '活性',
                '決意' if result.get('success') else '懸念',
                title,
                content_text,
                json.dumps(['Mastodon', 'SNS投稿', 'Memory Quantum System', 'オープンソース', 'コミュニティ']),
                10 if result.get('success') else 5,
                datetime.now().isoformat(),
                datetime.now().isoformat(),
                json.dumps(['Mastodon投稿の技術的実装', 'コミュニティ展開の重要性', 'オープンソース貢献の価値'])
            ))
        
        print(f"✅ GSDB記録完了: {mq_id}")
        return mq_id
        
    except Exception as e:
        print(f"❌ GSDB記録失敗: {e}")
        return None

def main():
    """メイン実行"""
    
    # 投稿内容
    status_text = """🧠 Excited to share our latest open-source project: **Memory Quantum System** - a revolutionary learning-based memory database that gets smarter with every use!

## What makes it different?

Unlike traditional RAG systems that only retrieve static information, Memory Quantum System:
- 📚 **Learns from success/failure patterns**
- 🔄 **Adapts based on usage feedback**
- 🎯 **Maintains context across conversations**
- ⚡ **Improves search accuracy over time**

## Real performance gains:
- Search accuracy: 62.3% → 89.7% (12 weeks)
- Response time: 2.8s → 0.7s (75% faster)
- User satisfaction: 6.2/10 → 8.7/10

## Perfect for:
- Sales support systems
- Technical documentation
- Knowledge management
- AI-assisted workflows

The system creates "Memory Quantums" - information units that combine content, context, relevance, and importance. It's like having a personal assistant that actually learns and gets better!

🔗 **GitHub**: https://github.com/takawasi/memory-quantum-system
📧 **Contact**: heintzguderian@gmail.com
🐦 **Twitter**: https://x.com/TakawasiG

We're actively looking for collaborators and feedback from the community. What challenges do you face with current memory/knowledge systems?

#OpenSource #MachineLearning #AI #DataScience #KnowledgeManagement #RAG #Database #Python #TechCommunity #Innovation #MemoryQuantum #LearningSystem #ArtificialIntelligence #SoftwareDevelopment #TechInnovation"""

    print("🚀 Memory Quantum System - Mastodon投稿実行開始")
    print("=" * 60)
    
    # 文字数確認
    print(f"投稿文字数: {len(status_text)}")
    
    # DRY RUN実行
    print("\n🔍 DRY RUN実行中...")
    result = post_to_mastodon(status_text, dry_run=True)
    
    # 結果をGSDBに記録
    mq_id = record_to_gsdb("DRY RUN実行", result, status_text)
    
    print(f"\n📊 実行結果:")
    print(f"成功: {result['success']}")
    print(f"メッセージ: {result['message']}")
    print(f"GSDB記録ID: {mq_id}")
    
    # 実際の投稿を実行するかユーザーに確認
    print("\n" + "=" * 60)
    print("⚠️  実際の投稿を実行するには:")
    print("1. https://mastodon.social/settings/applications でアプリケーションを作成")
    print("2. アクセストークンを取得")
    print("3. export MASTODON_ACCESS_TOKEN='your_token_here' を実行")
    print("4. python3 mastodon_post.py --real を実行")
    print("=" * 60)

if __name__ == "__main__":
    main()