from app.international_organizations import InternationalOrganizationsScrapper

def start_scrapping():
    # Create class
    mysearch = InternationalOrganizationsScrapper()

    # Add OSCE jobs:
    mysearch.OSCE()

    # Add UN jobs:
    mysearch.UN_jobs()

    # Save file:
    mysearch.save_file(path="C:/Users/brian/OneDrive/Escritorio/")