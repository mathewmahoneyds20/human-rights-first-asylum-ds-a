import plotly.graph_objects as go
from app.db_ops import get_df
import pandas as pd


def get_judge_vis(judge_id: int) -> go.Figure:
    df = get_df()
    judge_df = df[df["judge_id"] == judge_id]
    cross_tab = pd.crosstab(
        judge_df["protected_grounds"],
        judge_df["outcome"],
    )
    data = [
        go.Bar(name=col, x=cross_tab.index, y=cross_tab[col])
        for col in cross_tab.columns
    ]
    layout = go.Layout(
        title="Outcome by Protected Grounds",
        barmode="group",
    )
    return go.Figure(data, layout)


def get_judge_feature_vis(judge_id: int, feature: str, feature_2: str = "outcome") -> go.Figure:
    # Changes the variable names to be more readable without underscores
    feature_name = feature.title().replace('_', ' ')
    feature_name_2 = feature.title().replace('_', ' ')
    
    df = get_df()
    judge_df = df[df["judge_id"] == judge_id]
    cross_tab = pd.crosstab(
        judge_df[feature],
        judge_df[feature_2],
    )
    data = [
        go.Bar(name=col, x=cross_tab.index, y=cross_tab[col])
        for col in cross_tab.columns
    ]
    layout = go.Layout(
        title=f"{feature_name_2} by {feature_name}",
        barmode="group",
    )
    return go.Figure(data, layout)


def vis_national() -> go.Figure:
    """
    Home page visualization of outcomes for each type of protected grounds
    """
    df = get_df()
    cross_tab = pd.crosstab(
        df["protected_grounds"],
        df["outcome"],
    )
    data = [
        go.Bar(name=col, x=cross_tab.index, y=cross_tab[col])
        for col in cross_tab.columns
    ]
    layout = go.Layout(
        title="Outcome by Protected Grounds",
        barmode="group",
    )
    return go.Figure(data, layout)
