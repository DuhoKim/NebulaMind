import sys
from astroquery.vizier import Vizier

def main():
    Vizier.ROW_LIMIT = 50
    try:
        jades = Vizier.find_catalogs('JADES')
        ceers = Vizier.find_catalogs('CEERS')
        glass = Vizier.find_catalogs('GLASS')
        uncover = Vizier.find_catalogs('UNCOVER')
        
        print("JADES catalogs:", list(jades.keys()))
        print("CEERS catalogs:", list(ceers.keys()))
        print("GLASS catalogs:", list(glass.keys()))
        print("UNCOVER catalogs:", list(uncover.keys()))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
