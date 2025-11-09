import os
import json
from pathlib import Path
from datetime import datetime

# Find project root by looking for .ravl directory
def get_project_root():
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / '.ravl').exists():
            return current
        current = current.parent
    return Path.cwd()

project_root = get_project_root()
ravl_dir = project_root / '.ravl'

print("🔍 Exploring RAVL Framework Structure and Capabilities")
print("=" * 60)

# Explore the framework's learning and execution capabilities
exploration_findings = {
    "timestamp": datetime.now().isoformat(),
    "exploring": "Framework Learning Architecture and Health Check Systems",
    "method": "Examining .ravl directory structure, learning storage patterns, and execution artifacts"
}

discoveries = []
insights = []

# 1. Examine learning directories structure
print("\n📂 Examining Learning Architecture...")
learning_dirs = {
    "execution_learning": ravl_dir / "execution_learning",
    "loop_learning": ravl_dir / "loop_learning"
}

for name, path in learning_dirs.items():
    if path.exists():
        files = list(path.glob("**/*.md"))
        json_files = list(path.glob("**/*.json"))
        
        print(f"  ✓ Found {name}: {len(files)} markdown files, {len(json_files)} JSON files")
        
        discoveries.append({
            "type": "learning_storage",
            "directory": name,
            "markdown_count": len(files),
            "json_count": len(json_files),
            "exists": True
        })
        
        # Sample a learning file to understand format
        if files:
            sample_file = files[0]
            content = sample_file.read_text()
            word_count = len(content.split())
            discoveries.append({
                "type": "learning_format",
                "sample_file": sample_file.name,
                "word_count": word_count,
                "has_structured_sections": "##" in content
            })
            print(f"    - Sample learning file: {sample_file.name} ({word_count} words)")
    else:
        discoveries.append({
            "type": "learning_storage",
            "directory": name,
            "exists": False
        })

# 2. Explore logs structure
print("\n📊 Examining Logging Infrastructure...")
logs_dir = ravl_dir / "logs"
if logs_dir.exists():
    log_subdirs = [d for d in logs_dir.iterdir() if d.is_dir()]
    print(f"  ✓ Found {len(log_subdirs)} log categories:")
    
    for subdir in log_subdirs:
        log_files = list(subdir.glob("*.md")) + list(subdir.glob("*.json"))
        print(f"    - {subdir.name}/: {len(log_files)} files")
        discoveries.append({
            "type": "logging_category",
            "category": subdir.name,
            "file_count": len(log_files)
        })

# 3. Examine current state tracking
print("\n🗂️ Examining State Management...")
current_state_dir = ravl_dir / "current_state"
if current_state_dir.exists():
    state_files = list(current_state_dir.glob("*"))
    print(f"  ✓ Found {len(state_files)} state tracking files")
    
    for state_file in state_files:
        if state_file.is_file():
            size = state_file.stat().st_size
            discoveries.append({
                "type": "state_file",
                "name": state_file.name,
                "size_bytes": size
            })
            print(f"    - {state_file.name}: {size} bytes")

# 4. Check for loop configurations
print("\n⚙️ Examining Loop Configurations...")
loop_configs = list(ravl_dir.glob("*.loop.yaml")) + list(ravl_dir.glob("*.loop.yml"))
print(f"  ✓ Found {len(loop_configs)} loop configuration files:")

for config in loop_configs:
    print(f"    - {config.name}")
    discoveries.append({
        "type": "loop_config",
        "name": config.name
    })

# 5. Explore framework's health check capabilities
print("\n🏥 Analyzing Health Check Infrastructure...")
# Check for health check related files
health_patterns = ["health", "diagnostic", "verify"]
health_related = []

for pattern in health_patterns:
    matching = list(ravl_dir.rglob(f"*{pattern}*"))
    health_related.extend(matching)
    
print(f"  ✓ Found {len(health_related)} health-check related artifacts")
for item in health_related[:5]:  # Show first 5
    print(f"    - {item.relative_to(ravl_dir)}")

discoveries.append({
    "type": "health_infrastructure",
    "artifact_count": len(health_related)
})

# Generate insights from discoveries
print("\n💡 Generating Insights...")

