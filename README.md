# website-blocker

It’s a simple program yet tricky that runs on the background and all it does is it doesn’t let you browse certain distracting websites such as Facebook or your e-mail account, during your working hours.

The program is tested to work on Windows, Mac and linux.
The idea is that once you build this program, you pa to the program website links that you think are distracting.

So you pas links as strings and the time that you are working on your computer and the program will block these webites during the working hours.
And in thi way you not only are much more productive but this also reduces stress as distraction is also known to cause stress.

In order to make the script execute automatically on start-up, Create a task through TASK SCHEDULER.
Steps are as follows:
1. Open task scheduler
2. Click on create new task
3. Give a name to your task
4. Check the option ‘execute with highest priviledges’
5. Click on Triggers
6. Select ‘on start-up’ from the drop down list
7. Click on actions
8. Select ‘start a program’
9. Click on conditions
10. Deselect ‘start task only if computer on AC power’ and ‘start tak only if computer is idle’
