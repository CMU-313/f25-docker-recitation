from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


RECITATION_HOURS = {"a": "09:00~09:50", "b": "10:00~10:50",
                    "c": "11:00~11:50", "d": "1:00~1:50",
                    "e": "2:00~2:50", "f": "3:00~3:50"}

MICROSERVICE_LINK = "https://f25-docker-recitation-8jvfc6jzu-juans-projects-a6ad89e9.vercel.app/section_info/"


@app.get("/section_info/{section_id}")
def get_section_info(section_id: str):

    if section_id is None:
        raise HTTPException(status_code=404, detail="Missing section id")

    section_id = section_id.lower()

    response = requests.get(MICROSERVICE_LINK + section_id)

    # You can check out what the response body looks like in terminal using the print statement
    # print(response)
    data = response.json()
    print(data)
    ta_name_list = data["ta"]
    ta1_name = ta_name_list[0]
    ta2_name = ta_name_list[1]

    start_time = data["start_time"]
    end_time = data["end_time"]

    # OR 
    # start_time, end_time = RECITATION_HOURS[section_id].split("~")

    # print(ta1_name)
    # TODO
    
    if section_id in RECITATION_HOURS:
        return {
            "section": section_id,
            "start_time": start_time,
            "end_time": end_time,
            "ta": [ta1_name, ta2_name]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid section id")
