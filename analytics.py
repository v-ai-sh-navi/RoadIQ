import plotly.express as px


def ward_complaint_chart(df):

    fig = px.bar(
        df,
        x="Complaints",
        y="Ward_Name",
        orientation="h",
        color="Complaints",
        text="Complaints",
        title="Top 10 Wards by Complaint Count"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        template="plotly_white",
        xaxis_title="Number of Complaints",
        yaxis_title="Ward",
        height=500,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    fig.update_coloraxes(showscale=False)

    return fig

def complaint_status_chart(df):

    fig = px.pie(
        df,
        names="Status",
        values="Count",
        title="Complaint Status Distribution",
        hole=0.45
    )

    fig.update_layout(
        template="plotly_white"
    )
    fig.update_layout(
        height=500,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    fig.update_layout(
        legend=dict(
            orientation="h",
            y=-0.35,
            x=0.5,
            xanchor="center",
            yanchor="top"
    )
)

    return fig



def monthly_trend_chart(df):

    import plotly.express as px

    fig = px.line(
        df,
        x="Month",
        y="Complaints",
        markers=True,
        title="Monthly Complaint Trend"
    )

    fig.update_layout(
        template="plotly_white"
    )
    fig.update_layout(
        height=500,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig