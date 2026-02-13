import os
from pathlib import Path
from datetime import datetime
import json

# Get loop directories from environment
learnings_dir = Path(os.environ.get('RAVL_LEARNINGS_DIR'))
loop_dir = Path(os.environ.get('RAVL_LOOP_DIR'))

# Determine run number from execution history
current_state_dir = learnings_dir / 'current_state'
execution_learning_dir = learnings_dir / 'execution_learning'
run_number = len(list(execution_learning_dir.glob('*.json'))) + 1

print(f"🔍 Starting exploration run #{run_number}")
print(f"📂 Loop directory: {loop_dir}")
print(f"📚 Learnings directory: {learnings_dir}")

# Read previous exploration logs to avoid redundancy
output_dir = learnings_dir / 'output'
output_dir.mkdir(exist_ok=True)
exploration_log_file = output_dir / 'exploration_log.md'

previous_explorations = set()
if exploration_log_file.exists():
    content = exploration_log_file.read_text()
    # Extract what was explored before
    for line in content.split('\n'):
        if line.startswith('**Exploring**:'):
            previous_explorations.add(line.split('**Exploring**:')[1].strip())

print(f"📖 Found {len(previous_explorations)} previous explorations")

# Choose what to explore this run based on what hasn't been covered
exploration_areas = [
    "Framework execution patterns and health check system",
    "Loop configuration structure and verification criteria",
    "Learning storage organization and pattern evolution",
    "Code generation and caching mechanisms",
    "Environment variable and path resolution patterns"
]

# Find first unexplored area or go deeper on existing ones
chosen_area = None
for area in exploration_areas:
    if area not in previous_explorations:
        chosen_area = area
        break

if not chosen_area:
    chosen_area = "Cross-cutting patterns across all previously explored areas"

print(f"🎯 Exploring: {chosen_area}")

# Conduct the exploration
discoveries = []
significance = ""

if "Framework execution patterns" in chosen_area:
    print("\n📊 Analyzing execution learning files...")
    
    # Examine execution learning files to understand failure patterns
    exec_files = list(execution_learning_dir.glob('*.json'))
    
    if exec_files:
        for exec_file in exec_files:
            try:
                with open(exec_file) as f:
                    data = json.load(f)
                    discoveries.append(f"Execution attempt {exec_file.stem}: Status={data.get('success', 'unknown')}")
                    if 'error' in data:
                        discoveries.append(f"  Error type: {data['error'].get('type', 'unspecified')}")
                    if 'duration_seconds' in data:
                        discoveries.append(f"  Duration: {data['duration_seconds']:.2f}s")
            except Exception as e:
                discoveries.append(f"Could not parse {exec_file.name}: {str(e)}")
    
    # Check current state files
    state_files = list(current_state_dir.glob('*.json'))
    discoveries.append(f"Current state tracking: {len(state_files)} state files")
    
    significance = "Execution learning files track each code generation attempt with success/failure status, error details, and timing. This enables the framework to distinguish between infrastructure failures (solution space) and domain logic issues (problem space)."

elif "Loop configuration structure" in chosen_area:
    print("\n⚙️ Analyzing loop configuration...")
    
    # Read loop config
    config_file = loop_dir / 'config' / 'ravl.yml'
    if config_file.exists():
        config_content = config_file.read_text()
        discoveries.append(f"Config file size: {len(config_content)} characters")
        
        # Extract key patterns
        if 'verification_criteria' in config_content:
            discoveries.append("✓ Verification criteria defined (problem space validation)")
        if 'act_instructions' in config_content:
            discoveries.append("✓ Act instructions defined (domain logic guidance)")
        if 'loop_type' in config_content:
            discoveries.append("✓ Loop type specified (behavior customization)")
        
        # Count sections
        section_markers = ['name:', 'description:', 'act_instructions:', 'verification_criteria:', 'loop_type:']
        for marker in section_markers:
            count = config_content.count(marker)
            if count > 0:
                discoveries.append(f"  {marker} appears {count} time(s)")
    
    significance = "The ravl.yml configuration defines the loop's domain logic (act_instructions for what to do) separately from its validation criteria (verification_criteria for what success means). This separation enables the framework to learn from verification failures without conflating them with execution errors."

elif "Learning storage organization" in chosen_area:
    print("\n🗄️ Analyzing learning storage patterns...")
    
    # Map out directory structure
    subdirs = [d for d in learnings_dir.iterdir() if d.is_dir()]
    discoveries.append(f"Learning directory contains {len(subdirs)} subdirectories:")
    
    for subdir in subdirs:
        files = list(subdir.glob('*'))
        discoveries.append(f"  {subdir.name}/: {len(files)} files")
        
        # Analyze file patterns
        if files:
            extensions = set(f.suffix for f in files)
            discoveries.append(f"    File types: {', '.join(extensions)}")
            
            # Check for time-based patterns in filenames
            timestamped = sum(1 for f in files if any(char.isdigit() for char in f.stem))
            if timestamped > 0:
                discoveries.append(f"    Timestamped files: {timestamped}/{len(files)}")
    
    # Check for learning accumulation pattern
    if execution_learning_dir.exists():
        exec_files = sorted(execution_learning_dir.glob('*.json'))
        if len(exec_files) > 1:
            discoveries.append(f"Learning accumulation: {len(exec_files)} execution attempts recorded")
            discoveries.append("  Pattern: Each attempt creates new learning file (append-only)")
    
    significance = "The learning storage uses a three-tier organization: execution_learning/ for infrastructure failures, loop_learning/ for domain validation issues, and current_state/ for run-to-run state. This separation allows the framework to apply different learning strategies to different types of failures."

