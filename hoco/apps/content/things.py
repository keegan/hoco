from enum import Enum
from datetime import datetime

class Day(Enum):
    mon = 1
    tues = 2
    wed = 3
    thurs = 4
    fri_a = 5
    fri_b = 6

week = [Day.mon, Day.tues, Day.wed, Day.thurs, Day.fri_a, Day.fri_b]

dates = {
    Day.mon: datetime(year=2019, month=9, day=20, hour=8), 
    Day.tues: datetime(year=2019, month=9, day=24, hour=8),
    Day.wed: datetime(year=2019, month=9, day=25, hour=8),
    Day.thurs: datetime(year=2019, month=9, day=26, hour=8),
    Day.fri_a: datetime(year=2019, month=9, day=27, hour=8), 
    Day.fri_b: datetime(year=2019, month=9, day=27, hour=14, minute=30),
}

rally_links = {
    Day.mon: "https://docs.google.com/forms/d/e/1FAIpQLSel5lTqUF4tNJzOeIIkOcXyBcZ8HZ-s1pbj-m4P_pHDUjxRgg/viewform?embedded=true",
    Day.tues: "https://docs.google.com/forms/d/e/1FAIpQLSfcMEeidH1ZTC9liStXnMIsANk3nFcvvSbqDBwlc1lgrY0XMg/viewform?embedded=true",
    Day.wed: "https://docs.google.com/forms/d/e/1FAIpQLSdGb1_h1xZMmHzmEG9RQS1RhSrWbZmn5ZRN31VDjqn6p_hp6g/viewform?embedded=true",
    Day.thurs: "https://docs.google.com/forms/d/e/1FAIpQLSdzUpJO-jHjoU2ePjgmrakjXfMYfdWAV-o77bg9bySZk5J14w/viewform?embedded=true",
    Day.fri_a: "https://docs.google.com/forms/d/e/1FAIpQLSfDDMxYPVI4HnZlmnMA1XYlg-1UlApUexKrJWUgzvgUacFw4A/viewform?embedded=true",
    Day.fri_b: "https://docs.google.com/forms/d/e/1FAIpQLScFCqKtCQohJBXjP8mbq5zPzHMRI7NxxaTIdt_i6BZnIepFig/viewform?embedded=true",
    
}

rally_themes = {
    Day.mon: "Old School Cool",
    Day.tues: "Iconic Idols",
    Day.wed: "Bodacious Bunches",
    Day.thurs: "Throwback Thursday",
    Day.fri_a: "Retro Rainbow",
    Day.fri_b: "Retro Rainbow"
}

rally_subthemes = {
    
    Day.mon: "Dress Your Best Day",
    Day.tues: "Meme Day",
    Day.wed: "Group Day",
    Day.thurs: "Class Theme (Decade) Day",
    Day.fri_a: "Class Color Day",
    Day.fri_b: "Class Color Day"
}
