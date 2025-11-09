import json
import os
from pathlib import Path
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from common.llm.llm_providers import LLMProviderFactory

def load_existing_data():
    """Load existing Springbok game results from JSON file."""
    output_file = Path("./output/springboks-results.json")
    if output_file.exists():
        print("✓ Loading existing Springbok game data...")
        with open(output_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"  Found {len(data.get('games', []))} existing games")
            return data
    print("✓ No existing data found, starting fresh")
    return {"games": [], "last_updated": None, "most_recent_game_date": None}

def fetch_springbok_results():
    """Fetch Springbok rugby game results from ESPN Scrum."""
    print("\n✓ Fetching Springbok game results from ESPN Scrum...")
    
    games = []
    
    # Fetch recent results from ESPN Scrum
    url = "https://www.espn.com/rugby/team/fixtures-results/_/id/2359/south-africa"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all match rows
        matches = soup.find_all('tr', class_='Table__TR')
        
        print(f"  Found {len(matches)} match entries")
        
        for match in matches:
            try:
                # Extract date
                date_elem = match.find('td', class_='date__col')
                if not date_elem:
                    continue
                    
                date_text = date_elem.get_text(strip=True)
                
                # Extract opponent and result
                opponent_elem = match.find('td', class_='opponent__col')
                result_elem = match.find('td', class_='result__col')
                
                if not opponent_elem or not result_elem:
                    continue
                
                opponent_text = opponent_elem.get_text(strip=True)
                result_text = result_elem.get_text(strip=True)
                
                # Skip if no result yet (upcoming match)
                if result_text in ['', 'vs', '-']:
                    continue
                
                # Parse result (e.g., "W 27-13" or "L 10-29")
                result_parts = result_text.split()
                if len(result_parts) < 2:
                    continue
                    
                outcome = result_parts[0]  # W or L
                score_parts = result_parts[1].split('-')
                
                if len(score_parts) != 2:
                    continue
                
                # Determine Springbok score and opponent score
                if outcome == 'W':
                    springbok_score = int(score_parts[0])
                    opponent_score = int(score_parts[1])
                else:  # L
                    springbok_score = int(score_parts[0])
                    opponent_score = int(score_parts[1])
                
                game = {
                    "date": date_text,
                    "opponent": opponent_text.replace('vs ', '').replace('@ ', ''),
                    "springbok_score": springbok_score,
                    "opponent_score": opponent_score,
                    "result": outcome,
                    "venue": "Home" if 'vs' in opponent_text else "Away",
                    "try_scorers": [],
                    "conversion_scorers": [],
                    "penalty_scorers": [],
                    "drop_goal_scorers": [],
                    "player_performance": {}
                }
                
                games.append(game)
                
            except Exception as e:
                print(f"  Warning: Could not parse match: {e}")
                continue
        
        print(f"✓ Successfully parsed {len(games)} completed games")
        
    except Exception as e:
        print(f"  Warning: Could not fetch data from ESPN: {e}")
    
    return games

def merge_game_data(existing_data, new_games):
    """Merge new game data with existing data, avoiding duplicates."""
    print("\n✓ Merging new game data with existing data...")
    
    existing_games = existing_data.get("games", [])
    
    # Create a set of existing game identifiers (date + opponent)
    existing_identifiers = set()
    for game in existing_games:
        identifier = f"{game['date']}_{game['opponent']}"
        existing_identifiers.add(identifier)
    
    # Add new games that don't exist
    new_count = 0
    for game in new_games:
        identifier = f"{game['date']}_{game['opponent']}"
        if identifier not in existing_identifiers:
            existing_games.append(game)
            new_count += 1
            print(f"  + Added new game: {game['date']} vs {game['opponent']}")
    
    # Sort games by date (most recent first)
    # Convert date strings to sortable format
    def parse_date(date_str):
        try:
            # Try various date formats
            for fmt in ['%d %b %Y', '%d %B %Y', '%Y-%m-%d', '%d/%m/%Y']:
                try:
                    return datetime.strptime(date_str, fmt)
                except:
                    continue
            return datetime.min
        except:
            return datetime.min
    
    existing_games.sort(key=lambda x: parse_date(x['date']), reverse=True)
    
    print(f"✓ Merge complete: {new_count} new games added, {len(existing_games)} total games")
    
    return existing_games

