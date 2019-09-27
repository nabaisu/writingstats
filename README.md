# Writing Stats
## description
Some time ago I set up a daily goal to write 1000 words per day.
About what, you might ask ? About actually nothing in special, if I felt like i had nothing in my mind (which is not true), then I'd just write `i have nothing to say, but because i am here writing about what i don't know, let's think about how the snakes make love...` and so on, and this made me think about one topic, and start to write about it to clear my head a bit =)
But with which goal, you might ask ? To become better at writing. I am no good at it and just figured that, if i kept the thing of writing 1000 words a day, even if sometimes it was about nothing in special, I'd become a better writer.
Result ? I am more confortable and am also writing faster. But that's normal since I really stuck into it for about 6 months, which... in a year made an average of about 500 words per day, not bad for a rookie =)

### it's a webapp to see my daily writing stats, not more =) 
I just logged it all with a script I wrote while i wrote and would like to go back to it.

#### this is a test app that I'm doing in order to learn BTW, feel free to steal and copy paste my code as you wish 

# Technical parts of the app 
## pages:
Single page web application that is aimed to be a PWA and easily accessible in my phone:
 - Main page / dashboard

## requisites:
 - my writing data stats:
   - API fetch request from a google Sheets using the service $$name of the service 
 - patience with CSS (everyone needs this) =)
 - it should show the metrics of my writing data

## visuals:
 - the application should display
   - a form with the goal that is set to achieve my objective
   - a form with a date (set to default the current month)
   - a form (select) with the options of:
     - last week
     - this week
     - last month
     - this month
   - a graph with the values that i wrote in the latest days with an average value as well
   - the total number of words written in those days
   - the average number of words written in those days
   - the number of words I need to write to achieve my goals
   - a value saying that, with this pace, how long should it take to write a 75000 words novel

## interaction:
 - When any of the forms is updated, update the other values in the app

## considerations:
 - In order to consume the api as few as possible, just make an api call if the date has changed or if the user clicks a refresh button.
 - the refresh button should not be clicked more than once every minute