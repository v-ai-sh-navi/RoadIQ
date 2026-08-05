import geopandas as gpd
import folium


def create_map():

    # -------------------------
    # Load Data
    # -------------------------
    roads = gpd.read_file("data/Bengaluru/roads.kml")
    potholes = gpd.read_file("data/Bengaluru/potholes.kml")
    print(potholes["Status"].unique())

    # -------------------------
    # Reduce data for performance
    # -------------------------
    roads = roads.sample(2500, random_state=42)
    potholes = potholes.head(500)

    # -------------------------
    # Create Base Map
    # -------------------------
    m = folium.Map(
        location=[12.9716, 77.5946],
        zoom_start=12,
        tiles=None
    )

    # -------------------------
    # Base Maps
    # -------------------------
    folium.TileLayer(
        "OpenStreetMap",
        name="Street Map"
    ).add_to(m)

    folium.TileLayer(
        "CartoDB positron",
        name="Light Map"
    ).add_to(m)

    folium.TileLayer(
        "CartoDB dark_matter",
        name="Dark Map"
    ).add_to(m)

    # -------------------------
    # Road Network Layer
    # -------------------------
    roads_layer = folium.FeatureGroup(
        name="Road Network"
    )

    folium.GeoJson(
        roads,
        style_function=lambda x: {
            "color": "#2563EB",
            "weight": 2
        }
    ).add_to(roads_layer)

    roads_layer.add_to(m)

    # -------------------------
    # Pothole Layer
    # -------------------------
    pothole_layer = folium.FeatureGroup(
        name="Pothole Complaints"
    )

    for _, row in potholes.iterrows():

        if row.geometry is None:
            continue
        status = str(row["Status"]).strip()

        # High Priority
        if status in [
        "Complaint Received",
        "Assigned",
        "Ack by Contractor",
        "Ack by Engineer",
        "Scheduled",
        "In Progress",
        "Re Opened"
    ]:
            color = "red"

    # Medium Priority
        elif status in [
    "Long Term Solution",
    "Sent for Approval",
    "Transferred",
    "Approved with Addendum",
    "Under DLP"
]:
            color = "orange"

    # Completed
        elif status in [
    "Resolved",
    "Resolved with Addendum",
    "Resolved with modified Addendum",
    "Work Done",
    "Work Done with Addendum",
    "Closed"
]:
            color = "green"

    # Rejected
        elif status == "Rejected":
            color = "gray"

        else:
            color = "blue"

        popup = f"""
        <b>Ward:</b> {row['Ward_Name']}<br>
        <b>Status:</b> {row['Status']}<br>
        <b>Problem:</b> {row['Problem_De']}<br>
        <b>Estimated Cost:</b> ₹{row['Total_Esti']}<br>
        <b>Open Date:</b> {row['Open_Date']}
        """

        folium.CircleMarker(
            location=[
                row.geometry.y,
                row.geometry.x
            ],
            radius=6 if color == "red" else 4,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.9,
            popup=folium.Popup(
                popup,
                max_width=300
            )
        ).add_to(pothole_layer)

    pothole_layer.add_to(m)

    # -------------------------
    # Layer Control
    # -------------------------
    folium.LayerControl().add_to(m)

    return m