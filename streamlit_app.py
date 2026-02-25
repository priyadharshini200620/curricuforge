def generate_curriculum(grade, subject, duration, approach):

    # Extract number of weeks from duration
    try:
        weeks = int(duration.split()[0])
    except:
        weeks = 4  # default fallback

    weekly_plan = ""

    for i in range(1, weeks + 1):

        if approach == "Project-Based":
            if i == 1:
                topic = f"Introduction to core concepts of {subject}"
            elif i < weeks:
                topic = f"Hands-on project development and applied learning in {subject}"
            else:
                topic = f"Final project completion and presentation"
        
        elif approach == "Lecture-Based":
            if i == 1:
                topic = f"Fundamental theories of {subject}"
            elif i < weeks:
                topic = f"Advanced concepts and structured exercises in {subject}"
            else:
                topic = f"Comprehensive review and final assessment"
        
        else:  # Hybrid
            if i == 1:
                topic = f"Concept introduction and discussion in {subject}"
            elif i < weeks:
                topic = f"Blended learning: theory + practical exercises"
            else:
                topic = f"Capstone refinement and evaluation"

        weekly_plan += f"\n## Week {i}\n{topic}\n"

    return f"""
# Course Overview
This {duration} {subject} course is designed for {grade} students using a {approach} approach.

The course balances conceptual understanding with applied skills.

# Learning Objectives
- Develop foundational understanding of {subject}
- Apply knowledge through structured activities
- Strengthen analytical thinking
- Complete a capstone aligned with learning outcomes

# Weekly Breakdown
{weekly_plan}

# Assessment Strategy
- Continuous evaluation
- Weekly tasks
- Mid-term review (if applicable)
- Final assessment
- Capstone project

# Capstone Project
Students will design and present a practical project demonstrating mastery of {subject}.
"""
