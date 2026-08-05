import sqlite3
import pandas as pd

DB_PATH = "database/roadiq.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


def get_total_roads():
    conn = get_connection()
    df = pd.read_sql("SELECT COUNT(*) AS Total_Roads FROM Roads;", conn)
    conn.close()
    return df


def get_total_potholes():
    conn = get_connection()
    df = pd.read_sql("SELECT COUNT(*) AS Total_Potholes FROM Potholes;", conn)
    conn.close()
    return df


def get_total_repairs():
    conn = get_connection()
    df = pd.read_sql("SELECT COUNT(*) AS Total_Repairs FROM Repairs;", conn)
    conn.close()
    return df


def get_total_wards():
    conn = get_connection()
    df = pd.read_sql("SELECT COUNT(*) AS Total_Wards FROM Wards;", conn)
    conn.close()
    return df

def get_roads():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM Roads",
        conn
    )

    conn.close()

    return df

def get_top_wards():

    conn = get_connection()

    query = """
    SELECT Ward_Name,
           COUNT(*) AS Complaints
    FROM Potholes
    GROUP BY Ward_Name
    ORDER BY Complaints DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_complaint_status():

    conn = get_connection()

    query = """
    SELECT Status,
           COUNT(*) AS Count
    FROM Potholes
    GROUP BY Status
    ORDER BY Count DESC;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def get_monthly_complaints():

    conn = get_connection()

    query = """
    SELECT substr(Open_Date,1,7) AS Month,
           COUNT(*) AS Complaints
    FROM Potholes
    GROUP BY Month
    ORDER BY Month;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_priority_data():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM Potholes",
        conn
    )

    conn.close()

    return df