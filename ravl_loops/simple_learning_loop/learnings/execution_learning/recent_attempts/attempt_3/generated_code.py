import os
import json
from pathlib import Path
from datetime import datetime

# Get loop directories from environment
learnings_dir = Path(os.environ.get('RAVL_LEARNINGS_DIR'))
loop_dir = Path(os.environ.get('RAVL_LOOP_DIR'))

print("🔍 Starting exploration run...")

# Determine run number by checking existing exploration log
exploration_log = learnings_dir / 'output' / 'exploration_log.md'
run_number = 1
if exploration_log.exists():
    content = exploration_log.read_text()
    run_number = content.count('## Run ') + 1

print(f"📋 This is exploration run #{run_number}")

# Read previous exploration context if available
current_state_file = learnings_dir / 'current_state' / 'last_exploration.json'
previous_context = {}
if current_state_file.exists():
    try:
        previous_context = json.loads(current_state_file.read_text())
        print(f"✓ Loaded context from previous run")
    except:
        print("⚠ Could not load previous context, starting fresh")

# Exploration strategy: Progressive discovery of loop structure and configuration
print("\n🎯 Exploration Focus: Understanding Loop Configuration and Learnings Structure")

discoveries = []
exploration_method = "Systematic analysis of loop directory structure and configuration files"

# Discovery 1: Analyze the loop configuration
print("\n📁 Examining loop configuration...")
config_file = loop_dir / 'config' / 'ravl.yml'
if config_file.exists():
    config_content = config_file.read_text()
    discoveries.append(f"Loop config file found at: {config_file.relative_to(loop_dir.parent)}")
    
    # Parse key configuration elements
    lines = config_content.split('\n')
    config_insights = []
    for line in lines[:20]:  # First 20 lines for key config
        if line.strip() and not line.strip().startswith('#'):
            config_insights.append(line.strip())
    
    discoveries.append(f"Configuration structure has {len(lines)} lines")
    discoveries.append(f"Key config elements: {config_insights[:5]}")
    print(f"  ✓ Found configuration with {len(lines)} lines")
else:
    discoveries.append("No config/ravl.yml found - loop may use default configuration")
    print("  ⚠ No explicit config found")

# Discovery 2: Analyze learnings directory structure
print("\n📊 Mapping learnings directory structure...")
learnings_structure = {}
for item in learnings_dir.iterdir():
    if item.is_dir():
        file_count = len(list(item.glob('*')))
        learnings_structure[item.name] = file_count
        print(f"  - {item.name}/: {file_count} files")

discoveries.append(f"Learnings directory has {len(learnings_structure)} subdirectories: {list(learnings_structure.keys())}")
discoveries.append(f"Total files across learnings: {sum(learnings_structure.values())}")

# Discovery 3: Analyze execution learning patterns
print("\n🔧 Examining execution learnings...")
exec_learning_dir = learnings_dir / 'execution_learning'
if exec_learning_dir.exists():
    exec_files = list(exec_learning_dir.glob('*.md'))
    if exec_files:
        discoveries.append(f"Found {len(exec_files)} execution learning files")
        # Read most recent execution learning
        most_recent = max(exec_files, key=lambda f: f.stat().st_mtime)
        exec_content = most_recent.read_text()
        discoveries.append(f"Most recent execution learning: {most_recent.name} ({len(exec_content)} chars)")
        print(f"  ✓ Analyzed {len(exec_files)} execution learning files")
    else:
        discoveries.append("No execution learning files yet - loop has been successful so far")
        print("  ✓ No execution failures recorded")

# Discovery 4: Analyze current state tracking
print("\n💾 Examining state management...")
current_state_dir = learnings_dir / 'current_state'
if current_state_dir.exists():
    state_files = list(current_state_dir.glob('*'))
    discoveries.append(f"Current state tracking: {len(state_files)} files")
    for sf in state_files:
        size = sf.stat().st_size
        discoveries.append(f"  - {sf.name}: {size} bytes")
        print(f"  - {sf.name}: {size} bytes")

# Discovery 5: Analyze output artifacts
print("\n📤 Examining output artifacts...")
output_dir = learnings_dir / 'output'
if output_dir.exists():
    output_files = list(output_dir.glob('*'))
    discoveries.append(f"Output directory contains {len(output_files)} files")
    for of in output_files:
        size = of.stat().st_size
        discoveries.append(f"  - {of.name}: {size} bytes")
        print(f"  - {of.name}: {size} bytes")

# Discovery 6: Cross-reference with loop directory
print("\n🔗 Cross-referencing loop directory structure...")
loop_contents = []
for item in loop_dir.iterdir():
    if item.is_dir():
        loop_contents.append(f"{item.name}/ (directory)")
    else:
        loop_contents.append(f"{item.name} (file)")

discoveries.append(f"Loop directory structure: {len(loop_contents)} top-level items")
discoveries.append(f"Loop contents: {loop_contents}")
print(f"  ✓ Found {len(loop_contents)} items in loop directory")

# Synthesis: What patterns emerge?
print("\n🧠 Synthesizing discoveries...")
significance = f"""
This exploration reveals the loop's operational structure:

1. **Configuration Pattern**: The loop {'has explicit configuration' if config_file.exists() else 'uses default configuration'}
   
2. **Learning Evolution**: With {sum(learnings_structure.values())} total learning files across {len(learnings_structure)} categories, 
   the loop is building a knowledge base progressively.

3. **Execution Health**: {'No execution failures recorded - loop is operating cleanly' if not list(exec_learning_dir.glob('*.md')) else f'{len(list(exec_learning_dir.glob("*.md")))} execution learnings indicate areas where the loop has adapted'}

4. **State Management**: The loop maintains {len(list(current_state_dir.glob('*')))} state tracking files, 
   suggesting {'minimal' if len(list(current_state_dir.glob('*'))) < 3 else 'comprehensive'} state persistence.

5. **Output Patterns**: {'Output directory is actively used' if len(list(output_dir.glob('*'))) > 0 else 'Output directory is being initialized'}

Key Insight: This is run #{run_number} of a discovery loop that progressively maps its own operational environment.
Each run adds depth to understanding how the RAVL framework structures learning and state management.
"""

print("\n✓ Exploration complete!")

# Save discoveries to exploration log
log_entry = f"""
## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Exploring**: {exploration_method}

### Discoveries:
{chr(10).join(f'- {d}' for d in discoveries)}

### Significance:
{significance}

---
"""

exploration_log.parent.mkdir(parents=True, exist_ok=True)
with open(exploration_log, 'a') as f:
    f.write(log_entry)

print(f"\n💾 Saved exploration log to: {exploration_log.relative_to(learnings_dir.parent)}")

# Update current state for next run
new_state = {
    'run_number': run_number,
    'timestamp': datetime.now().isoformat(),
    'discoveries_count': len(discoveries),
    'learnings_structure': learnings_structure,
    'explored_areas': [
        'loop_configuration',
        'learnings_directory_structure', 
        'execution_learning_patterns',
        'state_management',
        'output_artifacts',
        'loop_directory_structure'
    ]
}

current_state_file.parent.mkdir(parents=True, exist_ok=True)
current_state_file.write_text(json.dumps(new_state, indent=2))

print(f"✓ Updated state for next run")
print(f"\n🎉 Exploration #{run_number} complete with {len(discoveries)} discoveries")