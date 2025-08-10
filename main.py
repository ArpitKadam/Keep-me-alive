import requests
import datetime

def ping_backend():
    urls = [
        ("Web App", "https://hackrx-insurance-app-1.onrender.com"),
        ("API Health", "https://hackrx-insurance-app.onrender.com/health")
    ]
    
    for name, url in urls:
        try:
            print(f"{datetime.datetime.now()}: Pinging {name} - {url}")
            response = requests.get(url, timeout=30)
            print(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                if "health" in url.lower():
                    try:
                        data = response.json()
                        print(f"Health metrics: {data}")
                    except ValueError:
                        print("⚠️ Expected JSON but got something else")
                else:
                    print("Web app is alive")
            else:
                print(f"⚠️ Unexpected status code: {response.status_code}")

        except Exception as e:
            print(f"❌ Error pinging {name}: {e}")

if __name__ == "__main__":
    ping_backend()