def save_results(games, previous_most_recent_date):
    """Save game results to JSON file."""
    print("\n✓ Saving updated game data...")
    
    output_dir = Path("./output")
    output_dir.mkdir(exist_ok=True)
    
    # Determine most recent game date
    most_recent_date = None
    if games:
        most_recent_date = games[0]['date']  # Already sorted by date descending
    
    data = {
        "games": games,
        "last_updated": datetime.now().isoformat(),
        "most_recent_game_date": most_recent_date,
        "total_games": len(games)
    }
    
    output_file = output_dir / "springboks-results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved {len(games)} games to {output_file}")
    print(f"  Most recent game: {most_recent_date}")
    
    # Check if new game detected
    new_game_detected = False
    if previous_most_recent_date is None and most_recent_date is not None:
        new_game_detected = True
        print(f"✓ New game detected (first run)")
    elif previous_most_recent_date != most_recent_date:
        new_game_detected = True
        print(f"✓ New game detected: {most_recent_date} (previous: {previous_most_recent_date})")
    else:
        print(f"✓ No new game detected (most recent still: {most_recent_date})")
    
    return new_game_detected, most_recent_date

def generate_coaching_tips(games):
    """Generate coaching tips based on recent game performance."""
    print("\n✓ Analyzing game data to generate coaching tips...")
    
    if not games:
        print("  No games to analyze")
        return None
    
    # Analyze recent games (last 5 or all if fewer)
    recent_games = games[:min(5, len(games))]
    
    # Build analysis prompt
    analysis_data = []
    for game in recent_games:
        analysis_data.append(f"Date: {game['date']}")
        analysis_data.append(f"Opponent: {game['opponent']}")
        analysis_data.append(f"Result: {game['result']} {game['springbok_score']}-{game['opponent_score']}")
        analysis_data.append(f"Venue: {game['venue']}")
        analysis_data.append("")
    
    prompt = f"""You are a rugby analyst providing coaching insights for Rassie Erasmus, head coach of the South African Springboks.

Based on the following recent game results:

{chr(10).join(analysis_data)}

Provide EXACTLY 3 specific, actionable coaching suggestions for the Springboks. Each suggestion should:
1. Be based on observable patterns in the results (wins/losses, scoring, venues)
2. Be specific and actionable (not generic advice)
3. Be relevant to professional international rugby
4. Focus on tactical, strategic, or player development areas

Format your response as:

## Coaching Tip 1: [Title]
[2-3 sentences explaining the insight and actionable recommendation]

## Coaching Tip 2: [Title]
[2-3 sentences explaining the insight and actionable recommendation]

## Coaching Tip 3: [Title]
[2-3 sentences explaining the insight and actionable recommendation]

Be direct and professional. Focus on what the data shows and what can be improved."""

    # Use LLM provider
    try:
        provider = LLMProviderFactory.create_provider("anthropic")
        response = provider.complete(prompt, max_tokens=2048)
        print("✓ Generated coaching tips using LLM analysis")
        return response
    except Exception as e:
        print(f"  Warning: Could not generate tips with LLM: {e}")
        return None

def save_coaching_tips(tips_content):
    """Save coaching tips to markdown file with today's date."""
    print("\n✓ Saving coaching tips...")
    
    output_dir = Path("./output")
    output_dir.mkdir(exist_ok=True)
    
    # Format: springbok-coach-tips-YYYY-MMM-DD.md
    today = datetime.now()
    filename = f"springbok-coach-tips-{today.strftime('%Y-%b-%d').upper()}.md"
    output_file = output_dir / filename
    
    # Add header
    content = f"""# Springbok Coaching Tips
Generated: {today.strftime('%Y-%m-%d %H:%M:%S')}

{tips_content}
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Saved coaching tips to {output_file}")

def main():
    print("=" * 60)
    print("SPRINGBOK GAME RESULTS TRACKER")
    print("=" * 60)
    
    # Load existing data
    existing_data = load_existing_data()
    previous_most_recent_date = existing_data.get("most_recent_game_date")
    
    # Fetch new game results
    new_games = fetch_springbok_results()
    
    # Merge with existing data
    merged_games = merge_game_data(existing_data, new_games)
    
    # Save results and check for new games
    new_game_detected, current_most_recent_date = save_results(merged_games, previous_most_recent_date)
    
    # Generate coaching tips only if new game detected
    if new_game_detected:
        print("\n" + "=" * 60)
        print("NEW GAME DETECTED - GENERATING COACHING TIPS")
        print("=" * 60)
        
        tips = generate_coaching_tips(merged_games)
        if tips:
            save_coaching_tips(tips)
        else:
            print("  Could not generate coaching tips")
    else:
        print("\n" + "=" * 60)
        print("NO NEW GAME DETECTED - SKIPPING COACHING TIPS")
        print("=" * 60)
    
    print("\n✓ Process complete!")

if __name__ == "__main__":
    main()