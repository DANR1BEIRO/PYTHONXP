"""
Create a tuple filled with the top 20 teams in the 
Brazilian soccer championship, ordered by 
their position. Then display:

1 - Only the top 5
2 - Only the last four teams
3 - All of the teams sorted alphabetically
4 - The position of Fluminense
"""



class Championship:
    def __init__(self):
        self.teams = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
                      "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama",
                      "EC Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude",
                      "Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá")
        
   
    def top_five(self):
        return "\n".join(self.teams[:5])
        
    def last_four(self):
        return "\n".join(self.teams[-4:])

    def alphabetically_sorted(self):
        return "\n".join(sorted(self.teams))

    def find_fluminense(self):
        for index, value in enumerate(self.teams, start=1):
            if value == "Fluminense":
                return index
            
    def display_results(self):
        print("Top five are:")
        print(f"{self.top_five()}")

        print("\nThe last four are:")
        print(f"{self.last_four()}")
        
        print("\nChampionship teams sorted alphabetically:")
        print(f"{self.alphabetically_sorted()}")

        print("\nFluminense is in:")
        print(f"{self.find_fluminense()} position") 

championship = Championship()
championship.display_results()