def edit_summary_menu() -> str:

    summaries = {
        "1": "Created Bulgarian noun",
        "2": "Created Bulgarian verb",
        "3": "Created Bulgarian adjective",
        "4": "Created entry with definition and pronunciation",
        "5": "Creadted Bulgarian adverb",
        "6": "Created Bulgarian proper noun",
    }

    result = None
    while result is None:
        typed = input("Please type in an edit summary: ")
        if typed in ("help", "хелп") or len(typed) < 10:
            print(f"Help:{' (please type in a longer summary to proceed)' if len(typed) < 10 else ''}")
            for key, value in summaries.items():
                print(f"[{key}]: {value}")
        else:
            # If something has been typed, assume that is the edit summary
            result = typed
        
        # Now, check whether if it is in fact a reference to a pre-written summary
        if typed in summaries:
            result = summaries[typed]
        
    return result