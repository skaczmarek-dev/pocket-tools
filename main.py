from pocket_tools import get_pocket_data

def main():

    # Example: Fetch all Pocket data
    get_pocket_data('config/settings.json', 'output/pocket_all_data.json')

if __name__ == "__main__":
    main()