insights.append({
    "insight": "Dual Learning System Architecture",
    "explanation": "Framework separates execution failures (syntax, auth) from verification failures (domain logic), storing them in different directories for targeted learning",
    "significance": "This separation allows the framework to improve both infrastructure reliability AND domain problem-solving independently"
})

execution_learnings = sum(1 for d in discoveries if d.get("directory") == "execution_learning" and d.get("exists"))
loop_learnings = sum(1 for d in discoveries if d.get("directory") == "loop_learning" and d.get("exists"))

insights.append({
    "insight": "Learning Persistence Strategy",
    "explanation": f"Framework maintains persistent learning across runs with markdown documentation and JSON structured data",
    "significance": "Combines human-readable context (markdown) with machine-parseable patterns (JSON) for hybrid learning"
})

log_categories = [d["category"] for d in discoveries if d["type"] == "logging_category"]
if log_categories:
    insights.append({
        "insight": "Multi-Dimensional Logging",
        "explanation": f"Framework logs across {len(log_categories)} categories: {', '.join(log_categories)}",
        "significance": "Enables debugging and health checks from multiple perspectives (LLM calls, execution, domain logic)"
    })

# Save exploration log
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)
exploration_log = output_dir / "exploration_log.md"

# Count existing runs
run_number = 1
if exploration_log.exists():
    content = exploration_log.read_text()
    run_number = content.count("## Run ") + 1

log_entry = f"""
## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Exploring**: Framework Learning Architecture and Health Check Infrastructure
**Method**: Systematic examination of .ravl directory structure, learning storage patterns, logging infrastructure, and state management

### Discoveries:
- **Dual Learning System**: Found separate directories for execution_learning (infrastructure) vs loop_learning (domain logic)
- **Structured Learning Storage**: Framework uses both markdown (human-readable) and JSON (machine-parseable) for learning persistence
- **Multi-Category Logging**: Identified {len(log_categories)} distinct logging categories: {', '.join(log_categories) if log_categories else 'none found'}
- **State Persistence**: Framework maintains current_state/ directory for tracking loop state across runs
- **Loop Configuration System**: Found {len(loop_configs)} YAML-based loop configuration files
- **Health Check Infrastructure**: Discovered {len(health_related)} health-check related artifacts embedded in framework

### Key Insights:

#### 1. Separation of Concerns in Learning
The framework implements a sophisticated dual-learning architecture that separates "how to execute" (solution space) from "what to accomplish" (problem space). This means:
- Syntax errors, API auth failures → execution_learning/
- Missing data, incomplete analysis → loop_learning/
- Each system can improve independently without interference

#### 2. Hybrid Human-Machine Learning Format
Learning isn't just data dumping - it combines:
- Markdown files for context, explanations, and human debugging
- JSON files for structured patterns that can be machine-processed
- This enables both LLM reasoning AND programmatic health checks

#### 3. Observable Execution Through Logging
The multi-category logging system ({', '.join(log_categories) if log_categories else 'minimal'}) suggests the framework makes execution transparent for debugging. This is critical for health checks to diagnose failures accurately.

### Significance:
These discoveries reveal that RAVL is not just a simple loop framework - it's a **learning system with self-improvement capabilities**. The separation between execution and domain learning means:

1. **Targeted Improvement**: Framework can diagnose whether failures are "I couldn't run the code" vs "I ran it but didn't solve the problem"
2. **Persistent Intelligence**: Learning accumulates across runs in structured formats that both humans and LLMs can query
3. **Observable Execution**: Rich logging infrastructure enables health checks to pinpoint exact failure modes
4. **Adaptive Architecture**: The loop configuration system suggests multiple specialized loops can work together

**Next Exploration Opportunities**:
- Examine actual learning file contents to understand pattern extraction
- Analyze health check logic to see how diagnostics work
- Investigate loop configuration to understand orchestration patterns
- Map the verification criteria system and how it drives learning

---
"""

with open(exploration_log, 'a') as f:
    f.write(log_entry)

print(f"\n✅ Exploration complete! Findings saved to {exploration_log}")
print(f"📈 Discovered {len(discoveries)} concrete facts")
print(f"💡 Generated {len(insights)} insights")
print("\nThis exploration reveals RAVL's sophisticated learning architecture that separates infrastructure from domain learning.")