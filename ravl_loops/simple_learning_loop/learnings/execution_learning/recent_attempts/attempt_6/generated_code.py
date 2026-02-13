import os
import json
from pathlib import Path
from datetime import datetime

# Get loop directories from environment
learnings_dir = Path(os.environ.get('RAVL_LEARNINGS_DIR'))
loop_dir = Path(os.environ.get('RAVL_LOOP_DIR'))

print("=== Exploration Run Starting ===")
print(f"Learnings directory: {learnings_dir}")
print(f"Loop directory: {loop_dir}")

# Determine run number from existing exploration log
exploration_log = learnings_dir / 'output' / 'exploration_log.md'
run_number = 1
if exploration_log.exists():
    content = exploration_log.read_text()
    run_number = content.count('## Run ') + 1

print(f"\n🔍 This is exploration run #{run_number}")

# Area to explore: Execution learning patterns - what have we learned from execution failures?
exploring = "Execution learning directory patterns and failure insights"
method = "Analyzing execution_learning directory structure, file contents, and failure patterns"

print(f"\n📍 Exploring: {exploring}")
print(f"🔬 Method: {method}")

discoveries = []
exec_learning_dir = learnings_dir / 'execution_learning'

# Discovery 1: What types of execution learnings exist?
if exec_learning_dir.exists():
    learning_files = list(exec_learning_dir.glob('*.md'))
    print(f"\n📊 Found {len(learning_files)} execution learning files")
    
    if learning_files:
        discoveries.append(f"Execution learning directory contains {len(learning_files)} markdown files documenting past execution issues")
        
        # Discovery 2: Analyze the content patterns
        failure_types = {}
        for learning_file in learning_files:
            print(f"  📄 Analyzing: {learning_file.name}")
            content = learning_file.read_text()
            
            # Extract key patterns
            if 'import' in content.lower() or 'module' in content.lower():
                failure_types['import_errors'] = failure_types.get('import_errors', 0) + 1
            if 'credential' in content.lower() or 'auth' in content.lower():
                failure_types['auth_errors'] = failure_types.get('auth_errors', 0) + 1
            if 'timeout' in content.lower():
                failure_types['timeout_errors'] = failure_types.get('timeout_errors', 0) + 1
            if 'syntax' in content.lower():
                failure_types['syntax_errors'] = failure_types.get('syntax_errors', 0) + 1
            if 'exception' in content.lower() or 'error' in content.lower():
                failure_types['runtime_errors'] = failure_types.get('runtime_errors', 0) + 1
        
        discoveries.append(f"Failure type distribution: {json.dumps(failure_types, indent=2)}")
        print(f"\n📈 Failure type analysis:")
        for ftype, count in failure_types.items():
            print(f"    {ftype}: {count} occurrences")
        
        # Discovery 3: Most recent learning insights
        latest_file = max(learning_files, key=lambda f: f.stat().st_mtime)
        print(f"\n📌 Most recent learning: {latest_file.name}")
        latest_content = latest_file.read_text()
        
        # Extract the diagnosis section
        if '## Diagnosis' in latest_content:
            diagnosis_start = latest_content.index('## Diagnosis')
            diagnosis_section = latest_content[diagnosis_start:diagnosis_start+500]
            first_line = diagnosis_section.split('\n')[1] if '\n' in diagnosis_section else "No diagnosis found"
            discoveries.append(f"Latest execution issue diagnosed as: {first_line.strip()}")
            print(f"    Diagnosis: {first_line.strip()}")
else:
    discoveries.append("No execution_learning directory found - this loop has not encountered execution failures yet")
    print("\n✨ No execution failures yet - clean execution history")

# Discovery 4: Compare with current_state to understand loop progression
current_state_dir = learnings_dir / 'current_state'
if current_state_dir.exists():
    state_files = list(current_state_dir.glob('*'))
    print(f"\n📂 Current state directory has {len(state_files)} files")
    discoveries.append(f"Current state tracking: {len(state_files)} state files maintained")
    
    for state_file in state_files[:3]:  # Sample first 3
        print(f"    State file: {state_file.name} ({state_file.stat().st_size} bytes)")

# Discovery 5: Output directory analysis
output_dir = learnings_dir / 'output'
if output_dir.exists():
    output_files = list(output_dir.glob('*'))
    print(f"\n📤 Output directory has {len(output_files)} files")
    
    if output_files:
        total_size = sum(f.stat().st_size for f in output_files if f.is_file())
        discoveries.append(f"Output artifacts: {len(output_files)} files, total {total_size} bytes")
        print(f"    Total output size: {total_size} bytes")

# Significance analysis
significance = []

if len(discoveries) > 0 and 'execution_learning' in str(discoveries[0]):
    significance.append("This loop has experienced and learned from execution failures, building resilience through the execution_learning mechanism")

if failure_types:
    most_common = max(failure_types.items(), key=lambda x: x[1])
    significance.append(f"Most common failure pattern is '{most_common[0]}' - framework should prioritize preventing this category")

significance.append("The separation of execution_learning (infrastructure) from loop_learning (domain) enables targeted improvement in both problem and solution spaces")

print("\n🎯 Significance Analysis:")
for sig in significance:
    print(f"  • {sig}")

# Format the exploration log entry
log_entry = f"""
## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Exploring**: {exploring}
**Method**: {method}

### Discoveries:
"""

for discovery in discoveries:
    log_entry += f"- {discovery}\n"

log_entry += "\n### Significance:\n"
for sig in significance:
    log_entry += f"{sig}\n\n"

log_entry += "---\n"

# Append to exploration log
output_dir.mkdir(parents=True, exist_ok=True)
with open(exploration_log, 'a') as f:
    f.write(log_entry)

print(f"\n✅ Exploration log updated: {exploration_log}")
print(f"📝 Added {len(discoveries)} discoveries and {len(significance)} significance insights")
print("\n=== Exploration Complete ===")