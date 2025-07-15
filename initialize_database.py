#!/usr/bin/env python3
"""
Memory Quantum System - Database Initialization Script
"""

import sqlite3
import sys
from pathlib import Path

def initialize_database(db_path: str = "memory_quantum.db"):
    """Memory Quantum System データベース初期化"""
    
    db_file = Path(db_path)
    
    # 既存データベースがある場合の確認
    if db_file.exists():
        response = input(f"Database {db_path} already exists. Do you want to recreate it? (y/N): ")
        if response.lower() != 'y':
            print("Database initialization cancelled.")
            return
        
        # バックアップ作成
        backup_path = f"{db_path}.backup"
        db_file.rename(backup_path)
        print(f"Existing database backed up to {backup_path}")
    
    # データベース作成
    with sqlite3.connect(db_path) as conn:
        # Memory Quantumテーブル作成
        conn.execute('''
            CREATE TABLE IF NOT EXISTS memory_quantums (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                status TEXT NOT NULL,
                emotion_state TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT,
                importance REAL DEFAULT 5.0,
                usage_count INTEGER DEFAULT 0,
                success_rate REAL DEFAULT 0.0,
                created_at TEXT,
                updated_at TEXT,
                related_ids TEXT,
                lessons_learned TEXT
            )
        ''')
        
        # インデックス作成
        indices = [
            "CREATE INDEX IF NOT EXISTS idx_mq_type ON memory_quantums(type)",
            "CREATE INDEX IF NOT EXISTS idx_mq_status ON memory_quantums(status)",
            "CREATE INDEX IF NOT EXISTS idx_mq_importance ON memory_quantums(importance)",
            "CREATE INDEX IF NOT EXISTS idx_mq_usage ON memory_quantums(usage_count)",
            "CREATE INDEX IF NOT EXISTS idx_mq_created ON memory_quantums(created_at)",
            "CREATE INDEX IF NOT EXISTS idx_mq_title ON memory_quantums(title)",
            "CREATE INDEX IF NOT EXISTS idx_mq_content ON memory_quantums(content)"
        ]
        
        for idx in indices:
            conn.execute(idx)
        
        # 動的索引テーブル作成
        conn.execute('''
            CREATE TABLE IF NOT EXISTS dynamic_index (
                quantum_id TEXT,
                concept TEXT,
                weight REAL,
                last_updated TEXT,
                FOREIGN KEY (quantum_id) REFERENCES memory_quantums(id)
            )
        ''')
        
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_dynamic_concept ON dynamic_index(concept)
        ''')
        
        conn.commit()
        print(f"✅ Database initialized successfully: {db_path}")

def main():
    """メイン関数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Memory Quantum System Database Initialization")
    parser.add_argument("--db", default="memory_quantum.db", help="Database file path")
    
    args = parser.parse_args()
    
    try:
        initialize_database(args.db)
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()