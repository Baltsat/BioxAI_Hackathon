from bs4 import BeautifulSoup

def extract_interaction_info(html_content):
    # soup = BeautifulSoup(html_content, 'lxml')
    soup = BeautifulSoup(html_content, 'html.parser')
    interaction_info = {}

    # Extract interacting proteins
    subject_protein = soup.select_one(".interactions-col.subject h5 a").text
    affected_protein = soup.select_one(".interactions-col.affected h5 a").text
    interaction_info["Interacting Proteins"] = (subject_protein, affected_protein)

    # Extract severity
    severity = soup.select_one(".interactions-col.severity .severity-badge").text
    interaction_info["Severity"] = severity.strip()

    # Extract description
    description = soup.select_one(".interactions-col.description p").text
    interaction_info["Description"] = description.strip()

    # Extract extended description
    extended_description = soup.select_one(".interactions-row .truncate-overflow p").text
    interaction_info["Extended Description"] = extended_description.strip()

    # Extract references
    # Extract references with their names and links
    references = [{"name": li.text, "link": li.a["href"] if li.a else None} for li in soup.select(".cite-this-references li")]
    interaction_info["References"] = references

    return interaction_info
