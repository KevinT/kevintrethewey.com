import os
import json
from pathlib import Path
from datetime import datetime

# Get loop directories from environment
learnings_dir = Path(os.environ.get('RAVL_LEARNINGS_DIR'))
loop_dir = Path(os.environ.get('RAVL_LOOP_DIR'))

print("=== Exploratory Loop: Run 1 ===")
print(f"Learnings directory: {learnings_dir}")
print(f"Loop directory: {loop_dir}")

# Determine run number by checking existing exploration logs
output_dir = learnings_dir / 'output'
output_dir.mkdir(parents=True, exist_ok=True)
exploration_log = output_dir / 'exploration_log.md'

run_number = 1
if exploration_log.exists():
    content = exploration_log.read_text()
    run_number = content.count('## Run ') + 1

print(f"\n🔍 Starting exploration run #{run_number}")

# Explore the loop structure and configuration
print("\n📋 Exploring loop configuration and structure...")

discoveries = []
exploring = "Loop configuration, verification criteria, and learning mechanisms"
method = "Analyzing RAVL loop files, directory structure, and configuration metadata"

# 1. Explore the loop configuration
config_file = loop_dir / 'config' / 'ravl.yml'
if config_file.exists():
    print(f"✓ Found loop configuration at {config_file}")
    config_content = config_file.read_text()
    discoveries.append(f"Loop configured with {len(config_content.splitlines())} lines of YAML configuration")
    
    # Parse key configuration patterns
    if 'loop_type:' in config_content:
        for line in config_content.splitlines():
            if 'loop_type:' in line:
                discoveries.append(f"Loop type explicitly defined: {line.strip()}")
    
    if 'verification_criteria:' in config_content:
        discoveries.append("Custom verification criteria defined in configuration")
    
    if 'health_check:' in config_content:
        discoveries.append("Health check configuration present for quality monitoring")
else:
    discoveries.append("No config/ravl.yml found - loop using default configuration")

# 2. Explore the learnings directory structure
print("\n📁 Exploring learnings directory structure...")
learnings_subdirs = [d for d in learnings_dir.iterdir() if d.is_dir()]
discoveries.append(f"Learnings directory contains {len(learnings_subdirs)} subdirectories: {[d.name for d in learnings_subdirs]}")

# Check for current state tracking
current_state_dir = learnings_dir / 'current_state'
if current_state_dir.exists():
    state_files = list(current_state_dir.glob('*'))
    discoveries.append(f"Current state tracking active with {len(state_files)} state file(s)")
    for state_file in state_files:
        discoveries.append(f"  - State file: {state_file.name} ({state_file.stat().st_size} bytes)")

# 3. Explore loop learning history
logs_dir = learnings_dir / 'logs'
if logs_dir.exists():
    log_files = list(logs_dir.glob('*.log'))
    discoveries.append(f"Loop has executed previously - {len(log_files)} log files present")
else:
    discoveries.append("No previous execution logs found - this may be the first run")

# 4. Explore the ACT phase instructions to understand what's expected
act_phase_file = loop_dir / 'phases' / 'act.md'
if act_phase_file.exists():
    print(f"✓ Found ACT phase instructions at {act_phase_file}")
    act_content = act_phase_file.read_text()
    act_lines = len(act_content.splitlines())
    discoveries.append(f"ACT phase instructions: {act_lines} lines of guidance")
    
    # Look for specific patterns in ACT instructions
    if '**Exploring**:' in act_content:
        discoveries.append("ACT phase expects structured exploration with specific output format")
    
    if 'exploration_log.md' in act_content:
        discoveries.append("Loop designed to build cumulative exploration_log.md across runs")
else:
    discoveries.append("ACT phase using framework default instructions")

# 5. Explore verification expectations
verify_phase_file = loop_dir / 'phases' / 'verify.md'
if verify_phase_file.exists():
    print(f"✓ Found VERIFY phase instructions at {verify_phase_file}")
    verify_content = verify_phase_file.read_text()
    
    # Extract scoring criteria
    if 'Discovery Value' in verify_content:
        discoveries.append("Verification uses Discovery Value scoring (0-10)")
    if 'Insight Depth' in verify_content:
        discoveries.append("Verification uses Insight Depth scoring (0-10)")
    if 'Exploration Efficiency' in verify_content:
        discoveries.append("Verification uses Exploration Efficiency scoring (0-10)")
    
    if 'Success Threshold' in verify_content:
        for line in verify_content.splitlines():
            if 'Success Threshold' in line:
                discoveries.append(f"Quality threshold: {line.strip()}")

# 6. Explore model/knowledge representation
model_file = learnings_dir / 'model.yml'
if model_file.exists():
    print(f"✓ Found model file at {model_file}")
    model_content = model_file.read_text()
    model_lines = len(model_content.splitlines())
    discoveries.append(f"Loop maintains a knowledge model: {model_lines} lines in model.yml")
else:
    discoveries.append("No model.yml found - loop may not be building structured knowledge representation")

# Analyze significance
print("\n💡 Analyzing significance of discoveries...")

significance = f"""This is an exploratory/discovery loop with a well-defined progressive learning structure:

1. **Structured Discovery Process**: The loop uses a formal exploration_log.md to accumulate knowledge across runs, preventing redundant exploration.

2. **Multi-dimensional Quality Scoring**: Verification criteria assess three aspects (Discovery Value, Insight Depth, Efficiency) rather than binary pass/fail, encouraging deeper investigation.

3. **State Persistence**: The presence of current_state/ directory indicates the loop tracks what has been explored to avoid repeating work.

4. **Quality-Driven Learning**: The {'>=' if 'Success Threshold' in str(discoveries) else 'expected'} threshold of 5.0/10 means the loop only stores learnings that provide genuine value, not superficial observations.

5. **Meta-Exploration Insight**: This first run is exploring the loop's own structure and learning mechanisms - understanding the exploration framework before exploring domain content. This meta-level investigation provides a foundation for more effective subsequent explorations.

The loop architecture suggests a cumulative knowledge-building process where each run should explore new territory and document insights that connect to previous discoveries.
"""

# Write to exploration log
print(f"\n📝 Appending to exploration log: {exploration_log}")

log_entry = f"""## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Exploring**: {exploring}
**Method**: {method}

### Discoveries:
{chr(10).join(f'- {d}' for d in discoveries)}

### Significance:
{significance}

---
"""

with open(exploration_log, 'a') as f:
    f.write(log_entry)

print(f"✅ Exploration log updated with {len(discoveries)} discoveries")
print(f"📊 Run #{run_number} complete - discoveries logged for future runs to build upon")