# Dictionary of protein names mapped to their corresponding product_concept_ids
protein_data = {
    "Zoledronic acid monohydrate": "DBPC0127348",
    "Clodronic acid": "DBPC0118686",
    "Protein3": "DBPC0000003",
    "Protein4": "DBPC0000004",
    # ... (I'll add dummy data for the sake of the example)
    "Protein28": "DBPC0000028",
    "Protein29": "DBPC0000029",
    "Protein30": "DBPC0000030",
}

# Extracting the list of available proteins from the dictionary keys
available_proteins = list(protein_data.keys())
