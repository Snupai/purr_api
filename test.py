from src.purr_api import Purr
from src.purr_api.exceptions import APIError, NetworkError

def test_endpoints():
    purr = Purr()
    
    try:
        # Test SFW endpoints
        print("Testing SFW endpoints...")
        angry_gif = purr.img.sfw.angry.get()
        print(f"Angry GIF: {angry_gif}")
        
        neko_img = purr.img.sfw.neko.get()
        print(f"Neko Image: {neko_img}")
        
        # Test owoify endpoint
        print("\nTesting owoify endpoint...")
        text = "Hello, this is a test message!"
        owoified = purr.owoify.get(text)
        print(f"Original: {text}")
        print(f"Owoified: {owoified}")
        
    except APIError as e:
        print(f"API Error {e.response_code}: {e.message}")
    except NetworkError as e:
        print(f"Network Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    test_endpoints() 