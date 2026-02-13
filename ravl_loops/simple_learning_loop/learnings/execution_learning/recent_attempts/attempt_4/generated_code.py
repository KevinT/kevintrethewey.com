import os
import json
from pathlib import Path
from datetime import datetime

# Get loop directories from environment
learnings_dir = Path(os.environ.get('RAVL_LEARNINGS_DIR'))
output_dir = learnings_dir / 'output'
output_dir.mkdir(parents=True, exist_ok=True)

exploration_log = output_dir / 'exploration_log.md'

# Determine run number
current_state_dir = learnings_dir / 'current_state'
run_number = 1
if current_state_dir.exists():
    state_files = list(current_state_dir.glob('*.json'))
    run_number = len(state_files) + 1

print(f"Starting exploration run #{run_number}")
print("=" * 60)

# For this run, explore the execution learning patterns
print("\n🔍 Exploring: Execution learning patterns and framework health indicators")
print("Method: Analyzing execution_learning directory structure and content patterns\n")

execution_learning_dir = learnings_dir / 'execution_learning'
discoveries = []
significance_notes = []

# Discovery 1: Examine execution learning files
if execution_learning_dir.exists():
    exec_files = list(execution_learning_dir.glob('*.json'))
    print(f"✓ Found {len(exec_files)} execution learning files")
    
    if exec_files:
        # Analyze the most recent execution learning
        latest_file = max(exec_files, key=lambda p: p.stat().st_mtime)
        print(f"  Latest: {latest_file.name}")
        
        with open(latest_file, 'r') as f:
            exec_data = json.load(f)
            
        discoveries.append(f"Execution learning files track: {', '.join(exec_data.keys())}")
        
        if 'error_type' in exec_data:
            discoveries.append(f"Error tracking includes: {exec_data.get('error_type', 'unknown')}")
        
        if 'timestamp' in exec_data:
            discoveries.append(f"Execution failures are timestamped for trend analysis")
            
        # Check for patterns in error types
        error_types = []
        for ef in exec_files:
            with open(ef, 'r') as f:
                data = json.load(f)
                if 'error_type' in data:
                    error_types.append(data['error_type'])
        
        if error_types:
            unique_errors = set(error_types)
            discoveries.append(f"Error type diversity: {len(unique_errors)} unique types across {len(error_types)} failures")
            significance_notes.append("Multiple execution learning files suggest framework is actively learning from failures")
    else:
        discoveries.append("No execution failures recorded - suggesting code is executing successfully")
        significance_notes.append("Clean execution history indicates stable domain logic generation")
else:
    discoveries.append("Execution learning directory not yet created")

# Discovery 2: Examine current_state structure
print("\n🔍 Analyzing: Current state persistence patterns")
if current_state_dir.exists():
    state_files = list(current_state_dir.glob('*.json'))
    print(f"✓ Found {len(state_files)} state snapshots")
    
    if state_files:
        # Analyze state evolution
        state_sizes = [(f.name, f.stat().st_size) for f in state_files]
        discoveries.append(f"State files range from {min(s[1] for s in state_sizes)} to {max(s[1] for s in state_sizes)} bytes")
        
        # Check for state growth pattern
        if len(state_sizes) > 1:
            size_trend = [s[1] for s in sorted(state_sizes)]
            if size_trend[-1] > size_trend[0]:
                discoveries.append("State size is growing - loop is accumulating knowledge")
                significance_notes.append("Growing state suggests progressive discovery is working")
            else:
                discoveries.append("State size is stable - loop may have reached exploration plateau")

# Discovery 3: Examine log patterns
print("\n🔍 Analyzing: Logging patterns and debugging infrastructure")
logs_dir = learnings_dir / 'logs'
if logs_dir.exists():
    log_files = list(logs_dir.glob('*.log'))
    print(f"✓ Found {len(log_files)} log files")
    
    # Check for structured logging
    if log_files:
        discoveries.append(f"Framework maintains {len(log_files)} log files for debugging")
        
        # Sample a log file to understand structure
        sample_log = log_files[0]
        with open(sample_log, 'r') as f:
            lines = f.readlines()[:10]  # First 10 lines
        
        if any('[' in line and ']' in line for line in lines):
            discoveries.append("Logs use structured format with timestamps and levels")
        
        significance_notes.append("Comprehensive logging enables post-hoc analysis of loop behavior")

# Discovery 4: Check for output artifacts
print("\n🔍 Analyzing: Output artifact patterns")
output_files = list(output_dir.glob('*'))
print(f"✓ Found {len(output_files)} output artifacts")

if len(output_files) > 1:  # More than just exploration_log.md
    output_types = {}
    for of in output_files:
        ext = of.suffix or 'no_extension'
        output_types[ext] = output_types.get(ext, 0) + 1
    
    discoveries.append(f"Output format diversity: {dict(output_types)}")
    significance_notes.append("Multiple output formats suggest loop is producing varied deliverables")

# Discovery 5: Framework structure insights
print("\n🔍 Analyzing: Framework organization principles")
subdirs = [d for d in learnings_dir.iterdir() if d.is_dir()]
print(f"✓ Found {len(subdirs)} top-level learning directories")

discoveries.append(f"Framework organizes learnings into {len(subdirs)} categories: {', '.join(d.name for d in subdirs)}")
significance_notes.append("Separation of concerns: execution failures vs domain learnings vs outputs vs logs")

# Write exploration log
print(f"\n📝 Writing discoveries to exploration_log.md")

with open(exploration_log, 'a') as f:
    f.write(f"\n## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("**Exploring**: Framework learning infrastructure and organizational patterns\n")
    f.write("**Method**: Analyzing learnings directory structure, file patterns, and metadata\n\n")
    
    f.write("### Discoveries:\n")
    for discovery in discoveries:
        f.write(f"- {discovery}\n")
    
    f.write("\n### Significance:\n")
    if significance_notes:
        for note in significance_notes:
            f.write(f"- {note}\n")
    else:
        f.write("- Initial baseline exploration of framework structure established\n")
    
    f.write("\n### Meta-Insight:\n")
    f.write("The RAVL framework implements a clear separation of concerns:\n")
    f.write("- **execution_learning/**: Infrastructure failures (imports, auth, API errors)\n")
    f.write("- **loop_learning/**: Domain-specific learnings (verification failures, discoveries)\n")
    f.write("- **current_state/**: Persistent state across runs enabling progressive exploration\n")
    f.write("- **logs/**: Debugging infrastructure for post-hoc analysis\n")
    f.write("- **output/**: Deliverable artifacts and exploration documentation\n\n")
    f.write("This architecture enables the framework to distinguish between 'how to execute' problems\n")
    f.write("(solution space) and 'what to explore' problems (problem space), learning from each separately.\n")

print(f"✓ Exploration log updated successfully")
print("\n" + "=" * 60)
print(f"Run #{run_number} complete - {len(discoveries)} discoveries logged")