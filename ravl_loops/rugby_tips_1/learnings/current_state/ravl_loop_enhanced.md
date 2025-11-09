# Act

1. **Locate and access a comprehensive source of Springbok rugby game results**
   - Find a reliable source that includes match scores, scorers, and individual player performance data

2. **Extract game information and player performance data**
   - For each game, collect: date, opponent, final score, try scorers, penalty/drop goal scorers, and individual player ratings/performance notes
   - Track which players participated and notable performance metrics

3. **Load existing data from `./output/springboks-results.json`**
   - If file exists, parse the JSON to identify which games are already tracked
   - If file doesn't exist, initialize an empty data structure

4. **Identify new or missing games**
   - Compare sourced games against existing data in `./output/springboks-results.json`
   - Determine which games need to be added

5. **Update `./output/springboks-results.json` with new/missing game data**
   - Add newly found games to the JSON file
   - Preserve all existing game records
   - Ensure consistent JSON structure

6. **Determine the most recent game date**
   - From the updated JSON file, identify the date of the most recent Springbok game
   - Compare against the most recent game from any previous run (check for existence of previous coaching tips files)

7. **Generate coaching suggestions only if a new game is detected**
   - If the most recent game is newer than previously processed games:
     - Analyze the most recent game data and overall trends
     - Produce the top 3 coaching suggestions for Rassie based on recent performance, player form, and tactical patterns
     - Save suggestions in `./output/springbok-coach-tips-YYYY-MMM-DD.md` where YYYY-MMM-DD is the date of the most recent game
   - If no new game is detected, skip creating a new coaching tips file

# Verify

- [ ] `./output/springboks-results.json` exists and contains valid JSON
- [ ] All previously existing games in `springboks-results.json` are preserved unchanged
- [ ] Any new or missing Springbok games found from the source are added to `springboks-results.json`
- [ ] Each game record includes: date, opponent, score, scorers, and player performance data
- [ ] The most recent game date has been correctly identified
- [ ] If a new game was detected (more recent than any previous run):
  - [ ] A new file `./output/springbok-coach-tips-YYYY-MMM-DD.md` exists with the correct date
  - [ ] The coaching tips file contains exactly 3 coaching suggestions
  - [ ] The suggestions are based on the most recent game information
- [ ] If no new game was detected:
  - [ ] No new coaching tips file was created
  - [ ] The most recent existing coaching tips file (if any) remains unchanged