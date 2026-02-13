import os
import json
from pathlib import Path
from datetime import datetime

# Get loop directories from environment
learnings_dir = Path(os.environ.get('RAVL_LEARNINGS_DIR'))
loop_dir = Path(os.environ.get('RAVL_LOOP_DIR'))

print("🔍 Starting exploratory loop - Run 1")
print("=" * 60)

# Determine what to explore on this run
exploration_log_path = learnings_dir / 'output' / 'exploration_log.md'
run_number = 1

# For first run, explore the loop configuration and structure
print("\n📋 Exploring: Loop configuration and directory structure")
print("Method: Analyzing RAVL configuration files and environment setup\n")

discoveries = []
insights = []

# Discovery 1: Loop directory structure
print("🔎 Analyzing loop directory structure...")
if loop_dir.exists():
    loop_contents = list(loop_dir.rglob('*'))
    config_files = [f for f in loop_contents if f.is_file() and f.suffix in ['.yml', '.yaml', '.json']]
    python_files = [f for f in loop_contents if f.is_file() and f.suffix == '.py']
    
    discoveries.append(f"Loop directory contains {len(config_files)} configuration files")
    discoveries.append(f"Loop directory contains {len(python_files)} Python files")
    
    print(f"  ✓ Found {len(config_files)} config files")
    print(f"  ✓ Found {len(python_files)} Python files")

# Discovery 2: RAVL configuration content
print("\n🔎 Analyzing RAVL configuration...")
config_file = loop_dir / 'config' / 'ravl.yml'
if config_file.exists():
    with open(config_file, 'r') as f:
        config_content = f.read()
    
    # Extract key configuration elements
    config_lines = config_content.split('\n')
    loop_type = None
    verification_criteria = []
    
    for line in config_lines:
        if 'loop_type:' in line.lower() or 'type:' in line.lower():
            loop_type = line.strip()
        if 'verification' in line.lower() or 'criteria' in line.lower():
            verification_criteria.append(line.strip())
    
    if loop_type:
        discoveries.append(f"Loop type configuration: {loop_type}")
        print(f"  ✓ Loop type: {loop_type}")
    
    discoveries.append(f"Configuration file is {len(config_content)} characters long")
    discoveries.append(f"Configuration has {len(config_lines)} lines")
    print(f"  ✓ Config size: {len(config_lines)} lines")

# Discovery 3: Learning directory structure
print("\n🔎 Analyzing learning directory structure...")
if learnings_dir.exists():
    subdirs = [d.name for d in learnings_dir.iterdir() if d.is_dir()]
    discoveries.append(f"Learning directory has subdirectories: {', '.join(subdirs)}")
    print(f"  ✓ Learning subdirs: {', '.join(subdirs)}")
    
    # Check what's in current_state
    current_state_dir = learnings_dir / 'current_state'
    if current_state_dir.exists():
        state_files = list(current_state_dir.glob('*'))
        discoveries.append(f"Current state contains {len(state_files)} files")
        print(f"  ✓ Current state: {len(state_files)} files")
        
        # Analyze state file types
        file_types = {}
        for f in state_files:
            ext = f.suffix or 'no_extension'
            file_types[ext] = file_types.get(ext, 0) + 1
        
        if file_types:
            discoveries.append(f"State file types: {dict(file_types)}")
            print(f"  ✓ File types: {dict(file_types)}")

# Discovery 4: Environment configuration
print("\n🔎 Analyzing environment configuration...")
env_vars = {
    'RAVL_LEARNINGS_DIR': os.environ.get('RAVL_LEARNINGS_DIR'),
    'RAVL_LOOP_DIR': os.environ.get('RAVL_LOOP_DIR'),
    'ANTHROPIC_API_KEY': 'SET' if os.environ.get('ANTHROPIC_API_KEY') else 'NOT SET',
    'GOOGLE_CREDENTIALS': 'SET' if os.environ.get('GOOGLE_CREDENTIALS') else 'NOT SET',
}

discoveries.append(f"Framework environment variables configured: {len([v for v in env_vars.values() if v and v != 'NOT SET'])} of {len(env_vars)}")
print(f"  ✓ Environment vars: {len([v for v in env_vars.values() if v and v != 'NOT SET'])}/{len(env_vars)} configured")

# Insight generation
print("\n💡 Generating insights from discoveries...")

insights.append("This is an exploratory/discovery loop designed for progressive learning across runs")
insights.append("The framework provides isolated execution via environment variables for directory access")

if loop_type and 'exploratory' in loop_type.lower():
    insights.append("Loop configuration confirms exploratory nature - each run should explore new territory")

if subdirs:
    insights.append(f"Learning persistence structure includes: {len(subdirs)} organizational directories for different types of learnings")

insights.append("Framework abstracts execution environment from loop logic - code runs in temp dir but accesses loop data via env vars")

print(f"  ✓ Generated {len(insights)} insights")

# Prepare exploration log entry
print("\n📝 Writing exploration log...")
log_entry = f"""## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Exploring**: Loop configuration and directory structure
**Method**: Analyzing RAVL configuration files, directory layout, and environment setup

### Discoveries:
{chr(10).join(f'- {d}' for d in discoveries)}

### Insights:
{chr(10).join(f'- {i}' for i in insights)}

### Significance:
This initial exploration establishes the foundational understanding of the loop's structure and configuration. 
The discoveries reveal that this is an exploratory loop with proper framework abstractions in place (environment-based 
directory access, separated learning directories). Understanding this architecture is crucial for subsequent runs to 
explore more specific domain aspects. The presence of {len(subdirs)} learning subdirectories shows the framework's 
organization for different types of accumulated knowledge.

Key takeaway: The loop is properly configured for progressive discovery with clear separation between execution 
environment (temporary) and persistent state (learnings directory). Future runs should focus on exploring domain-specific 
aspects rather than infrastructure.

---

"""

# Ensure output directory exists
output_dir = learnings_dir / 'output'
output_dir.mkdir(parents=True, exist_ok=True)

# Append to exploration log
with open(exploration_log_path, 'a') as f:
    f.write(log_entry)

print(f"  ✓ Exploration log updated: {exploration_log_path}")

print("\n" + "=" * 60)
print(f"✅ Exploration complete!")
print(f"   Discoveries: {len(discoveries)}")
print(f"   Insights: {len(insights)}")
print(f"   Log entry saved to: exploration_log.md")
print("=" * 60)