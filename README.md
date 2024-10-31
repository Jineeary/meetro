# meetro

Team 9 Project
[Meetro (Meet + Metro)]

22011855 김연진(Yeon-jin Kim) 22011867 염예은(Ye-eun Yeom)
22011870 김여진(Yeo-jin Kim) 22011872 윤수빈(Soo-been Yun)

1.	Problem Identification and Analysis
As I went to college, I had many friends who lived in various places. So when I made plans to meet up with friends, it became important to set a midpoint. It was always a hassle to calculate the distance and meet up, and the more people I met, the harder it was to find a midpoint. So I felt the need for a program that would automatically find a midpoint when I entered the places where the people I was meeting lived.
•	Research: 
1.	Wemeetplace https://wemeetplace.com 
Open Source (github): https://github.com/we-meetting/weMeet-frontend
To improve or rethink the concept: We found that although the wemeetplace is good at finding midpoints, it has problems when there are no attractions or attractions at those points. This is because people would prefer places with attractions rather than perfect midpoints, even if they are slightly further away. In addition, although the wemeetplace provides nearby attractions at midpoints, the attractions are based on old data, and some subway stations do not even recommend attractions. Therefore, we aim to recommend nearby attractions at all subway stations in the metropolitan area. 
  
“Oops! I haven't found a place to recommend in Boramae Station yet! I'll try to find it and add it!”
2.	Ya-manna(야만나) https://ya-manna.com 
Open Source (github): https://github.com/mandooro/YaManNa
To improve or rethink the concept: Ya-manna focuses on providing a variety of attractions and entertainment in addition to subway stations at the midpoint of the group. However, Yamanna also has the disadvantage of pursuing an exact midpoint. As mentioned above, people may want to go to a place with a famous attraction, such as an amusement park, even if it is a little further away.







2.	Project Naming and Branding
The name of our project is meetro. It is a combination of the words meet and metro, and the name emphasizes that we will meet at a subway station.

3.	Mission Statement
"Our mission is to help friends effortlessly find the most efficient subway station and nearby places to enjoy. Whether for casual meetups or special occasions, we simplify the process of choosing the perfect meeting spot."
•	Goal: A web service that finds the midpoint subway station for friends and recommends nearby attractions. (Main Keywords: Efficient, convenient, recommendation, subway station, meeting.)
•	Target Audience: People who have difficulty deciding on a meeting place, friends who want to meet at a midpoint and hang out, and those who want to choose a meeting spot more efficiently.












4.	Features and Functionalities
•	Key Features:
Goal: Recommend subway stations that are midpoints and have many famous attractions
1. Set the midpoint between two users to a wide range.
2. Set the weight to 1 for common attractions, and set the weight to 3 for famous attractions that most people know (e.g., amusement parks, large shopping malls, etc.).
3. Assign the attractions to nearby stations and score each subway station. At this time, the farther away the subway station is from the exact midpoint between the two users, the lower the score of the subway station.
4. Recommend the subway station with the highest score among the subway stations that fall within the midpoint range.
•	Differentiation:
Wemeetplace / Ya-manna features	Meetro features	Differences
(benefits of meetro)
Finding a simple midpoint	Providing a midpoint considering landmarks	Score landmarks and recommend them
Providing outdated information	Providing more up-to-date information	following the trend
small amount of data	A large amount of data	Giving users more choices






5.	Development Tools and Languages
•	Technical Stack: 
JavaScript (Node.js): A backend language used to handle server-side logic and APIs.
Python: For data processing, weight calculation algorithms, and map service integration.
HTML/CSS: Used to build the user interface (UI) on the frontend.
JavaScript (React): A frontend framework for developing the user interface.
•	Tools:
GitHub: To share the current development progress of WeMeetPlace and YaManna with the team.
OpenStreetMap (OSM): An open-source platform that provides map data.
Google Maps API: To provide map data, calculate midpoints, and retrieve information about nearby landmarks.
Figma: A collaborative tool for UI/UX design.

6.	Team Responsibilities
Project Leader - Soo-bin Yoon
Code Manager - Ye-eun Yeom
Data Collector - Yeon-jin Kim
Website Creator - Yeo-jin Kim
