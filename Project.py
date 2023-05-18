import pandas as pd

import matplotlib.pyplot as plt

covid_data = pd.read_csv(

 "covidDataset.csv", usecols=["State_code", "Confirmed", "Deaths", "Recovered"])

covid_data["Active"] = (

 covid_data["Confirmed"] - covid_data["Deaths"] - covid_data["Recovered"])

plt.stackplot(

 covid_data["State_code"],

 covid_data["Recovered"],

 covid_data["Deaths"],

 covid_data["Confirmed"],

 covid_data["Active"],

 colors=["green", "red", "cyan", "orange"],

 baseline="zero",

)

plt.ylim(1, max(covid_data.Confirmed))

plt.title("Active Cases Record in INDIA 2021-22")

plt.ylabel("No. of Cases")

plt.xlabel("State Code")

plt.plot([], [], color="green", label="Recovered")

plt.plot([], [], color="red", label="Death")

plt.plot([], [], color="cyan", label="Confirmed")

plt.plot([], [], color="orange", label="Active")

plt.legend()

plt.grid(True)

plt.show()
