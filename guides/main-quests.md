# Main quests

Main quests keep a solo campaign from drifting. Claude always has the next one drafted before it starts.

Everything below (3 stages, who the quest is about, the twist) is the **default**. The player can change any of it in the pre-main-quest interview, for that quest or for good.

## The cycle

1. **Interview.** Before a main quest starts (the first one included), Claude asks spoiler-free questions.
2. **Draft.** Claude writes the whole quest in a hidden DM file, `.dm/main-quest-N.md`, from `templates/dm/main-quest-plan.md`. The player never reads it.
3. **Play** the 3 stages, one or more story threads per stage.
4. **Conclude.** When the quest's final stage resolves, Claude records a one-line, spoiler-free summary in `campaign.md`, folds the quest into the journal's Done list, and goes back to step 1.

## Who it's about

- **Main quest 1:** the main character (their past, their power, their enemy).
- **Main quest 2 onward:** one of the main character's companions or their familiar. The player picks who in the interview, or lets Claude choose.

## Shape

- **3 stages.** Each stage has a clear goal, a place, a main obstacle and an ending that opens the next stage.
- **At least one twist,** set up with clues in earlier stages so it feels fair in hindsight.
- Room for side quests and loose ends, but the journal always shows the main quest's next step.

## Interview questions (pick what fits, keep them spoiler-free)

1. Who should this quest be about? (later quests: which companion, or the familiar)
2. What tone: heroic, grim, mysterious, light-hearted, surprise me?
3. How long: a few sessions, or a long arc?
4. More or less of: combat, talking, exploring, puzzles, travel?
5. Any themes you'd love (family, betrayal, redemption, a rival) or want to avoid?
6. How dark can it get?
7. Big moments you'd like for anyone in the party?
8. Slow build or fast start? Big twist or small surprises?
9. Keep the defaults (3 stages, focus character), or change them for this quest?

## Thread names

`MainQuest.Post Name`, e.g. `3.2. Thal at Coldhearth` is main quest 3, second thread of that quest.

- Posts are numbered from 1 within each main quest: `1.1.`, `1.2.`, `1.3.` …
- The next post starts when a new stage begins, or when a thread gets long (about 20 player turns), always at a calm point.
- Claude opens each new thread itself: the story thread asks the project's coordinator to start it, with the name and a handoff of the current state. The player just keeps playing in the new thread.
- A new main quest starts again at `N.1.`, e.g. main quest 3 opens with `3.1.`.