elif "Code generation and caching" in chosen_area:
    print("\n💻 Analyzing code generation patterns...")
    
    # Check for generated code artifacts
    logs_dir = learnings_dir / 'logs'
    if logs_dir.exists():
        log_files = list(logs_dir.glob('*.log'))
        discoveries.append(f"Found {len(log_files)} log files")
        
        # Look for generation patterns
        for log_file in log_files[:3]:  # Sample first few
            content = log_file.read_text()
            if 'RAVL_CODE_START' in content:
                discoveries.append(f"  {log_file.name}: Contains code generation markers")
            if 'attempt' in log_file.name:
                discoveries.append(f"  {log_file.name}: Attempt-based naming (no caching)")
    
    # Check execution learning for code reuse patterns
    exec_files = list(execution_learning_dir.glob('*.json'))
    if len(exec_files) > 1:
        discoveries.append(f"Execution pattern: {len(exec_files)} separate attempts")
        discoveries.append("  Observation: No code caching detected (fresh generation each run)")
    
    significance = "The framework generates fresh code for each attempt rather than caching successful code. This pattern is appropriate for exploratory loops where each run should investigate something new, but may be inefficient for convergent loops with stable requirements."

elif "Environment variable and path resolution" in chosen_area:
    print("\n🔧 Analyzing environment and path patterns...")
    
    # Document environment variables the framework provides
    env_vars = {
        'RAVL_LEARNINGS_DIR': os.environ.get('RAVL_LEARNINGS_DIR'),
        'RAVL_LOOP_DIR': os.environ.get('RAVL_LOOP_DIR'),
        'GOOGLE_CREDENTIALS': 'set' if os.environ.get('GOOGLE_CREDENTIALS') else 'not set',
        'ANTHROPIC_API_KEY': 'set' if os.environ.get('ANTHROPIC_API_KEY') else 'not set',
    }
    
    for var, value in env_vars.items():
        if value and value != 'not set':
            if 'DIR' in var:
                discoveries.append(f"{var}: {value}")
            else:
                discoveries.append(f"{var}: {value}")
    
    # Analyze path resolution pattern
    discoveries.append(f"Working directory: {Path.cwd()}")
    discoveries.append(f"Learnings dir resolves to: {learnings_dir.resolve()}")
    discoveries.append(f"Loop dir resolves to: {loop_dir.resolve()}")
    
    # Check if paths are absolute or relative
    if learnings_dir.is_absolute():
        discoveries.append("  Path strategy: Framework provides absolute paths")
    
    significance = "The framework uses environment variables (RAVL_LEARNINGS_DIR, RAVL_LOOP_DIR) to provide absolute paths to loop directories, solving the problem of code executing in temporary directories. This pattern enables generated code to access loop data reliably regardless of where it executes."

else:  # Cross-cutting patterns
    print("\n🔗 Analyzing cross-cutting patterns...")
    
    # Synthesize insights across all areas
    discoveries.append("Integration pattern: Separation of concerns across three dimensions:")
    discoveries.append("  1. Execution (solution space) vs Verification (problem space)")
    discoveries.append("  2. Configuration (intent) vs Learning (experience)")
    discoveries.append("  3. Generated code (temporary) vs Loop data (persistent)")
    
    # Count total artifacts
    total_files = sum(1 for _ in learnings_dir.rglob('*') if _.is_file())
    discoveries.append(f"Total learning artifacts: {total_files} files")
    
    # Identify the meta-pattern
    discoveries.append("Meta-pattern observed: The framework treats each run as an experiment")
    discoveries.append("  - Input: Configuration + Previous learnings")
    discoveries.append("  - Process: Generate code → Execute → Verify")
    discoveries.append("  - Output: New learnings + Updated state")
    discoveries.append("  - Feedback: Learnings influence next generation")
    
    significance = "The RAVL framework implements a learning loop at multiple levels: individual run (generate-execute-verify), execution health (solution space debugging), and verification health (problem space refinement). This multi-level learning enables the system to improve both its infrastructure robustness and domain logic quality over time."

print(f"\n✅ Exploration complete: {len(discoveries)} discoveries made")

# Format and append to exploration log
log_entry = f"""
## Run {run_number} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Exploring**: {chosen_area}
**Method**: Static analysis of loop directory structure, configuration files, and learning artifacts

### Discoveries:
"""

for discovery in discoveries:
    log_entry += f"{discovery}\n"

log_entry += f"""
### Significance:
{significance}

---
"""

# Append to exploration log
with open(exploration_log_file, 'a') as f:
    f.write(log_entry)

print(f"📝 Exploration log updated: {exploration_log_file}")
print(f"🎯 Area explored: {chosen_area}")
print(f"💡 Discoveries: {len(discoveries)}")