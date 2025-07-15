#!/usr/bin/env python3
"""
Memory Quantum System - Learning-based Memory Database

Revolutionary memory system for AI-human collaboration
- Dynamic memory structure that gets smarter with use
- Learning and leveraging success/failure patterns
- High-precision search with context preservation
- Self-improving feedback loop
"""

import sys
import os
import json
import sqlite3
import hashlib
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class MQType(Enum):
    """Memory Quantum Type"""
    SUCCESS = "success_experience"
    FAILURE = "failure_experience" 
    NEW_DISCOVERY = "new_discovery"
    INSIGHT = "insight"
    LEARNING = "learning_record"
    STRATEGY = "strategy"
    PATTERN = "pattern"
    SOLUTION = "solution"


class MQStatus(Enum):
    """Memory Quantum Status"""
    ACTIVE = "active"
    RESOURCED = "resourced"
    ARCHIVED = "archived"
    PENDING = "pending"


class EmotionState(Enum):
    """Emotion State"""
    JOY = "joy"
    CURIOSITY = "curiosity"
    CONCERN = "concern"
    DETERMINATION = "determination"
    NEUTRAL = "neutral"
    SATISFACTION = "satisfaction"
    FRUSTRATION = "frustration"


@dataclass
class MemoryQuantum:
    """Memory Quantum - Basic unit of memory"""
    id: str
    type: MQType
    status: MQStatus
    emotion_state: EmotionState
    title: str
    content: str
    tags: List[str]
    importance: float
    usage_count: int
    success_rate: float
    created_at: str
    updated_at: str
    related_ids: List[str]
    lessons_learned: List[str]


