import pandas as pd

def get_supply_chain_data():
    nodes = pd.DataFrame([
        {"id": "OEM", "label": "EcoAuto HQ", "tier": 0, "emissions": 120, "country": "Germany"},
        {"id": "T1_Battery", "label": "VoltCell Inc.", "tier": 1, "emissions": 850, "country": "South Korea"},
        {"id": "T1_Steel", "label": "Apex Steel Works", "tier": 1, "emissions": 1400, "country": "India"},
        {"id": "T1_Chips", "label": "MicroLogic Corp", "tier": 1, "emissions": 310, "country": "Taiwan"},
        {"id": "T2_Lithium", "label": "Andes Lithium Co.", "tier": 2, "emissions": 2100, "country": "Chile"},
        {"id": "T2_Iron", "label": "Pilbara Iron Ore", "tier": 2, "emissions": 1750, "country": "Australia"},
        {"id": "T2_Silicon", "label": "PureSilica Refinery", "tier": 2, "emissions": 920, "country": "China"},
    ])

    edges = [
        ("T2_Lithium", "T1_Battery"),
        ("T1_Battery", "OEM"),
        ("T2_Iron", "T1_Steel"),
        ("T1_Steel", "OEM"),
        ("T2_Silicon", "T1_Chips"),
        ("T1_Chips", "OEM"),
    ]
    return nodes, edges
