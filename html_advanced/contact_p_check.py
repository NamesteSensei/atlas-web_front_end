from bs4 import BeautifulSoup

# Open and read the 12-index.html file
with open("12-index.html", "r") as f:
    contents = f.read()

# Parse the HTML content
soup = BeautifulSoup(contents, "html.parser")

# Find the Contact section
contact_section = soup.find("section", id="contact")

# Ensure there's an h2 with text "Contact"
h2 = contact_section.find("h2")
if h2 and h2.text.strip() == "Contact":
    print("correct number of paragraphs in contact section")
    
    # Ensure paragraphs exist
    paragraphs = contact_section.find_all("p")
    if len(paragraphs) == 2:
        print("paragraphs are in correct places")
        
        # Check the first paragraph text
        correct_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?"
        if paragraphs[0].text.strip() == correct_text:
            print("paragraph has correct text")
        else:
            print("paragraph text is incorrect")
    else:
        print("incorrect number of paragraphs in contact section")
else:
    print("h2 Contact not found or incorrect")
