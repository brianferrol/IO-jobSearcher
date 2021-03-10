from app.international_organizations import InternationalOrganizationsScrapper

def start_scrapping():
    # Create class
    mysearch = InternationalOrganizationsScrapper()

    # Add OCSE jobs:
    mysearch.OCSE()

    print(mysearch.job_list)

    # Save file:
    mysearch.save_file(path="C:/Users/brian/OneDrive/Escritorio/")