class MemoryQuantumDB:
    """Memory Quantum Database - Learning-based memory database"""
    
    def __init__(self, db_path: str = "memory_quantum.db"):
        self.db_path = Path(db_path)
        self._init_database()
        
    def _init_database(self):
        """Initialize database"""
        with sqlite3.connect(self.db_path) as conn:
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
            
            # Create indexes
            indices = [
                "CREATE INDEX IF NOT EXISTS idx_mq_type ON memory_quantums(type)",
                "CREATE INDEX IF NOT EXISTS idx_mq_status ON memory_quantums(status)",
                "CREATE INDEX IF NOT EXISTS idx_mq_importance ON memory_quantums(importance)",
                "CREATE INDEX IF NOT EXISTS idx_mq_usage ON memory_quantums(usage_count)",
                "CREATE INDEX IF NOT EXISTS idx_mq_created ON memory_quantums(created_at)"
            ]
            
            for idx in indices:
                conn.execute(idx)
    
    def generate_mq_id(self, title: str) -> str:
        """Generate Memory Quantum ID"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        title_hash = hashlib.sha256(title.encode()).hexdigest()[:6]
        return f"MQ-{timestamp}-{title_hash}"
    
    def create_quantum(self, 
                      title: str,
                      content: str,
                      mq_type: MQType = MQType.NEW_DISCOVERY,
                      emotion: EmotionState = EmotionState.CURIOSITY,
                      tags: List[str] = None,
                      importance: float = 5.0) -> str:
        """Create new Memory Quantum"""
        
        if tags is None:
            tags = []
            
        mq_id = self.generate_mq_id(title)
        
        mq = MemoryQuantum(
            id=mq_id,
            type=mq_type,
            status=MQStatus.ACTIVE,
            emotion_state=emotion,
            title=title,
            content=content,
            tags=tags,
            importance=importance,
            usage_count=0,
            success_rate=0.0,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            related_ids=[],
            lessons_learned=[]
        )
        
        self._save_to_db(mq)
        return mq_id
    
    def _save_to_db(self, mq: MemoryQuantum):
        """Save to database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO memory_quantums 
                (id, type, status, emotion_state, title, content, tags, importance,
                 usage_count, success_rate, created_at, updated_at, related_ids, lessons_learned)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                mq.id, mq.type.value, mq.status.value, mq.emotion_state.value,
                mq.title, mq.content, json.dumps(mq.tags), mq.importance,
                mq.usage_count, mq.success_rate, mq.created_at, mq.updated_at,
                json.dumps(mq.related_ids), json.dumps(mq.lessons_learned)
            ))
    
    def search(self, query: str, limit: int = 10) -> List[MemoryQuantum]:
        """Search function"""
        results = []
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT * FROM memory_quantums 
                WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?
                ORDER BY importance DESC, usage_count DESC, updated_at DESC
                LIMIT ?
            ''', (f'%{query}%', f'%{query}%', f'%{query}%', limit))
            
            for row in cursor.fetchall():
                results.append(self._row_to_mq(row))
        
        return results
    
    def get(self, mq_id: str) -> Optional[MemoryQuantum]:
        """Get MQ by ID"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                'SELECT * FROM memory_quantums WHERE id = ?', 
                (mq_id,)
            )
            row = cursor.fetchone()
            return self._row_to_mq(row) if row else None
    
    def register_feedback(self, mq_id: str, success: bool, feedback: str = ""):
        """Register usage feedback"""
        mq = self.get(mq_id)
        if not mq:
            return
        
        # Increase usage count
        mq.usage_count += 1
        
        # Update success rate
        if success:
            mq.success_rate = (mq.success_rate * (mq.usage_count - 1) + 1.0) / mq.usage_count
        else:
            mq.success_rate = (mq.success_rate * (mq.usage_count - 1) + 0.0) / mq.usage_count
        
        # Adjust importance
        if success:
            mq.importance = min(10.0, mq.importance + 0.1)
        else:
            mq.importance = max(0.0, mq.importance - 0.1)
        
        # Record feedback
        if feedback:
            mq.lessons_learned.append(feedback)
        
        mq.updated_at = datetime.now().isoformat()
        self._save_to_db(mq)
    
    def _row_to_mq(self, row) -> MemoryQuantum:
        """Convert database row to MQ object"""
        return MemoryQuantum(
            id=row[0],
            type=MQType(row[1]),
            status=MQStatus(row[2]),
            emotion_state=EmotionState(row[3]),
            title=row[4],
            content=row[5],
            tags=json.loads(row[6]) if row[6] else [],
            importance=row[7],
            usage_count=row[8],
            success_rate=row[9],
            created_at=row[10],
            updated_at=row[11],
            related_ids=json.loads(row[12]) if row[12] else [],
            lessons_learned=json.loads(row[13]) if row[13] else []
        )
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT 
                    COUNT(*) as total,
                    AVG(importance) as avg_importance,
                    AVG(success_rate) as avg_success_rate,
                    SUM(usage_count) as total_usage,
                    MAX(importance) as max_importance,
                    MIN(importance) as min_importance
                FROM memory_quantums
            ''')
            
            stats = cursor.fetchone()
            
            return {
                "total_quantums": stats[0],
                "avg_importance": stats[1] or 0,
                "avg_success_rate": stats[2] or 0,
                "total_usage": stats[3] or 0,
                "max_importance": stats[4] or 0,
                "min_importance": stats[5] or 0
            }
    
    def get_high_performing_quantums(self, limit: int = 10) -> List[MemoryQuantum]:
        """Get high-performing quantums"""
        results = []
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT * FROM memory_quantums 
                WHERE success_rate > 0.7 AND usage_count > 2
                ORDER BY importance DESC, success_rate DESC, usage_count DESC
                LIMIT ?
            ''', (limit,))
            
            for row in cursor.fetchall():
                results.append(self._row_to_mq(row))
        
        return results


# Usage example
if __name__ == "__main__":
    # Initialize database
    db = MemoryQuantumDB("memory_quantum.db")
    
    # Create new memory
    mq_id = db.create_quantum(
        title="API authentication error resolution",
        content="Token expiration was the cause. Re-authenticate with refresh token.",
        mq_type=MQType.SOLUTION,
        tags=["API", "authentication", "troubleshooting"],
        importance=8.0
    )
    
    print(f"Created MQ ID: {mq_id}")
    
    # Search
    results = db.search("API")
    print(f"\nSearch results: {len(results)} items")
    
    for mq in results:
        print(f"- {mq.title} (importance: {mq.importance})")
    
    # Display statistics
    stats = db.get_statistics()
    print(f"\nStatistics:")
    print(f"Total quantums: {stats['total_quantums']}")
    print(f"Average importance: {stats['avg_importance']:.2f}")
    print(f"Average success rate: {stats['avg_success_rate']:.2f}")
