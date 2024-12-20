import requests

API_KEY = "d0962101532aa3bb5c6150b61c0b7d45"

def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ =="__main__":
    fd = get_data(place="Tokyo", days=3)
    dates = [dic["dt_txt"] for dic in fd]
    print(dates)



