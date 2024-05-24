from hempy.survey_results import plot_consumption_percentage, plot_time_vs_age

#These functions depend on the results of an anonimous survey done back in April. The topic was about the effects of cannabis consumption, https://docs.google.com/forms/d/e/1FAIpQLSfJeva1E3bdncBiHNJaO4mWmyXZ9Zls786URSozsB1nThb1iQ/viewform?vc=0&c=0&w=1&flr=0 

def test_plot_consumption_percentage():
    plot_consumption_percentage() #Consumption percentage according to indicated age displayed

def test_plot_time_vs_age():
    plot_time_vs_age() #Effects duration according to age displayed

