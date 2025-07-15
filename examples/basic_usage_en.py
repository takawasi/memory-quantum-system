#!/usr/bin/env python3
"""
Memory Quantum System - Basic Usage Examples (English)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memory_quantum_system import MemoryQuantumDB, MQType, EmotionState

def main():
    """Basic usage example"""
    
    print("=== Memory Quantum System Basic Usage Example ===")
    
    # 1. Database initialization
    print("\n1. Database initialization")
    db = MemoryQuantumDB("example_memory_quantum.db")
    print("✅ Database initialization completed")
    
    # 2. Create new Memory Quantum
    print("\n2. Memory Quantum creation")
    
    # Business improvement case
    mq_id1 = db.create_quantum(
        title="Monthly report automation",
        content="Python script automatically generates monthly sales reports. Excel output functionality included. 50% reduction in work hours achieved.",
        mq_type=MQType.SUCCESS,
        emotion=EmotionState.SATISFACTION,
        tags=["business_improvement", "automation", "Python", "Excel"],
        importance=8.5
    )
    print(f"✅ Success case created: {mq_id1}")
    
    # Technical problem resolution
    mq_id2 = db.create_quantum(
        title="API connection timeout countermeasure",
        content="Changed request timeout setting to 30 seconds. Implemented retry functionality as well.",
        mq_type=MQType.SOLUTION,
        emotion=EmotionState.DETERMINATION,
        tags=["API", "timeout", "technical_issue", "solution"],
        importance=7.0
    )
    print(f"✅ Solution created: {mq_id2}")
    
    # Learning record
    mq_id3 = db.create_quantum(
        title="Docker basic operations mastery",
        content="Learned basic operations of container creation, startup, and stopping. Also understood docker-compose usage.",
        mq_type=MQType.LEARNING,
        emotion=EmotionState.CURIOSITY,
        tags=["Docker", "learning", "infrastructure", "containers"],
        importance=6.5
    )
    print(f"✅ Learning record created: {mq_id3}")
    
    # 3. Search functionality
    print("\n3. Search functionality test")
    
    # Keyword search
    results = db.search("automation")
    print(f"Search results for 'automation': {len(results)} items")
    for mq in results:
        print(f"  - {mq.title} (importance: {mq.importance})")
    
    # Tag search
    results = db.search("API")
    print(f"\nSearch results for 'API': {len(results)} items")
    for mq in results:
        print(f"  - {mq.title} (type: {mq.type.value})")
    
    # 4. Feedback functionality
    print("\n4. Feedback functionality test")
    
    # Success feedback
    db.register_feedback(mq_id1, success=True, feedback="Other departments also requested introduction")
    print(f"✅ Success feedback registered for {mq_id1}")
    
    # Failure feedback
    db.register_feedback(mq_id2, success=False, feedback="Some APIs still experience timeouts")
    print(f"✅ Failure feedback registered for {mq_id2}")
    
    # 5. Statistics
    print("\n5. Statistics")
    stats = db.get_statistics()
    print(f"Total Memory Quantums: {stats['total_quantums']}")
    print(f"Average importance: {stats['avg_importance']:.2f}")
    print(f"Average success rate: {stats['avg_success_rate']:.2f}")
    print(f"Total usage: {stats['total_usage']}")
    
    # 6. High-performing Quantum retrieval
    print("\n6. High-performing Memory Quantums")
    high_performing = db.get_high_performing_quantums(limit=5)
    print(f"High-performing Quantums: {len(high_performing)} items")
    for mq in high_performing:
        print(f"  - {mq.title} (importance: {mq.importance:.1f}, success rate: {mq.success_rate:.1f})")
    
    # 7. Individual retrieval
    print("\n7. Individual Memory Quantum retrieval")
    mq = db.get(mq_id1)
    if mq:
        print(f"Retrieved MQ: {mq.title}")
        print(f"Content: {mq.content}")
        print(f"Tags: {', '.join(mq.tags)}")
        print(f"Usage count: {mq.usage_count}")
        print(f"Lessons learned: {mq.lessons_learned}")
    
    print("\n=== Basic usage example completed ===")

if __name__ == "__main__":
    main()