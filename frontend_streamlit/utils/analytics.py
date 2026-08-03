"""
=========================================================
AI Road Damage Detection System
Analytics Utility
Developer : Warda Ahad
=========================================================
"""

from collections import Counter
import pandas as pd


# ==========================================================
# Total Damages
# ==========================================================

def total_damages(result):
    """
    Return total detected damages.
    """

    if not result:
        return 0

    return result["result"]["total_damages"]


# ==========================================================
# Detection Count
# ==========================================================

def total_detections(result):
    """
    Return number of detections.
    """

    if not result:
        return 0

    return len(result["result"]["detections"])


# ==========================================================
# Damage Distribution
# ==========================================================

def damage_distribution(result):
    """
    Count every damage class.
    """

    if not result:
        return {}

    detections = result["result"]["detections"]

    classes = [
        item["class"]
        for item in detections
    ]

    return dict(Counter(classes))


# ==========================================================
# Confidence List
# ==========================================================

def confidence_scores(result):
    """
    Return confidence scores.
    """

    if not result:
        return []

    return [

        round(
            item["confidence"] * 100,
            2
        )

        for item in result["result"]["detections"]

    ]


# ==========================================================
# Detection DataFrame
# ==========================================================

def detection_dataframe(result):
    """
    Convert detections to DataFrame.
    """

    if not result:
        return pd.DataFrame()

    detections = result["result"]["detections"]

    data = []

    for item in detections:

        data.append({

            "Class": item["class"],

            "Confidence":
            round(item["confidence"] * 100, 2),

            "Bounding Box":
            str(item["bbox"])

        })

    return pd.DataFrame(data)
# ==========================================================
# Average Confidence
# ==========================================================

def average_confidence(result):
    """
    Return average confidence score.
    """

    scores = confidence_scores(result)

    if len(scores) == 0:
        return 0

    return round(sum(scores) / len(scores), 2)


# ==========================================================
# Highest Confidence
# ==========================================================

def highest_confidence(result):
    """
    Return highest confidence score.
    """

    scores = confidence_scores(result)

    if len(scores) == 0:
        return 0

    return max(scores)


# ==========================================================
# Lowest Confidence
# ==========================================================

def lowest_confidence(result):
    """
    Return lowest confidence score.
    """

    scores = confidence_scores(result)

    if len(scores) == 0:
        return 0

    return min(scores)


# ==========================================================
# Most Frequent Damage
# ==========================================================

def most_frequent_damage(result):
    """
    Return the most common damage class.
    """

    distribution = damage_distribution(result)

    if len(distribution) == 0:
        return "No Damage"

    return max(
        distribution,
        key=distribution.get
    )


# ==========================================================
# Dashboard Summary
# ==========================================================

def dashboard_summary(result):
    """
    Return dashboard statistics.
    """

    return {

        "Total Damages":
            total_damages(result),

        "Detections":
            total_detections(result),

        "Average Confidence":
            average_confidence(result),

        "Highest Confidence":
            highest_confidence(result),

        "Lowest Confidence":
            lowest_confidence(result),

        "Most Frequent":
            most_frequent_damage(result)

    }


# ==========================================================
# Detection Report
# ==========================================================

def detection_report(result):
    """
    Return complete report dictionary.
    """

    return {

        "Filename":
            result.get("filename", ""),

        "Total Damages":
            total_damages(result),

        "Average Confidence":
            average_confidence(result),

        "Highest Confidence":
            highest_confidence(result),

        "Lowest Confidence":
            lowest_confidence(result),

        "Damage Distribution":
            damage_distribution(result)

    }


# ==========================================================
# Class Frequency DataFrame
# ==========================================================

def class_frequency_dataframe(result):
    """
    Convert class frequency into DataFrame.
    """

    distribution = damage_distribution(result)

    if len(distribution) == 0:

        return pd.DataFrame()

    return pd.DataFrame({

        "Damage Class": distribution.keys(),

        "Count": distribution.values()

    })


# ==========================================================
# Export Summary
# ==========================================================

def export_summary(result):
    """
    Export dashboard summary as DataFrame.
    """

    summary = dashboard_summary(result)

    return pd.DataFrame(

        list(summary.items()),

        columns=[
            "Metric",
            "Value"
        ]

    )
