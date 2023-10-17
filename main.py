import streamlit as st
import requests
from protein_data import available_proteins, protein_data
from interaction_extractor import extract_interaction_info

@st.cache_resource
def load_env():
    from predict import load_env
    return load_env()

def main():
    st.title("Drug Interaction Checker")
    
    predict, drugs = load_env()

    # Multi-select widget for users to select proteins
    #selected_proteins = st.multiselect("Select proteins:", available_proteins)
    selected_proteins = st.multiselect("Select drugs:", drugs, max_selections=2)

    # Button to check interactions of the selected proteins
    if st.button("Check Interactions"):
        # Prepare data for POST request
        data = {
            "product_concept_names[]": selected_proteins,
            "product_concept_ids[]": [protein_data[protein] for protein in selected_proteins if protein in protein_data]
        }

        # Send POST request
        response = requests.post("https://go.drugbank.com/drug-interaction-checker", data=data)

        #try:
        if True:
            # Extract interaction information from the response HTML
            #interaction_info = extract_interaction_info(response.text)
            interaction_info = {
                "Interacting Proteins": selected_proteins,
                "Severity": "minor", # TODO: map number to severity
                # TODO: ask ChatGPT for these
                "Description": "tuna",
                "Extended Description": "foobar", 
            }

            # Display the extracted information in a more design-centric manner
            st.write("### Interaction Results:")

            # Display interacting proteins with icons
            st.write(f"🧬 **{interaction_info['Interacting Proteins'][0]}** interacts with 🧬 **{interaction_info['Interacting Proteins'][1]}**")

            # Display severity with appropriate color
            severity_color = {
                "minor": "green",
                "moderate": "orange",
                "major": "red"
            }
            st.markdown(f"**Severity:** <span style='color: {severity_color[interaction_info['Severity'].lower()]};'>{interaction_info['Severity']}</span>", unsafe_allow_html=True)

            # Create two columns for description and extended description
            col1, col2 = st.columns(2)

            # Display description in the first column
            with col1:
                st.write("### Description")
                st.write(interaction_info["Description"])

            # Display extended description in the second column
            with col2:
                st.write("### Extended Description")
                with st.expander("Show More"):
                    st.write(interaction_info["Extended Description"])

                # Display references in a separate expander in the same column
                # with st.expander("References"):
                #     for ref in interaction_info["References"]:
                #         if ref["link"]:
                #             st.markdown(f"- [{ref['name']}]({ref['link']})")
                #         else:
                #             st.write(f"- {ref['name']}")

        #except Exception as e:
        #    st.warning("No interactions were found or there was an issue processing the response.")

if __name__ == "__main__":
    main()
