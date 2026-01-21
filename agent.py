from prompts import STUDY_ANALYSIS_PROMPT

def analyze_study(sessions):
    logs = ""
    for s in sessions:
        logs += f"""
        Date: {s[0]}
        Subject: {s[1]}
        Topics: {s[2]}
        Time: {s[3]} minutes
        Completed: {s[4]}
        """

    prompt = STUDY_ANALYSIS_PROMPT.format(study_logs=logs)

    # TEMP: No API yet (safe testing)
    return "AI Analysis will appear here once API is connected."

